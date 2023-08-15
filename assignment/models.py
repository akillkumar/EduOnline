from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from course.models import Course
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to='assignments/%d')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class StudentAssignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='assignments/%d', null=True, blank=True)


    def __str__(self):
        return self.assignment.title
    


class TeacherReview(models.Model):
    student_assignment = models.OneToOneField(StudentAssignment, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField()
    comments = models.TextField()
