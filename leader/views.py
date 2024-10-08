from django.contrib import messages
from django.shortcuts import redirect, render
from group.models import *
from user.models import *
# Create your views here.
def leader_login(request):
    if request.session.has_key('leader_mobile'):
        return redirect('leader_home')
    else:
        if request.method == "POST":
            number=request.POST ['number']
            pin=request.POST ['pin']
            l = Leader.objects.filter(mobile=number,pin=pin,status=1)
            if l:
                request.session['leader_mobile'] = request.POST["number"]
                return redirect('leader_home')
            else:
                messages.success(request,"please insert correct information or call more suport 9730991252")            
                return redirect('/leader/')

    return render(request,'leader/leader_login.html')


def leader_home(request):
    if request.session.has_key('leader_mobile'):
        mobile = request.session['leader_mobile']
        l = Leader.objects.filter(mobile=mobile).first()
        if l:
            group = Group.objects.filter(leader_id=l.id).first()
            if group:
                if 'send_image'in request.POST:
                    image = request.FILES.get("image")
                    Chat_images(
                        image=image,
                        leader_id=l.id,
                    ).save()                    
                    im = Chat_images.objects.filter(leader_id=l.id).last()
                    Chat_message(
                        group_id=group.id,
                        leader_id=l.id,
                        image_id=im.id,
                    ).save()                
                    return redirect('leader_home')
                if 'send'in request.POST:
                    message = request.POST.get('message')
                    Chat_message(
                        group_id = group.id,
                        leader_id=l.id,
                        msg=message,
                    ).save()
                    return redirect('leader_home')
                if 'edit'in request.POST:
                    id = request.POST.get('id')
                    message = request.POST.get('message')
                    msg = Chat_message.objects.filter(id=id).first()
                    msg.msg = message
                    msg.save()
                    return redirect('leader_home')
                if 'delete'in request.POST:
                    id = request.POST.get('id')
                    msg = Chat_message.objects.filter(id=id).first()
                    msg.self_remove_status = 0
                    msg.save()
                    return redirect('leader_home')
        contaxt={
            'l':l,
            'msg':Chat_message.objects.filter(leader_id=l.id, status=1, self_remove_status=1).order_by('-id')
        }
        return render(request,'leader/leader_home.html', contaxt)
    else:
        return redirect('/office/')
