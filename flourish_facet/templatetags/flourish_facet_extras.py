from datetime import datetime
from urllib.parse import unquote, urlencode

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from edc_base.utils import age, get_utcnow
from edc_visit_schedule.models import SubjectScheduleHistory

register = template.Library()


@register.filter
def get_item(dictionary, key):
    if dictionary is not None:
        # breakpoint()
        return dictionary.get(key)

@register.inclusion_tag('flourish_facet/buttons/consent_button.html')
def consent_button(model_wrapper):

    return dict(
        title='title',
        model_wrapper = model_wrapper)