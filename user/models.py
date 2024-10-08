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

class Chat_images(models.Model):
    user_id = models.IntegerField(null=True)
    image = models.ImageField(upload_to="chat_images",default="",null=True, blank=True) 
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        image = Image.open(self.image.path)
        print('image...',image)
        output_size = (300,300)
        image.thumbnail(output_size)
        image.save(self.image.path)

class Chat_message(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE, null=True)
    image=models.ForeignKey(Chat_images,on_delete=models.CASCADE,null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    leader=models.ForeignKey(Leader,on_delete=models.CASCADE, null=True)
    msg=RichTextField(null=True,blank=True)
    date=models.DateField(auto_now_add=True,null=True)
    added_date=models.DateTimeField(auto_now_add=True,null=True)
    status = models.IntegerField(default=1)
    verify_status = models.IntegerField(default=1, null=True)
    self_remove_status = models.IntegerField(default=1, null=True)
    post_typing_status = models.IntegerField(default=1, null=True) #0 == post , 1 == msg
    advertise = models.IntegerField(default=0, null=True) #0 == post , 1 == msg

class Chat_like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat_message,on_delete=models.CASCADE)
    like_status = models.IntegerField(default=0)
    