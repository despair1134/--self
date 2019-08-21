from django.conf.urls import include, url
from django.contrib import admin
from user.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'day6.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name='index'),
    url(r'^user/',include('user.urls',namespace='user')),
    url(r'^student/',include('student.urls',namespace='student'))
]
