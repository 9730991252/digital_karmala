from django.db import models
from PIL import Image
from embed_video.fields import EmbedVideoField

# Create your models here.
class Leader(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    pin = models.IntegerField(null=True)
    added_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    image = models.ImageField(upload_to="leader_images",default="",null=True, blank=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        image = Image.open(self.image.path)
        output_size = (300,300)
        image.thumbnail(output_size)
        image.save(self.image.path)
        
class Taluka(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    
class Village(models.Model):
    taluka = models.ForeignKey(Taluka,on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    
class Group(models.Model):
    leader = models.ForeignKey(Leader,on_delete=models.PROTECT,null=True)
    village = models.ForeignKey(Village,on_delete=models.PROTECT,null=True)
    status = models.IntegerField(default=1)
    added_date = models.DateField(auto_now_add=True)
    
class Group_video(models.Model):
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    code = EmbedVideoField()
    status = models.IntegerField(default=1)