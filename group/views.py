from django.shortcuts import render, redirect
from .models import *
from user.views import *
from user.models import *
# Create your views here.
def group(request, leader_id):
    if Leader.objects.filter(id=leader_id).exists():
        group = Group.objects.filter(leader_id=leader_id).first()
        check_leader_group(group.id)
        user = ''
        village = 0
        if request.session.has_key('user_mobile'):
            mobile = request.session['user_mobile']
            user = User.objects.filter(mobile=mobile).first()
            user_login = 1
            check_user_selected_leader_group(user.id, leader_id)
        else:
            user_login = 0
        if 'Add_User'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            village = request.POST.get('village')
            add_user(name, mobile, village)
            request.session['user_mobile'] = mobile
            return redirect(f'/group/{leader_id}/0/')
            
    else:
        return redirect('/')
    context={
        'group':group,
        'user_login':user_login,
        'user':user,
        'taluka':Taluka.objects.filter(status=1),
        'village':village,
    }
    return render(request, 'group/group.html', context)

def check_leader_group(leader_id):
    if Group.objects.filter(leader_id=leader_id).exists():
        pass
    else:
        Group(
            leader_id=leader_id
        ).save()
        
def check_village_group(village_id):
    if Group.objects.filter(village_id=village_id).exists():
        pass
    else:
        Group(
            village_id=village_id
        ).save()
        
def check_user_selected_leader_group(user_id, leader_id):
    if Group.objects.filter(leader_id=leader_id).exists():
        group = Group.objects.filter(leader_id=leader_id).first()
        if Select_user_group.objects.filter(user_id=user_id, group_id=group.id).exists():
            pass
        else:
            Select_user_group(
                user_id=user_id,
                group_id=group.id
            ).save()
            
def check_user_selected_village_group(user_id, village_id):
    if Group.objects.filter(village_id=village_id).exists():
        group = Group.objects.filter(village_id=village_id).first()
        if Select_user_group.objects.filter(user_id=user_id, group_id=group.id).exists():
            pass
        else:
            Select_user_group(
                user_id=user_id,
                group_id=group.id
            ).save()