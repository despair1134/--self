from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import StudentInfo

# Create your views here.
def index(request):
    '''学生首页'''
    return render(request,'index.html')

def student_add(request):
    '''添加学生'''
    #  根据请求方式 返回不同页面
    if request.method == 'GET':
        return render(request,'student_add.html')
    else:
        # 获取数据
        name = request.POST.get('stuname',None)
        age = request.POST.get('stuage',None)
        gender = request.POST.get('stugender',None)

        # 创建学生对象
        student = StudentInfo()
        student.name = name
        student.age = age
        student.gender = gender
        student.save()

        # 添加数据后  返回首页
        return render(request,'index.html')


def student_del(request,stuid):
    '''删除学生'''
    # 找到对应id的学生，删除
    StudentInfo.objects.filter(id = int(stuid)).delete()
    # 执行删除操作后 返回学生首页 使用重定向和反向解析技术
    return redirect(reverse('student:student_all'))


def student_update(request,stuid):
    '''修改学生'''
    if request.method == 'GET':
        student = StudentInfo.objects.filter(id = int(stuid))[0]
        return render(request,'student_update.html',{
            'student':student
        })
    else:
        # 获取数据
        name = request.POST.get('stuname',None)
        age = request.POST.get('stuage',None)
        gender = request.POST.get('stugender',None)

        # 获取对应id的学生，修改数据
        student = StudentInfo.objects.filter(id = int(stuid))[0]
        student.name = name
        student.age = age
        student.gender = gender
        # 修改完毕后，保存数据
        student.save()

        # 修改数据后  返回所有学生信息页 使用重定向和反向解析技术
        return redirect(reverse('student:student_all'))
    pass

def student_all(request):
    '''查找学生'''
    all_students = StudentInfo.objects.filter()
    return render(request,'student_all.html',{
        'all_students':all_students
    })
