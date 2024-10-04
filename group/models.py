from django.db import models

# Create your models here.
class Leader(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    
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
    
