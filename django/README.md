# Instalacja i konfiguracja Django REST Framework

Django REST Framework (DRF) to potężne narzędzie do budowania API w Django. Ten przewodnik pomoże Ci zainstalować i skonfigurować DRF w istniejącym projekcie Django.

## Wymagania

- Python 3.6 lub nowszy
- Django (w wersji 3.0 lub nowszej)
- PIP (menedżer pakietów Pythona)

## Krok 1: Instalacja Django REST Framework

Najpierw upewnij się, że masz aktywne środowisko wirtualne. Aby zainstalować Django REST Framework, uruchom w terminalu poniższe polecenie:

```bash
pip install djangorestframework
```

## Krok 2: Dodanie DRF do aplikacji Django

Po instalacji należy dodać `rest_framework` do listy aplikacji zainstalowanych w projekcie Django. Otwórz plik `settings.py` i znajdź sekcję `INSTALLED_APPS`. Dodaj tam `rest_framework`:

```python
INSTALLED_APPS = [
    # inne aplikacje
    'rest_framework',
]
```

## Krok 3: Podstawowa konfiguracja DRF

Aby skonfigurować Django REST Framework, w pliku `settings.py` dodaj sekcję `REST_FRAMEWORK`. Możesz tutaj ustawić różne opcje, takie jak filtrowanie i uprawnienia.

Poniżej znajduje się przykładowa konfiguracja:

```python
REST_FRAMEWORK = {
    # Domyślne uprawnienia: użytkownik nie musi być zalogowany
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    # Filtrowanie na poziomie widoku (bez dodatkowych bibliotek)
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter',  # Filtrowanie według kolejności
        'rest_framework.filters.SearchFilter',  # Filtrowanie za pomocą wyszukiwania
    ],

    # Domyślna klasa paginacji: oparta na numerze strony
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    # Ilość elementów na stronie
    'PAGE_SIZE': 10,
}
```

## Podsumowanie

Gratulacje! Pomyślnie zainstalowałeś i skonfigurowałeś Django REST Framework w swoim projekcie. Teraz możesz rozszerzać swoją aplikację o dodatkowe funkcje API.
