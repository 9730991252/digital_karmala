from django.urls import path
from . import views

urlpatterns = [
    path('', views.sunil_login, name='sunil_login'),
    path('sunil_home/', views.sunil_home, name='sunil_home'),
    path('office_staff/', views.office_staff, name='office_staff'),
    path('leader/', views.leader, name='leader'),
    path('taluka/', views.taluka, name='taluka'),
    path('village/', views.village, name='village'),
    path('advertise/', views.advertise, name='advertise'),
    path('add_video/', views.add_video, name='add_video'),
]
