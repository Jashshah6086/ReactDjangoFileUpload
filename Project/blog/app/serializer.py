
from rest_framework import serializers
from . models import *
  
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserName
        fields = ['author', 'title','file','visible']

        
class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['name']