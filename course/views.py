from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Course, CourseVideos, Enrolled
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CourseForm, CourseEditForm, UploadForm
from accounts.models import FeedBack
from accounts.views import is_teacher, is_student
@login_required
def myCourses(request):
    #profile = Profile.objects.get(username=request.user)
    enrolled = Enrolled.objects.filter(student=request.user)

    context = {
        #'profile':profile,
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        'myCourses':enrolled
    }
    return render(request, 'courses/myCourses.html', context)


def courses(request):
    feedbacks = FeedBack.objects.all()
    categories = Course.objects.values_list('field', flat=True).distinct()
    courses_by_category = {}

    for category in categories:
        courses_by_category[category] = Course.objects.filter(field=category)

    courses = Course.objects.all()
    context = {
        'feedbacks':feedbacks,
        'courses_by_category': courses_by_category,
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        "courses":courses,
        }
    return render(request, 'courses/courses.html', context)

@login_required(login_url='login')
def details(request, courseName):
    enrolled = Enrolled.objects.filter(student=request.user)
    course = Course.objects.get(course_name=courseName)
    video = CourseVideos.objects.first()
    context = {
        'enrollments':enrolled,
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        "course":course, 
        'video':video,
        }
    return render(request, 'courses/courseDetails.html', context)






@login_required(login_url='login')
def enroll(request, course_name):
    try:
        course = Course.objects.get(course_name=course_name)
        enroll = Enrolled.objects.create(student=request.user, course=course)
        enroll.save()
    except:
        return redirect('myCourses')
    return redirect('course_page', course_name)


#to make user view his course
def course_page(request, course_name):
    try:
        course = Course.objects.get(course_name=course_name)
        videos = CourseVideos.objects.filter(course=course).first().id
    except:
        return redirect('/')
        print(TypeError)
    
    context = {
        'course':course,
        'videos':videos,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
    }
    return render(request, 'courses/course_page.html', context)

@login_required(login_url='login')
def watchCourse(request, courseName, videoId):
    course = Course.objects.get(course_name=courseName)
    videos = course.videos.all()
    if not videos:
        return  HttpResponse('No videos')
    current_video = get_object_or_404(CourseVideos, id=videoId, course=course)

    # Find the indices of the current video and get the previous and next video IDs
    video_ids = list(videos.values_list('id', flat=True))
    current_index = video_ids.index(current_video.id)
    prev_video_id = video_ids[current_index - 1] if current_index > 0 else None
    next_video_id = video_ids[current_index + 1] if current_index < len(video_ids) - 1 else None

    context = {
        #'profile':profile,
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        'course': course,
        'video':current_video,
        'current_video': current_video.video,
        'prev_video_id': prev_video_id,
        'next_video_id': next_video_id,
    }
    return render(request, 'courses/watchCourse.html', context)

def management(request):
    courses = Course.objects.all()

    context = {
        'courses':courses,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
    }
    return render(request, 'courses/management.html', context)

def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    
    if request.method == 'POST':
        form = CourseEditForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('assignment')
    else:
        form = CourseEditForm(instance=course)
    
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'form': form,
        'course': course}
    return render(request, 'courses/edit-course.html', context)


def upload_videos(request, course_id ):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            course_video = form.save(commit=False)
            course_video.course = course
            course_video.save()
            messages.success(request, 'the video added successfully..')
    else:
        form = UploadForm()
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'form': form,
        'course':course
    }
    return render(request, 'courses/upload-videos.html', context )




import os
def create_course_videos_from_file(request, course_name):

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c#.txt')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        title, video_link = line.strip().split(':')  # Assuming comma-separated values
        
        # Assuming you have a course instance, replace it with your logic to get the appropriate course
        course = Course.objects.get(course_name=course_name)

        # Create and save the CourseVideos object
        course_video = CourseVideos(course=course, title=title, video=video_link)
        course_video.save()

    return redirect('/')
