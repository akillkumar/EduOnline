from django.contrib import admin
from .models import *


admin.site.register(Assignment)
admin.site.register(StudentAssignment)
admin.site.register(TeacherReview)
admin.site.register(Exam)
admin.site.register(ExamQuestion)
admin.site.register(QuestionAnswer)
admin.site.register(ExamResult)
