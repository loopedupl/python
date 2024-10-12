# Tworzenie panelu administracyjnego w Django

Django ma wbudowany panel administracyjny, który umożliwia zarządzanie danymi aplikacji bez konieczności pisania własnych interfejsów. W tym przewodniku pokażę, jak skonfigurować panel admina i jak dodawać modele, które można edytować w panelu.

## Wymagania wstępne

Upewnij się, że masz zainstalowane:

- Django (w wersji 3.0 lub nowszej)
- Utworzony projekt Django

## Krok 1: Utwórz superużytkownika

Aby mieć dostęp do panelu administracyjnego, musisz utworzyć superużytkownika. Superużytkownik to konto, które ma pełny dostęp do zarządzania wszystkimi danymi w panelu administracyjnym.

Aby utworzyć superużytkownika, w terminalu użyj polecenia:

```bash
python manage.py createsuperuser
```

Postępuj zgodnie z instrukcjami, podając nazwę użytkownika, adres e-mail oraz hasło.

## Krok 2: Dodaj aplikację do panelu administracyjnego

Aby model był dostępny w panelu administracyjnym, musisz go zarejestrować. Otwórz plik `admin.py` w aplikacji, do której chcesz dodać model.

Na przykład, jeśli masz aplikację `myapp`, przejdź do `myapp/admin.py` i dodaj tam swój model:

```python
from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
```

Zamień `MyModel` na nazwę swojego modelu.

## Krok 3: Migracja bazy danych

Upewnij się, że wszystkie migracje są zastosowane, aby panel admina miał dostęp do aktualnych danych. Użyj poleceń:

```bash
python manage.py makemigrations
python manage.py migrate
```

Te polecenia utworzą i zastosują migracje, które zaktualizują bazę danych.

## Krok 4: Dostęp do panelu administracyjnego

Po zarejestrowaniu modelu i migracji bazy danych możesz uzyskać dostęp do panelu admina. Aby uruchomić serwer deweloperski, użyj polecenia:

```bash
python manage.py runserver
```

Następnie otwórz przeglądarkę i przejdź pod adres:

```
http://127.0.0.1:8000/admin
```

Zaloguj się, używając danych superużytkownika, które stworzyłeś wcześniej.

## Krok 5: Konfiguracja modelu w panelu admina

Możesz spersonalizować sposób wyświetlania modeli w panelu administracyjnym. Aby to zrobić, zmodyfikuj plik `admin.py` i dodaj specjalną klasę `ModelAdmin`:

```python
from django.contrib import admin
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')  # Kolumny wyświetlane w panelu
    search_fields = ('field1', 'field2')  # Pola, po których można wyszukiwać
    list_filter = ('field3',)  # Dodanie filtrów w panelu bocznym

admin.site.register(MyModel, MyModelAdmin)
```

Dostosuj `list_display`, `search_fields` i `list_filter` do swoich potrzeb, zamieniając `field1`, `field2`, itp. na rzeczywiste pola swojego modelu.

## Krok 6: Dodanie kolejnych modeli

Jeśli chcesz dodać więcej modeli do panelu administracyjnego, powtórz te same kroki dla każdego z nich. Dodaj je do pliku `admin.py` i zarejestruj:

```python
from .models import AnotherModel

admin.site.register(AnotherModel)
```

## Krok 7: Dodanie relacji między modelami

Jeśli twoje modele są połączone relacjami (np. za pomocą klucza obcego), możesz skonfigurować te relacje w panelu admina, aby ułatwić zarządzanie. Na przykład, dla modeli połączonych relacją 1 do wielu:

```python
from django.contrib import admin
from .models import ParentModel, ChildModel

class ChildModelInline(admin.TabularInline):  # Inline dla modelu zależnego
    model = ChildModel

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [ChildModelInline]

admin.site.register(ParentModel, ParentModelAdmin)
```

To umożliwia zarządzanie zależnymi modelami bezpośrednio w edycji głównego modelu.

## Podsumowanie

Z powodzeniem utworzyliśmy panel administracyjny w Django, dodaliśmy modele i skonfigurowaliśmy wyświetlanie danych. Panel administracyjny jest potężnym narzędziem do zarządzania danymi w aplikacji, a dzięki jego elastyczności możesz go dostosować do swoich potrzeb.

Jeśli masz pytania, nie wahaj się ich zadać!
