>[!info] Cookova (Cookova-Levivona) věta
>- Problém SAT je NP-úplný.
>  
>  **Název:** SAT (problém splnitelnosti booleovských formulí)
>  **Vstup:** Booleovská formule v konjunktivní normální formě.
>  **Otázka:** Je daná formule splnitelná?


- Víme že SAT patří do $NPTIME$, protože **existuje nedeterministický polynomiální algoritmus**, který jej řeší
- Musíme dokázat, že je také NP-těžký

- **Myšlenka důkazu:**
	- Základní myšlenkou důkazu je ukázat, že existuje polynomiální, univerzální TS, který může simulovat libovolný nedeterministický algoritmus v polynomiálním čase.
	- Tento stroj pak může být použit k převedení libovolného problému v NP na SAT

>[!Example] Důkaz
>- Musíme dokázat $\forall P \in NPTIME: P \leq_{p} SAT$, o každém problému $P$ víme, že je reprezentován nedeterministickým TS.
>- Ukážeme konstrukci, která **pro TS $M$ a vstupní slovo $w$ sestrojí formuli $\psi_{M,w}$**, tak že formule $\psi_{M,w}$ bude splnitelná právě tehdy, když TS přijme slovo $w$
>- **Výpočet** TS $M$ na vstupním slově $w\ (|w|=n)$ můžeme **reprezentovat tabulkou**![[MacBook-2024-05-31-001423.png| 400]]
>	- Zavedeme proměnné 
>		- $x_{i,j,(q,s)}$ pro každé $0 \leq i \leq n^{k}$ (konfigurace = řádek), 
>		- $0 \leq j \leq n^{k}$ (pozice symbolu = sloupec), 
>		- $s \in \Gamma$ (páskový symbol).
>	- Zavedeme proměnné 
>		- $x_{i,j,(q,s)}$ pro každé $0 \leq j \leq n^{k}$, 
>		- $0 \leq j \leq n^{k}$, 
>		- $s \in \Gamma$, 
>		- $q \in Q$ (stav).
>- Formuli $\psi_{M,w}$ vytvoříme jako (musí splňovat podmínky) $$\psi_{M,w} = \psi_{cell} \land \psi_{start} \land \psi_{move} \land \psi_{accept}$$
>	- $\psi_{cell}$ musí zajistit, že v každé buňce tabulky je právě jeden symbol
>	- $\psi_{start}$ musí zajistit, že první řádek odpovídá počáteční konfiguraci
>	- $\psi_{accept}$ musí zajistit, že na posledním řádku tabulky se vyskytuje stav $q_{ANO}$. (Předpokládáme, že pokud TS skončí výpočet dřív než po $n^{k}$ krocích, všechny následující konfigurace (řádky tabulky) jsou stejné)
>	- $\psi_{move}$ musí zajistit, že každé následující konfigurace vznikne z předchozí správným způsobem.
>- Formule $\psi_{M,w} = \psi_{cell} \land \psi_{start} \land \psi_{move} \land \psi_{accept}$ je polynomiální vzhledem k $n$.
>- **Jestliže je splnitelná tato formule,** dokážeme vyplnit tabulku tak, že reprezentuje **přijímající výpočet TS $M$ na slově $w$.** (Jestliže je formule nesplnitelná, tak neexistuje přijímající výpočet TS $M$ na slově $w$, protože se nám nepodaří vyplnit tabulku reprezentující takový výpočet.)
>- Ukázali jsme tedy **polynomiální převod libovolného problému** z NP na problém SAT

##### Navigace
Předchozí:  [[NP-úplné problémy]]
Následující: [[Příklady NP-úplných problémů, dokazování NP-úplnosti]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]