from django.test import TestCase

# Create your tests here.
# Create your views here.
def group(request, leader_id, village_id):
    if village_id == 0: #*run leader group
        if Leader.objects.filter(id=leader_id).exists():
            group = Group.objects.filter(leader_id=leader_id).first()
            check_leader_group(group.id)
            user = ''
            village = 0
            if request.session.has_key('user_mobile'):
                mobile = request.session['user_mobile']
                user = User.objects.filter(mobile=mobile).first()
                user_login = 1
                check_user_selected_leader_group(user.id, leader_id)
            else:
                user_login = 0
            if 'Add_User'in request.POST:
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                village = request.POST.get('village')
                add_user(name, mobile, village)
                request.session['user_mobile'] = mobile
                return redirect(f'/group/{leader_id}/0/')
                
        else:
            return redirect('/')
    if leader_id == 0: #*run village group
        if Village.objects.filter(id=village_id).exists():
            group = Group.objects.filter(village_id=village_id).first()
            check_village_group(group.id)
            mobile = request.session['user_mobile']
            user = User.objects.filter(mobile=mobile).first()
            check_user_selected_village_group(user.id, village_id)
            user_login = 1
            village = 1
        else:
            return redirect('/')
    context={
        'group':group,
        'user_login':user_login,
        'user':user,
        'taluka':Taluka.objects.filter(status=1),
        'village':village,
    }
    return render(request, 'group/group.html', context)
