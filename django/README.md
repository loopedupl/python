# Zarządzanie plikami statycznymi i mediami w Django

W tej lekcji nauczysz się, jak zarządzać plikami statycznymi (np. CSS, JavaScript, obrazki) oraz plikami medialnymi (uploadowane przez użytkowników) w projekcie Django. Skonfigurujemy plik `settings.py`, dodamy ścieżki do plików i zrozumiemy różnice między nimi.

---

## Krok 1: Zrozumienie plików statycznych i mediów

1. **Pliki statyczne** – to pliki, które nie zmieniają się dynamicznie, jak pliki CSS, JavaScript czy obrazy wykorzystywane w szablonach. Są one dostarczane bezpośrednio do przeglądarki.
2. **Pliki medialne** – to pliki, które są uploadowane przez użytkowników, takie jak zdjęcia profilowe, dokumenty czy inne pliki.

---

## Krok 2: Konfiguracja plików statycznych

1. **STATIC_URL**: W pliku `settings.py` ustaw ścieżkę URL dla plików statycznych. Django będzie używać tej ścieżki do serwowania plików.

   ```python
   STATIC_URL = '/static/'
   ```

2. **STATIC_ROOT**: W przypadku wdrażania aplikacji na produkcji, wszystkie pliki statyczne powinny zostać zebrane w jedno miejsce. Skonfiguruj `STATIC_ROOT` do katalogu, w którym będą przechowywane zebrane pliki.

   ```python
   STATIC_ROOT = BASE_DIR / 'static'
   ```

3. **Tworzenie katalogu na pliki statyczne**:
   W głównym katalogu projektu utwórz folder `static`:

   ```bash
   mkdir static
   ```

4. **Dodanie plików statycznych**:
   Umieść swoje pliki CSS, JavaScript i obrazy w odpowiednich podkatalogach w folderze `static`. Na przykład:
   ```
   static/
       css/
           style.css
       js/
           script.js
       images/
           logo.png
   ```

---

## Krok 3: Serwowanie plików statycznych

1. **W czasie dewelopmentu**:
   Django automatycznie serwuje pliki statyczne podczas pracy w trybie deweloperskim (DEBUG=True).

2. **Na produkcji**:
   Po wdrożeniu aplikacji na serwerze produkcyjnym, użyj komendy `collectstatic`, aby zebrać wszystkie pliki statyczne w jednym katalogu:
   ```bash
   python manage.py collectstatic
   ```
   Pliki zostaną przeniesione do katalogu `STATIC_ROOT`.

---

## Krok 4: Konfiguracja plików medialnych

1. **MEDIA_URL**: Określa URL, pod którym dostępne będą pliki uploadowane przez użytkowników.

   ```python
   MEDIA_URL = '/media/'
   ```

2. **MEDIA_ROOT**: Określa katalog, w którym będą przechowywane pliki uploadowane przez użytkowników. Tworzymy katalog `media/` w głównym katalogu projektu.

   ```python
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

3. **Tworzenie katalogu na pliki medialne**:
   Utwórz folder `media` w głównym katalogu projektu:
   ```bash
   mkdir media
   ```

---

## Krok 5: Ustawienie URL dla plików statycznych i mediów

1. Aby móc serwować pliki statyczne i media w trybie deweloperskim, musisz zaktualizować plik `urls.py` projektu.

2. **Edytuj plik `urls.py`**:
   Dodaj obsługę dla plików statycznych i mediów:

   ```python
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns = [
       # inne ścieżki
   ]

   if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

---

## Krok 6: Praca z plikami na produkcji

1. Na produkcji powinieneś używać serwera takiego jak Nginx lub S3 (dla plików mediów) do serwowania plików statycznych i mediów.
2. Pliki statyczne i media na serwerze produkcyjnym nie są serwowane przez Django. Skorzystaj z dedykowanego rozwiązania jak Nginx, aby serwować te pliki bezpośrednio.

---

## Krok 7: Podsumowanie

Zarządzanie plikami statycznymi i mediami w Django wymaga odpowiedniej konfiguracji, aby serwowanie plików przebiegało bezproblemowo. Pliki statyczne są używane do wyświetlania elementów UI, takich jak style i skrypty, a pliki media obsługują treści przesyłane przez użytkowników.
