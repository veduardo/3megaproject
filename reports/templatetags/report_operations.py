from django import template

register = template.Library()

##
# Requirement about aggregations #1: implement one in Python code.
##
@register.filter(name='sum')
def sum(site, a=False):
    tmp = 0
    for record in site.report_set.all():
        if a:
            tmp += record.a_value
        else:
            tmp += record.b_value
    return tmp