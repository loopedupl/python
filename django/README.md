# Stworzenie projektu Django i plik .gitignore

## Spis treści

1. [Czym jest Django?](#1-czym-jest-django)
2. [Instalacja Django](#2-instalacja-django)
3. [Tworzenie nowego projektu Django](#3-tworzenie-nowego-projektu-django)
4. [Konfiguracja pliku .gitignore](#4-konfiguracja-pliku-gitignore)
5. [Uruchomienie serwera deweloperskiego](#5-uruchomienie-serwera-deweloperskiego)
6. [Podsumowanie](#6-podsumowanie)

---

## 1. Czym jest Django?

**Django** to wysokopoziomowy framework webowy napisany w Pythonie, który ułatwia tworzenie aplikacji internetowych. Oferuje wiele funkcji, takich jak automatyczne generowanie paneli administracyjnych, ORM (Object-Relational Mapping) i wsparcie dla wielu baz danych.

---

## 2. Instalacja Django

### Krok 1: Instalacja Pythona

Upewnij się, że masz zainstalowanego Pythona (najlepiej wersja 3.6 lub nowsza). Możesz sprawdzić wersję Pythona, uruchamiając:

```bash
python --version
```

Jeśli nie masz zainstalowanego Pythona, możesz go pobrać z [oficjalnej strony Pythona](https://www.python.org/downloads/).

### Krok 2: Instalacja Django

1. Otwórz terminal.
2. Zainstaluj Django za pomocą pip:

```bash
pip install django
```

---

## 3. Tworzenie nowego projektu Django

### Krok 1: Stworzenie nowego projektu

1. W terminalu przejdź do katalogu, w którym chcesz stworzyć projekt:

```bash
cd /ścieżka/do/katalogu
```

2. Wykonaj polecenie, aby utworzyć nowy projekt Django:

```bash
django-admin startproject nazwa_projektu
```

Zastąp `nazwa_projektu` nazwą swojego projektu.

### Krok 2: Przejdź do katalogu projektu

```bash
cd nazwa_projektu
```

---

## 4. Konfiguracja pliku .gitignore

Aby skonfigurować plik `.gitignore`, wykonaj następujące kroki:

### Krok 1: Utworzenie pliku .gitignore

1. W katalogu głównym projektu utwórz plik o nazwie `.gitignore`:

```bash
touch .gitignore
```

### Krok 2: Dodanie reguł do pliku .gitignore

Otwórz plik `.gitignore` w edytorze tekstowym i dodaj następujące linie, aby zignorować pliki i foldery, które nie powinny być śledzone przez Git:

```plaintext
# Django #
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files #
*.bak

# If you are using PyCharm #
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python #
*.py[cod]
*$py.class

# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.whl
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery
celerybeat-schedule.*

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Sublime Text #
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

# sftp configuration file
sftp-config.json

# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings

# Visual Studio Code #
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history
```

Te reguły pomogą w zignorowaniu plików tymczasowych i prywatnych danych.

---

## 5. Uruchomienie serwera deweloperskiego

Aby uruchomić serwer deweloperski Django:

1. Upewnij się, że jesteś w katalogu projektu.
2. Wykonaj polecenie:

```bash
python manage.py runserver
```

3. Otwórz przeglądarkę i przejdź do `http://127.0.0.1:8000/`, aby zobaczyć swoją aplikację Django.

---

## 6. Podsumowanie

W tej lekcji nauczyłeś się, jak stworzyć nowy projekt Django, skonfigurować plik `.gitignore`, aby ignorować niepotrzebne pliki, oraz uruchomić serwer deweloperski. Django to potężne narzędzie, które ułatwia rozwój aplikacji internetowych. Zachęcamy do dalszej eksploracji jego możliwości!
