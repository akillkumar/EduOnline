from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):
    field_choices = [
        ('Technology', 'Technology'),
        ('Programming', 'Programming'),
        ('Artificial Intelligence & Machine Learning', 'Artificial Intelligence & Machine Learning'),
        ('Web Development', 'Web Development'),
        ('Mobile App Development', 'Mobile App Development'),
        ('Data Science', 'Data Science'),
        ('Networking', 'Networking'),
        ('Cybersecurity', 'Cybersecurity'),
        ('Game Development', 'Game Development'),
        ('Other','Other'),
    ]
    
    name = models.CharField(max_length=40)
    link = models.URLField(default='https://')
    description = models.CharField(max_length=100)
    field = models.CharField(max_length=50, choices=field_choices)
    image = models.ImageField(upload_to='library/book/', blank=True, null=True)


class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog/thumbnails/', blank=True, null=True)


class ContactUs(models.Model):
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    email = models.EmailField()
    message = models.TextField()

    def get_full_name(self):
        return f"{self.firstName} {self.lastName}"
    def __str__(self):
        return f"{self.message}"
    
    class Meta:
        verbose_name_plural = 'Contact Us'