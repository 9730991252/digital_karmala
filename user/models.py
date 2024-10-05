from django.db import models
from group.models import *
from ckeditor.fields import RichTextField
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    status = models.IntegerField(default=1)
    added_date = models.DateField(auto_now_add=True)
    village = models.ForeignKey(Village,on_delete=models.PROTECT,null=True)

class Select_user_group(models.Model):
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True)

class Chat_message(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    msg=RichTextField()
    date=models.DateField(auto_now_add=True,null=True)
    added_date=models.DateTimeField(auto_now_add=True,null=True)
    status = models.IntegerField(default=1)
    verify_status = models.IntegerField(default=1)
