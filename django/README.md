# Testowanie manualne endpointów API

W tej lekcji nauczysz się, jak ręcznie testować endpointy API w aplikacji Django. Testowanie manualne jest ważnym krokiem w zapewnieniu, że Twoje API działa zgodnie z oczekiwaniami. Wykorzystamy narzędzia takie jak Postman oraz cURL, aby sprawdzić, jak działają różne endpointy.

## Krok 1: Instalacja Postmana

Postman to popularne narzędzie do testowania API. Możesz je pobrać i zainstalować ze strony [Postman](https://www.postman.com/downloads/). Po zainstalowaniu uruchom aplikację.

## Krok 2: Uruchomienie serwera Django

Upewnij się, że Twój serwer Django działa. Możesz to zrobić, wykonując poniższe polecenie w terminalu:

```bash
python manage.py runserver
```

Domyślnie serwer uruchomi się na adresie `http://127.0.0.1:8000/`.

## Krok 3: Tworzenie nowego żądania w Postmanie

1. Otwórz Postmana.
2. Kliknij na przycisk `New` (Nowy) i wybierz `Request` (Żądanie).
3. Nazwij swoje żądanie i przypisz je do nowego lub istniejącego kolekcjonera, a następnie kliknij `Save` (Zapisz).

## Krok 4: Ustawienie żądania

1. Wybierz typ żądania (GET, POST, PUT, DELETE) z rozwijanej listy obok pola URL.
2. Wprowadź adres URL swojego endpointu. Na przykład, jeśli testujesz endpoint do pobierania wszystkich postów, wprowadź:

   ```
   http://127.0.0.1:8000/api/posts/
   ```

## Krok 5: Dodawanie danych do żądania (dla POST/PUT)

Jeśli wysyłasz dane (np. w żądaniu POST lub PUT), wykonaj poniższe kroki:

1. Kliknij zakładkę `Body` (Treść) w Postmanie.
2. Wybierz `raw` i następnie wybierz `JSON` z rozwijanej listy po prawej stronie.
3. Wprowadź dane w formacie JSON. Na przykład:

   ```json
   {
     "title": "Nowy post",
     "content": "Treść nowego posta"
   }
   ```

## Krok 6: Wysyłanie żądania

1. Po skonfigurowaniu żądania kliknij przycisk `Send` (Wyślij).
2. Postman wyśle żądanie do serwera, a odpowiedź pojawi się w dolnej części okna.

## Krok 7: Analiza odpowiedzi

- **Status odpowiedzi**: Sprawdź kod statusu HTTP. Kod `200` oznacza, że żądanie zakończyło się sukcesem, `201` oznacza, że zasób został stworzony, `404` oznacza, że zasób nie został znaleziony, a `500` oznacza błąd serwera.
- **Treść odpowiedzi**: Zobacz treść odpowiedzi w zakładce `Body`. Powinieneś zobaczyć dane zwracane przez API.

## Krok 8: Testowanie innych endpointów

Powtórz kroki 3-7 dla innych endpointów API, które chcesz przetestować, zmieniając typ żądania i dane, jeśli to konieczne.

## Krok 9: Testowanie za pomocą cURL (opcjonalnie)

Jeśli wolisz testować API za pomocą terminala, możesz użyć cURL. Oto przykład żądania GET:

```bash
curl -X GET http://127.0.0.1:8000/api/posts/
```

A oto przykład żądania POST:

```bash
curl -X POST http://127.0.0.1:8000/api/posts/ -H "Content-Type: application/json" -d '{"title": "Nowy post", "content": "Treść nowego posta"}'
```

## Podsumowanie

W tej lekcji nauczyłeś się, jak ręcznie testować endpointy API w aplikacji Django. Wykorzystując Postmana lub cURL, możesz sprawdzić, czy Twoje API działa poprawnie i zgodnie z oczekiwaniami. Regularne testowanie jest kluczowe dla zapewnienia jakości i niezawodności Twojej aplikacji.
