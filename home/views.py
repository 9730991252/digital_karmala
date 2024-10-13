from django.shortcuts import render
from group.models import *
from user.models import *

# Create your views here.
def index(request):
    context={
        'leader':Leader.objects.filter(status=1),
        'taluka':Taluka.objects.all()
    }
    return render(request, 'home/index.html', context)

def contact_us(request):
    return render(request, 'home/contact_us_f.html')
def about_us(request):
    return render(request, 'home/about_us1.html')
def features(request):
    return render(request, 'home/features.html')
def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')
def terms_of_service(request):
    return render(request, 'home/terms_of_service.html')
def disclaimer(request):
    return render(request, 'home/disclaimer.html')