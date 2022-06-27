from django.contrib import admin
from blog.models import BlogCategory,BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display=['id','title','content','created_at','updated_at']
admin.site.register(BlogPost,BlogPostAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','created_at','updated_at']
admin.site.register(BlogCategory,BlogCategoryAdmin)

