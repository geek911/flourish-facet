from datetime import datetime
from urllib.parse import unquote, urlencode

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from edc_base.utils import age, get_utcnow
from edc_visit_schedule.models import SubjectScheduleHistory
from dateutil.relativedelta import relativedelta

register = template.Library()


@register.filter
def get_item(dictionary, key):
    if dictionary is not None:

        return dictionary.get(key)


@register.inclusion_tag('flourish_facet/buttons/consent_button.html')
def consent_button(model_wrapper):

    return dict(
        title='title',
        model_wrapper=model_wrapper)


@register.inclusion_tag('flourish_facet/buttons/listboard_button.html')
def listboard_button(title, href, exists):

    return dict(
        href=href,
        title=title,
        exists=exists)
