from django.shortcuts import render, redirect
from .models import *
from user.views import *
from user.models import *
from channels.layers import get_channel_layer

# Create your views here.
def group(request, leader_id, village_id):
    if village_id == 0: #*run leader group
        if Leader.objects.filter(id=leader_id).exists():
            leader = Leader.objects.filter(id=leader_id).first()
            group = check_leader_group(leader.id)
            chat = Chat_message.objects.filter(group_id=group.id, status=1, verify_status=1)
            user = ''
            village = 0
            
            if request.session.has_key('user_mobile'):
                mobile = request.session['user_mobile']
                user = User.objects.filter(mobile=mobile, status=1).first()
                user_login = 1
                if user:
                    check_user_selected_leader_group(user.id, leader_id)
                if 'send_image'in request.POST:
                    image = request.FILES.get("image")
                    group_id = request.POST.get("group_id")
                    user_id = request.POST.get("user_id")
                    Chat_images(
                        user_id=user_id,
                        image=image
                    ).save()
                    im = Chat_images.objects.filter(user_id=user_id).last()
                    Chat_message(
                        group_id=group_id,
                        user_id=user_id,
                        image_id=im.id,
                    ).save()
                    

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
    if leader_id == 0: #*run village group
        if Village.objects.filter(id=village_id).exists():
            village = Village.objects.filter(id=village_id).first()
            group = check_village_group(village.id)
            chat = Chat_message.objects.filter(group_id=group.id, status=1, verify_status=1)
            mobile = request.session['user_mobile']
            user = User.objects.filter(mobile=mobile).first()
            check_user_selected_village_group(user.id, village_id)
            user_login = 1
            village = 1
        else:
            return redirect('/')
    context={
        'group':group,
        'user_login':user_login,
        'user':user,
        'taluka':Taluka.objects.filter(status=1),
        'village':village,
        'chat':chat
    }
    return render(request, 'group/group.html', context)









def check_leader_group(leader_id):
    if Group.objects.filter(leader_id=leader_id).exists():
        group = Group.objects.filter(leader_id=leader_id).first()
        return group
    else:
        Group(
            leader_id=leader_id
        ).save()
        group = Group.objects.filter(leader_id=leader_id).first()
        return group
        
def check_village_group(village_id):
    if Group.objects.filter(village_id=village_id).exists():
        group = Group.objects.filter(village_id=village_id).first()
        return group
    else:
        Group(
            village_id=village_id
        ).save()
        group = Group.objects.filter(village_id=village_id).first()
        return group
        
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