from django.conf.urls import include, url
from django.contrib import admin
from .views import user_login,user_logout,user_register

urlpatterns = [
    url(r'^user_login/$',user_login,name='user_login'),
    url(r'^user_logout/$',user_logout,name='user_logout'),
    url(r'^user_register/$',user_register,name='user_register')
]
