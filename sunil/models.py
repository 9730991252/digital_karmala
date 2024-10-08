from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Office_staff(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    pin = models.IntegerField()
    status = models.IntegerField(default=1)
    
