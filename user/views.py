from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def user_register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password1 = request.POST.get('password1',None)

        user = User.objects.filter(username = username)
        if user:
            return render(request, 'register.html', {
                'msg': '用户已存在'
            })
        else:
            if password == password1:
                user = User()
                user.username = username
                user.password = password
                user.set_password(password)
                user.save()
                return redirect(reverse('user:user_login'))
            else:
                return render(request, 'register.html', {
                    'msg': '两次输入的密码不一致'
                })

def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        #  如果这个地方使用authenticate方法验证  在注册逻辑中 必须使用set_password方法
        a = authenticate(username=username,password=password)
        if a:
            login(request,a)
            return redirect(reverse('index'))
        else:
            return render(request, 'login.html', {
                'msg': '用户名或密码错误'
            })


def user_logout(request):
    logout(request)
    return redirect(reverse('index'))