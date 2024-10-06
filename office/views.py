from django.contrib import messages
from django.shortcuts import redirect, render
from sunil.models import *
from user.models import *
# Create your views here.
def office_login(request):
    if request.session.has_key('office_mobile'):
        return redirect('office_dashboard')
    else:
        if request.method == "POST":
            number=request.POST ['number']
            pin=request.POST ['pin']
            e= Office_staff.objects.filter(mobile=number,pin=pin,status=1)
            if e:
                request.session['office_mobile'] = request.POST["number"]
                return redirect('office_home')
            else:
                messages.success(request,"please insert correct information or call more suport 9730991252")            
                return redirect('/office/')

    return render(request,'office/office_login.html')

def office_home(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        o = Office_staff.objects.filter(mobile=mobile).first()
        if o:
            if "show" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Chat_message.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "hide" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Chat_message.objects.get(id=id)
                ac.status='1'
                ac.save() 
        contaxt={
            'o':o,
            'message':Chat_message.objects.all()
        }
        return render(request,'office/office_home.html', contaxt)
    else:
        return redirect('/office/')