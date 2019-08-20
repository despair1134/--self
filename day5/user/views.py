from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import UserProfile
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    '''首页'''
    uname = request.session.get('uname',None)
    # request.session.flush()
    # uname = request.COOKIES.get('uname',None)
    return render(request,'index.html',{
        'uname':uname
    })

def user_register(request):
    '''注册'''
    if request.method == 'GET':
        return render(request,'user_register.html')
    else:
        username = request.POST.get('username',None)
        password1 =request.POST.get('password1',None)
        password2 = request.POST.get('password2',None)

        user = UserProfile.objects.filter(username = username)
        if user:
            # 用户存在
            msg = '用户已存在，请重新注册'
            return render(request,'user_register.html',{
                'msg':msg
            })
        else:
            if password1 == password2:
                user = UserProfile()
                user.username = username
                user.password = password1
                user.save()
                return redirect(reverse('index'))
            else:
                msg = '两次输入的密码不一致  请重新注册'
                return render(request, 'user_register.html', {
                    'msg': msg
                })


def user_login(request):
    '''登录'''
    if request.method == 'GET':
        usercheck = request.COOKIES.get('usercheck',None)
        username = request.COOKIES.get('uname','')
        return render(request,'user_login.html',{
            'usercheck':usercheck,
            'username':username
        })
    else:
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        usercheck = request.POST.get('usercheck',None)

        user = UserProfile.objects.filter(username = username)
        if user:
            if password == user[0].password:
                request.session['uname'] = username
                # request.session.set_expiry(5)
                # return redirect(reverse('index'))
                #

                ret = HttpResponseRedirect(reverse('index'))
                if usercheck:
                    ret.set_cookie('uname',username,max_age=60)
                    ret.set_cookie('usercheck',usercheck,max_age=60)

                else:
                    ret.delete_cookie('uname')
                    ret.delete_cookie('usercheck')
                return ret
            else:
                msg = '密码不正确'
                return render(request,'user_login.html',{
                    'msg':msg
                })
        else:
            msg = '用户不存在'
            return render(request,'user_login.html',{
                'msg':msg
            })

def user_logout(request):
    # 清除所有会话
    request.session.clear()
    # 删除cookie
    ret = HttpResponseRedirect(reverse('index'))
    ret.delete_cookie('uname')
    return ret