from django.db import models
from django.contrib.auth.models import User
from course.models import Course


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=200)

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.question.content}"






