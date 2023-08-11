from django.db import models
from django.contrib.auth.models import User
from course.models import Course
class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pic/Student/',null=True,blank=True)
    address = models.CharField(max_length=40, null=True, blank=True)
    mobile = models.CharField(max_length=20,null=True, blank=True)
    
    @property
    def get_name(self):
        return self.username.first_name+" "+self.username.last_name
    
    @property
    def get_instance(self):
        return self
    
    def __str__(self):
        return self.username.first_name
    

class FeedBack(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    content = models.TextField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    course_rate = models.CharField( max_length=5 ,choices=[('*','*'),('**','**'),
                                    ('***','***'),('****','****'),('*****','*****'),])

    def __str__(self):
        return f"{self.user} {self.content}"