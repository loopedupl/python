# Serializacja złożonych struktur danych w Django REST Framework

W tej lekcji omówimy serializację złożonych modeli i relacji między nimi. Dowiesz się, jak radzić sobie z relacjami jeden-do-wielu oraz wiele-do-wielu, co jest często spotykane w aplikacjach.

## Krok 1: Przygotowanie modeli z relacjami

Zaczniemy od stworzenia dwóch modeli, które będą miały relację typu **ForeignKey** (jeden-do-wielu) oraz **ManyToMany** (wiele-do-wielu). Wykorzystamy model autora (Author) oraz postów (Post), aby zademonstrować relację jeden-do-wielu, oraz kategorię (Category), aby pokazać relację wiele-do-wielu.

### Przykładowe modele

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title
```

- Model `Author` reprezentuje autora, który może mieć wiele postów.
- Model `Post` jest powiązany z autorem poprzez **ForeignKey**, a z kategoriami poprzez **ManyToManyField**.

## Krok 2: Zrozumienie relacji między modelami

### Relacja `ForeignKey` – jeden-do-wielu

Relacja `ForeignKey` służy do łączenia dwóch modeli w taki sposób, że jeden obiekt może być powiązany z wieloma innymi. Na przykład, **Autor** może mieć wiele **Postów**, ale każdy **Post** jest przypisany tylko do jednego **Autora**.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

W tym przypadku każdy post może być powiązany z jednym autorem, ale autor może mieć wiele postów.

### Relacja `ManyToMany` – wiele-do-wielu

Relacja `ManyToMany` umożliwia łączenie dwóch modeli, w których każdy obiekt z jednego modelu może być powiązany z wieloma obiektami z drugiego modelu, i na odwrót. Na przykład, **Kategoria** może być przypisana do wielu **Postów**, a każdy **Post** może mieć wiele **Kategorii**.

```python
class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)
```

Tutaj, jeden post może mieć wiele kategorii, a jedna kategoria może być przypisana do wielu postów.

---

## Krok 3: Serializacja relacji złożonych w DRF

### Serializacja `ForeignKey` (jeden-do-wielu)

Aby serializować relację `ForeignKey`, musimy zagnieździć jeden serializer w drugim. Przykład serializera dla modeli **Author** i **Post** wygląda tak:

```python
from rest_framework import serializers
from .models import Author, Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Zagnieżdżony serializer dla relacji jeden-do-wielu

    class Meta:
        model = Post
        fields = ['id', 'title', 'author']
```

W ten sposób, gdy serializujemy post, automatycznie dodawane są dane o autorze.

### Serializacja `ManyToMany` (wiele-do-wielu)

Dla relacji `ManyToMany`, także używamy zagnieżdżonych serializerów. Musimy jednak uwzględnić, że będzie zwracana lista powiązanych obiektów. W tym celu stosujemy argument `many=True` w serializerze.

```python
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)  # Serializacja listy powiązanych kategorii

    class Meta:
        model = Post
        fields = ['id', 'title', 'categories']
```

Dzięki temu możemy serializować wiele kategorii przypisanych do jednego posta.

---

## Krok 4: Zrozumienie `many=True`

Argument `many=True` w Django REST Framework mówi serializerowi, że ma do czynienia z **listą obiektów**. Jest to niezbędne, gdy mamy relację jeden-do-wielu lub wiele-do-wielu, i chcemy serializować więcej niż jeden obiekt.

Przykład:

```python
# Serializacja jednej instancji
category = Category.objects.first()
serializer = CategorySerializer(category)
print(serializer.data)  # Zwróci dane jednej kategorii

# Serializacja wielu instancji
categories = Category.objects.all()
serializer = CategorySerializer(categories, many=True)
print(serializer.data)  # Zwróci listę danych wielu kategorii
```

W przypadku relacji złożonych, gdy mamy wiele powiązanych obiektów (np. lista kategorii w poście), argument `many=True` informuje serializer, aby zserializował wszystkie obiekty, zamiast jednego.

---

## Krok 5: Serializacja listy postów z autorami i kategoriami

Aby przetestować serializację, dodaj widok, który zwróci listę postów z pełnymi danymi autorów oraz kategorii.

### Przykładowy widok

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
```

## Krok 6: Testowanie relacji

Po skonfigurowaniu widoku uruchom serwer Django i odwiedź endpoint (np. `/posts/`). Powinieneś zobaczyć listę postów z danymi o autorach oraz kategoriach, np.:

```json
[
  {
    "id": 1,
    "title": "Post 1",
    "content": "Treść posta 1",
    "author": {
      "id": 1,
      "name": "Author 1",
      "bio": "Biografia autora 1"
    },
    "categories": [
      {
        "id": 1,
        "name": "Kategoria 1"
      },
      {
        "id": 2,
        "name": "Kategoria 2"
      }
    ]
  },
  {
    "id": 2,
    "title": "Post 2",
    "content": "Treść posta 2",
    "author": {
      "id": 2,
      "name": "Author 2",
      "bio": "Biografia autora 2"
    },
    "categories": [
      {
        "id": 1,
        "name": "Kategoria 1"
      }
    ]
  }
]
```

## Podsumowanie

W tej lekcji dowiedziałeś się, jak serializować złożone struktury danych, takie jak relacje jeden-do-wielu i wiele-do-wielu, używając zagnieżdżonych serializerów. Używając **ForeignKey** i **ManyToManyField**, możesz łatwo serializować powiązane obiekty w Django REST Framework. Dzięki temu możesz zwracać kompletne dane związane z różnymi modelami w jednym żądaniu API, co jest bardzo przydatne w bardziej złożonych aplikacjach.
