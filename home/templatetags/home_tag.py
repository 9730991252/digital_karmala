from django import template
from user.models import *
from group.models import *
from datetime import timedelta, date
register = template.Library()

@register.simple_tag
def user_count_group(leader_id):
    count = Select_user_group.objects.filter(group__leader_id=leader_id).count()
    return count