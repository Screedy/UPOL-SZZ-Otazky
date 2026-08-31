- Klasická teorie složitosti měří **sériový čas —** kolik provede instrukcí jeden výpočetní model**.**
- Paralelní model ukazuje, že může být více instrukcí provedeno současně. Díky tomu lze některé problémy řešit výrazně rychleji.
- Nejpoužívanějším teoretickým modelem paralelního výpočtu jsou **Booleovské výpočetní obvody (Boolean circuits)**.

---

# 1. Booleovský obvod

> [!success]
> **Booleovský obvod** je _orientovaný acyklický graf_ $G=(V,E).$ Vrcholům říkáme brány.  
> Každá brána je označena jedním ze symbolů z množiny
>
> $$
> \set{\lor,\land,\neg,0,1} \cup \set{x_1,x_2,x_3,...},
> $$
>
> kde:
>
> - $x_1,...,x_n$ představují **vstupní proměnné** (vstupní brány)
> - 0 a 1 představují **konstantní hodnoty** (konstantní brány)
> - $\lor,\land \text{ a }\neg$ představují l**ogická operace** (výpočetní brány)
>
> Hrany určují _závislosti mezi jednotlivými_ bránami **při vyhodnocování** obvodu.

> [!warning]
> **Booleovský obvod** je základní matematický a hardwarový model _pro výpočet booleovských funkcí_.
>
> $$
> f:\set{0,1}^n→\set{0,1}
> $$

## 1.1 Indegree a outdegree

- Počet hran _vstupujících do brány_ se nazývá **indegree**.
- Platí:
  - _Vstupní a konstantní brány_ mají **indegree 0**,
  - _Brána označená_ $\neg$ má **indegree 1**,
  - _Brány označené_ $\land$ a $\lor$ mají **indegree 2** (v některých modelech neomezený)
- Počet hran _vystupujících z brány_ se nazývá **outdegree**. Ten bývá _obvykle neomezený_, takže výstup jedné brány může sloužit jako vstup několika dalších bran.

## 1.2 Vyhodnocení obvodu

> [!info]
> Nechť
>
> $$
> e:\set{x_1,...,x_n} \rightarrow \set{0,1}
> $$
>
> je **ohodnocení vstupních proměnných**.
>
> _Pravdivostní hodnota každé brány_ $q$,označená $T(q)$, je definována **rekurzivně**:
>
> - Pokud brána má **indegree 0:**
>   $$
>   T(q)= \begin{cases}0, & \text{je-li označena } 0, \\ 1, & \text{je-li označena } 1, \\ e(x_i), & \text{je-li označena } x_i. \end{cases}
>   $$
>
> - Pokud brána má **indegree 1**,$h$ _je její vstupní brána a je-li označena_ $\neg$
>   $$
>   T(q)=\neg T(h)
>   $$
>
> - Pokud brána má **indegree 2**,$h_1$ a $h_2$ _jsou její vstupná hrany_
>
> $$
> T(q) = \begin{cases} T(h_1) \land T(h_2), & \text{je-li označena } \land, \\ T(h_1) \lor T(h_2), & \text{je-li označena } \lor. \end{cases}
> $$
>
> Pravdivostní hodnota celého Booleovského obvodu je rovna hodnotě jeho **výstupní brány**.

## 1.3 Míry složitosti

| Míra | Definice |
| --- | --- |
| **Velikost** obvodu $C$ | **Velikost Booleovského obvodu** je počet jeho bran. |
| **Hloubka** obvodu $C$ | **Hloubka Booleovského obvodu** je délka nejdelší orientované cesty od vstupní brány k výstupní bráně |

> [!note]
> **Intuice**:
>
> Velikost udává, kolik elementárních logických operací musí být celkem provedeno. Je analogií **časové složitosti sekvenčního algoritmu**, protože odpovídá celkovému množství vykonané práce.
>
> Brány ve stejné vrstvě _lze vyhodnocovat současně_, proto hloubka odpovídá **paralelnímu času** potřebnému k vyhodnocení obvodu. Čím je _hloubka menší, tím efektivněji lze výpočet paralelizovat_.

# 2. Rodina booleovských obvodů

- Jeden Booleovský obvod dokáže zpracovat pouze vstupy pevné délky $n$, protože obsahuje právě $n$ vstupních bran. Nelze jej proto použít pro vstupy jiné délky.
- Chceme-li popsat algoritmus pracující pro vstupy libovolné velikosti, musíme místo jednoho obvodu uvažovat **rodinu Booleovských obvodů**.

> [!success]
> **Rodina Booleovských obvodů** je posloupnost
>
> $$
> C=(C_n)_{n \geq 1},
> $$
>
> kde každý obvod $C_n$ _zpracovává právě všechny vstupy délky_ $n$.
>
> Pro každý $n$ tedy **existuje samostatný obvod** odpovídající _této délce vstupu._
>
> Rodina $C$ **rozhoduje jazyk** $A \sube \set{0,1}^*$_, pokud pro každé_ $x \in \set{0,1}^*$ platí:$x \in A$ právě když $C_{|x|}(x) = 1$.

## 2.1 Uniformní rodina obvodů

> [!danger]
> Samotná _existence rodiny obvodů nestačí_.
>
> Mohli bychom totiž pro každé $n$ zvolit **zcela libovolný obvod**, aniž by _mezi jednotlivými obvody existovala jakákoli souvislost_. Taková rodina **by nepředstavovala algoritmus**.
>
> Proto se zavádí pojem **uniformní rodina obvodů**, který zajišťuje, že všechny obvody lze efektivně _konstruovat jednotným způsobem_.

> [!success]
> Rodina obvodů $(C_n)_{n≥1}$ je **uniformní**, pokud _existuje algoritmus_, který _pro každé_ $n$ _sestrojí popis obvod_u $C_n$.
>
> V teorii složitosti se nejčastěji používá **logaritmická uniformita**.
>
> Rodina obvodů je **logspace-uniformní**, pokud _existuje DTS pracující v prostoru_
>
> $$
> O(\log n),
> $$
>
> který **na vstupu**
>
> $$
> 1^n
> $$
>
> _vygeneruje popis obvodu_ $C_n$.
>
> Použití vstupu ve tvaru $1^n$ slouží pouze k tomu, aby _stroj znal požadovanou velikost vstupu._

> [!note]
> **Intuice**:
>
> Uniformita říká, že obvody _nesmějí být připraveny „ručně“ nebo libovolně zvoleny pro každé_ $n$_._ **Musí existovat jednoduchý algoritmus**, který _je dokáže automaticky sestrojit_.
>
> Díky tomu _skutečně popisují algoritmus_, nikoli pouze libovolnou posloupnost obvodů.

---

# 3. Třída NC

- Třída $\text{NC}$ **(Nick's Class)** obsahuje problémy, které _lze efektivně řešit paralelně pomocí Booleovských obvodů_.

> [!success]
> Pro $i \geq 1$ řekneme, že $L \in \text{NC}^i$, pokud _existuje_ **uniformní** rodina booleovských obvodů $C$ **rozhodující** $L$ taková, že:
>
> - **Velikost** obvodu $C_n$ je $n^{O(1)}$ (polynomiální počet bran),
> - **Hloubka** $C_n$ **je** $O(\log^i n)$ (logaritmická hloubka na i-tou).

> [!note]
> _Řekneme_: Tedy jazyk patří do $\text{NC}^i$, pokud jej rozhoduje **uniformní rodina Booleovských obvodů** **polynomiální velikosti a hloubky** $O((\log n)^i)$.

> [!success]
> Celou třídu definujeme jako
>
> $$
> \text{NC}=\bigcup_{i \ge 1}\text{NC}^i.
> $$

> [!info]
> Obvody z třídy $\text{NC}$ mají:
>
> - polynomiální počet bran,
> - pouze **brány s konstantní aritou** (typicky dvě vstupní hrany),
> - malou (polylogaritmickou) hloubku.
>
> Díky tomu lze jejich jednotlivé vrstvy vyhodnocovat paralelně.

## 3.1 Příklad problémů v NC

| Problém | Kde leží |
| --- | --- |
| Sčítání dvou n-bitových čísel | $\text{NC}^1$ |
| Násobení booleovských matic $(n \times n)$ | $\text{NC}^1$ |
| Tranzitivní uzávěr, PATH | $\text{NC}^2$ |
| Vyhodnocení booleovské formule | $\text{NC}^1$ |

---

# 4. Třída AC

- Třída $\text{AC}$ **(Alternating Circuit)** vznikne **zobecněním** definice třídy $\text{NC}$.
- Na rozdíl od $\text{NC}$ dovolujeme, aby brány označené $\land$ a $\lor$ měly **neomezenou aritu** místo arity 2.

> [!success]
> Pro $i \geq 1$ řekneme, že $L \in \text{AC}^i$, pokud _existuje_ **uniformní** rodina booleovských obvodů $C$ **rozhodující** $L$ taková, že:
>
> - **Velikost** obvodu $C_n$ je $n^{O(1)}$ (polynomiální počet bran),
> - **Hloubka** $C_n$ **je** $O(\log^i n)$ (logaritmická hloubka na i-tou).
> - Brány $\land$ a $\lor$ mají **neomezenou aritu**
>
> - Celou třídu definujeme jako:
>
> $$
> AC = \bigcup_{i≥0} AC^i
> $$

> [!note]
> **Intuice:** jedno hradlo $\vee$ smí spojit najednou libovolně mnoho vstupů — odpovídá to procesoru, který v jednom taktu udělá `OR` přes celé pole. Reálné hardwarové omezení tedy ignorujeme.

## 4.1 Vztah NC a AC

> [!info]
> **Věta:** Pro každé $i ≥ 0$ platí: $NC^i \sube AC^i \sube NC^{i+1}$

**Důkaz intuice:**

- $NCⁱ ⊆ ACⁱ:$ Každý _obvod s branami arity 2_ je **speciálním případem** _obvodu s neomezenou arito_u
- $ACⁱ ⊆ NCⁱ⁺¹:$ Bránu s aritou $k$ _nahradíme binárním stromem bran_ arity 2. Takový strom má **hloubku** $O(\log k)$ a obsahuje $O(k)$ **bran**. Protože obvody z $\text{AC}^i$ mají _polynomicky mnoho bran a arita každé je tedy polynomicky omezená_, hloubka **vzroste nejvýše o faktor** $O(\log n)$. Hloubka $O(\logⁱ n)$ _se tak zvýší na_ $O(\logⁱ⁺¹ n)$.

> [!info]
> **Důsledek:**
>
> $AC = NC$
>
> Obě hierarchie, přestože jsou definovány různě (omezená vs. neomezená arita), definují **tutéž třídu**.

---

# 5. Vztahy NC k dalším třídám

### 5.1 Věta o vztazích

> [!info]
> **Věta:** (základní vztahy $\text{NC}$ k prostorovým/časovým třídám):
>
> (a) $\text{NC}^1 \sube L$  
> (b) $\text{NL} \sube \text{NC}^2$  
> (c) $\text{NC} \sube P$

| Inkluze | Co říká | Poznámka |
| --- | --- | --- |
| $\text{NC}^1 \sube L$ | Každý problém s $O(\log n)$ hloubkou a pol. velikostí je v log-prostoru | **Důkaz**: DTS simuluje obvod průchodem do hloubky, paměť $O(\log n)$ |
| $\text{NL} \sube \text{NC}^2$ | Nedeterministický log-prostor $\sube$ obvody hloubky $O(\log² n)$ | **Důkaz**: dosažitelnost $(\text{PATH}) \in \text{NC}^2$ přes tranzitivní uzávěr |
| $\text{NC} \sube P$ | Každý NC-problém je polynomiálně sériově řešitelný | **Důkaz**:$C_n$ má pol. bran, vyhodnocení trvá pol. čas |

---

# 6. Příklad: Simulace NL pomocí NC²

Cílem je ukázat, že každý jazyk z $\text{NL}$ lze rozhodnout pomocí uniformní rodiny Booleovských obvodů hloubky $O(\log^2n)$, tedy že

$$
\text{NL} \sube \text{NC2}.
$$

Postup konstrukce je následující:

1. Uvažujme nedeterministický TS $M$, který pracuje v logaritmickém prostoru, a vstup $x$ délky $n$.
2. Z konfigurací stroje $M$ sestrojíme **graf konfigurací**.
  - Vrcholy grafu představují jednotlivé konfigurace stroje.
  - Hrana mezi dvěma konfiguracemi existuje právě tehdy, pokud lze v jednom kroku přejít z první konfigurace do druhé.
  - Protože stroj používá pouze logaritmický prostor, má tento graf pouze **polynomiální počet konfigurací**.
3. Pomocí vstupních bran $x_1,…,x_n$ vytvoříme obvod, který sestrojí **matici sousednosti grafu konfigurací**.
  - Struktura grafu závisí pouze na délce vstupu $n$.
  - Konkrétní přechody však mohou záviset na hodnotách vstupních bitů $x$.
  - Tento obvod má konstantní hloubku, polynomiální velikost a lze jej zkonstruovat logspace transducerem.
4. Za tento obvod připojíme **obvod pro výpočet tranzitivního uzávěru** matice sousednosti.
  - Tento obvod určí, mezi kterými dvojicemi konfigurací existuje cesta.
  - Jeho hloubka je $O(\log^2n)$.
5. Výstupem celého obvodu je hodnota odpovídající tomu, zda je **akceptační konfigurace dosažitelná z počáteční konfigurace**.
6. Platí tedy

$$
x\in A ⟺ C_n(x)=1.
$$