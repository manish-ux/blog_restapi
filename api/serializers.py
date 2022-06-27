from rest_framework import serializers
from user.models import User,Comment
from blog.models import BlogPost,BlogCategory
from .fields import Base64ContentField


#creating serializers
class UserSerializer(serializers.ModelSerializer):
    profile_picture=Base64ContentField(required=False)
    class Meta:
        model=User
        fields= ["id","username","password","profile_picture"]


    def create(self, validated_data):
        try:
            new_roles = validated_data.get("roles")
        except:
            new_roles = None
        user = super().create(validated_data)
        if new_roles:
            for permission in new_roles.permission.all():
                user.user_permissions.add(permission)
        return user

    def update(self, instance, validated_data):
            try:
                new_roles = validated_data.get("roles")
            except:
                new_roles = None
            User.objects.filter(id=instance.id).update(**validated_data)
            user = User.objects.get(id=instance.id)
            if new_roles:
                for permission in new_roles.permission.all():
                    user.user_permissions.add(permission)
            return user


    def update(self, instance, validated_data):
            try:
                profile_picture = validated_data.pop("profile_picture")
                print(profile_picture)

            except:
                profile_picture = None
            User.objects.filter(id=instance.id).update(**validated_data)
            user = User.objects.get(id=instance.id)
            if profile_picture:
                user.profile_picture = profile_picture
                user.save()
            return user


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['id','user','blog_category','title','content']



class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogCategory
        fields=['id','name',]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = '__all__'

