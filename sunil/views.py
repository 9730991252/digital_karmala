from django.contrib import messages
from django.shortcuts import redirect, render
from group.models import *
from user.models import Chat_message
from .models import *
# Create your views here.
def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["number"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 10000 :
            request.session['sunil_mobile'] = s
            return redirect('sunil_home')
        else:
            return redirect('sunil_login')
    return render(request, 'sunil/sunil_login.html')



def sunil_home(request):
    if request.session.has_key('sunil_mobile'):
        context={}
        return render(request, 'sunil/sunil_home.html', context)
    else:
        return redirect('sunil_login')
def office_staff(request):
    if request.session.has_key('sunil_mobile'):
        context={}
        if 'Add_staff'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if Office_staff.objects.filter(mobile=mobile).exists():
                messages.warning(request,"Already Exists")  
            else:
                Office_staff(
                    name=name,
                    mobile=mobile,
                    pin=pin,
                ).save()
                messages.success(request,"success")  
            return redirect('office_staff')
        if 'edit_staff'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            office_staff = Office_staff.objects.get(id=id)
            office_staff.name = name
            office_staff.mobile = mobile
            office_staff.pin = pin
            office_staff.save()
            return redirect('office_staff')
        context={
            'staff':Office_staff.objects.all()
        }
        return render(request, 'sunil/office_staff.html', context)
    else:
        return redirect('sunil_login')
    
def leader(request):
    if request.session.has_key('sunil_mobile'):
        context={}
        if 'Add_leader'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            image = request.FILES.get("image")
            if Leader.objects.filter(mobile=mobile).exists():
                messages.warning(request,"Already Exists")  
            else:
                Leader(
                    name=name,
                    mobile=mobile,
                    pin=pin,
                    status=1,
                    image=image,
                ).save()
                messages.success(request,"success")  
            return redirect('leader')
        if 'edit_leader'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            image = request.FILES.get("image")
            leader = Leader.objects.get(id=id)
            leader.name = name
            leader.mobile = mobile
            leader.pin = pin
            if image != None:
                leader.image = image
            else:
                leader.image = leader.image
            leader.save()
            return redirect('leader')
        ### end if
        context={
            'leader':Leader.objects.all()
        }
        return render(request, 'sunil/leader.html', context)
    else:
        return redirect('sunil_login')
    
def taluka(request):
    if request.session.has_key('sunil_mobile'):
        if 'Add_Taluka'in request.POST:
            name = request.POST.get('name').upper()
            if Taluka.objects.filter(name=name).exists():
                messages.warning(request,"Already Exists")  
            else:
                Taluka(
                    name=name,
                ).save()
                messages.success(request,"success")  
            return redirect('taluka')
        if 'edit_taluka'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name').upper()
            taluka = Taluka.objects.get(id=id)
            taluka.name = name
            taluka.save()
            return redirect('taluka')
        context={
            'taluka':Taluka.objects.all()
        }
        return render(request, 'sunil/taluka.html', context)
    else:
        return redirect('sunil_login')
    
    
def village(request):
    if request.session.has_key('sunil_mobile'):
        if 'Add_village'in request.POST:
            name = request.POST.get('name').upper()
            taluka = request.POST.get('taluka')
            if Village.objects.filter(name=name).exists():
                messages.warning(request,"Already Exists")  
            else:
                Village(
                    name=name,
                    taluka_id=taluka,
                ).save()
                messages.success(request,"success")  
            return redirect('village')
        if 'edit_village'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name').upper()
            taluka = request.POST.get('taluka')
            village = Village.objects.get(id=id)
            village.name = name
            village.taluka_id = taluka
            village.save()
            return redirect('village')
        context={
            'village':Village.objects.all().order_by('name'),
            'taluka':Taluka.objects.all()
        }
        return render(request, 'sunil/village.html', context)
    else:
        return redirect('sunil_login')

def add_video(request):
    if request.session.has_key('sunil_mobile'):
        if "add_code"in request.POST:
            group_id = request.POST.get('group_id')
            code = request.POST.get('code')
            if group_id:
                Group_video(
                    group_id=group_id,
                    code=code
                ).save()
                return redirect('add_video')
        
        if "active" in request.POST:
            id=request.POST.get('id')
            #print(id)
            c=Group_video.objects.get(id=id)
            c.status='0'
            c.save()
        elif "deactive" in request.POST:
            id=request.POST.get('id')
            #print(id)
            c=Group_video.objects.get(id=id)
            c.status='1'
            c.save() 
        if "edit_code"in request.POST:
            id = request.POST.get('id')
            group_id = request.POST.get('group_id')
            code = request.POST.get('code')
            if group_id:
                Group_video(
                    id=id,
                    group_id=group_id,
                    code=code
                ).save()
                return redirect('add_video')
        context={
            'group':Group.objects.filter(status=1).order_by('-leader_id'),
            'code':Group_video.objects.all(),
        }
        return render(request, 'sunil/add_video.html', context)
    else:
        return redirect('sunil_login')


def advertise(request):
    if request.session.has_key('sunil_mobile'):
        if 'send'in request.POST:
            message = request.POST.get('message')
            Chat_message(
                msg=message,
                advertise = 1
            ).save()
            return redirect('advertise')
        if 'edit'in request.POST:
            id = request.POST.get('id')
            message = request.POST.get('message')
            msg = Chat_message.objects.filter(id=id).first()
            msg.msg = message
            msg.save()
            return redirect('advertise')
        if 'delete'in request.POST:
            id = request.POST.get('id')
            msg = Chat_message.objects.filter(id=id).first()
            msg.self_remove_status = 0
            msg.save()
            return redirect('advertise')
        context={
            'msg':Chat_message.objects.filter(advertise=1, self_remove_status=1)
        }
        return render(request, 'sunil/advertise.html', context)
    else:
        return redirect('sunil_login')
