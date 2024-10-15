# Konfiguracja Bezpieczeństwa w Django - settings.py

W tej lekcji dowiesz się, jak poprawnie skonfigurować plik `settings.py` w projekcie Django, aby poprawić jego bezpieczeństwo. Django dostarcza wiele narzędzi, które pomagają zabezpieczyć aplikację przed popularnymi atakami, takimi jak Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF) i inne.

---

## Krok 1: Ustawienie `SECRET_KEY`

1. **Klucz tajny (SECRET_KEY)** jest kluczowy dla bezpieczeństwa aplikacji. Należy upewnić się, że klucz ten jest wystarczająco długi, losowy i trudny do odgadnięcia.
2. Nigdy nie należy przechowywać klucza `SECRET_KEY` w repozytorium publicznym. Zamiast tego, najlepiej ustawić go jako zmienną środowiskową:

   W pliku `settings.py`:

   ```python
   import os

   SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'domyślny_klucz')
   ```

3. W środowisku produkcyjnym ustaw `DJANGO_SECRET_KEY` w pliku `.env` lub w systemie.

---

## Krok 2: Zabezpieczenie trybu debugowania

1. Nigdy nie uruchamiaj aplikacji w trybie **debugowania** na produkcji. Tryb debugowania wyświetla szczegółowe informacje o błędach, które mogą zawierać wrażliwe dane.

2. Ustaw `DEBUG` na `False` w pliku `settings.py` dla produkcji:

   ```python
   DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
   ```

3. W środowisku produkcyjnym `DJANGO_DEBUG` powinno być ustawione na `False`.

---

## Krok 3: Konfiguracja dozwolonych hostów

1. **ALLOWED_HOSTS** to ustawienie, które ogranicza dostęp do aplikacji tylko z wybranych domen. Ustaw tę listę, aby zapobiec atakom DNS rebinding:

   W pliku `settings.py`:

   ```python
   ALLOWED_HOSTS = ['twoja-domena.com', 'www.twoja-domena.com']
   ```

2. Na etapie rozwoju aplikacji, dla lokalnego środowiska, można ustawić:
   ```python
   ALLOWED_HOSTS = ['localhost', '127.0.0.1']
   ```

---

## Krok 4: Zabezpieczenie cookies

1. Aby zapobiec atakom typu **Cross-Site Scripting (XSS)** oraz **Cross-Site Request Forgery (CSRF)**, ustaw bezpieczne flagi dla cookies.

2. Dodaj do pliku `settings.py`:

   ```python
   # Zabezpieczenie sesji
   SESSION_COOKIE_SECURE = True  # Wymusza użycie HTTPS do przesyłania cookies sesji
   SESSION_COOKIE_HTTPONLY = True  # Zapobiega dostępowi do ciasteczek sesji z JavaScript

   # Zabezpieczenie cookies CSRF
   CSRF_COOKIE_SECURE = True  # Wymusza użycie HTTPS do przesyłania ciasteczek CSRF
   CSRF_COOKIE_HTTPONLY = True  # Zapobiega dostępowi do ciasteczek CSRF z JavaScript
   ```

3. Pamiętaj, aby `SESSION_COOKIE_SECURE` oraz `CSRF_COOKIE_SECURE` ustawić na `True` tylko na produkcji (czyli gdy aplikacja działa na HTTPS).

---

## Krok 5: HSTS (HTTP Strict Transport Security)

1. Aby wymusić użycie HTTPS w całej aplikacji, skonfiguruj HSTS. To ustawienie informuje przeglądarkę, że powinna łączyć się z serwerem wyłącznie przez HTTPS.

2. W pliku `settings.py`:

   ```python
   SECURE_HSTS_SECONDS = 31536000  # Czas przechowywania informacji o HTTPS (1 rok)
   SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Wymusza HTTPS dla wszystkich subdomen
   SECURE_HSTS_PRELOAD = True  # Zezwala na umieszczenie w liście HSTS preload
   ```

3. Aby dodać swoją domenę do listy HSTS preload, odwiedź [hstspreload.org](https://hstspreload.org/).

---

## Krok 6: Zabezpieczenie przekierowań (SECURE_SSL_REDIRECT)

1. Aby przekierować wszystkie żądania HTTP na HTTPS, dodaj ustawienie:

   ```python
   SECURE_SSL_REDIRECT = True
   ```

2. Na etapie rozwoju aplikacji, to ustawienie powinno być wyłączone.

---

## Krok 7: Zabezpieczenie nagłówków

1. Aby zapobiec atakom, możesz ustawić nagłówki zabezpieczające, takie jak X-Content-Type-Options, X-Frame-Options i X-XSS-Protection.

2. W pliku `settings.py`:
   ```python
   SECURE_BROWSER_XSS_FILTER = True  # Włącza XSS filter w przeglądarkach
   X_FRAME_OPTIONS = 'DENY'  # Zapobiega ładowaniu strony w ramkach (clickjacking)
   SECURE_CONTENT_TYPE_NOSNIFF = True  # Wymusza poprawne typy MIME
   ```

---

## Krok 8: Ochrona przed Cross-Site Request Forgery (CSRF)

1. Django automatycznie chroni formularze przed atakami CSRF, ale upewnij się, że token CSRF jest wysyłany i sprawdzany w widokach.

2. W pliku `settings.py`:

   ```python
   CSRF_TRUSTED_ORIGINS = ['https://twoja-domena.com']
   ```

3. Możesz także dostosować nagłówki, które CSRF będzie sprawdzać:
   ```python
   CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
   ```

---

## Krok 9: Logowanie wyjątków

1. Konfiguracja logowania może pomóc w identyfikacji potencjalnych zagrożeń bezpieczeństwa. Upewnij się, że błędy są logowane w bezpieczny sposób.

2. Przykład konfiguracji logowania w `settings.py`:
   ```python
   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'file': {
               'level': 'ERROR',
               'class': 'logging.FileHandler',
               'filename': '/path/to/error.log',
           },
       },
       'loggers': {
           'django': {
               'handlers': ['file'],
               'level': 'ERROR',
               'propagate': True,
           },
       },
   }
   ```

---

## Krok 10: Zarządzanie bazą danych

1. Upewnij się, że dane uwierzytelniające do bazy danych (hasła, użytkownicy) nie są przechowywane bezpośrednio w pliku `settings.py`. Zamiast tego, używaj zmiennych środowiskowych:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.getenv('DB_NAME'),
           'USER': os.getenv('DB_USER'),
           'PASSWORD': os.getenv('DB_PASSWORD'),
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

2. Upewnij się, że hasła do bazy danych są długie i trudne do odgadnięcia.

---

## Podsumowanie

Zastosowanie tych kroków poprawi bezpieczeństwo Twojej aplikacji Django. Pamiętaj, aby regularnie aktualizować Django oraz inne zależności, aby minimalizować ryzyko ataków wynikających z podatności w starszych wersjach.
