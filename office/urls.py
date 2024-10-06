from django.urls import path
from . import views

urlpatterns = [
    path('', views.office_login, name='office_login'),
    path('office_home/', views.office_home, name='office_home'),

]
