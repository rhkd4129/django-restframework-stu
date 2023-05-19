from rest_framework.serializers import ModelSerializer
from .models import Post
from django.contrib.auth import get_user_model

from rest_framework import serializers



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','email']

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'author.username')
    author_email = serializers.ReadOnlyField(source = 'author.email')
    # author = AuthorSerializer
    class Meta:
        model = Post
        fields = ['pk','username','messages','created_at','updated_at','author_email','is_public']