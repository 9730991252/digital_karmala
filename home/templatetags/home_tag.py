from django import template
from user.models import *
from group.models import *
from datetime import timedelta, date
register = template.Library()

@register.simple_tag
def user_count_group(group_id):
    count = Select_user_group.objects.filter(group_id=group_id).count()
    return count

@register.simple_tag
def leader_page_count(leader_id):
    g = Group.objects.filter(leader_id=leader_id).first()
    if g:
        p = Page_count.objects.filter(group_id=g.id).first()
    if p == None:
        p = 0
        return p
    else:
        return p.count
    
@register.simple_tag
def group_page_count(group_id):
    if group_id:
        p = Page_count.objects.filter(group_id=group_id).first()
    if p == None:
        p = 0
        return p
    else:
        return p.count


@register.simple_tag
def user_count_group_home(id):
    count = Select_user_group.objects.filter(group__leader_id=id).count()
    return count


@register.simple_tag
def sms_count_group(leader_id):
    group = Group.objects.filter(leader_id=leader_id).first()
    if group:
        count = Chat_message.objects.filter(group_id=group.id).count()
        return count
    
    
@register.inclusion_tag('inclusion_tag/group/user_chat_like.html')
def user_chat_like(chat_id, user_id):
    status = ''
    if user_id:
        if Chat_like.objects.filter(chat_id = chat_id , user_id = user_id, like_status = 1).exists():
            status = 'yes'
        if Chat_like.objects.filter(chat_id = chat_id , user_id = user_id, like_status = 0).exists():
            status = 'no'
    count = Chat_like.objects.filter(chat_id = chat_id, like_status = 1).count()
    return {
        'count':count,
        'status':status,
        
    }
    
@register.simple_tag
def chat_like_leader(chat_id):
    if chat_id:
        like = Chat_like.objects.filter(chat_id=chat_id).count()
        return like