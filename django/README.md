### Zarządzanie aplikacjami i bibliotekami w `INSTALLED_APPS` w Django

W tej lekcji dowiesz się, jak zarządzać aplikacjami oraz bibliotekami w Django za pomocą sekcji `INSTALLED_APPS` w pliku `settings.py`. Sekcja ta jest odpowiedzialna za aktywowanie i konfigurację aplikacji oraz bibliotek, które są używane w projekcie.

---

## Krok 1: Zrozumienie `INSTALLED_APPS`

1. `INSTALLED_APPS` to lista aplikacji Django i bibliotek zewnętrznych, które są aktywowane w projekcie.
2. Znajduje się ona w pliku `settings.py` i jest kluczowa dla działania projektu, ponieważ Django korzysta z tych aplikacji do ładowania modeli, widoków, formularzy i innych komponentów.

---

## Krok 2: Znalezienie sekcji `INSTALLED_APPS`

1. Otwórz plik `settings.py` w głównym katalogu swojego projektu.
2. Przewiń plik, aż znajdziesz sekcję `INSTALLED_APPS`. Powinna ona wyglądać mniej więcej tak:
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
3. Każdy wpis w tej liście to albo wbudowana aplikacja Django, albo aplikacja zewnętrzna/biblioteka, albo własna aplikacja, którą utworzyłeś.

---

## Krok 3: Dodawanie własnych aplikacji do `INSTALLED_APPS`

1. **Tworzenie własnej aplikacji**:

   - Aby stworzyć nową aplikację w Django, użyj komendy:
     ```bash
     python manage.py startapp nazwa_aplikacji
     ```
   - Ta komenda stworzy nowy folder aplikacji z podstawową strukturą w katalogu projektu.

2. **Dodanie aplikacji do `INSTALLED_APPS`**:

   - Po utworzeniu aplikacji, dodaj jej nazwę do listy `INSTALLED_APPS` w pliku `settings.py`. Na przykład, jeśli utworzyłeś aplikację o nazwie `blog`, zaktualizuj sekcję `INSTALLED_APPS`:
     ```python
     INSTALLED_APPS = [
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'blog',
     ]
     ```

3. **Restart serwera**:
   - Po dodaniu aplikacji, uruchom ponownie serwer, aby Django załadowało nową aplikację. Użyj komendy:
     ```bash
     python manage.py runserver
     ```

---

## Krok 4: Dodawanie zewnętrznych bibliotek do `INSTALLED_APPS`

1. **Instalacja biblioteki**:

   - Aby dodać bibliotekę zewnętrzną, najpierw zainstaluj ją za pomocą `pip`. Na przykład, aby zainstalować bibliotekę Django REST Framework:
     ```bash
     pip install djangorestframework
     ```

2. **Dodanie biblioteki do `INSTALLED_APPS`**:

   - Po instalacji, dodaj nazwę biblioteki do listy `INSTALLED_APPS`. W przypadku Django REST Framework będzie to wyglądać tak:
     ```python
     INSTALLED_APPS = [
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'rest_framework',
     ]
     ```

3. **Migracje bazy danych (jeśli wymagane)**:
   - Niektóre biblioteki lub aplikacje mogą wymagać migracji bazy danych po ich instalacji. W takim przypadku uruchom komendę:
     ```bash
     python manage.py migrate
     ```

---

## Krok 5: Usuwanie aplikacji z `INSTALLED_APPS`

1. Jeśli chcesz usunąć aplikację z projektu, wystarczy, że usuniesz jej nazwę z listy `INSTALLED_APPS` w pliku `settings.py`.

   - Na przykład, aby usunąć aplikację `blog`, usuń wpis:
     ```python
     INSTALLED_APPS = [
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         # 'blog' - usunięto aplikację
     ]
     ```

2. Jeśli aplikacja miała migracje lub dane w bazie, może być konieczne ręczne usunięcie tabel związanych z aplikacją z bazy danych lub cofnięcie migracji.

---

## Krok 6: Podsumowanie

Sekcja `INSTALLED_APPS` jest centralnym miejscem, w którym zarządzasz aplikacjami i bibliotekami w Django. Każda aplikacja, którą chcesz używać, musi być tutaj dodana. Dzięki poprawnej konfiguracji tej sekcji, Django może prawidłowo ładować aplikacje, które definiują modele, widoki, szablony i inne komponenty.
