# Instalacja Pythona i tworzenie środowiska wirtualnego

## Spis treści

1. [Instalacja Pythona](#1-instalacja-pythona)
2. [Sprawdzenie instalacji](#2-sprawdzenie-instalacji)
3. [Tworzenie środowiska wirtualnego](#3-tworzenie-środowiska-wirtualnego)
4. [Aktywacja środowiska wirtualnego](#4-aktywacja-środowiska-wirtualnego)
5. [Dezaktywacja środowiska wirtualnego](#5-dezaktywacja-środowiska-wirtualnego)

---

## 1. Instalacja Pythona

### Krok 1: Pobranie Pythona

1. Wejdź na stronę [python.org](https://www.python.org/downloads/).
2. Pobierz najnowszą wersję Pythona odpowiednią dla Twojego systemu operacyjnego (Windows, macOS, Linux).

### Krok 2: Instalacja Pythona (Windows/macOS)

- **Windows**:

  1. Uruchom pobrany plik `.exe`.
  2. Zaznacz opcję **Add Python to PATH**.
  3. Kliknij **Install Now** i postępuj zgodnie z instrukcjami instalatora.

- **macOS**:

  1. Otwórz pobrany plik `.pkg`.
  2. Postępuj zgodnie z instrukcjami instalatora, aby zainstalować Pythona.

- **Linux**:

  1. Otwórz terminal.
  2. Wpisz komendę:

  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

---

## 2. Sprawdzenie instalacji

Po instalacji upewnij się, że Python został zainstalowany poprawnie:

1. Otwórz terminal (lub wiersz poleceń w Windowsie).
2. Wpisz komendę, aby sprawdzić wersję Pythona:

   ```bash
   python --version
   ```

   lub (na niektórych systemach):

   ```bash
   python3 --version
   ```

3. Prawidłowy wynik to np. `Python 3.x.x`.

---

## 3. Tworzenie środowiska wirtualnego

Środowisko wirtualne pozwala na izolowanie zależności projektów. Aby stworzyć środowisko:

1. Przejdź do folderu, w którym chcesz utworzyć środowisko:

   ```bash
   cd /ścieżka/do/folderu/projektu
   ```

2. Utwórz środowisko wirtualne:

   ```bash
   python -m venv venv
   ```

   lub:

   ```bash
   python3 -m venv venv
   ```

   To polecenie utworzy katalog `venv`, który będzie zawierał wszystkie pliki środowiska wirtualnego.

---

## 4. Aktywacja środowiska wirtualnego

Aby aktywować środowisko wirtualne:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

Po aktywacji środowiska wirtualnego w terminalu powinno pojawić się `(venv)` przed ścieżką katalogu, co oznacza, że środowisko jest aktywne.

---

## 5. Dezaktywacja środowiska wirtualnego

Aby dezaktywować środowisko wirtualne, wpisz komendę:

```bash
deactivate
```
