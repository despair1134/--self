from django.contrib import admin

# Register your models here.
from student.models import StudentInfo

# admin后台管理组件
class StudentInfoAdmin(admin.ModelAdmin):
    # 配置列表页的字段显示
    list_display = ['name','age','gender','addtime']
    # 配置添加搜索框
    search_fields = ['name','age','gender']
    # 配置分页显示数据条数
    list_per_page = 1
    # 配置过滤器
    list_filter = ['age','gender']
    # 配置详情页的字段显示以及顺序
    fields = ['addtime','name']


# 将学生信息模型注册到admin后台
admin.site.register(StudentInfo,StudentInfoAdmin)