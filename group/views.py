from django.shortcuts import render, redirect
from .models import *
from user.views import *
from user.models import *
from channels.layers import get_channel_layer
from django.contrib import messages
# Create your views here.
def group(request, leader_id, village_id):
    user_login = ''
    user = ''
    if village_id == 0: #*run leader group
        if Leader.objects.filter(id=leader_id).exists():
            leader = Leader.objects.filter(id=leader_id).first()
            group = check_leader_group(leader.id)
            chat = Chat_message.objects.filter(status=1, verify_status=1, self_remove_status=1)
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
                    return redirect(f'/group/{leader_id}/0/')
                if 'remove_chat'in request.POST:
                    c=Chat_message.objects.filter(id=request.POST.get("chat_id")).first()
                    c.self_remove_status=0
                    c.save()
                    return redirect(f'/group/{leader_id}/0/')

            else:
                user_login = 0
            if 'Add_User'in request.POST:
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                village = request.POST.get('village')
                if village == '':
                    messages.success(request,"success") 
                else:
                    add_user(name, mobile, village)
                    request.session['user_mobile'] = mobile
                    return redirect(f'/group/{leader_id}/0/')
                
        else:
            return redirect('/')
    if leader_id == 0: #*run village group
        if Village.objects.filter(id=village_id).exists():
            village = Village.objects.filter(id=village_id).first()
            group = check_village_group(village.id)
            chat = Chat_message.objects.filter(status=1, verify_status=1,  self_remove_status=1)
            if request.session.has_key('user_mobile'):
                mobile = request.session['user_mobile']
                user = User.objects.filter(mobile=mobile).first()
                check_user_selected_village_group(user.id, village_id)
                user_login = 1
                village = 1
                if 'remove_chat'in request.POST:
                    c=Chat_message.objects.filter(id=request.POST.get("chat_id")).first()
                    c.self_remove_status=0
                    c.save()
                    return redirect(f'/group/0/{village_id}/')
            else:
                user_login = 0
        else:
            return redirect('/')
    context={
        'group':group,
        'user_login':user_login,
        'user':user,
        'taluka':Taluka.objects.filter(status=1),
        'village':village,
        'chat':chat,
        'video':Group_video.objects.filter(group_id=group.id, status=1).first()
    }
    return render(request, 'group/group.html', context)









def check_leader_group(leader_id):
    if Group.objects.filter(leader_id=leader_id).exists():
        group = Group.objects.filter(leader_id=leader_id).first()
        page_count(group.id)
        return group
    else:
        Group(
            leader_id=leader_id
        ).save()
        group = Group.objects.filter(leader_id=leader_id).first()
        page_count(group.id)
        return group
        
def check_village_group(village_id):
    if Group.objects.filter(village_id=village_id).exists():
        group = Group.objects.filter(village_id=village_id).first()
        page_count(group.id)
        return group
    else:
        Group(
            village_id=village_id
        ).save()
        group = Group.objects.filter(village_id=village_id).first()
        page_count(group.id)
        return group
        
def page_count(group_id):
    if group_id:
        if Page_count.objects.filter(group_id=group_id).exists():
            p = Page_count.objects.filter(group_id=group_id).first()
            p.count += 1
            p.save()
        else:
            Page_count(
                group_id=group_id,
                count=1
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