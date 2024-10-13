# Tworzenie widoków API z Django REST Framework

W tej lekcji nauczysz się, jak tworzyć widoki API z użyciem Django REST Framework (DRF), wykorzystując istniejące modele `Post` i `Author`. Skupimy się na tworzeniu widoków opartych na funkcjach (FBV), widoków opartych na klasach (CBV), oraz `ViewSet`. Pokażemy również, jak połączyć widoki z URL-ami, aby Twoje API było w pełni funkcjonalne.

## Krok 1: Utworzenie serializera

Najpierw musimy utworzyć serializery dla modeli `Post` i `Author`, które będą konwertować dane do i z formatu JSON.

Utwórz plik `serializers.py`, jeśli go jeszcze nie masz, i dodaj serializery dla obu modeli:

```python
# blog/serializers.py
from rest_framework import serializers
from .models import Post, Author

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
```

## Krok 2: Tworzenie widoków API (Function-Based Views)

Teraz utworzymy widoki API oparte na funkcjach (FBV) dla modelu `Post`. Te widoki będą obsługiwać standardowe operacje: listowanie, tworzenie, aktualizowanie i usuwanie postów.

W pliku `views.py` dodaj następujące widoki:

```python
# blog/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## Krok 3: Tworzenie widoków API (Class-Based Views)

Korzystanie z widoków opartych na klasach (CBV) upraszcza kod i pozwala lepiej organizować logikę widoku. Poniżej tworzymy widok listowania i tworzenia postów oraz widok szczegółowy dla modelu `Post` za pomocą `APIView`.

Dodaj następujący kod do pliku `views.py`:

```python
# blog/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## Krok 4: Tworzenie widoków API (ViewSet)

Widoki `ViewSet` są najbardziej elastycznym sposobem pracy z widokami w DRF. Łączą one wiele operacji w jednym widoku. Stwórzmy widok `ViewSet` dla modelu `Post`.

```python
# blog/views.py
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

## Krok 5: Mapowanie widoków do URL-i

Teraz musimy połączyć nasze widoki z URL-ami. W pliku `urls.py` utwórz ścieżki dla każdego widoku.

Najpierw dla widoków opartych na funkcjach (FBV):

```python
# projekt_django/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:pk>/', views.post_detail),
]
```

Dla widoków opartych na klasach (CBV):

```python
# projekt_django/urls.py
from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
]
```

Dla widoków `ViewSet`:

```python
# projekt_django/urls.py
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
```

## Krok 6: Uruchomienie serwera

Na koniec uruchom serwer, aby sprawdzić, czy wszystko działa poprawnie:

```bash
python manage.py runserver
```

## Podsumowanie

W tej lekcji stworzyliśmy różne typy widoków API: oparte na funkcjach (FBV), oparte na klasach (CBV) oraz widoki `ViewSet` dla modelu `Post`. Dzięki tym przykładom jesteś teraz w stanie tworzyć elastyczne i skalowalne API z użyciem Django REST Framework.
