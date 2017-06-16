from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<report_id>\d+)/$', views.report, name='report'),
    url(r'^(?P<report_id>\d+)/(?P<format>\w+)/$', views.report, name='report'),
)
