from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def user_login(request):
    if request.method == 'GET':
        return render(request,'user_login.html')
    else:
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        res = authenticate(username = username,password=password)
        if res:
            # 这个方法本质是写session
            login(request,res)
            return redirect(reverse('index'))
        else:
            msg = '用户名或密码错误'
            return render(request,'user_login.html',{
                'msg':msg
            })
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))

def user_register(request):
    if request.method == 'GET':
        return render(request,'user_register.html')
    else:
        username = request.POST.get('username',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2',None)

        user = User.objects.filter(username = username)
        if user:
            return render(request, 'user_register.html', {
                'msg': '该用户已存在'
            })
        else:
            if password1 == password2:
                user = User()
                user.username = username
                user.password = password1
                user.set_password(password1)
                user.save()
                return redirect(reverse('user:user_login'))
            else:
                return render(request,'user_register.html',{
                    'msg':'两次输入的密码不一致'
                })