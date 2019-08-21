from django.conf.urls import include, url
from .views import user_register,user_logout,user_login

urlpatterns = [
    url(r'user_register/$',user_register,name='user_register'),
    url(r'user_login/$',user_login,name='user_login'),
    url(r'user_logout/$',user_logout,name='user_logout'),
]

