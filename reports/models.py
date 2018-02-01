# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "%s" % self.name

class Report(models.Model):
    name = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    a_value = models.PositiveIntegerField(default=0)
    b_value = models.PositiveIntegerField(default=0)