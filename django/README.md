### Zarządzanie plikiem settings.py dla różnych środowisk

W tej lekcji dowiesz się, jak skonfigurować jeden plik `settings.py`, który zmienia swoje ustawienia w zależności od środowiska (development, staging, production) przy użyciu zmiennych środowiskowych z pliku `.env`. Skorzystamy z biblioteki `python-dotenv`.

---

## Krok 1: Zainstaluj `python-dotenv`

`python-dotenv` pozwala na zarządzanie zmiennymi środowiskowymi przechowywanymi w pliku `.env`, co ułatwia konfigurację środowisk.

1. Zainstaluj `python-dotenv`:
   ```bash
   pip install python-dotenv
   ```

---

## Krok 2: Utwórz plik `.env`

Plik `.env` będzie zawierał wartości zmiennych środowiskowych dla Twojego projektu, takich jak `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`, i dane bazy danych.

1. W głównym katalogu projektu utwórz plik `.env`:

   ```bash
   touch .env
   ```

2. Wypełnij go odpowiednimi zmiennymi, np. dla środowiska deweloperskiego:

   ```ini
   DEBUG=True
   SECRET_KEY='dev-secret-key'
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   ```

   A dla środowiska produkcyjnego zmienisz te wartości na bardziej odpowiednie (np. `DEBUG=False`).

---

## Krok 3: Załaduj zmienne z `.env` w `settings.py`

Teraz zmodyfikujemy plik `settings.py`, aby używał wartości ze zmiennych środowiskowych.

1. Otwórz plik `settings.py` i zaimportuj `load_dotenv` oraz `os`:

   ```python
   import os
   from dotenv import load_dotenv
   from pathlib import Path

   # Wczytaj zmienne z pliku .env
   load_dotenv()

   # Ustawienia projektu
   BASE_DIR = Path(__file__).resolve().parent.parent
   ```

2. Zmodyfikuj ustawienia w `settings.py`, aby odwoływały się do zmiennych środowiskowych:

   ```python
   SECRET_KEY = os.getenv('SECRET_KEY')

   DEBUG = os.getenv('DEBUG', 'False') == 'True'

   ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

   # Baza danych (korzystamy ze zmiennej DATABASE_URL)
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }

   # Jeśli korzystasz z PostgreSQL:
   # DATABASES = {
   #     'default': {
   #         'ENGINE': 'django.db.backends.postgresql',
   #         'NAME': os.getenv('DB_NAME'),
   #         'USER': os.getenv('DB_USER'),
   #         'PASSWORD': os.getenv('DB_PASSWORD'),
   #         'HOST': os.getenv('DB_HOST'),
   #         'PORT': os.getenv('DB_PORT'),
   #     }
   # }
   ```

   Dzięki temu wartości zmiennych, takich jak `SECRET_KEY`, `DEBUG` i inne, są wczytywane z pliku `.env`.

---

## Krok 4: Przykłady plików `.env` dla różnych środowisk

### Plik `.env` dla środowiska deweloperskiego:

```ini
DEBUG=True
SECRET_KEY='dev-secret-key'
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Plik `.env` dla środowiska produkcyjnego:

```ini
DEBUG=False
SECRET_KEY='prod-secret-key'
ALLOWED_HOSTS=your-production-domain.com
DATABASE_URL=postgres://user:password@db-host/db-name
```

---

## Krok 5: Zabezpieczenie pliku `.env`

Upewnij się, że plik `.env` nie zostanie przypadkowo dodany do systemu kontroli wersji (np. Git):

1. Dodaj plik `.env` do `.gitignore`:
   ```bash
   echo '.env' >> .gitignore
   ```

---

## Krok 6: Dynamiczna zmiana ustawień zależnych od środowiska

Dzięki użyciu `python-dotenv` i pliku `.env` możesz łatwo przełączać konfiguracje między różnymi środowiskami (development, production) poprzez zmianę zawartości pliku `.env`.

Przykład uruchomienia aplikacji w trybie produkcyjnym:

1. Ustaw zmienne w pliku `.env` dla środowiska produkcyjnego.
2. Uruchom serwer Django.

---

## Podsumowanie

Teraz masz jeden plik `settings.py`, który korzysta ze zmiennych środowiskowych, dostosowując ustawienia aplikacji w zależności od środowiska. Wystarczy zmienić wartości w pliku `.env` dla odpowiedniego środowiska (np. produkcja, staging, development), a reszta konfiguracji automatycznie się dostosuje.
