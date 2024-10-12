# Struktura projektu Django

## Wymagania wstępne

Upewnij się, że masz zainstalowane:

- Python 3.6 lub nowszy
- Pip (menedżer pakietów dla Pythona)
- Django (w wersji 3.0 lub nowszej)

---

## Krok 1: Tworzenie środowiska wirtualnego

Zaleca się użycie wirtualnego środowiska do zarządzania zależnościami projektu. Możesz utworzyć środowisko wirtualne za pomocą `venv`:

```bash
python -m venv myenv
```

### Aktywuj środowisko wirtualne:

- **Windows:**

```bash
myenv\Scripts\activate
```

- **macOS/Linux:**

```bash
source myenv/bin/activate
```

---

## Krok 2: Instalacja Django

Zainstaluj Django w aktywowanym środowisku wirtualnym:

```bash
pip install django
```

---

## Krok 3: Tworzenie projektu Django

Utwórz nowy projekt Django, używając polecenia:

```bash
django-admin startproject projekt_django
```

Zamień `projekt_django` na nazwę swojego projektu.

---

## Krok 4: Struktura projektu

Po utworzeniu projektu zobaczysz następującą strukturę katalogów:

```
projekt_django/
    manage.py
    projekt_django/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

### Opis plików:

- **manage.py**: Skrypt do zarządzania projektem (uruchamianie serwera, migracje, itp.).
- **projekt_django/** (katalog): Główny katalog projektu, który zawiera konfigurację.
- **`__init__.py`**: Plik, który oznacza, że ten katalog jest pakietem Pythona.
- **settings.py**: Plik konfiguracyjny projektu, w którym definiujesz ustawienia.
- **urls.py**: Plik, w którym definiujesz ścieżki URL dla swojego projektu.
- **asgi.py**: Plik, który pozwala na uruchomienie aplikacji w serwerze ASGI.
- **wsgi.py**: Plik, który pozwala na uruchomienie aplikacji w serwerze WSGI.

---

## Krok 5: Tworzenie aplikacji Django

Aplikacje w Django to komponenty, które realizują konkretne funkcjonalności. Aby utworzyć nową aplikację, użyj polecenia:

```bash
python manage.py startapp app_name
```

My zamienimy `app_name` na nazwę naszej przykładowej aplikacji `blog`.

---

## Krok 6: Struktura aplikacji

Po utworzeniu aplikacji zobaczysz następującą strukturę katalogów w katalogu `blog`:

```
blog/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

### Opis plików:

- **migrations/**: Katalog, w którym przechowywane są migracje bazy danych.
- **admin.py**: Plik do rejestracji modeli w panelu administracyjnym.
- **apps.py**: Plik konfiguracyjny aplikacji.
- **models.py**: Plik, w którym definiujesz modele bazy danych.
- **tests.py**: Plik, w którym możesz pisać testy dla aplikacji.
- **views.py**: Plik, w którym definiujesz widoki aplikacji.

---

## Krok 7: Dodanie aplikacji do projektu

Aby dodać nowo utworzoną aplikację do projektu, otwórz plik `settings.py` i dodaj nazwę aplikacji do listy `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'blog',
]
```

---

## Krok 8: Uruchomienie serwera deweloperskiego

Na koniec uruchom serwer deweloperski, aby sprawdzić, czy wszystko działa poprawnie:

```bash
python manage.py runserver
```

Serwer powinien być dostępny pod adresem `http://127.0.0.1:8000/`.

---

## Podsumowanie

Stworzyliśmy podstawową strukturę projektu Django oraz dodaliśmy aplikację. Teraz możesz zacząć rozwijać swoje funkcjonalności!
