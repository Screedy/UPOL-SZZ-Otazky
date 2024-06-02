>[!info] Definice problém
>- Problém **je určen trojicí $(IN, OUT, p)$**, kde $IN$ je množina (přípustných) vstupů, $OUT$ je množina výstupů a $p : IN \rightarrow OUT$ je funkce přiřazující každému vstupu odpovídající výstup
>- Algoritmus $A$ řeší problém $P$ zadaný trojicí $(IN, OUT, p)$ spolu s dohodnutým kódováním vstupů a výstupů (tj. prvků množin $IN$ a $OUT$), jestliže **je schopen přijmout** (přečíst) kód jakéhokoli vstupu $x$ z množiny $IN$ a **vydat k němu po konečném počtu kroků kód výstupu $y$** z množiny $OUT$, pro nějž $y = p(x)$.

## ANO/NE problém, neboli rozhodovací problém
- U rozhodovacího problému, neboli ANO/NE problému **je množina $OUT$ dvouprvková**, standardně chápána jako $OUT=\set{ANO, NE}$ (či $OUT=\set{1,0}$).
- U takových problémů je přirozenější a kratší definovat žádaný výstup pomocí otázky (týkající se vstupu), na kterou je odpověď buď $ANO$ nebo $NE$.

- Turingův stroj $M$ řeší problém $P$ právě tehdy, když **ke každému vstupu problému $P$ stroj $M$ vydá problémem předepsaný výstup**.

- Turingův strom $M$ řeší problém $ANO/NE$ problém $P$ právě tehdy, když ke **každému vstupu problému $P$ stroj $M$ skončí ve stavu $q_{ANO}$, je-li odpověď na otázku problém $P$ ano,** či ve stavu $q_{NE}$, je-li odpověď na otázku problému $P$ ne.

>[!example] Příklad rozhodovacího problému
>- Problém prvočíselnosti
>	- Název: Prvočíselnost
>	- Vstup: Přirozené číslo $x$ (zadané např. dekadickým zápisem).
>	- Otázka: Je $x$ prvočíslo?

- Množinu všech slov $w \in \Sigma^{*}$, které TS $T$ **přijímá**, značíme $L(T)$. Jazyk $L(T)$ nazýváme **jazyk částečně rekurzivní** TS $T$ a říkáme, že TS $T$ částečně rozhoduje jazyk $L(T)$.
- Pokud navíc platí, že TS $T$ **zamítá** každé slovo, které **nepatří** do $L(T)$, nazýváme jazyk $L(T)$ **jazyk rekurzivní** TS $T$ a říkáme, že TS $T$ rozhoduje jazyk $L(T)$.

- Jazyk $L \subseteq \Sigma^{*}$ nazveme jazyk rekurzivní TS, pokud existuje TS $T$, který jej rozhoduje.
- Jazyk $L \subseteq \Sigma^{*}$ nazveme jazyk částečně rekurzivní TS, pokud existuje TS $T$, který jej částečně rozhoduje.

##### Navigace
Předchozí:  [[Church-Turingova teze, varianty TS]]
Následující: [[Vztah rekurzivních a částečně rekurzivních jazyků]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]