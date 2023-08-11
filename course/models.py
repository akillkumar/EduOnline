from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')

    fields = [
        ('COMPUTER-SCIENCE', 'Computer Science'),
        ('FRONT-END', 'Front End'),
        ('BACK-END', 'Back End'),
        ('FULLSTACK', 'Full stack'),
        ('MOBILE-DEVELOPMENT', 'Mobile Development'),
        ('GRAPHIC-DESIGN', 'Graphic Design'),
        ('MOTION-GRAPHICS', 'Motion Graphics'),
        ('MARKETING', 'Marketing'),
        ('PHOTOGRAPHY', 'Photography'),
        ('OTHER', 'Other'),
    ]
    field = models.CharField(max_length=30, choices=fields)

    def __str__(self):
        return self.course_name


class CourseVideos(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=40)
    video = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course} - {self.title}"

class Enrolled(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return  str(self.course)



