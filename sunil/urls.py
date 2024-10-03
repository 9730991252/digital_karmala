from django.urls import path
from . import views

urlpatterns = [
    path('', views.sunil_login, name='sunil_login'),
    path('sunil_home/', views.sunil_home, name='sunil_home'),
    path('office_staff/', views.office_staff, name='office_staff'),
    path('leader/', views.leader, name='leader'),
]
