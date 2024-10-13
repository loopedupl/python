# Praca z serializerami w Django REST Framework

W tej lekcji skupimy się na pracy z serializerami w Django REST Framework (DRF). Serializery są kluczowym elementem w konwersji danych do formatu JSON. Dowiesz się, jak tworzyć różne typy serializerów i jak konfigurować ich właściwości.

## Krok 1: Utworzenie modelu

Upewnij się, że masz model, z którym będziesz pracować. Użyjmy prostego modelu `Post` jako przykładu:

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

## Krok 2: Tworzenie prostego serializera

Zacznijmy od stworzenia prostego serializera dla modelu `Post`. Utwórz plik `serializers.py`, jeśli jeszcze go nie masz:

```python
# blog/serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published_at']
```

### Wyjaśnienie `class Meta`

- **model**: Wskazuje model, z którym serializer będzie pracował. W tym przypadku to `Post`.
- **fields**: Określa, które pola modelu mają być uwzględnione w serializacji. Możesz podać listę pól, które chcesz uwzględnić.

## Krok 3: Użycie `__all__` w fields

Możesz również użyć `__all__`, aby uwzględnić wszystkie pola modelu w serializacji:

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Użycie __all__ do uwzględnienia wszystkich pól
```

## Krok 4: Użycie `exclude`

Alternatywnie, możesz użyć opcji `exclude`, aby wykluczyć określone pola z serializacji. Na przykład, jeśli chcesz wykluczyć pole `published_at`:

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['published_at']  # Wyklucza pole published_at
```

## Krok 5: Tworzenie zagnieżdżonego serializera

Zagnieżdżone serializery pozwalają na serializację powiązanych modeli. Załóżmy, że masz model `Author`:

```python
# blog/models.py
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
```

Teraz stwórz zagnieżdżony serializer dla `Author`:

```python
# blog/serializers.py
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Zagnieżdżony serializer

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published_at', 'author']
```

## Podsumowanie

W tej lekcji dowiedziałeś się, jak tworzyć różne typy serializerów w Django REST Framework, używać właściwości `class Meta`, oraz korzystać z `fields`, `__all__` i `exclude`. Ponadto zobaczyłeś, jak tworzyć zagnieżdżone serializery. Serializery są kluczowym elementem w tworzeniu API i umożliwiają efektywne przetwarzanie danych w Twoich aplikacjach Django.
