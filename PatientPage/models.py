from django.db import models
from django.core.urlresolvers import reverse





# Create your models here.
class Details(models.Model):
       Name = models.CharField(max_length=250)
       age = models.CharField(max_length=3)
       profilePic = models.FileField()

       def get_absolute_url(self):
           reverse('index',kwargs={'Patient_name':self.Name})





       def __str__(self):
           return self.Name


class Medical_History(models.Model):
    Name = models.ForeignKey(Details,on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)


