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

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Tytuł musi mieć co najmniej 5 znaków.")
        return value