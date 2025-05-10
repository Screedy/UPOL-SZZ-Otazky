>[!tip] Pojem algoritmus
>- Návod, postup, či posloupnost elementárních kroků, které je možné provádět mechanicky a jednotlivé kroky jsou konečné. Nemá přesnou matematickou definici.
>- Algoritmus můžeme formalizovat pomocí TS.

>[!info] Definice problém
>- Problém **je určen trojicí $(IN, OUT, p)$**, kde $IN$ je množina (přípustných) vstupů, $OUT$ je množina výstupů a $p : IN \rightarrow OUT$ je funkce přiřazující každému vstupu odpovídající výstup
>- Algoritmus $A$ řeší problém $P$ zadaný trojicí $(IN, OUT, p)$ spolu s dohodnutým kódováním vstupů a výstupů (tj. prvků množin $IN$ a $OUT$), jestliže **je schopen přijmout** (přečíst) kód jakéhokoli vstupu $x$ z množiny $IN$ a **vydat k němu po konečném počtu kroků kód výstupu $y$** z množiny $OUT$, pro nějž $y = p(x)$.

## Church-Turingova teze
>[!info] Church-Turingova teze
>- **Algoritmus = Turingův stroj**
>- Ke každému algoritmu je možné zkonstruovat s ním ekvivalentní Turingův stroj (s rozumným kódováním vstupů a výstupů řetězce v určité abecedě). Ekvivalencí zde rozumíme podmínku, že algoritmus i Turingův stroj vydají pro tytéž vstupy tytéž výstupy.

## Varianty Turingových strojů
1) Oboustranně nekonečná páska
2) Jednostranně nekonečná páska
3) Vícepáskový turingův stroj

>[!info] Jednostranně nekonečná páska
>![[MacBook-2024-05-29-001402.png]]
>- Je třeba definovat, co se má stát, když se hlava nachází na nejlevějším políčku pásky a má se posunout doleva
>- Dvě nejběžnější možnosti:
>	1) **Nastane "chybový" stav** - výpočet se neúspěšně ukončí
>	2) **Na levém konci je "zarážka"**
>		- reprezentována speciálním symbolem
>		- tuto zarážku není možné přepsat a není na ni možný pohyb směrem doleva

- Simulace TS s oboustranně nekonečnou páskou pomocí TS s jednostranně nekonečnou pásku
	- Nepoužije se "levá" strana pásky
- Simulace TS s jednostranně nekonečnou páskou pomocí TS s oboustranně nekonečnou páskou:
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
## Univerzální TS
- Stroj, který **provádí univerzální algoritmus**
- Na vstup dostane TS (zakódovaný do $0$ a $1$) a slovo, na které má daný stroj aplikovat
- Dělá to, že simuluje chod libovolného TS na zadané vstupní slovo (provádí jeho výpočet)
- **Jak se to provádí?**
	- Pomocí 3-páskového TS. Na první pásce je slovo a na druhé instrukce zadaného TS (obojí v 0 a 1). Třetí páska slouží k zapamatování aktuálního stavu. Simulace začíná hledáním instrukce na druhé pásce, která se má vykonat v počátečním stavu. Takto pokračujeme dále. Po každé iteraci je nutné se na druhé pásce vrátit na začátek. V první pásce se zase posouváme o symbol dopředu.
- Sám o sobě nemá roli, slouží jen k simulaci dalších TS.

##### Navigace
Předchozí:  [[Jazyk přijímaný TS, jazyk rozhodovaný TS]]
Následující: [[Částečně rekurzivní a rekurzivní jazyky, jazyky a rozhodovací problémy]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]