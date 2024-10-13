# Walidacja danych oraz obsługa błędów w Django REST Framework

W tej lekcji nauczysz się, jak walidować dane w Django REST Framework (DRF) oraz jak obsługiwać błędy walidacji, aby zapewnić użytkownikom przyjazne i zrozumiałe komunikaty o błędach. Walidacja danych jest kluczowa w procesie przetwarzania danych przesyłanych przez użytkowników.

## Krok 1: Podstawowa walidacja w serializerze

Django REST Framework automatycznie waliduje dane na poziomie pól w serializerze. Gdy tworzysz serializer, DRF zapewnia podstawową walidację dla zdefiniowanych pól.

Przykład prostego serializera z podstawową walidacją:

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']
```

W tym przypadku DRF automatycznie zweryfikuje, czy pola `title` i `content` są obecne w przesyłanych danych.

## Krok 2: Walidacja na poziomie pola

Możesz dodać własne zasady walidacji na poziomie pola, definiując metodę `validate_<field_name>` w serializerze.

Przykład:

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Tytuł musi mieć co najmniej 5 znaków.")
        return value
```

W tym przykładzie, jeśli `title` ma mniej niż 5 znaków, zostanie zgłoszony błąd walidacji.

## Krok 3: Walidacja całego obiektu

Możesz również walidować dane na poziomie całego obiektu, definiując metodę `validate` w serializerze.

Przykład:

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def validate(self, attrs):
        if attrs['content'] == "":
            raise serializers.ValidationError("Zawartość posta nie może być pusta.")
        return attrs
```

W tym przypadku, jeśli `content` jest pusty, walidacja zakończy się niepowodzeniem.

## Krok 4: Użycie walidatorów

Django REST Framework pozwala na użycie wbudowanych walidatorów, które mogą być używane w polach serializerów.

Przykład:

```python
from rest_framework import serializers
from django.core.validators import MinLengthValidator

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[MinLengthValidator(5)])

    class Meta:
        model = Post
        fields = ['title', 'content']
```

W tym przypadku pole `title` musi mieć co najmniej 5 znaków, a walidator `MinLengthValidator` zapewnia tę funkcjonalność.

## Krok 5: Walidacja z użyciem kontekstu

Możesz używać kontekstu do walidacji, co pozwala na uwzględnienie dodatkowych informacji, takich jak inne pola lub status użytkownika.

Przykład:

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def validate(self, attrs):
        user = self.context['request'].user
        if user.is_authenticated and not user.has_perm('can_create_post'):
            raise serializers.ValidationError("Nie masz uprawnień do tworzenia postów.")
        return attrs
```

W tym przykładzie walidacja sprawdza, czy użytkownik ma odpowiednie uprawnienia do tworzenia postów.

## Krok 6: Obsługa błędów walidacji

Gdy walidacja się nie powiedzie, DRF automatycznie generuje odpowiedź z informacjami o błędach. Możesz dostosować te komunikaty, aby były bardziej przyjazne dla użytkownika.

Przykład:

```python
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def validate(self, attrs):
        if 'title' not in attrs:
            raise serializers.ValidationError({"title": "To pole jest wymagane."})
        return attrs
```

## Najczęstsze błędy HTTP i ich znaczenie

1. **400 Bad Request** - Żądanie nie może być przetworzone z powodu błędu klienta (np. niepoprawne dane wejściowe).
2. **401 Unauthorized** - Użytkownik nie jest autoryzowany do wykonania żądanej akcji. Wymagana jest autoryzacja.
3. **403 Forbidden** - Serwer rozumie żądanie, ale odmawia jego wykonania, ponieważ użytkownik nie ma odpowiednich uprawnień.
4. **404 Not Found** - Żądany zasób nie został znaleziony. Może to być spowodowane tym, że zasób został usunięty lub adres URL jest niepoprawny.
5. **405 Method Not Allowed** - Metoda żądania jest niedozwolona dla wskazanego zasobu. Na przykład, jeśli próbujesz użyć metody POST na zasobie, który obsługuje tylko GET.
6. **500 Internal Server Error** - Serwer napotkał niespodziewany błąd i nie może zrealizować żądania. Może to być spowodowane błędem w kodzie aplikacji.

## Podsumowanie

W tej lekcji nauczyłeś się, jak walidować dane w Django REST Framework oraz jak obsługiwać różne błędy, aby zapewnić użytkownikom jasne i pomocne komunikaty o błędach. Zrozumienie tych mechanizmów jest kluczowe dla tworzenia aplikacji API, które są zarówno funkcjonalne, jak i przyjazne dla użytkownika.
