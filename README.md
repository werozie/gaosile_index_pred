### 1.Charakterystyka oprogramowania:
- **Nazwa skrócona**
Petrol 95 predictor 
- **Nazwa pełna**
Unleaded 95 Petrol Octane Predictive Suite 
- **Krótki opis ze wskazaniem celów**
Oprogramowanie ma służyć jako narzędzie prognozujące ceny benzyny pb 95. 
Celem, który chcemy osiągnąć przy konstrukcji takiego oprogramowania jest utworzenie modeli, które w zależności od horyzontu czasowego, w jakim użytkownik będzie chciał prognozować dane, będą zwracać potencjalne wyniki dla przyszłości.  
Program będzie uwzględniał czynniki skorelowane ze zjawiskiem kształtowania tych właśnie cen.

### 2.Prawa autorskie:
- **Autorzy**
Jolanta Mieczyńska,
Weronika Zielińska,
Dominik Zakrzewski 
- **Warunki licencyjne do oprogramowania wytworzonego przez grupę**
  - CC BY-NC 4.0 DEED
  - BY - Uznanie autorstwa 
  - NC - Użycie niekomercyjne 
  - Brak dodatkowych ograniczeń

### 3.Specyfikacja wymagań.
Pogrupowana lista składająca się z następujących kolumn:
- Identyfikator,
- Nazwa,
- Opis,
- Priorytet: [1 – wymaganie, 2 – przydatne, 3 – opcjonalne]
- Kategoria: [funkcjonalne, poza funkcjonalne]

| Identyfikator | Nazwa                        | Opis | Priorytet | Kategoria       |
|---------------|------------------------------| --- |-----------|-----------------|
| WF1           | Prognozowanie cen benzyny 95 | System powinien umożliwiać precyzyjne prognozowanie cen benzyny PB95 | 1         | Funkcjonalne             |
| WF1.1           | Biblioteki | System powinien załadować biblioteki używane w projekcie | 1         | Funkcjonalne             |
| WF1.2           | Dane | System powinien załadować dane potrzebne do utworzenia modeli dla prognozy  | 1         | Funkcjonalne             |
| WF1.3           | Przygotowanie danych | System powinien odpowiednio przygotować dane do dalszej analizy | 1         | Funkcjonalne             |
| WF1.3.1           | Przygotowanie danych do modelu LSTM | System powinien odpowiednio przygotować dane w celu umożliwienia utworzenia modelu LSTM| 1        | Funkcjonalne             |
| WF1.3.2           | Przygotowanie danych do modelu SARIMA | System powinien odpowiednio przygotować dane w celu umożliwienia utworzenia modelu SARIMA| 1         | Funkcjonalne             |
| WF1.4           | Wizualizacja danych | System powinien zwiauzalizowac dane w celu lepszego ich zrozumienia | 1         | Funkcjonalne             |
| WF1.5           | Modele | System powinien utworzyć dwa modele do prognozowania cen benzyny PB95 | 1         | Funkcjonalne             |
| WF1.5.1           | Model 1 | System powinien utworzyć optymalny model LSTM do prognozowania cen benzyny PB95 | 1         | Funkcjonalne             |
| WF1.5.2           | Model 2 | System powinien utworzyć optymalny model SARIMA do prognozowania cen benzyny PB95 | 1         | Funkcjonalne             |
| WF1.6          | Wizualizacja wyników | System powinien zwizualizować prognozę cen benzyny PB95 | 1         | Funkcjonalne             |
| WF1.6.1          | Wizualizacja wyników 1 | System powinien zwizualizować prognozę cen benzyny PB95 przy użyciu modelu LSTM| 1         | Funkcjonalne             |
| WF1.6.2         | Wizualizacja wyników 2 | System powinien zwizualizować prognozę cen benzyny PB95 przy użyciu modelu SARIMA | 1         | Funkcjonalne             |
| WF2           | Interfejs użytkownika        | System powinien dostarczać intuicyjny interfejs użytkownika umożliwiający łatwe korzystanie z funkcji prognozowania cen. | 1         | Funkcjonalne    |
| WF3           | Baza danych cen paliw        | System powinien zarządzać bazą danych zawierającą historyczne ceny benzyny PB95 do celów trenowania modeli prognozowania. | 1         | Funkcjonalne    |
| NWF1          | Dokumentacja użytkownika     | Opracować pełną dokumentację użytkownika, zawierającą instrukcje obsługi, opis algorytmów prognozowania oraz dane wejściowe/wyjściowe. | 2         | Niefunkcjonalne    |
| NWF2          | Skalowalność systemu         | System powinien być skalowalny, dostosowuje się do zmieniającej się ilości danych historycznych. | 2         | Niefunkcjonalne |
| NWF3          | Rozszerzalność               | Program powinien być elastyczny ze względu na wprowadzanie nowych wariantów prognozowania (np. rozszerzenie o prognozowanie cen benzyny 98)| 2         | Niefunkcjonalne             |

### 4.Architektura systemu/oprogramowania
- **Architektura rozwoju – stos technologiczny**
  - **Język programowania:** Python 
  - **Pakiety:** Pandas, Keras 3.0, scikit-learn,  statsmodels, pyramid-arima
  - **Baza danych:** Baza danych zostanie poddana przekształceniom w programie Power Query, aby ujednolicić poziomy agregacji dla wszystkich zmiennych


**Zarządzanie zależnościami i wersjami:**
- **System kontroli wersji** - Github

**Architektura uruchomieniowa** – stos technologiczny

**Hosting:**
- Git Hub, Google Collab,


### 5.Testy
- **Scenariusz testów**
Wykonanie testów na wszystkich modelach - wyliczenie statystyk w celu zbadania dobroci modeli (MSE), uwzględnienie różnicy w działaniu obu modeli w zależności od horyzontu czasowego, w którym prognozujemy dane

- **Sprawozdanie z wykonania scenariuszy testów** - 
Porównanie właściwości obu modeli, zestawienie statystyk, interpretacja wyników.
  Po przeprowadzeniu testów zamieścimy raport z ich przebiegu w tym miejscu.  
