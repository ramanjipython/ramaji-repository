from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'khyaathi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','tcloud.views.hellow',name='hellow'),
    url(r'^student/','tcloud.views.Student',name='student'),
    url(r'^status/','tcloud.views.Joined',name='status'),
]
