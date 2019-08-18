from django.conf.urls import include, url
from .views import student_all,student_update,student_add,student_delete

urlpatterns = [
    # Examples:
    # url(r'^$', 'day4_3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^student_all/$',student_all,name='student_all'),
    url(r'^student_update/(\d+)/$',student_update,name='student_update'),
    url(r'^student_add/$', student_add, name='student_add'),
    url(r'^student_delete/(\d+)/$', student_delete, name='student_delete'),

]
