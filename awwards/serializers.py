from rest_framework import serializers
from .models import Profile,Project
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ['id','user', 'profile_pic', 'bio', 'contact']

class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'user', 'title', 'image', 'url','description','date']