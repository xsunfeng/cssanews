from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cssanews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace="news")),
)
