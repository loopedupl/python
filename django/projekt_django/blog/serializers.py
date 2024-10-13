from rest_framework import serializers
from .models import Post, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']  # Pola do serializacji

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Zagnieżdżony serializer

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published_at', 'author']  # Pola do serializacji

    def validate_title(self, value):
        """Walidacja tytułu posta."""
        if len(value) < 5:
            raise serializers.ValidationError("Tytuł musi mieć co najmniej 5 znaków.")
        return value

    def create(self, validated_data):
        """Tworzenie posta oraz zagnieżdżonego autora."""
        author_data = validated_data.pop('author')  # Pobranie danych autora
        author = Author.objects.create(**author_data)  # Utworzenie autora
        post = Post.objects.create(author=author, **validated_data)  # Utworzenie posta
        return post

    def update(self, instance, validated_data):
        """Aktualizacja posta oraz autora."""
        author_data = validated_data.pop('author', None)  # Pobranie danych autora
        if author_data:
            instance.author.name = author_data.get('name', instance.author.name)  # Aktualizacja nazwy autora
            instance.author.save()  # Zapisanie autora

        instance.title = validated_data.get('title', instance.title)  # Aktualizacja tytułu
        instance.content = validated_data.get('content', instance.content)  # Aktualizacja treści
        instance.is_published = validated_data.get('is_published', instance.is_published)  # Aktualizacja statusu
        instance.save()  # Zapisanie posta
        return instance
