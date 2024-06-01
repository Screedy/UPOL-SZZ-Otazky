>[!tip] Pojem algoritmus
>- Návod, postup, či posloupnost elementárních kroků, které je možné provédět mechanicky a jednotlivé kroky jsou konečné

>[!info] Definice problém
>- Problém **je určen trojicí $(IN, OUT, p)$**, kde $IN$ je množina (přípustných) vstupů, $OUT$ je množina výstupů a $p : IN \rightarrow OUT$ je funkce přiřazující každému vstupu odpovídající výstup
>- Algoritmus $A$ řeší problém $P$ zadaný trojicí $(IN, OUT, p)$ spolu s dohodnutým kódováním vstupů a výstupů (tj. prvků množin $IN$ a $OUT$), jestliže **je schopen přijmout** (přečíst) kód jakéhokoli vstupu $x$ z množiny $IN$ a **vydat k němu po konečném počtu kroků kód výstupu $y$** z množiny $OUT$, pro nějž $y = p(x)$.

## Church-Turingova teze
>[!info] Teze
>- Ke každému algoritmu je možné zkonstruovat s ním ekvivalentní Turingův stroj (s rozumným kódováním vstupů a výstupů řetězci v určité abecedě), ekvivalencí zde rozumíme podmínku, že algoritmus i Turingův stroj vydají pro tytéž vstupy tytéž výstupy

## Varianty Turingových strojů
- Oboustranně nekonečná páska
- Jednostranně nekonečná páska
- Více páskový turingův stroj

>[!info] Jednostranně nekonečná páska
>![[MacBook-2024-05-29-001402.png]]
>- Je třeba definovat, co se má stát, když se hlava nachází na nejlevějším poláčku pásky a má se posunout doleva
>- Dvě nejběžnější možnosti:
>	- **Nastane "chybový" stav** - výpočet se neúspěšně ukončí
>	- **Na levém konci je "zarážka"**
>		- reprezentována speciálním symbolem
>		- tuto zarážku není možné přepsat a nneí na ní možný pohyb směrem doleva

- Simulace oboustranně nekonečnou páskou simulovat jednostranně nekonečnou pásku:
	- Nepouije se levá strana pásky

- Simulace jednostranně nekonečnou páskou simulovat oboustranně nekonečnou:
	- Oboustranně nekonečná páska ![[MacBook-2024-05-29-001403.png| 500]]
	- Jednostranně nekonečná páska![[MacBook-2024-05-29-001404.png| 450]]

>[!info] Vícepáskové Turingovy stroje
>![[MacBook-2024-05-29-001405.png]]
>- Vícepáskovým TS míníme model, který je definován odborně jako TS, ale **má $k$ pásek $(k>1)$ se samostatně řízenými hlavami.**
>	- Přechodová funkce bere ohled na symboly čtené hlavami ze všech pásek a určuje pohyb každé hlavy (na její pásce) zvlášť.
>- Každý z $k$ pásek má svou vlastní páskovou abecedu, máme páskové abecedy $\Gamma_{1}, \Gamma_{2}, ..., \Gamma_{k}$
>- **Přechodová funkce $\delta$ je typu** $$(Q-F) \times \Gamma_{1} \times ... \times \Gamma_{k} \rightarrow Q \times \Gamma_{1} \times \set{-1, 0, 1} \times ... \times \Gamma_{k} \times \set{-1,0,1}$$
>
>>[!example] Příklad
>>$$\delta (q_{5}, a, 1, \square)=(q1_{2}, a, -1, x, 0, 1, +1)$$

- **Simulace více páskového TS pomocí jedno páskového TS**
- Více pásek![[MacBook-2024-05-29-001406.png]]
- Jedna páska s jednou hlavou (varianta, kde se posunují značky hlav)![[MacBook-2024-05-29-001407.png]]
- Jedna páska s jednou hlavou (varianta, kde se posunují obsahy pásek)![[MacBook-2024-05-29-001408.png]]

##### Navigace
Předchozí:  [[Jazyk přijímaný TS, jazyk rozhodovaný TS]]
Následující: [[Částečně rekurzivní a a rekurzivní jazyky, jazyky a rozhodovací problémy]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]