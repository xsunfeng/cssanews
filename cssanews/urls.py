from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cssanews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace="news")),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    url(r'^login/$', views.login_view),
    url(r'^register/$', views.register_view),
    url(r'^logout/$', views.logout_view),
)
