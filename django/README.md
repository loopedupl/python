# Testowanie automatyczne endpointów API

W tej lekcji nauczysz się, jak tworzyć testy automatyczne dla endpointów API w aplikacji Django. Testy automatyczne pozwalają na szybkie i efektywne sprawdzanie, czy Twoje API działa zgodnie z oczekiwaniami oraz pomagają w identyfikacji błędów.

## Krok 1: Utworzenie pliku testowego

1. Przejdź do folderu swojej aplikacji Django.
2. Utwórz nowy plik o nazwie `tests.py` w katalogu aplikacji, jeśli jeszcze go nie masz.

## Krok 2: Importowanie niezbędnych modułów

Otwórz plik `tests.py` i dodaj następujące importy:

```python
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Post
```

## Krok 3: Utworzenie klasy testowej

Utwórz klasę testową, która będzie dziedziczyć po `APITestCase`. Wewnątrz klasy możesz zdefiniować metody testowe.

```python
class PostAPITestCase(APITestCase):
    def setUp(self):
        self.url = "/posts/"
        # Tworzymy autora
        self.author = Author.objects.create(name="Test Author", bio="Test bio")
        # Tworzymy post
        self.post = Post.objects.create(title="Test Post", content="Test content", author=self.author)
```

## Krok 4: Testowanie endpointu GET

Dodaj metodę testową, aby sprawdzić, czy endpoint GET dla wszystkich postów działa poprawnie.

```python
    def test_get_post_list(self):
        """Testowanie pobierania listy postów"""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Sprawdzamy, czy jeden post jest zwrócony
        self.assertEqual(len(response.data['results']), 1)

    def test_get_post_detail(self):
        """Testowanie pobierania szczegółów posta"""
        response = self.client.get(f"{self.url}{self.post.pk}/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)
```

## Krok 5: Testowanie endpointu POST

Dodaj metodę testową, aby sprawdzić, czy endpoint POST do tworzenia nowego posta działa poprawnie.

```python
    def test_create_post(self):
        """Testowanie tworzenia nowego posta"""
        data = {
            'title': 'New Post',
            'content': 'Content for new post',
            'author': {'id': self.author.id, 'name': self.author.name},
            'is_published': False
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(id=response.data['id']).title, 'New Post')
```

## Krok 6: Testowanie endpointu PUT

Dodaj metodę testową do aktualizacji istniejącego posta.

```python
    def test_update_post(self):
        """Testowanie aktualizacji posta"""
        data = {
            'title': 'Updated Title',
            'content': 'Updated content',
            'author': {'id': self.author.id, 'name': self.author.name},
            'is_published': True
        }
        response = self.client.put(f"{self.url}{self.post.pk}/", data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
```

## Krok 7: Testowanie endpointu DELETE

Dodaj metodę testową do usunięcia istniejącego posta.

```python
    def test_delete_post(self):
        """Testowanie usuwania posta"""
        response = self.client.delete(f"{self.url}{self.post.pk}/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
```

## Krok 8: Uruchamianie testów

Aby uruchomić testy, przejdź do terminala i wpisz poniższe polecenie:

```bash
python manage.py test
```

Django wykona wszystkie testy zdefiniowane w klasach testowych i wyświetli wyniki w terminalu.

## Podsumowanie

W tej lekcji nauczyłeś się, jak automatyzować testowanie endpointów API w Django. Dzięki zastosowaniu zestawów testowych i asercji możesz skutecznie weryfikować funkcjonalność API, co znacznie zwiększa efektywność procesu deweloperskiego oraz zapewnia stabilność aplikacji.
