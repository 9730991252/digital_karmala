from django.urls import path
from . import views

urlpatterns = [
    path('check_mobile_number/', views.check_mobile_number, name='check_mobile_number'),
    path('check_taluka_village/', views.check_taluka_village, name='check_taluka_village'),
    path('like_chat_count/', views.like_chat_count, name='like_chat_count'),
    path('check_taluka_village_index/', views.check_taluka_village_index, name='check_taluka_village_index'),
    path('show_hide_chat_office/', views.show_hide_chat_office, name='show_hide_chat_office'),
    
]
