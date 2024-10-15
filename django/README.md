# Optymalizacja Wydajności i Cache w Django REST Framework (DRF)

W tej lekcji nauczysz się, jak zoptymalizować wydajność API w Django REST Framework, wykorzystując mechanizmy cache, optymalizację zapytań ORM oraz inne techniki. Wydajność API ma ogromny wpływ na doświadczenia użytkowników, dlatego warto stosować dobre praktyki w tym zakresie.

---

## Krok 1: Włączenie cache'owania dla API w DRF

1. **Cache** pozwala na przechowywanie wyników odpowiedzi API, co zmniejsza liczbę zapytań do bazy danych i poprawia czas odpowiedzi.

2. Aby skonfigurować cache, edytuj plik `settings.py` i skonfiguruj backend cache'owania, np. Redis:

   W pliku `settings.py`:

   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.redis.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',
       }
   }
   ```

3. Upewnij się, że Redis jest zainstalowany i działa na serwerze.

---

## Krok 2: Cache'owanie wyników widoków API

1. W Django REST Framework możesz cache'ować wyniki zapytań do API, co przyspiesza odpowiedzi w przypadku częstych zapytań.

2. Aby cache'ować wyniki widoku, użyj dekoratora `@method_decorator` w widoku opartym na klasach:

   ```python
   from django.utils.decorators import method_decorator
   from django.views.decorators.cache import cache_page
   from rest_framework.views import APIView

   @method_decorator(cache_page(60 * 15), name='dispatch')  # Cache na 15 minut
   class MyAPIView(APIView):
       def get(self, request, *args, **kwargs):
           # logika widoku
           return Response({'data': 'cached data'})
   ```

3. To spowoduje cache'owanie odpowiedzi tego widoku na 15 minut, co zmniejszy liczbę wywołań bazy danych.

---

## Krok 3: Cache'owanie na poziomie DRF Viewsets

1. Jeżeli korzystasz z **Viewsets**, możesz także zastosować cache na poziomie tych widoków.

2. W pliku `views.py`, dodaj cache do odpowiednich akcji (np. `list()`):

   ```python
   from django.utils.decorators import method_decorator
   from django.views.decorators.cache import cache_page
   from rest_framework.viewsets import ModelViewSet

   @method_decorator(cache_page(60 * 15), name='list')
   class MyModelViewSet(ModelViewSet):
       queryset = MyModel.objects.all()
       serializer_class = MyModelSerializer
   ```

3. Teraz wyniki zapytań do endpointu listowania zasobów będą cache'owane na 15 minut.

---

## Krok 4: Cache'owanie wyników zapytań do bazy danych

1. W przypadku zapytań do bazy danych możesz cache'ować ich wyniki, aby zmniejszyć liczbę wykonywanych zapytań.

2. Przykład użycia cache'owania zapytania w widoku API:

   ```python
   from django.core.cache import cache
   from rest_framework.response import Response
   from rest_framework.views import APIView

   class MyAPIView(APIView):
       def get(self, request, *args, **kwargs):
           data = cache.get('my_data')
           if not data:
               data = MyModel.objects.all()
               cache.set('my_data', data, timeout=60*15)  # Cache na 15 minut
           return Response({'data': list(data.values())})
   ```

3. Dzięki temu zapytanie do bazy danych jest wykonywane tylko raz na 15 minut, a dane są przechowywane w cache.

---

## Krok 5: Optymalizacja zapytań ORM

1. Django ORM jest potężny, ale domyślnie może generować wiele niepotrzebnych zapytań. Aby temu zapobiec, używaj metod takich jak `select_related()` i `prefetch_related()` w widokach DRF.

2. Przykład:

   ```python
   class MyModelViewSet(ModelViewSet):
       queryset = MyModel.objects.select_related('related_model').all()
       serializer_class = MyModelSerializer
   ```

3. `select_related()` redukuje liczbę zapytań, wykonując złączenia na poziomie SQL, co zwiększa wydajność.

---

## Krok 6: Optymalizacja serializatorów

1. Serializatory w DRF mogą generować duże obciążenie przy serializowaniu złożonych obiektów. Używaj opcji takich jak `only()` i `defer()`, aby ograniczyć liczbę pól pobieranych z bazy danych:

   ```python
   class MyModelViewSet(ModelViewSet):
       queryset = MyModel.objects.only('field1', 'field2').all()
       serializer_class = MyModelSerializer
   ```

2. Ograniczenie liczby pobieranych pól zmniejsza ilość przesyłanych danych i przyspiesza odpowiedź API.

---

## Krok 7: Kompresja odpowiedzi API

1. Możesz kompresować odpowiedzi API, aby zmniejszyć ilość przesyłanych danych. W DRF, możesz użyć kompresji Gzip:

   W pliku `settings.py`:

   ```python
   MIDDLEWARE = [
       'django.middleware.gzip.GZipMiddleware',
       # inne middleware
   ]
   ```

2. Użycie `GZipMiddleware` spowoduje, że odpowiedzi API będą kompresowane, co przyspieszy ich transfer do klienta.

---

## Krok 8: Korzystanie z limitowania zapytań (Rate Limiting)

1. Aby zapobiec przeciążeniu serwera, można ograniczyć liczbę zapytań od jednego użytkownika w określonym czasie. DRF posiada wbudowane wsparcie dla rate limiting.

2. W pliku `settings.py` skonfiguruj globalny limit zapytań:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_THROTTLE_RATES': {
           'user': '100/hour',  # 100 zapytań na godzinę na użytkownika
       }
   }
   ```

3. Możesz też skonfigurować throttling na poziomie widoków, np.:

   ```python
   from rest_framework.throttling import UserRateThrottle
   from rest_framework.views import APIView

   class MyAPIView(APIView):
       throttle_classes = [UserRateThrottle]

       def get(self, request, *args, **kwargs):
           return Response({'message': 'This is rate-limited'})
   ```

4. Rate limiting zapobiega nadmiernym zapytaniom i chroni serwer przed przeciążeniem.

---

## Krok 9: Optymalizacja paginacji

1. W przypadku dużych zbiorów danych, zamiast zwracać wszystkie dane na raz, warto zastosować paginację.

2. W pliku `settings.py`:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
       'PAGE_SIZE': 20  # Liczba wyników na stronę
   }
   ```

3. Dzięki paginacji serwer nie musi zwracać całego zestawu danych na raz, co przyspiesza odpowiedź i zmniejsza obciążenie serwera.

---

## Podsumowanie

Optymalizacja wydajności w Django REST Framework obejmuje wiele obszarów, w tym cache'owanie, optymalizację zapytań do bazy danych, kompresję odpowiedzi oraz paginację. Implementując te techniki, poprawisz szybkość działania swojego API i zwiększysz jego skalowalność.
