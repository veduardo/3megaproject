# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView

from models import Site, Report

class SiteList(ListView):
    model = Site

class SiteDetail(DetailView):
    model = Site

class Summary(ListView):
    model = Site
    template_name = 'reports/summary.html'