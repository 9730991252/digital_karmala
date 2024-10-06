from django import template
from user.models import *
from group.models import *
from datetime import timedelta, date
register = template.Library()

@register.simple_tag
def user_count_group(leader_id):
    count = Select_user_group.objects.filter(group__leader_id=leader_id).count()
    return count

@register.simple_tag
def sms_count_group(leader_id):
    group = Group.objects.filter(leader_id=leader_id).first()
    if group:
        count = Chat_message.objects.filter(group_id=group.id).count()
        return count