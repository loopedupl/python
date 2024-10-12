# Konfiguracja bazy danych w Django

## Spis treści

1. [Wprowadzenie](#1-wprowadzenie)
2. [Wybór bazy danych](#2-wybór-bazy-danych)
3. [Instalacja bazy danych](#3-instalacja-bazy-danych)
4. [Instalacja biblioteki bazy danych](#4-instalacja-biblioteki-bazy-danych)
5. [Konfiguracja ustawień bazy danych](#5-konfiguracja-ustawień-bazy-danych)
6. [Podsumowanie](#6-podsumowanie)

---

## 1. Wprowadzenie

Django obsługuje wiele różnych baz danych, w tym SQLite, PostgreSQL, MySQL i inne. W tym przewodniku omówimy, jak skonfigurować bazę danych w projekcie Django.

---

## 2. Wybór bazy danych

Domyślną bazą danych w Django jest SQLite, która jest łatwa w użyciu i nie wymaga dodatkowej konfiguracji. Jeśli jednak potrzebujesz bardziej zaawansowanej bazy danych, możesz wybrać PostgreSQL lub MySQL. Upewnij się, że masz zainstalowaną odpowiednią bazę danych na swoim systemie.

---

## 3. Instalacja bazy danych

### PostgreSQL

#### Krok 1: Zainstaluj PostgreSQL

- **Windows**: Możesz pobrać instalator z [oficjalnej strony PostgreSQL](https://www.postgresql.org/download/windows/).
- **macOS**: Użyj Homebrew:

  ```bash
  brew install postgresql
  ```

- **Linux**: Użyj menedżera pakietów (np. `apt` dla Debiana/Ubuntu):

  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```

#### Krok 2: Utwórz bazę danych i użytkownika

Po zainstalowaniu PostgreSQL, uruchom terminal i wykonaj następujące polecenia, aby utworzyć bazę danych i użytkownika:

1. Uruchom konsolę PostgreSQL:

   ```bash
   sudo -u postgres psql
   ```

2. Utwórz nowego użytkownika:

   ```sql
   CREATE USER nazwa_użytkownika WITH PASSWORD 'twoje_hasło';
   ```

3. Utwórz bazę danych:

   ```sql
   CREATE DATABASE nazwa_bazy_danych OWNER nazwa_użytkownika;
   ```

4. Przyznaj uprawnienia:

   ```sql
   GRANT ALL PRIVILEGES ON DATABASE nazwa_bazy_danych TO nazwa_użytkownika;
   ```

5. Wyjdź z konsoli PostgreSQL:

   ```sql
   \q
   ```

### MySQL

#### Krok 1: Zainstaluj MySQL

- **Windows**: Możesz pobrać instalator z [oficjalnej strony MySQL](https://dev.mysql.com/downloads/installer/).
- **macOS**: Użyj Homebrew:

  ```bash
  brew install mysql
  ```

- **Linux**: Użyj menedżera pakietów (np. `apt` dla Debiana/Ubuntu):

  ```bash
  sudo apt update
  sudo apt install mysql-server
  ```

#### Krok 2: Utwórz bazę danych i użytkownika

Po zainstalowaniu MySQL, uruchom terminal i wykonaj następujące polecenia, aby utworzyć bazę danych i użytkownika:

1. Uruchom konsolę MySQL:

   ```bash
   sudo mysql -u root -p
   ```

2. Utwórz nowego użytkownika:

   ```sql
   CREATE USER 'nazwa_użytkownika'@'localhost' IDENTIFIED BY 'twoje_hasło';
   ```

3. Utwórz bazę danych:

   ```sql
   CREATE DATABASE nazwa_bazy_danych;
   ```

4. Przyznaj uprawnienia:

   ```sql
   GRANT ALL PRIVILEGES ON nazwa_bazy_danych.* TO 'nazwa_użytkownika'@'localhost';
   ```

5. Wyjdź z konsoli MySQL:

   ```sql
   EXIT;
   ```

## 4. Instalacja biblioteki bazy danych

### Krok 1: Zainstaluj odpowiednią bibliotekę

W zależności od wybranej bazy danych, będziesz musiał zainstalować odpowiednią bibliotekę. Oto przykłady:

- Dla **PostgreSQL**:

  ```bash
  pip install psycopg2
  ```

- Dla **MySQL**:

  ```bash
  pip install mysqlclient
  ```

- Dla **SQLite** (nie wymaga instalacji, jest wbudowana w Pythona).

## 5. Konfiguracja ustawień bazy danych

### Krok 1: Edytuj plik `settings.py`

Otwórz plik `settings.py`, który znajduje się w folderze twojego projektu. W sekcji `DATABASES` skonfiguruj ustawienia bazy danych. Oto przykładowa konfiguracja dla różnych baz danych:

**Dla PostgreSQL:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nazwa_bazy_danych',
        'USER': 'nazwa_użytkownika',
        'PASSWORD': 'twoje_hasło',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**Dla MySQL:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nazwa_bazy_danych',
        'USER': 'nazwa_użytkownika',
        'PASSWORD': 'twoje_hasło',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**Dla SQLite (domyślna konfiguracja):**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

## 6. Podsumowanie

W tej lekcji nauczyłeś się, jak skonfigurować bazę danych w projekcie Django, w tym jak zainstalować bazę danych, utworzyć użytkownika oraz bazę danych, zainstalować potrzebne biblioteki oraz skonfigurować ustawienia w pliku `settings.py`. Teraz możesz zaczynać pracę z bazą danych w swojej aplikacji Django!
