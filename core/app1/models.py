from django.db import models

# Create your models here.

class Datas(models.Model):
  userId = models.CharField(max_length=20,default="")
  fileName = models.CharField(max_length=50,default="")
  createdTimeStamp=models.TimeField(auto_now_add=True)
  fileExtention=models.CharField(max_length=20,default="")

