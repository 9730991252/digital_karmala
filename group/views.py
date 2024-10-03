from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def group(request, id):
    if Leader.objects.filter(id=id).exists():
        group = Leader.objects.filter(id=id).first()
        check_leader_group(group.id)
    else:
        return redirect('/')
    context={
        'group':group
    }
    return render(request, 'group/group.html', context)

def check_leader_group(leader_id):
    if Group.objects.filter(leader_id=leader_id).exists():
        pass
    else:
        Group(
            leader_id=leader_id
        ).save()