from django.http import *
from django.template.loader import *
from django.shortcuts import *
from user.models import *
from group.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def check_mobile_number(request):
    if request.method == 'GET':
        mobile_number = request.GET['mobile_number']
        if User.objects.filter(mobile=mobile_number, status=1).exists():
            request.session['user_mobile'] = mobile_number
            status = 1
        else:
            status = 0
        #t = render_to_string('ajax/office/fetch_batch.html', context)
    return JsonResponse({'status': status, 'mobile_number':mobile_number})

def check_taluka_village(request):
    if request.method == 'GET':
        id = request.GET['id']
        village = Village.objects.filter(taluka_id=id).order_by('name')
        context={
            'village':village
        }
        t = render_to_string('ajax/user/check_taluka_village.html', context)
    return JsonResponse({'village_list': t})

def like_chat_count(request):
    if request.method == 'GET':
        chat_id = request.GET['chat_id']
        user_id = request.GET['user_id']
        if Chat_like.objects.filter(chat_id=chat_id, user_id=user_id, like_status=1).exists():
            chat = Chat_like.objects.filter(chat_id=chat_id, user_id=user_id).first()
            chat.like_status = 0
            chat.save()
        else:
            if Chat_like.objects.filter(chat_id=chat_id, user_id=user_id, like_status=0).exists():
                chat = Chat_like.objects.filter(chat_id=chat_id, user_id=user_id).first()
                chat.like_status = 1
                chat.save()
            else:
                Chat_like(
                    user_id = user_id,
                    chat_id = chat_id,
                    like_status = 1
                ).save()
        if Chat_like.objects.filter(chat_id = chat_id , user_id = user_id, like_status = 1).exists():
            status = 'yes'
        if Chat_like.objects.filter(chat_id = chat_id , user_id = user_id, like_status = 0).exists():
            status = 'no'
        count = Chat_like.objects.filter(chat_id = chat_id, like_status = 1).count()
        context={
            'count':count,
            'status':status,
        }
        t = render_to_string('inclusion_tag/group/user_chat_like.html', context)
    return JsonResponse({'t': t})

def check_taluka_village_index(request):
    if request.method == 'GET':
        id = request.GET['id']
        village = Village.objects.filter(taluka_id=id).order_by('name')
        context={
            'village':village
        }
        t = render_to_string('ajax/home/check_taluka_village_index.html', context)
    return JsonResponse({'village_list': t})

def show_hide_chat_office(request):
    if request.method == 'GET':
        id = request.GET['chat_id']
        status = request.GET['status']
        print(status)
        if status == '1':
            #print(id)
            ac=Chat_message.objects.get(id=id)
            ac.status= '0'
            ac.save()
        elif status == '0':
            ac=Chat_message.objects.get(id=id)
            ac.status = '1'
            ac.save() 
        m=Chat_message.objects.get(id=id)
        context={
            'm':m
        }
        t = render_to_string('ajax/office/show_hide_chat_office.html', context)
    return JsonResponse({'t': t})

@csrf_exempt
def image_save_user(request):
    if request.method == 'POST':
        im = request.FILES.get('low_size')
        group_id = request.POST.get('group_id')
        user_id = request.POST.get('user_id')
        Chat_images(
            user_id=user_id,
            image=im
        ).save()
        im = Chat_images.objects.filter(user_id=user_id).last()
        Chat_message(
            group_id=group_id,
            user_id=user_id,
            image_id=im.id,
        ).save()
        status = 'ok'
    else:
        status = 'false'
        
    return JsonResponse({'status':status})