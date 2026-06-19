System Zarządzania Zadaniami Domowymi

Spis treści
- Tytuł i nazwa projektu
- Lista i krótki opis funkcjonalności
- Instrukcja obsługi
- Struktura kodu źródłowego
- Dane wejściowe

Lista i krótki opis zaimplementowanych w projekcie funkcjonalności

Przegląd zadań: Dynamiczna lista wszystkich wprowadzonych zadań domowych wyświetlana w czytelnej tabeli.
Zarządzanie zadaniami (CRUD): Pełna możliwość dodawania nowych zadań, edycji istniejących rekordów oraz ich usuwania.
Filtrowanie i wyszukiwanie: Możliwość filtrowania zadań po statusie (Nowe, W trakcie, Zakończone) oraz wyszukiwania tekstowego po opisie, gdzie aplikacja zachowuje stan filtrów w adresie URL.
Zabezpieczenie przed usuwaniem: Monit JavaScript potwierdzający chęć usunięcia zadania.
Walidacja danych: Blokada zapisu pustych pól oraz blokowanie dat z przeszłości przy tworzeniu nowych zadań.

Instrukcja obsługi

Do uruchomienia projektu wymagany jest Python w wersji 3.11 lub nowszej oraz framework Django.
W celu instalacji wymaganych paczek należy otworzyć terminal w folderze projektu i wykonać komendę pip install django.
Następnie należy uruchomić serwer deweloperski wpisując komendę python manage.py runserver.
Na koniec należy otworzyć przeglądarkę internetową i wejść pod adres http://127.0.0.1:8000/.

Kod źródłowy aplikacji

Repozytorium zawiera kompletny kod źródłowy aplikacji podzielony na główny folder konfiguracji ZadaniaDomowe oraz folder aplikacji app_zadania, w którym znajdują się pliki models.py (baza danych), views.py (logika biznesowa) oraz urls.py (routing ścieżek).

Plik z przykładowymi danymi wejściowymi

Projekt korzysta z lokalnej bazy danych SQLite zapisanej w pliku db.sqlite3, która zawiera już przygotowane, przykładowe zadania domowe gotowe do przetestowania od razu po uruchomieniu aplikacji.