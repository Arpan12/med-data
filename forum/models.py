from __future__ import unicode_literals
from django.db import models
import bleach
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True)
    date = models.DateTimeField(auto_now_add=True)
    post = models.CharField(max_length=1000)
    tag =  models.CharField(max_length=20)
    likes=models.IntegerField(default=0)
    comment=models.IntegerField(default=0)

    def __str__(self):
        return self.post
class Answers(models.Model):
    answer=models.CharField(max_length=2000)
    post= models.ForeignKey(Post,null=False)
    user= models.ForeignKey(settings.AUTH_USER_MODEL,null=True)
    upvotes=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='Answer_upvotes')
    comments=models.CharField(max_length=250,null=True)
    

