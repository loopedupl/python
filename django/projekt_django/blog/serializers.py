from rest_framework import serializers
from .models import Post, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Zagnieżdżony serializer

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published_at', 'author']