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
| WF2           | Interfejs użytkownika        | System powinien dostarczać intuicyjny interfejs użytkownika umożliwiający łatwe korzystanie z funkcji prognozowania cen. | 1         | Funkcjonalne    |
| WF3           | Baza danych cen paliw        | System powinien zarządzać bazą danych zawierającą historyczne ceny benzyny PB95 do celów trenowania modeli prognozowania. | 1         | Funkcjonalne    |
| WF4           | Powiadomienia                | System powiadomień o zaktualizowaniu bazy danych o nowe rekordy | 3         | Funkcjonalne    |
| NWF1          | Dokumentacja użytkownika     | Opracować pełną dokumentację użytkownika, zawierającą instrukcje obsługi, opis algorytmów prognozowania oraz dane wejściowe/wyjściowe. | 2         | Niefunkcjonalne    |
| NWF2          | Skalowalność systemu         | System powinien być skalowalny, dostosowuje się do zmieniającej się ilości danych historycznych. | 2         | Niefunkcjonalne |
| NWF3          | Rozszerzalność               | Program powinien być elastyczny ze względu na wprowadzanie nowych wariantów prognozowania (np. rozszerzenie o prognozowanie cen benzyny 98)| 2         | Niefunkcjonalne             |

### 4.Architektura systemu/oprogramowania
- **Architektura rozwoju – stos technologiczny**
- **Język programowania:** Python 
- **Pakiety:** Pandas, Keras 3.0, scikit-learn,  statsmodels, pyramid-arima
- **Baza danych:** System zarządzania bazą danych, MS SQL. 


**Zarządzanie zależnościami i wersjami:**
- **System kontroli wersji** - Github.

**Architektura uruchomieniowa** – stos technologiczny

**Hosting:**
- Chmura obliczeniowa, np. AWS, Azure lub Google Cloud dla skalowalności.


### 5.Testy
- **Scenariusz testów**
Wykonanie testów na wszystkich modelach -  walidacja krzyżowa, wyliczenie statystyk w celu zbadania dobroci modeli, uwzględnienie różnicy w działaniu obu modeli w zależności od horyzontu czasowego, w którym prognozujemy dane.
- **Sprawozdanie z wykonania scenariuszy testów** - 
Porównanie właściwości obu modeli, zestawienie statystyk, dla kolejnych prób w walidacji krzyżowej z uwzględnieniem horyzontu czasowego, w którym prognozujemy dane.
Sprawozdanie zostanie przygotowane w formie raportu w programie Excel. 
