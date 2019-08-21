from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import StudentInfo,StudentId,Banclass
# Create your views here.
@login_required(login_url='/user/user_login/')
def student_all(request):
    '''查看所有学生'''
    all_students = StudentInfo.objects.all()
    return render(request,'student_list.html',{
        'all_students':all_students
    })

@login_required(login_url='/user/user_login/')
def student_add(request):
    '''添加学生'''
    if request.method == 'GET':
        return render(request,'student_add.html',{
            'all_bans':Banclass.objects.all()
        })
    else:
        stuname = request.POST.get('stuname', None)
        stuage = request.POST.get('stuage', None)
        stugender = request.POST.get('stugender', None)
        stuban = request.POST.get('stuban', None)
        stuuid = request.POST.get('stuuid', None)

        student = StudentInfo()
        student.name = stuname
        student.age = stuage
        student.gender = stugender
        student.ban_id = Banclass.objects.filter(banname=stuban)[0].id
        student.save()

        studentid = StudentId()
        studentid.student_id = student.id
        studentid.stuid = stuuid
        studentid.save()

        return redirect(reverse('student:student_all'))
@login_required(login_url='/user/user_login/')
def student_del(request,stuid):
    '''删除学生'''
    student = StudentInfo.objects.filter(id = int(stuid))[0]
    student.studentid.delete()
    student.delete()
    return redirect(reverse('student:student_all'))

@login_required(login_url='/user/user_login/')
def student_update(request,stuid):
    '''修改学生'''
    if request.method == 'GET':
        student = StudentInfo.objects.filter(id = int(stuid))[0]
        all_bans = Banclass.objects.all()
        return render(request,'student_update.html',{
            'student':student,
            'all_bans':all_bans
        })
    else:
        stuname = request.POST.get('stuname',None)
        stuage = request.POST.get('stuage',None)
        stugender = request.POST.get('stugender',None)
        stuban = request.POST.get('stuban',None)
        stuuid = request.POST.get('stuuid',None)

        student = StudentInfo.objects.filter(id = int(stuid))[0]
        student.name = stuname
        student.age = stuage
        student.gender = stugender
        student.ban_id = Banclass.objects.filter(banname=stuban)[0].id
        student.save()

        studentid = student.studentid
        studentid.student_id = student.id
        studentid.stuid = stuuid
        studentid.save()

        return redirect(reverse('student:student_all'))
