# Raport privind cercetarea și analiza unui set de date despre filme

Sunt student in al treilea si ultimul an de facultate si elaborez o lucrare
pentru cursul "Fundamente de Big Data". Lucrarea reprezinta un raport scris in
urma cercetarii si analizei unui set de date despre filme. Ma vei ajuta sa
scriu acest raport in functie de uneltele pe care le folosesc, setul de date pe
care l-am ales, cerintele lucrarii si cercetarea pe care am facut-o.

## Unelte

Pentru cercetare folosesc Python (librarii: numpy, pandas, scikit-learn,
matplotlib, seaborn, xgboost) si mediile interactive Jupyter Notebooks.

## Setul de date

- nume: TMDB 15000 Movies Dataset
- url: https://www.kaggle.com/code/pratul007/revamped-recommendation-engine"
- incarcat de: Prabhakar Pal (Student at Thakur Instute of Management Studies
  Carrier Development and Research. Mumbai, Maharashtra, India)
- descrierea de pe Kaggle: This dataset contains data about the top rated movies
  of all time. Data was sourced from TMDB APIs.

Acest set de date contine urmatoarele coloane:

- original_language: Limba originala a filmului - engleza, hindu si cateva alte
  variante.
- popularity: Popularitatea filmului, intre 0 si 100.
- release_date: Data in care s-a lansat filmul.
- vote_average: Votul mediu a filmului, intre 0 si 10.
- vote_count: Numarul de voturi al filmului.
- genres: Genul filmului - o lista de obiecte, continand si numele genului.
- keywords: Cuvinte cheie reprezentative pentru film - o lista de strings.
- cast: O lista cu obiecte ce reprezinta persoanele care au jucat in film.
- crew: O lista cu obiecte ce reprezinta persoanele care au participat la
  executia filmului.

## Cerinte

- Rezultate si discutii: 30 puncte, aproximativ 10 pagini
  - Analiza realizata este potrivita pentru a raspunde intrebarilor de
    cercetare.
  - Metodele de analize sunt potrivite pentru setul de date.
  - Sarcinile de analizata au fost rulate corespunzator.
  - Rezultatele obtinute sunt interpretate corespunzator.
  - Rezultatele prezentate sunt clare.
  - Prezentarea rezultatelor are o ordine logica.
  - Tabelele si graficele realizate conving cititorul despre interpretarile
    textuale si, la final, despre concluzii.
  - Prezentarea limitarilor ale studiului si a muncii aditionale care se poate
    face pentru a obtine rezultate mai bune.

## Detalii despre lucrare si cercetare

Intrebarile de cercetare sunt:

- In ce masura putem prezice popularitatea unui film pe baza altor
  caracteristici?
- In ce masura putem prezice votul mediu al unui film pe baza altor
  caracteristici?

Relevanta/importanta intrebarilor: filmele populare sau cu voturi medii mari
atrag multe vizionari, ce pot genera venituri mai mari pentru producatorii de
filme.

Contributia lucrarii: incercarea de a determina relatii intre caracteristici de
baza a unui film si masuratorile acestuia (vot mediu, popularitate) pentru a
directiona investiile in domeniu spre proiectele care ar putea avea un succes
mai mare.

Pentru inceput am examniat coloanele numerice: vote_count, popularity,
vote_average.

- vote_average:
  - medie: 5.6
  - deviere standard: 2.55
  - valoare minima: 0
  - 25%: 5.7
  - 50%: 6.4
  - 75%: 7.1
  - valoare maxima: 10

- vote_count:
  - medie: 1035.29
  - deviere standard: 2366.74
  - valoare minima: 0
  - 25%: 3
  - 50%: 292
  - 75%: 864
  - valoare maxima: 33495

- popularity:
  - medie: 18
  - deviere standard: 114
  - minim: 0.6
  - 25%: 1.73
  - 50%: 10
  - 75%: 17
  - maxim: 9065

Am examinat si data de lansare, dupa ce am convertit-o la un format ce poate fi
examinat:
  - media: 2001-04-18
  - minim: 1895-06-10
  - 25%: 1991-01-01
  - 50%: 2007-07-04
  - 75%: 2016-06-24
  - maxim: 2026-12-08

De asemenea, am convertit coloanele genres, keywords si original_language in
formate ce se preteaza la analiza, prin one hot encoding.
  - Coloana genres este o lista cu obiecte ce contin, printre altele, si
    numele fiecarui gen. Transformarea a dus la coloane de tipul genre_action,
    genre_comedy, etc.
  - Coloana keywords este o lista cu strings. Transformarea a dus la coloane de
    tipul keywor_new_york_city, keyword_based_on_true_story, etc.
  - Coloana original_language este un string de 2 caractere. Transormarea a dus
    coloane de tipul original_language_hi, original_language_en, etc.

Pentru a analiza vizual datele am creat scatterplots pentru vote_average,
vote_count, popularity si release_year, fiecare in relatia cu cealalta,
obtinand o matrita 4x4 de grafice.

Pentru a analiza vizual datele de tip categorie am creat box plots pentru
fiecare (genres, keywords, original_language).

Observatii:
- vote_average: majoritatea sunt cuprinse intre 5.7 si 7.1. am standardizat
  coloana cu z score deoarece devierea standard e mare pentru minim si maxim.
- vote_count: majoritatea intre 3 si 864. am logaritmat in prima faza in baza
  10 si am standardizat cu z score deoarede devierea standard e uriasa.
- popularity: majoritatea sunt intre 1.73 si 17, am standardizat cu z score
  pentru ca devierea standard e foarte mare.
- nu se pot observa relatii liniare concrete intre valorile numerice sau anul
  lansarii
- din box plots pentru genuri si keywords se poate observa o oarecare relatie,
  dar pentru original_language nimic concludent

Modele:
- linear regression
- decision tree regression
- random forest regression
- gradient boost regression
- XGBoost regression

Relatii incercate si rezultate (ordinea modelelor e de la cel mai bun la cel
mai slab, valorile aproape de 0 sunt bune, valorile aproape de 1 sunt slabe):

```
===> Summary | Vote average -> Popularity
                          Model      RMSE
3  Gradient Boosting Regression  1.120490
2      Random Forest Regression  1.120666
4                XGB Regression  1.120714
1      Decision Tree Regression  1.120718
0             Linear Regression  1.120793

===> Summary | Vote count + Vote average -> Popularity
                          Model      RMSE
0             Linear Regression  1.115485
3  Gradient Boosting Regression  1.140315
2      Random Forest Regression  1.151524
4                XGB Regression  1.170730
1      Decision Tree Regression  1.172940

===> Summary | Genres + Keywords + Vote average + Vote count -> Popularity
                          Model      RMSE
0             Linear Regression  1.115250
3  Gradient Boosting Regression  1.158513
1      Decision Tree Regression  1.169271
2      Random Forest Regression  1.171162
4                XGB Regression  1.275667

===> Summary | Genres + Keywords + Popularity + Vote count -> Vote average
                          Model      RMSE
3  Gradient Boosting Regression  0.098926
4                XGB Regression  0.104490
2      Random Forest Regression  0.106875
1      Decision Tree Regression  0.133896
0             Linear Regression  0.177730

===> Summary | Genres + Keywords + Popularity -> Vote average
                          Model      RMSE
3  Gradient Boosting Regression  0.173075
4                XGB Regression  0.173878
2      Random Forest Regression  0.178651
1      Decision Tree Regression  0.216257
0             Linear Regression  0.223277

===> Summary | Genres + Keywords + Vote count -> Vote average
                          Model      RMSE
3  Gradient Boosting Regression  0.098853
4                XGB Regression  0.100275
2      Random Forest Regression  0.106891
1      Decision Tree Regression  0.120213
0             Linear Regression  0.177729

===> Summary | Genres + Keywords -> Vote average
                          Model      RMSE
4                XGB Regression  0.212372
2      Random Forest Regression  0.213308
1      Decision Tree Regression  0.216658
3  Gradient Boosting Regression  0.220337
0             Linear Regression  0.223633

===> Summary | Genres + Keywords -> Popularity
                          Model      RMSE
0             Linear Regression  1.119357
2      Random Forest Regression  1.123059
3  Gradient Boosting Regression  1.143800
4                XGB Regression  1.155326
1      Decision Tree Regression  1.444930
```
