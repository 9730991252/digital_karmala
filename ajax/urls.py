from django.urls import path
from . import views

urlpatterns = [
    path('check_mobile_number/', views.check_mobile_number, name='check_mobile_number'),
    path('check_taluka_village/', views.check_taluka_village, name='check_taluka_village'),
    path('like_chat_count/', views.like_chat_count, name='like_chat_count'),
    
]
