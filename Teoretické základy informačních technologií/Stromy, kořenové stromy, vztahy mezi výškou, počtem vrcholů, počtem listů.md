### Stromy - definice a základní vlastnosti
- Grafy připomínající vzhledem stromy / keře
```mermaid
graph BT;
A[ ] --- B[ ];
B --- C[ ];
B --- D[ ];
C --- E[ ];
E --- F[ ];
D --- G[ ];
D --- H[ ];
D --- CH[ ];
CH --- I[ ];
CH --- J[ ];

classDef default fill:green,stroke-width:3px;
```
```mermaid
graph TD;
A[ ] --- B[ ];
A --- C[ ];
B --- D[ ];
B --- E[ ];
D --- F[ ];
D --- G[ ];
E --- H[ ];
E --- CH[ ];
C --- I[ ];
C --- J[ ];
I --- K[ ];
I --- L[ ];
J --- M[ ];
J --- N[ ];

classDef default fill:green,stroke-width:3px;
```

- **Strom** je **neorientovaný graf bez kružnic**
- Vrchol se stupněm $1$ se nazývá **koncový**
- **Koncový** vrchol stromu se nazývá **list**

- Odebereme-li ze stromu list a hranu, která do něj vede, **vznikne opět strom**
- V každém stromu s alespoň dvěma vrcholy existují alespoň dva listy

- Pro graf $G$ a jeho koncový vrchol $v$ jsou následující tvrzení ekvivalentní
	- **G je strom**
	- **G - v je strom**

- Pro neorientovaný graf $G = <V,E>$ jsou následující tvrzení <u>ekvivalentní</u>
	- $G$ je strom
	- Mezi každými dvěma vrcholy grafu $G$ existuje právě jedna cesta
	- $G$ je souvislý, ale vynecháním libovolné hrany vznikne nesouvislý
	- $G$ neobsahuje kružnice, ale přidáním jakékoli hrany vznikne graf s kružnicí
	- $G$ neobsahuje kružnice a $\mid V \mid = \mid E \mid + 1$
	- $G$ je souvislý a $\mid V \mid = \mid E \mid + 1$

### Kořenové stromy
- **Kořenový strom** je dvojice **$<G, r>$**, kde $G = <V,E>$ je strom a $r \in V$ je vrchol, tzv. **kořen**

- Kořenový strom je tedy strom, ve kterém je vybrán jeden kořen. Může to být kterýkoliv vrchol. Bývá to ale vrchol, který je v nějakém smyslu na vrcholu hierarchie objektů, která je stromem reprezentována.

- Nechť $<G, r>$ je kořenový strom
	- Vrchol $v$ se nazývá **potomek** vrcholu **$u$** (**$u$** se nazývá **předek** vrcholu $v$), právě když cesta z kořene $r$ do $v$ má tvar $r, ..., u, ..., v$
	- Vrchol **$v$** se nazývá **následovník** (přímý potomek) vrcholu **$u$** (**$u$** se nazývá **předchůdce** (rodič) vrcholu **$v$**), právě když cesta z kořene $r$ do $v$ má tvar $r, ..., u, e, v$
	- Vrchol $v$ se nazývá **list** kořenového stromu, právě když nemá žádného následovníka (jinak se nazývá **vnitřní vrchol**)
	- **Hloubka** (úroveň) **vrcholu $v$** je délka cesty od kořene $r$ do $v$
	- **Výška vrcholu $v$** je délka nejdelší cesty od $v$ do některého z listů
	- **Výška** (hloubka) **stromu** je výška jeho kořene
	- Kořenový strom $<G, r>$ s hloubkou $h$ se nazývá **vyvážený**, pokud má každý jeho list úroveň *h* nebo *h-1*

- Kořenový strom se nazývá **$m$-ární**, právě když každý jeho vrchol má **nejvýše $m$ potomků** 
- $m$-ární kořenový strom $<G, r>$ výšky $h$ se nazývá **zaplněný**, pokud splňuje následující podmínky:
	- **každý vrchol** s výjimkou vrcholů s hloubkou $h-1$ má **0 nebo $m$ následovníků**
	- **každý list má hloubku $h$ nebo $h-1$**

- Kořenový strom se nazývá **uspořádaný**, je-li ke každému vrcholu, který není listem, zadáno **lineární uspořádání jeho potomků**

### Binární vyhledávací stromy
- Binární vyhledávací stromy slouží k ukládání a vyhledávání dat
- Jsou to binární kořenové stromy s dodatečnou informací, která splňuje jistá omezení usnadňující vyhledávání
- **Dodatečná informace:** Vrcholy binárního vyhledávacího stromu jsou ohodnoceny číselnými hodnotami; budeme předpokládat, že ohodnocení je **funkce $w: V \rightarrow \mathbb{Z}$**
- **Omezení:**
	- Je-li $u$ levým následníkem vrcholu $v$ nebo potomkem tohoto následníka, pak $w(u) \leq w(v)$
	- Je-li $u$ pravám následníkem vrcholu $v$ nebo potomkem tohoto následníka, pak $w(u) \geq w(v)$
```mermaid
graph TD
classDef hidden stroke:transparent,fill:transparent,color:transparent;
8 --- 2;
8 --- 15;
2 --- -3;
2 --- 4;
-3 --- -5;
-3 --- 0;
4 --- X;
4 --- 7;
15 --- 14;
15 --- 20;
14 --- 11;
14 --- XX;
20 --- 16;
20 --- 21;

class X,XX hidden;
linkStyle 6 stroke:transparent; linkStyle 11 stroke:transparent;
```

```mermaid
graph TD
classDef hidden stroke:transparent,fill:transparent,color:transparent;
5 --- X;
5 --- 6[4];
6 --- XX;
6 --- 10[2];
10 --- XXX;
10 --- 12[3];

class X,XX,XXX hidden;
linkStyle 0 stroke:transparent; linkStyle 2 stroke:transparent;
linkStyle 4 stroke:transparent;
```
- V **zaplněném** binárního kořenového stromu s $n$ vrcholy a $l$ listy, který má výšku $h$ platí:
	- $2^{h} \leq n \leq 2^{h+1} - 1;$
	- $h = \lfloor \log_{2}n \rfloor ;$
	- $2^{h-1} \leq l \leq 2^{h};$
	- $\lceil log_{2}l \rceil \leq h \leq \lfloor log_{2}l \rfloor + 1.$

- V **libovolném** binárním kořenovém stromu s $n$ vrcholy a $l$ listy, který má výšku $h$, platí:
	- $h+1 \leq n \leq 2^{h+1}-1;$
	- $\lfloor \log_{2}n \rfloor \leq h \leq n-1;$
	- $1 \leq l \leq 2^{h};$
	- $\lceil \log_{2}l \rceil \leq h.$

##### Navigace
Předchozí:  [[Minimální kostra grafu, Kruskalův algoritmus]]
Následující: [[Matice, operace s maticemi, hodnost, determinant]]
Celý okruh: [[1. Teoretické základy informačních technologií]]