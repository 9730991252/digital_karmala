from django.urls import path
from . import views

urlpatterns = [
    path('', views.leader_login, name="leader_login"),
    path('leader_home', views.leader_home, name="leader_home"),
]
