from django.urls import path
from . import views

urlpatterns = [
    path('<int:leader_id>/<int:village_id>/', views.group, name='group')
]
