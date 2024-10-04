from django.shortcuts import render
from .models import *
# Create your views here.
def add_user(name, mobile, village):
    User(
        name=name,
        mobile=mobile,
        village_id=village
    ).save()
    