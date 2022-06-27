from django.db import models
from ckeditor.fields import RichTextField
from core.models import BaseModel
# Create your models here.

class BlogPost(BaseModel):
    user = models.ForeignKey('user.User',on_delete=models.CASCADE)
    blog_category=models.ForeignKey('blog.BlogCategory',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()

    def __str__(self):
        return self.title

class BlogCategory(BaseModel):
   name = models.CharField(max_length=255)
   
   def __str__(self):
        return self.name
        



