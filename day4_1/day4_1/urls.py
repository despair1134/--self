from django.conf.urls import include, url
from django.contrib import admin
from student.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'day4_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name='index'),
    url(r'^student/',include('student.urls',namespace='student'))
]
