# Modele i migracje w Django

---

#### Spis treści

1. [Tworzenie projektu Django](#1-tworzenie-projektu-django)
2. [Tworzenie aplikacji Django](#2-tworzenie-aplikacji-django)
3. [Definiowanie modeli](#3-definiowanie-modeli)
4. [Tworzenie migracji](#4-tworzenie-migracji)
5. [Zastosowanie migracji](#5-zastosowanie-migracji)
6. [Praca z modelami w Django Shell](#6-praca-z-modelami-w-django-shell)

---

### 1. Tworzenie projektu Django

Zacznij od utworzenia nowego projektu Django. W terminalu wpisz poniższe komendy:

```bash
# Instalacja Django (jeśli nie masz go jeszcze zainstalowanego)
pip install django

# Tworzenie nowego projektu Django
django-admin startproject myproject

# Przejdź do katalogu projektu
cd myproject
```

### 2. Tworzenie aplikacji Django

Teraz utwórz aplikację wewnątrz swojego projektu. Na potrzeby tej lekcji stworzymy aplikację o nazwie `blog`:

```bash
# Tworzenie aplikacji blog
python manage.py startapp blog
```

Po utworzeniu aplikacji musisz dodać ją do pliku `settings.py` w sekcji `INSTALLED_APPS`:

```python
# myproject/settings.py

INSTALLED_APPS = [
    # Inne aplikacje Django
    'blog',  # Dodaj aplikację blog do zainstalowanych aplikacji
]
```

### 3. Definiowanie modeli

Przejdź teraz do pliku `models.py` w aplikacji `blog` i zdefiniuj dwa modele: `Author` oraz `Post`.

```python
# blog/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

- **Author**: Reprezentuje autora postów. Przechowuje jego imię i nazwisko oraz opcjonalną biografię.
- **Post**: Reprezentuje post na blogu, który ma tytuł, treść, datę publikacji i relację do autora.

### 4. Tworzenie migracji

Teraz musisz utworzyć migracje, aby Django mogło stworzyć tabele w bazie danych na podstawie zdefiniowanych modeli.

```bash
# Tworzenie migracji
python manage.py makemigrations
```

Django wygeneruje plik migracyjny, który zawiera instrukcje dotyczące tworzenia tabel w bazie danych.

### 5. Zastosowanie migracji

Po utworzeniu migracji musisz je zastosować, aby tabele zostały utworzone w bazie danych.

```bash
# Zastosowanie migracji
python manage.py migrate
```

Django utworzy wszystkie niezbędne tabele w bazie danych, w tym tabele dla aplikacji `blog`.

### 6. Praca z modelami w Django Shell

Aby przetestować działanie modeli, możesz otworzyć Django shell i utworzyć kilka rekordów w bazie danych.

```bash
# Otwieranie Django shell
python manage.py shell
```

W Django shell wykonaj następujące kroki:

- **Importowanie modeli:**

  ```python
  from blog.models import Author, Post
  ```

- **Tworzenie autora:**

  ```python
  author = Author.objects.create(name="Jan Kowalski", bio="Autor bloga o Django.")
  ```

- **Tworzenie posta:**

  ```python
  post = Post.objects.create(
      title="Jak działa Django?",
      content="Django to wspaniałe narzędzie do budowania aplikacji webowych.",
      author=author,
      is_published=True
  )
  ```

- **Pobieranie wszystkich postów:**

  ```python
  all_posts = Post.objects.all()
  print(all_posts)
  ```

- **Filtrowanie postów według autora:**

  ```python
  jan_posts = Post.objects.filter(author__name="Jan Kowalski")
  print(jan_posts)
  ```

### Podsumowanie

W tej lekcji stworzyliśmy modele Django, utworzyliśmy migracje i zastosowaliśmy je w bazie danych. Następnie pracowaliśmy z danymi w Django Shell. Ten proces pozwala na łatwe tworzenie, modyfikowanie i pobieranie danych z bazy, używając ORM Django.
