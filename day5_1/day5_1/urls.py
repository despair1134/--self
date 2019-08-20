from django.conf.urls import include, url
from django.contrib import admin
from user.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'day5_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name='index'),
    url(r'^student/',include('user.urls',namespace='user'))
]
