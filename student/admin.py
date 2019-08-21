from django.contrib import admin
from .models import StudentInfo,StudentId,Banclass
# Register your models here.
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['name','age','gender','ban']
    list_filter = ['age']

class StudentIdAdmin(admin.ModelAdmin):
    list_display = ['stuid','student']


admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.register(StudentId,StudentIdAdmin)
admin.site.register(Banclass)