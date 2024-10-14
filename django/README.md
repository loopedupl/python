### Podstawy pliku `settings.py` w Django

W tej lekcji dowiesz się, jak skonfigurować podstawowe ustawienia w pliku `settings.py` w projekcie Django. Plik ten pełni kluczową rolę w definiowaniu globalnych ustawień dla całego projektu. W kolejnych krokach omówimy najważniejsze sekcje pliku `settings.py` oraz ich znaczenie.

---

## Krok 1: Znalezienie pliku `settings.py`

1. Po utworzeniu nowego projektu Django, plik `settings.py` znajduje się w katalogu projektu.

   - Przykładowo, jeśli Twój projekt nazywa się `myproject`, plik będzie zlokalizowany w katalogu `myproject/myproject/settings.py`.

2. Otwórz ten plik w swoim edytorze kodu.

---

## Krok 2: Zmienna `DEBUG`

1. Zmienna `DEBUG` decyduje o tym, czy aplikacja działa w trybie debugowania.
   - **Wartość `True`**: Umożliwia wyświetlanie szczegółowych błędów podczas rozwoju aplikacji.
   - **Wartość `False`**: Powinna być ustawiona na `False` w środowisku produkcyjnym, aby chronić szczegóły błędów przed użytkownikami.
2. Znajdź linijkę:

   ```python
   DEBUG = True
   ```

3. Jeśli pracujesz nad aplikacją lokalnie, pozostaw `True`. W przeciwnym wypadku, dla środowiska produkcyjnego ustaw `False`.

---

## Krok 3: Konfiguracja `ALLOWED_HOSTS`

1. `ALLOWED_HOSTS` określa listę domen i adresów IP, z których serwer akceptuje połączenia.

2. Domyślnie ta lista jest pusta:

   ```python
   ALLOWED_HOSTS = []
   ```

3. W środowisku produkcyjnym, należy dodać domeny lub adresy IP. Na przykład:

   ```python
   ALLOWED_HOSTS = ['example.com', '127.0.0.1']
   ```

4. W środowisku lokalnym możesz ustawić:
   ```python
   ALLOWED_HOSTS = ['localhost', '127.0.0.1']
   ```

---

## Krok 4: Konfiguracja `INSTALLED_APPS`

1. `INSTALLED_APPS` zawiera listę aplikacji Django i bibliotek, które są używane w projekcie.

2. Domyślnie znajdziesz kilka wbudowanych aplikacji Django, takich jak:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

3. Aby dodać swoją własną aplikację do projektu, wystarczy dopisać jej nazwę. Na przykład, jeśli stworzyłeś aplikację `blog`, dodaj ją:
   ```python
   INSTALLED_APPS = [
       ...
       'blog',
   ]
   ```

---

## Krok 5: Konfiguracja `DATABASES`

1. Sekcja `DATABASES` określa konfigurację bazy danych używaną w projekcie.

2. Domyślna konfiguracja to baza danych SQLite:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

3. Jeśli używasz innej bazy danych (np. PostgreSQL, MySQL), musisz odpowiednio dostosować tę sekcję. Przykład dla PostgreSQL:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'mydatabaseuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

---

## Krok 6: Konfiguracja `TEMPLATES`

1. Sekcja `TEMPLATES` odpowiada za konfigurację systemu szablonów Django.

2. Domyślna konfiguracja:

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

3. Jeśli masz własne foldery ze szablonami HTML, dodaj ich ścieżki w polu `DIRS`. Na przykład:
   ```python
   TEMPLATES = [
       {
           ...
           'DIRS': [BASE_DIR / 'templates'],
           ...
       },
   ]
   ```

---

## Krok 7: Konfiguracja statycznych plików (`STATICFILES`)

1. `STATIC_URL` określa URL do plików statycznych (CSS, JavaScript, obrazy).

2. Domyślna konfiguracja:

   ```python
   STATIC_URL = '/static/'
   ```

3. Jeśli w środowisku produkcyjnym chcesz ustawić katalog dla plików statycznych, użyj `STATIC_ROOT`. Na przykład:
   ```python
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   ```

---

## Krok 8: Konfiguracja czasu i języka

1. W `settings.py` znajdziesz również ustawienia związane z językiem i strefą czasową projektu.

2. Przykład ustawienia języka na polski:

   ```python
   LANGUAGE_CODE = 'pl'
   ```

3. Ustawienia dla strefy czasowej:
   ```python
   TIME_ZONE = 'Europe/Warsaw'
   ```

---

## Krok 9: Podsumowanie

Plik `settings.py` to centralny element konfiguracji projektu Django. Dzięki niemu możesz kontrolować, jak działa Twoja aplikacja, jakie bazy danych używa, jakie aplikacje są zainstalowane oraz jak obsługiwane są szablony i pliki statyczne. Dobre zrozumienie i konfiguracja tego pliku to klucz do poprawnego działania Twojego projektu Django.
