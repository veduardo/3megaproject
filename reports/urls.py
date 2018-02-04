from django.conf.urls import url, include
from django.contrib import admin

import reports.views as report_views

urlpatterns = [
    url(r'^sites/$', report_views.SiteList.as_view(), name='sites'),
    url(r'^sites/(?P<pk>\d+)/$', report_views.SiteDetail.as_view(), name='site_detail'),
    url(r'^summary/$', report_views.Summary.as_view(), name='summary'),
    url(r'^summary-average/$', report_views.Average, name='average'),
]