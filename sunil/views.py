from django.contrib import messages
from django.shortcuts import redirect, render
from group.models import *
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
        return render(request, 'sunil/office_staff.html', context)
    else:
        return redirect('sunil_login')
    
def leader(request):
    if request.session.has_key('sunil_mobile'):
        context={}
        if 'Add_leader'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            if Leader.objects.filter(mobile=mobile).exists():
                messages.warning(request,"Already Exists")  
            else:
                Leader(
                    name=name,
                    mobile=mobile,
                    status=1,
                ).save()
                messages.success(request,"success")  
            return redirect('leader')
        if 'edit_leader'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            leader = Leader.objects.get(id=id)
            leader.name = name
            leader.mobile = mobile
            leader.save()
            return redirect('leader')
        ### end if
        context={
            'leader':Leader.objects.all()
        }
        return render(request, 'sunil/leader.html', context)
    else:
        return redirect('sunil_login')