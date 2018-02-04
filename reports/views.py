# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView

from models import Site, Report, get_sites_avg

#
# Class Based Views
#
class SiteList(ListView):
    model = Site

class SiteDetail(DetailView):
    model = Site

class Summary(ListView):
    model = Site
    template_name = 'reports/summary.html'

#
# Function Based Views
#
def Average(request):
    if request.method == 'GET':
        sites = get_sites_avg()

    return render(request, 'reports/average.html', {'sites':sites})