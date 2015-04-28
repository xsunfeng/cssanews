from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cssanews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^edit/$', views.edit, name='edit'),
	url(r'^add/$', views.add, name='add'),
	url(r'^list/$', views.list, name='list'),
	url(r'^(?P<news_id>[0-9]+)/$', views.detail, name='detail'),
	
)