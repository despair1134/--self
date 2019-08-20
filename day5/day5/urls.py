from django.conf.urls import include, url
from django.contrib import admin
from user.views import index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name='index'),
    url(r'^user/',include('user.urls',namespace='user'))
]
