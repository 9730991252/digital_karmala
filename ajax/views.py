from django.http import *
from django.template.loader import *
from django.shortcuts import *
from user.models import *
from group.models import *
# Create your views here.
def check_mobile_number(request):
    if request.method == 'GET':
        mobile_number = request.GET['mobile_number']
        if User.objects.filter(mobile=mobile_number).exists():
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