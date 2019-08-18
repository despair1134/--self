from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import StudentInfo,StudentId,Ban

# Create your views here.
def index(request):
    '''学生信息管理系统首页'''
    return render(request,'index.html')

def student_all(request):
    '''查看所有学生'''
    all_students = StudentInfo.objects.filter()
    return render(request,'student_all.html',{
        'all_students':all_students
    })



def student_add(request):
    '''添加学生'''
    if request.method == 'GET':
        all_bans = Ban.objects.filter()
        return render(request,'student_add.html',{
            'all_bans':all_bans
        })

    else:
        # POST 请求获取数据
        name = request.POST.get('stuname',None)
        age = request.POST.get('stuage',None)
        gender = request.POST.get('stugender',None)
        stuid = request.POST.get('stuid',None)
        banid = request.POST.get('stuban',None)

        # 创建学生对象
        student = StudentInfo()
        student.name = name
        student.age = age
        student.gender = gender
        student.ban_id = Ban.objects.filter(banid = banid)[0].id  #-----
        student.save()

        # 创建学号对象
        studentid = StudentId()
        studentid.stuid = stuid
        studentid.student_id=student.id  # ------
        studentid.save()

        # 多表操作时，保存数据使用的是数据库中表的字段 通常是子表对象.关系字段_id = 主表对象.id
        # 而在获取主表数据时 通常是 子表对象.关系字段 == 主表对象

        return redirect(reverse('student:student_all'))



def student_delete(request,stuid):
    '''删除学生'''
    # 找到学生对象
    student = StudentInfo.objects.filter(id = int(stuid))[0]
    # 先删除学号
    StudentId.objects.filter(id = student.studentid.stuid).delete()
    # 再删除学生
    student.delete()
    return redirect(reverse('student:student_all'))

def student_update(request,stuid):
    '''修改学生'''
    if request.method == 'GET':
        all_bans = Ban.objects.filter()
        student = StudentInfo.objects.filter(id = int(stuid))[0]
        return render(request,'student_update.html',{
            'all_bans':all_bans,
            'student':student
        })
    else:
        name = request.POST.get('stuname',None)
        age = request.POST.get('stuage',None)
        gender = request.POST.get('stugender',None)
        banid = request.POST.get('stuban',None)
        stuid = request.POST.get('stuid',None)

        student = StudentInfo.objects.filter(id = int(stuid))[0]
        student.name=name
        student.age=age
        student.gender=gender
        student.ban_id=Ban.objects.filter(banid=banid)[0].id
        student.save()

        #  修改说明：这里修改数据  不涉及学号修改  因为这里是直接查找学号信息对象 没有新建对象
        # 如果原来没有这个学号信息，查找时会报错
        studentid = StudentId.objects.filter(stuid=stuid)[0]
        studentid.student_id = student.id
        studentid.save()
        return redirect(reverse('student:student_all'))