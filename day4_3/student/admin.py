from django.contrib import admin
from .models import StudentInfo,StudentId,Ban

# Register your models here.
'''
class StudentInfoAdmin(admin.ModelAdmin):
    #配置列表页的字段显示
    list_display = ['name','age','gender','add_time']
    #配置添加搜索框及搜索字段
    search_fields = ['name','age','gender','add_time']
    #配置分页显示数据条数
    list_per_page = 1
    #配置过滤器---->这个非常有用，数据的筛选
    list_filter = ['age','gender']
    #配置详情页的字段显示以及顺序 ----》增加学生信息页的字段显示及顺序
    fields = ['add_time','name']

admin.site.register(StudentInfo,StudentInfoAdmin)
'''
class StudentInfoAdmin11(admin.ModelAdmin):
    # 配置列表页的字段显示
    list_display = ['ban','name','age','gender']
    # fields = ['name']
    search_fields = ['gender']
    list_filter = ['age','gender']
class StudentIdAdmin(admin.ModelAdmin):
    list_display = ['stuid','student']

class BanAdmin(admin.ModelAdmin):
    list_display = ['banid']
admin.site.register(StudentInfo,StudentInfoAdmin11)
admin.site.register(StudentId,StudentIdAdmin)
admin.site.register(Ban,BanAdmin)