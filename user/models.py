from django.db import models
from django.contrib.auth.models import AbstractUser,Permission

# Create your models here.
class UserTypeChoice(models.TextChoices):
   ADMIN = "ADMIN","Admin"
   PUBLISHER = "PUBLISHER",'Publisher'
   READER = "READER","Reader" 

class User(AbstractUser):
    profile_picture = models.FileField(null=True)
    user_type = models.CharField(max_length=255,choices=UserTypeChoice.choices,default=UserTypeChoice.READER,null=True)
    roles = models.ForeignKey('Role', null=True, on_delete=models.SET_NULL, blank=True, related_name='roles')


    def __str__(self):
        return self.username
    
class Role(models.Model):
    name = models.CharField(max_length=255,unique=True)
    permission=models.ManyToManyField(Permission,blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    body=models.TextField(max_length=200,null=True,default=True)
    user=models.ForeignKey('user.User',related_name="comments",on_delete=models.CASCADE,null=True,default=True)
    post_comment=models.ForeignKey('blog.BlogPost',related_name="comments",on_delete=models.CASCADE,null=True,default=True)


