from django.http import *
from django.template.loader import *
from django.shortcuts import *
from user.models import *
from group.models import *
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