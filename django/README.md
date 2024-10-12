# Lekcja: Struktura projektu Django

W tej lekcji nauczysz się jak utworzyć nowy projekt Django oraz zrozumieć jego podstawową strukturę.

---

## Krok 1: Zainstaluj Django

Najpierw zainstaluj Django, jeśli nie masz go jeszcze na swoim komputerze. Możesz to zrobić za pomocą `pip`:

```bash
pip install django
```

> **Uwaga:** Upewnij się, że masz zainstalowanego Pythona w wersji 3.6 lub nowszej.

---

## Krok 2: Stwórz nowy projekt Django

Aby utworzyć nowy projekt Django, użyj następującej komendy w terminalu:

```bash
django-admin startproject moja_strona
```

Ta komenda utworzy katalog o nazwie `moja_strona`, który będzie zawierał podstawową strukturę projektu Django.

---

## Krok 3: Przegląd struktury projektu

Po utworzeniu projektu Django, powinieneś zobaczyć następującą strukturę plików:

```
moja_strona/
    manage.py
    moja_strona/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### Wyjaśnienie plików:

- `manage.py`: Skrypt zarządzający projektem, używany do uruchamiania serwera, migracji bazy danych itd.
- `__init__.py`: Plik oznaczający folder `moja_strona` jako moduł Pythona.
- `settings.py`: Główne ustawienia projektu.
- `urls.py`: Deklaracja tras URL w projekcie.
- `asgi.py` i `wsgi.py`: Pliki odpowiedzialne za komunikację między serwerem a aplikacją (odpowiednio dla ASGI i WSGI).

---

## Krok 4: Uruchomienie serwera deweloperskiego

Aby uruchomić serwer deweloperski, użyj poniższej komendy:

```bash
python manage.py runserver
```

Serwer powinien być dostępny pod adresem `http://127.0.0.1:8000/`. Sprawdź go w swojej przeglądarce!

---

## Krok 5: Podsumowanie

Nauczyłeś się, jak zainstalować Django, utworzyć nowy projekt oraz zrozumieć podstawową strukturę projektu. W kolejnych lekcjach zajmiemy się tworzeniem aplikacji oraz konfiguracją szablonów i baz danych.
