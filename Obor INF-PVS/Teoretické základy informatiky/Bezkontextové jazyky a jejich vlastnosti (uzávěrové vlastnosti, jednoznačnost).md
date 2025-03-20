- Podobně jako regulární jazyky mají též CFG i značný praktický význam, například při definici syntaxe programovacích jazyků, formalizaci pojmu syntaktická analýza a návrhu překladu programovacích jazyků a dalších.

## Bezkontextová gramatika
>[!info] Definice bezkontextové gramatiky
>- Gramatika $G = (N, \Sigma, P, S)$ je **bezkontextová** (zkratka CFG z context-free grammar), pokud jsou všechna pravidla ve tvaru $A \rightarrow \alpha$, kde $\alpha \in (\Sigma \cup N)^{*}$, tedy neterminál generuje libovolný řetězec terminálů a neterminálů

## Derivační stromy
- Derivační strom je grafická reprezentace derivace nějakého řetězce v CFG

>[!info] Definice derivačního stromu
>- Nechť $G = (N, \Sigma, P, S)$ je CFG. Strom $T$ nazveme derivačním stromem v $G$, právě když platí tyto podmínky:
>	1. Každý uzel má návěští, které je symbolem z $N \cup \Sigma \cup \set{\epsilon}$
>	2. Kořen má návětší $S$
>	3. Má-li vnitřní uzel návěští $A$, pak $A \in N$
>	4. Má-li uzel $n$ návěští $A$ a jeho všichni synové $n_{1},...,n_{k}$ mají v uspořádání zleva doprava návěští $X_{1}, ..., X_{k}$, pak $A \rightarrow X_{1}, ..., X_{k} \in P$
>	5. Má-li uzel $n$ návěští $\epsilon$, pak $n$ je list a je jediným synem svého otce.

- Výsledkem derivačního stromu $T$ nazveme slovo vzniklé zřetězením návěští listů v uspořádání zleva doprava.

>[!Example] Příklad
>- Nechť $G_{0}$ je gramatika s pravidly 
>  $$
>  \begin{align}
>  E \rightarrow E+T |\ T\\
>  T \rightarrow T*F\ |\ F\\
>  F \rightarrow (E)\ \ \ \ \ |\ i\ \ 
>  \end{align}
> $$ 
>  pak derivační strom 
>  ![[MacBook-2024-05-29-001394.png| 300]] 
>  reprezentuje deset vzájemně ekvivalentních derivací, např.
>  1. $E \Rightarrow E+T \Rightarrow T+T \Rightarrow F+T \Rightarrow i+T \Rightarrow i+F \Rightarrow i+i$ nebo
>  2. $E \Rightarrow E+T \Rightarrow E+F \Rightarrow E+i \Rightarrow T+i \Rightarrow F+i \Rightarrow i+i$ a též
>  3. $E \Rightarrow E+T \Rightarrow T+T \Rightarrow T+F \Rightarrow F+F \Rightarrow F+i \Rightarrow i+i$ a další
>- Všimněme si, že $1$ je levá, kdežto $2$ je pravá derivace.


- CFG $G$ je **víceznačná/nejednoznačná**, pokud existuje řetězec $S \Rightarrow ^{*}\alpha$, který je derivací alespoň **dvou různých** derivačních stromů (v opačném případě je $G$ jednoznačná)
- **Bezkontextový jazyk** je **jednoznačný**, pokud *existuje jednoznačná gramatika*, která jej generuje (víceznačnost je vlastnost gramatiky, nikoliv jazyka který generuje)
- Pro některé bezkontextové jazyky neexistuje jednoznačná gramatika, takový **jazyk** je **dědičně víceznačný**

>[!Example] Příklad
>- Gramatika $G_{1}$ s pravidly $E \rightarrow E+E |\ E*E |\ (E) |\ i$, která je ekvivalentní s gramatikou $G_{0}$ z příkladu výše. Je víceznačná, např. protože věta $i+i+i$ má dvě různé levé derivace a jim odpovídající dva různé derivační stromy:![[MacBook-2024-05-29-001395.png]]

- **Chromského normální forma**
	- Řekneme, že CFG $G = (N, \Sigma, P, S)$ je v **Chromského normální formě**, právě když je $G$ bez $\epsilon$-pravidel a každé pravidlo z $P$ má jeden z těchto tvarů:
		- $A \rightarrow BC, B,C \in N$
		- $A \rightarrow a, a \in \Sigma$

- **Greibachová normální forma**
	- Řekneme, že CFG $G = (N, \Sigma, P, S)$ je v **Greibachové normální formě**, právě když je $G$ **bez $\epsilon$-pravidel** a každé pravidlo z $P$ je tvaru $A \rightarrow a \alpha (a \in \Sigma, \alpha \in N^{*})$

## Bezkontextové jazyky
- Jazyk, který je definovaný nějakou bezkontextovou gramatikou

>[!info] Vyjádření bezkontextových jazyků
>- Nechť máme bezkontextový jazyk $L$
>	1. $L = L(G)$ pro nějakou CFG $G$
>		- (Lze vyjádřit pomocí bezkontextové gramatiky)
>	2. $L = L(M)$ pro nějaký PDA $M$
>		- (Lze vyjádřit pomocí zásobníkového automatu akceptující pomocí koncového stavu)
>	3. $L = L_{e}(N)$ pro nějaký PDA $N$
>		- (Lze vyjádřit pomocí zásobníkového automatu akceptující pomocí prázdného zásobníku)

### Přehled rozhodnutelných vlastností CFL
- Řetězec $w$ patří do bezkontextového jazyka $L$.
	- Algoritmus CYK
- Bezkontextový jazyk $L$ je prázdný.
	- Umíme odstranit neterminály, které negenerují žádný terminální řetězec, jestliže je počáteční symbol jeden z nich, pak je bezkontextový jazyk prázdný; jinak ne
- Bezkontextový jazyk $L$ je nekonečný.
	- Použij konstantu $n$ z pumping lemmatu.
	- Jestliže existuje řetězec v jazyku délky mezi $n$ a $2n-1$, pak je jazyk nekončený; jinak je konečný.

### Uzávěrové vlastnosti bezkontextových jazyků
- V níže uvedených důkazech lze použít jak bezkontextových gramatik, tak i zásobníkových automatů.

>[!Example] Uzavřenost na sjednocení, konkatenaci a Kleeneho uzávěr
>- Třída všech bezkontextových jazyků je uzavřena vzhledem k operaci sjednocení, zřetězení (konkatenace), iteraci (Kleeneho uzávěr) a pozitivní iteraci
>
>>[!tip]- Důkaz
>>![[MacBook-2024-05-29-001396.png]]

>[!Example] Neuzavřenost na průnik a doplněk
>- Třída všech bezkontextových jazyků **není** uzavřena vzhledem k operaci průnik a doplněk.
>
>>[!tip]- Důkaz
>>![[MacBook-2024-05-29-001397.png]]

>[!Example] Uzavřenost na homomorfismu a inverzní homomorfismus
>- Třída všech bezkontextových jazyků je uzavřena vzhledem k substituci
>
>>[!tip]- Důkaz
>>![[MacBook-2024-05-29-001398.png]]
>
>- Třída všech bezkontextových jazyků je uzavřena vůči homomorfismu a izomorfismu
>
>>[!tip]- Důkaz
>>![[MacBook-2024-05-29-001399.png]]

>[!Example] Uzavřenost na reverz
>- Třída všech bezkontextových jazyků je uzavřena na reverz
>
>>[!tip]- Důkaz
>>- Nechť $L$ CFL generovaný gramatikou $G$
>>- Sestrojíme gramatiku pro $L^{R}$ tak, že otočíme pravou stranu každého pravidla
>>- Např. Nechť $G$ má pravidla $S \rightarrow 0S1 |\ 01$. Pak reverz jazyka $L(G)$ má gramatiku $S \rightarrow 1S0 |\ 10$

---
**! Navíc**
#### Deterministické ezlkontextové jazyky
- V řadě (i praktických) aplikací je třeba zjistit, zda daný jazyk $L$ je (a nebo není) DCFL.
- K důkazu, že je **DCFL stačí nalézt odpovídající DPDA**. Obrácená situace, kdy chceme ukázat, že $L$ není DCFL, může být složitější. Pokud by $L$ nebyl ani CFL, můžeme použít pumping lemma, ale často $L$ může být CFL, ale ne DCFL. Jelikož není známo žádné pumping lemma, které by platilo specialně do DCFL, **musíme se spolehnout jen na uzávěrové vlastnosti**. Naštěstí DCFL jsou uzavřeny na některé operace, například vůči doplňku, na něž CFL obecně uzavřeny nejsou.

- Třída DCFL **není** uzavřena vzhledem k operaci **průniku**.
- Třída deterministických bezkontextových jazyků je uzavřena vůči doplňku.
- Třída DCFL **není** uzavřena vzhledem ke **sjednocení**.

>[!Example] Příklad
>![[MacBook-2024-05-29-001400.png]]

---
##### Navigace
Předchozí:  [[Pumping lemma]]
Následující: [[Zásobníkové automaty]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]