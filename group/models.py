from django.db import models

# Create your models here.
class Leader(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()