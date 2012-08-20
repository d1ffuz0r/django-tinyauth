# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns('',)
if settings.DEBUG:
    urlpatterns += patterns('django_tinyauth.views',
        url(r'^admin/$', 'adminlogin', name='adminlogin'),
        url(r'^admin/tinylogin/(\d+)/$', 'tinylogin', name='tinylogin')
    )
