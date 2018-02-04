# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, connection

class Site(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "%s" % self.name

class Report(models.Model):
    name = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    a_value = models.PositiveIntegerField(default=0)
    b_value = models.PositiveIntegerField(default=0)


##
# Helper functions
##

# Source:
# https://docs.djangoproject.com/en/1.11/topics/db/sql/#executing-custom-sql-directly
def dict_fetchall(cursor):
    """
    Returns all rows from a cursor as a dict,
    adding their respective field name.
    """
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def get_sites_avg():
    """
    Query the database for the name of the sites, and
    the average of their respective a_value and b_value.
    """
    raw_sql = 'SELECT name, AVG(a_value) as a_value, AVG(b_value) as b_value \
                FROM reports_report as r, reports_site as s \
                WHERE r.name_id = s.id GROUP BY s.id;'

    with connection.cursor() as c:
        c.execute(raw_sql)
        res = dict_fetchall(c)
    return res