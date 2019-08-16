from django.conf.urls import include, url
from .views import student_add,student_del,student_update,student_all

urlpatterns = [
    url(r'^student_add/$',student_add,name='student_add'),
    url(r'^student_del/(\d+)$',student_del,name='student_del'),
    url(r'^student_update/(\d+)$',student_update,name='student_update'),
    url(r'^student_all/$',student_all,name='student_all')
]
