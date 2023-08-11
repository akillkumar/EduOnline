from django.contrib import admin
from .models import Assignment, StudentAssignment, TeacherReview


admin.site.register(Assignment)
admin.site.register(StudentAssignment)
admin.site.register(TeacherReview)