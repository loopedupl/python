# Międzynarodowość i lokalizacja w Django REST Framework

W tej lekcji nauczysz się, jak zaimplementować międzynarodowość (internationalization, `i18n`) i lokalizację (localization, `l10n`) w projekcie Django, używając Django REST Framework (DRF). Dzięki tym funkcjom, Twoje API będzie mogło zwracać treści dostosowane do różnych języków i formatów zależnych od lokalizacji użytkownika.

---

## Krok 1: Włączenie obsługi międzynarodowości i lokalizacji

1. Otwórz plik `settings.py` i upewnij się, że poniższe ustawienia są aktywne:

   ```python
   USE_I18N = True  # Międzynarodowość (internationalization)
   USE_L10N = True  # Lokalizacja (localization)
   USE_TZ = True  # Obsługa stref czasowych
   ```

2. Te ustawienia aktywują obsługę języków, formatów daty, liczby oraz obsługę stref czasowych.

---

## Krok 2: Ustawienie domyślnego języka i strefy czasowej

1. W pliku `settings.py` ustaw domyślny język API i strefę czasową:

   ```python
   LANGUAGE_CODE = 'pl'  # Ustawienie domyślnego języka na polski
   TIME_ZONE = 'Europe/Warsaw'  # Ustawienie strefy czasowej na Warszawę
   ```

2. Wartość `LANGUAGE_CODE` możesz zmieniać na inne kody językowe, np. `'en-us'` dla języka angielskiego (USA).

---

## Krok 3: Ustawienie lokalizacji w Django REST Framework

1. Aby DRF automatycznie zwracało treści w odpowiednich językach i formatach, upewnij się, że middleware `LocaleMiddleware` jest włączony. Sprawdź w pliku `settings.py` w sekcji `MIDDLEWARE`:

   ```python
   MIDDLEWARE = [
       'django.middleware.locale.LocaleMiddleware',  # Middleware lokalizacyjny
       # Inne middleware...
   ]
   ```

2. `LocaleMiddleware` odpowiada za rozpoznawanie preferencji językowych na podstawie nagłówków HTTP (np. `Accept-Language`).

---

## Krok 4: Konfiguracja języków w projekcie

1. W `settings.py` zdefiniuj listę obsługiwanych języków w projekcie:

   ```python
   LANGUAGES = [
       ('pl', 'Polski'),
       ('en', 'English'),
       ('de', 'Deutsch'),
   ]
   ```

2. Django i DRF będą teraz wspierały te języki i dostosują odpowiedzi w zależności od wybranego przez użytkownika języka.

---

## Krok 5: Tłumaczenie treści w API

1. Aby przetłumaczyć treści zwracane przez API, użyj mechanizmu tłumaczeń Django. Najpierw zaimportuj funkcję `gettext` w swoich widokach lub serializerach:

   ```python
   from django.utils.translation import gettext as _
   ```

2. W swoich serializerach lub widokach oznacz teksty, które chcesz przetłumaczyć, np. komunikaty walidacyjne:

   ```python
   class ExampleSerializer(serializers.Serializer):
       title = serializers.CharField()

       def validate_title(self, value):
           if len(value) < 5:
               raise serializers.ValidationError(_("Tytuł musi mieć co najmniej 5 znaków."))
           return value
   ```

---

## Krok 6: Tłumaczenie komunikatów błędów

1. W DRF tłumaczenia możesz wykorzystać do zmiany komunikatów błędów. Na przykład, gdy używasz walidatorów w serializerach, możesz oznaczyć je do tłumaczenia:

   ```python
   from django.utils.translation import gettext_lazy as _

   class PostSerializer(serializers.ModelSerializer):
       title = serializers.CharField(error_messages={'blank': _("Tytuł nie może być pusty.")})
   ```

2. Dzięki temu komunikaty błędów będą dostosowane do preferencji językowych użytkownika.

---

## Krok 7: Generowanie plików tłumaczeń

1. Aby wygenerować pliki tłumaczeń, uruchom komendę:

   ```bash
   django-admin makemessages -l pl
   ```

2. Plik `.po` zostanie utworzony w katalogu `locale/pl/LC_MESSAGES/`. Otwórz go i dodaj tłumaczenia dla oznaczonych tekstów:
   ```po
   msgid "Tytuł musi mieć co najmniej 5 znaków."
   msgstr "The title must have at least 5 characters."
   ```

---

## Krok 8: Kompilowanie tłumaczeń

1. Po wprowadzeniu tłumaczeń, uruchom komendę, aby je skompilować:

   ```bash
   django-admin compilemessages
   ```

2. Tłumaczenia będą teraz dostępne w Twoim API.

---

## Krok 9: Przełączanie języków za pomocą nagłówków

1. Użytkownicy mogą zmieniać język API, wysyłając odpowiedni nagłówek HTTP `Accept-Language`. Przykład zapytania z curl:

   ```bash
   curl -H "Accept-Language: pl" http://localhost:8000/api/posts/
   ```

2. DRF automatycznie dostosuje odpowiedzi do wybranego języka.

---

## Krok 10: Dodanie logiki przełączania języków

1. Możesz także zaimplementować logikę przełączania języka w widoku. Na przykład, w widoku opartym na klasach:

   ```python
   from django.utils import translation
   from rest_framework.views import APIView

   class MyView(APIView):
       def get(self, request, *args, **kwargs):
           user_language = request.headers.get('Accept-Language', 'en')
           translation.activate(user_language)
           # Twoja logika widoku
   ```

2. Możesz aktywować język na podstawie nagłówka lub dowolnego innego mechanizmu.

---

## Krok 11: Obsługa plików tłumaczeń

1. Dodaj ustawienie `LOCALE_PATHS` do pliku `settings.py`, aby wskazać Django, gdzie znajdują się pliki tłumaczeń:

   ```python
   LOCALE_PATHS = [BASE_DIR / 'locale']
   ```

2. Katalog `locale/` będzie przechowywać pliki tłumaczeń `.po` oraz `.mo` dla każdego języka.

---

## Podsumowanie

Dzięki powyższym krokom Twój projekt oparty na Django REST Framework będzie obsługiwał różne języki oraz lokalne formaty danych, takie jak daty i liczby. Mechanizm międzynarodowości i lokalizacji pozwoli Ci dostosować Twoje API do potrzeb użytkowników z różnych krajów.
