from django.contrib import admin
from .models import User,Role,Comment
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username']
admin.site.register(User,UserAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display=['id',]
admin.site.register(Role,RoleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display= ['id','body','user','post_comment']
admin.site.register(Comment,CommentAdmin)
