>[!tip] Konkrétní polynomiální redukce
>$$SAT \leq_{p} 3-SAT \leq_{p} IS_{DEC} \leq_{p} VC_{DEC} \leq_{p} HC \leq_{p} HK \leq_{p} \triangle - TSP_{DEC} \leq_{p} TSP_{DEC}$$

>[!info] $SAT$ (problém splnitelnosti booleovských formulí)
>**Název**: SAT
>**Vstup**: Booleovská formule v konjuktivní normální formě.
>**Otázka**: Je daná formule splnitelná?

>[!info] $3-SAT$ (problém SAT s omezením na 3 literály)
>**Název**: 3-SAT
>**Vstup**: Booleovská formule v konjunktivní normální formě, kde v každé klauzuli jsou právě 3 literály.
>**Otázka**: Je daná formule splnitelná?

>[!info] $IS_{DEC}$ (problém nezávislé množiny \[Independent Set\])
>**Název**: IS$_{DEC}$
>**Vstup**: Neorientovaný graf $G$ (o $n$ vrcholech); číslo $k$ ($k \leq n$).
>**Otázka**: Existuje v $G$ nezávislá množina velikosti $k$? (tj. množina $k$ vrcholů, z nichž žádné dva nejsou spojeny hranou)

>[!info] $VC_{DEC}$ (vrcholové pokrytí \[Vertex Cover\])
>**Název**: VC$_{DEC}$
>**Vstup**: Neorientovaný graf $G$ (o $n$ vrcholech); číslo $k (k \leq n)$.
>**Otázka**: Existuje v $G$ vrcholové pokrytí velikosti $k$? (tj. množina vrcholů, v níž má každá hrana aspoň jeden konec)

>[!info] $HC$ (problém hamiltonovského cyklu)
>**Název**: HC
>**Vstup**: Orientovaný graf $G$.
>**Otázka**: Existuje v $G$ hamiltonovský cyklus? (tj. uzavřená cesta, procházející každým vrcholem právě jednou)

>[!info] $HK$ (problém hamiltonovské kružnice)
>**Název**: HK
>**Vstup**: Neorientovaný graf $G$.
>**Otázka**: Existuje v $G$ hamiltonovská kružnice? (tj. uzavřená cesta, procházející každým vrcholem právě jednou)

>[!info] $TSP_{DEC}$ (problém obchodního cestujícího)
>**Název**: TSP$_{DEC}$
>**Vstup**: Množina "měst" $\set{1,2,...,n}$, přirozená čísla ("vzdálenosti") $d_{ij}(i=1,2,...,n, j= 1,2,...,n)$, kde $d_{ii} = 0$ a $d_{ij} = d_{ji}$; dále číslo $l$ ("limit").
>**Otázka**: Existuje "okružní jízda" dlouhá nejvýše $l$, tj. existuje permutace $(i_{1}, i_{2}, ..., i_{n})$ množiny $\set{1,2,...,n}$ tak, že $d(i_{1}, i_{2}) + d(i_{2}, i_{3}) + ... + d(i_{n-1}, i_{n}) + d(i_{n}, i_{1}) \leq l$?
>
>- $\triangle - TSP$ je podproblém problému TSP, v němž každá instance splňuje trojúhelníkovou nerosnost (tedy $d(i,j) \leq d(i,k) + d(k,j))$

---
>[!Example] $SAT \leq_{p} 3-SAT$
>1. Sestavím booleovský obvod
>2. Vypíšu pravidla, jaká musí booleovský obvod splňovat
>3. Uplatním na ně De Morganovy zákony

>[!Example] $3-SAT \leq_{p} IS_{DEC}$
>1. Udělám $3$ vrcholy pro každou klauzuli ve formuli a spojím je. (Udělám trojúhelníky)
>2. Vrchol s proměnnou $x$ propojím s vrcholem negací proměnné $x$
>3. Číslo $k$ je počet klauzulí ve formuli

>[!Example] $IS_{DEC} \leq_{p} VC_{DEC}$
>- V grafu $G = (V, E)$ je $V'$ nezávislá množina právě tehdy, když $V$ \\ $V'$ je vrcholové pokrytí.

>[!Example] $VC_{DEC} \leq_{p} HC
>- Pro (neorientovaný) graf $G = (V, E)$ a číslo $k$ jsme sestrojili graf $G' = (V', E')$ postupně takto:
>	- Pro každý vrchol $v \in V$ grafu $G$, se stupněm $deg(v)$, zařadíme do $G'$ "řetízek" vrcholů $v_{1} \rightarrow v_{2} \rightarrow ... \rightarrow v_{2 \cdot deg(v)}$ (šipky označují příslušné hrany v $G'$)
>	- Pro dané číslo $k$ zařadíme do $G'$ navíc vrcholy $u_{1}, u_{2}, ..., u_{k}$ a pro každé $i \in [1,k]$ a každý vrchol $v \in V$ s nenulovým stupněm přidáme do $G'$ hrany $u_{i} \rightarrow v_{1}$ a $v_{2 \cdot deg(v)} \rightarrow u_{i}$ (z $u_{i}$ lze tedy "skočit" na začátek libovolného "řetízku" a z konce libovolného "řetízku" lze zase skočit na $u_{i}$, pro každé $u_{i} \in \set{u_{1}, u_{2}, ..., u_{k}}$);
>	- Pro každý vrchol $v \in V$ grafu $G$ očíslujeme jeho incidentní hrany čísly $1, 2, ..., deg(v)$ a pro každou hranu $e = \set{v, v'} \in E$ grafu $G$ přidáme do $G'$ čtyři hrany $e$ vzhledem k $v'$; pak přidáme hrany $v_{2l-1} \leftrightarrow v_{'2l'-1}$ a $v_{2l} \leftrightarrow v_{'2l'}$ (kde $x \leftrightarrow y$ reprezentuje dvojici hran $x \rightarrow y$ a $y \rightarrow x$).

>[!Example] $HC \leq_{p} HK$
>- Místo každého vrcholu přidám $3$ vrcholy (začátek, střed, konec), které propojím podle orientace hran v grafu HC

>[!Example] $HK \leq_{p} \triangle - TSP_{DEC}$
>- V grafu $G = (V, E)$ jsme každé hraně přiřadili hodnotu (délku) $1$ a pak jsme doplnili hrany tak, aby vznikl úplný graf, každé doplněné hraně jsme přiřadili hodnotu $2$.


##### Navigace
Předchozí:  [[Cook-Levinova věta]]
Následující: [[Třída PSPACE, její vztah k třídám P a NP, PSPACE-úplné problémy]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]