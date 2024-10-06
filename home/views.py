from django.shortcuts import render
from group.models import *
from user.models import *

# Create your views here.
def index(request):
    #del request.session['user_mobile']
    Chat_message.objects.all().delete()
    context={
        'leader':Leader.objects.filter(status=1)
    }
    return render(request, 'home/index.html', context)