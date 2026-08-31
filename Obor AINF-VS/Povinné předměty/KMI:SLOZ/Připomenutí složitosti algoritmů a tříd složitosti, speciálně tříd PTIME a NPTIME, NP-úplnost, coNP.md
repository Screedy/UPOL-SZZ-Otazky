> [!warning]
> **Velikostí vstupu TS** rozumíme _počet buněk_ (vstupní pásky), které _daný vstup zabírá_.
>
> **Délka výpočtu TS** $M$ _pro konkrétní vstup_ se definuje jako _počet provedení instrukcí_, které $M$ pro daný vstup vykoná, než se zastaví.
>
> **Velikostí paměti TS** $M$ _potřebné při výpočtu pro konkrétní vstup_ rozumíme číslo $p + 1$, kde $p$ je _maximální počet buněk_, jež jsou během výpočtu (nad daným vstupem) _navštíveny_.

- Abychom mohli porovnávat efektivitu algoritmů, potřebujeme nějak změřit množství prostředků, které při výpočtu spotřebují. Nejčastěji sledujeme **časovou** a **paměťovou složitost.**

> [!success]
> **Časová složitost DTS** $M$ je funkce $T_M: \mathbb{N} \to \mathbb{N}$, kde $T_M(n)$ je _délka výpočtu_ $M$ nad vstupem délky $n$ **v nejhorším případě** (worst case).
>
> **Paměťová složitost** **DTS** $M$ je funkce $S_M: \mathbb{N} \to \mathbb{N}$, kde $S_M(n)$ je _velikost potřebné paměti při výpočtu_ $M$ nad vstupem délky $n$ **v nejhorším případě** (worst case).
>
>
> Pro NTS jsou _definice analogické_.

- Časová i paměťová složitost Turingova stroje jsou funkcemi velikosti vstupu. Při analýze _nás však obvykle nezajímá jejich přesná hodnota_ (nezajímají nás konstanty a implementační detaily), ale především to, jak rychle rostou se zvětšující se velikostí vstupu.
- Proto se v teorii složitosti používají **asymptotické notace**, které popisují pouze řád růstu těchto funkcí. Nejpoužívanější asymptotickou notací je **velké** $O$, které udává horní odhad růstu časové nebo paměťové složitosti algoritmu.

> [!success]
> **Asymptotická horní mez**:
>
> _Řekneme_, že
>
> $$
> f(n)∈O(g(n))
> $$
>
> jestliže **_existují konstanty_** $c>0$ a $n_0$, že pro všechna $n≥n_0$ platí
>
> $$
> f(n)≤c⋅g(n)
> $$

> [!note]
> **Intuice**:
>
> Notace $O$ udává **horní odhad růstu funkce**. Říká, že _algoritmus nebude asymptoticky růst rychleji_ než $g(n)$ (až na konstantní násobek).

> [!info]
> Při asymptotické analýze **zanedbáváme konstanty a členy nižších řádů**, protože _pro velká n rozhoduje člen s nejvyšším růstem_.

- Kromě asymptotické horní meze $O$ se používá také **ostrá asymptotická horní mez** $o$, která vyjadřuje, že jedna funkce roste asymptoticky **přísně pomaleji** než druhá.

> [!success]
> **Asymptotická ostrá horní mez**:
>
> _Řekneme_, že
>
> $$
> f(n)∈o(g(n))
> $$
>
> jestliže **_pro každou konstantu_** $c>0$ existuje $n_0$, že pro všechna $n≥n_0$ platí
>
> $$
> f(n)<c⋅g(n)
> $$

> [!note]
> **Intuice:**  
> Notace **malé** $o$ udává **ostrou horní mez**. Znamená, že funkce $f(n)$ roste **asymptoticky přísně pomaleji** než funkce $g(n)$. Na rozdíl od velkého $O$ tedy _není dovoleno, aby obě funkce měly stejný řád růstu_.

# 1. Základní třídy složitosti

- Pomocí časové a paměťové složitosti můžeme _Turingovy stroje rozdělit_ do **tříd složitosti**. Každá třída obsahuje problémy, které lze vyřešit při daném omezení na čas nebo paměť výpočtu.

| Třída | Definice |
| --- | --- |
| $\text{DTIME}(T(n))$ | $\{L(M) \mid M$ je **DTS** s časovou složitostí $O(T(n))\}$ |
| $\text{NTIME}(T(n))$ | $\{L(M) \mid M$ je **NTS** s časovou složitostí $O(T(n))\}$ |
| $\text{DSPACE}(S(n))$ | $\{L(M) \mid M$ je **DTS** s paměťovou složitostí $O(S(n))\}$ |
| $\text{NSPACE}(S(n))$ | $\{L(M) \mid M$ je **NTS** s paměťovou složitostí $O(S(n))\}$ |

> [!note]
> _Jak to správně říct_:
>
> Pro **časovou složitost** $T(n)$ definujeme $\text{DTIME}(T(n))$ jako _množinu všech jazyků_ rozhodnutelných **deterministickým** Turingovým strojem, jehož _časová složitost_ je $O(T(n))$.

#### Vztahy mezi základními třídami

> [!info]
> **Věta 19.** Pro funkce $s(n) \geq n$ a $t(n) \geq n$ platí:
>
> 1. $\text{DTIME}(t(n)) \subseteq \text{NTIME}(t(n))$ a $\text{DSPACE}(s(n)) \subseteq \text{NSPACE}(s(n))$
> 2. $\text{DTIME}(t(n)) \subseteq \text{DSPACE}(t(n))$ a $\text{NTIME}(t(n)) \subseteq \text{NSPACE}(t(n))$
> 3. $\text{DSPACE}(s(n)) \subseteq \text{DTIME}(2^{O(s(n))})$ a $\text{NSPACE}(s(n)) \subseteq \text{NTIME}(2^{O(s(n))})$
> 4. $\text{NTIME}(t(n)) \subseteq \text{DSPACE}(t(n))$
> 5. $\text{NSPACE}(s(n)) \subseteq \text{DTIME}(2^{O(s(n))})$

> [!warning]
> **Důkaz**:
>
> 1. _Deterministický_ TS můžeme chápat jako **speciální případ** _nedeterministického_ TS.
> 2. TS může pomocí jednoho kroku navštívit **nanejvýš jedno** _nové políčko pásky_.
> 3. Nerovnosti _plynou z 1. a 4. a 5._
> 4. _NTS_ $M$ s _časovou složitostí_ $f(n)$ simulujeme za pomoci _TS_ $N$ _s paměťovou složitostí_ $O(f(n))$.  
>   $N$ provádí **průchod do hloubky** _výpočetním stromem_ $M$, přičemž pokud _narazí na přijímací konfiguraci_, tak také **přijímá**. Jelikož $M$ má **časovou složitost** $f(n)$, tak **hloubka výpočetního stromu** je $f(n)$.   
>   První zavolání spustí s počáteční konfigurací. Dále nechť $k$ je maximální počet nedeterministických voleb, které má $M$ k dispozici. Tyto volby lineárně uspořádáme a _reprezentujeme je symbolem z vhodné k-prvkové abecedy_.$N$ si proto v rekurzivních volání _nemusí pamatovat aktuální konfiguraci_, místo toho si pamatuje řetězec $w$ nedeterministických voleb takový, že když stroj $M$ simuluje z počáteční konfigurace a nedeterministické volby vybírá podle $w$, dostane se do aktuální konfigurace. Rekurzivní volání $N$ provádí tak, že $w$ _rozšíří o další symbol_. Při návratu z rekurzivního volání pak $w$ zase o jeden symbol zkrátí. Paměťová složitost je tedy $2⋅f(n)$ (počáteční konfigurace a řetězec $w$), co je $O(f(n))$.
> 5. K NTS $M$ s _paměťovou složitostí_ $f(n)$ vytvoříme TS $N$ s _časovou složitostí_ $2^{O(f(n))}$ tak, že $L(M) = L(N)$.   
>   TS $N$ _na pásku zapíše všechny konfigurace stroje_ $M$, které odpovídají $f(n)$ políčkům pásky. **Počet konfigurací**, které zapíše _je omezen_ $2^{O(f(n))}$. _Zapsat_ všechny tyto konfigurace na pásku proto trvá také **nejvýše** $O(2^{O(f(n))})$ kroků.  
>   Poté $N$ _opakovaně prochází všechny konfigurace_ a značí se k nim, jestli jsou **dosažitelné z počáteční konfigurace**. V momentě, kdy $N$ _narazí na dosažitelno_u přijímací konfiguraci, tak **přijímá**. Pokud při průchodu konfiguracemi _neoznačí jako dosažitelnou žádnou_ novou konfiguraci, **zamítá**. Jeden průchod konfiguracemi lze provést _v čase polynomicky závislém_ na $O(2^{O(f(n))})$ a průchodů je nejvýše $O(2^{O(f(n))})$, proto _celková složitost_ je také $O(2^{O(f(n))})$.


---

# 2. Třída $\text{PTIME}$

> [!success]
> Třída $\text{PTIME}$ (Polynomial Time), značená také $\text P$, je _množina všech jazyků rozhodnutelnýc_h **deterministickým** Turingovým strojem **v polynomiálním čase**.
>
> $$
> \text{P} = \bigcup_{k > 0} \text{DTIME}(n^k)
> $$

> [!note]
> To znamená, že jazyk patří do $\text P$ právě tehdy, když _existuje deterministický Turingův stroj_, který jej **rozhodne v čase** $O(n^k)$ _pro nějaké_ $k$

- **Příklady problémů** z $P$
  - dosažitelnost v grafu (BFS, DFS),
  - nalezení nejkratší cesty (Dijkstrův algoritmus),
  - minimální kostra grafu (Kruskalův algoritmus),
  - třídění čísel,
  - test prvočíselnosti $\text{PRIMES}$.

> [!info]
> **Poznámka k** $\text{PRIMES}$**:**
>
> Historicky pěkný příklad problému, který _„_**_padal třídami dolů_**_“_:  
> nejdřív $\in \text{NP} \cap \text{coNP}$, pak $\in \text{BPP}$, nakonec $\in \text{P}$  
> Ukazuje, že zařazení do třídy je otázka _našeho poznání_, ne _vlastnosti problému samotného_.

> [!danger]
> **Uzavřenost na doplněk:** $\text{P} = \text{coP}$. _Prohodíme přijímací a zamítací stav_ — funguje, protože DTS _vždy zastaví_ a má _právě jednu výpočetní větev_. (Tohle u $\text{NP}$ selže!)

---

# 3. Třída $\text{NPTIME}$

> [!success]
> Třída $\text{NPTIME}$, značená $\text{NP}$, je _množina všech jazyků rozhodnutelných_ **NTS** **v polynomiálním čase**.
>
> $$
> \text{NP} = \bigcup_{k > 0} \text{NTIME}(n^k)
> $$

> [!note]
> To znamená, že jazyk patří do $\text {NP}$ právě tehdy, když _existuje nedeterministický_ Turingův stroj, který jej **rozhodne v čase** $O(n^k)$ pro nějaké $k$

## 3.1 Definice pomocí certifikátů

> [!success]
> Jazyk $L$ patří do třídy $\text{NP}$ právě když _existuje_ **_DTS_** $V$ (tzv. **verifikátor**) pracující v polynomiálním čase a **_polynom_** $p$, že _pro každé slovo_ $x$ platí
>
> $$
> x∈L
> $$
>
> právě když **existuje certifikát** $y$, pro který
>
> $$
> | y| \leq p(|x|)
> $$
>
> a
>
> $$
> V(x,y)=1.
> $$

> [!note]
> NP jsou problémy, u kterých lze **správnost kladné odpovědi** ("ANO") ověřit **v polynomiálním čase**.

> [!info]
> **Proč je tato definice tak důležitá:**  
> Certifikátová definice je to, co se v praxi používá _při dokazování_ „$L \in \text{NP}$“ (stačí říct, _co_ je certifikát a _jak_ se ověřuje)  
> Definice přes NTS je zase to, co se používá _v důkazech NP-těžkosti_ (Cook–Levin).

### 3.1.1 Příklady

**Název:** $\text{SAT}$ (problém splnitelnosti booleovských formulí)  
**Vstup:** Booleovská formule $\varphi$ v _konjunktivní normální formě_.  
**Otázka:** Je daná formule _splnitelná_?

- Jako **certifikát lze použít ohodnocení** $e$ výrokových proměnných.
- Verifikátor pro dvojici $(\varphi, e)$, _spočítá pravdivost_ $\varphi$ při ohodnocení $e$.

**Název:** $\text{CLIQUE}$  
**Vstup:** Neorientovaný graf $G, k ∈ N$.  
Otázka: Obsahuje $G$ kliku s alespoň $k$ uzly?

- _Klika_ = Maximální úplný podgraf (Podgraf, takový že všechny uzly v něm jsou navzájem sousední)
- Jako **certifikát lze použít množinu vrcholů** $V'$ potřebné velikosti.
- Verifikátor pro dvojici $(G, V')$, ověří _zda se jedná o kliku_.

**Název:** $\text{HK}$ (problém Hamiltonovské kružnice)  
**Vstup:** Neorientovaný graf $G$.  
Otázka: Existuje v $G$ hamiltonovská kružnice? (uzavřená cesta, procházející každým vrcholem pouze jednou)

## 3.2 Vztah $\text{P a NP}$

> [!success]
> **Platí**:
>
> $$
> \text{P} \subseteq \text{NP}
> $$

> [!warning]
> Důkaz:
>
> _Důvod je jednoduchý_: pokud lze problém **vyřešit** deterministickým Turingovým strojem v polynomiálním čase, pak lze jeho řešení samozřejmě také v polynomiálním čase **ověřit**.  
> **Každý problém z třídy** $\text P$ **tedy _automaticky patří_ i do třídy** $\text{NP}$

> [!danger]
> Jednou _z nejvýznamnějších otevřených otázek teoretické informatiky_ je, zda platí
>
> $$
> \text P = \text{NP}
> $$

---

# 4. $\text{NP-těžkost}$ a $\text{NP-úplnost}$

> [!warning]
> - Funkce $f: Σ^* → Σ^*$ je **spočítatelná v polynomickém čase**, pokud _existuje_ TS $M$, který pro vstup $w$, _zastaví po polynomickém počtu kroků_ (vzhledem k $|w|$) a _na pásce zůstane_ řetězec $f(w)$. (Funkce nemusí být ani surjektivní ani injektivní)
> - Jazyk $A$ je **v polynomickém čase redukovatelný** na $B$, značíme $A ≤_p B$, pokud _existuje funkce_ $f$ _spočitatelná v polynomickém čase_ tak, že $x∈A$ právě když $f(x)∈B$

> [!note]
> Intuitivně to znamená, že **pokud bychom uměli efektivně řešit problém** $B$**, uměli bychom pomocí redukce efektivně řešit i problém** $A$.

> [!info]
> **Věta.** $A \leq_p B$ a $B \in \text{P} \Rightarrow A \in \text{P}.$
>
> **Důsledek**.$A \notin P$ implikuje $B \notin P$.

> [!info]
> **Věta (tranzitivita).** $A \leq_p B$ a $B \leq_p C \Rightarrow A \leq_p C.$

> [!success]
> _Jazyk_ $L$ je **NP-těžký**, jestliže na něj lze _v polynomiálním čase_ převést **každý jazyk** z třídy $\text{NP}$
>
> $$
> ∀L' \in \text{NP}:\qquad L' \leq_p L
> $$

> [!note]
> **Intuitivně**_:_ NP-těžký problém je **alespoň tak obtížný** _jako všechny problémy z_ **NP**.  
> Nemusí však _sám patřit do NP_ ani být _rozhodnutelný_. (Např. halting problem je NP-těžký)

> [!success]
> Jazyk $L$ je **NP-úplný**, pokud:
>
> - je **NP-těžký**
> - **patří do třídy** $\text{NP}$

> [!note]
> _NP-úplné problémy_ tedy představují **nejtěžší problémy uvnitř třídy** $\text{NP}$.  
> Pokud by se _podařilo nalézt polynomiální algoritmus_ **pro jediný NP-úplný problém**, pak by platilo
>
> $$
> \text{P}=\text{NP}
> $$
>
> Naopak, _pokud bychom dokázali_, že _některý NP-úplný problém_ **nelze řešit v polynomiálním čase**, znamenalo by to
>
> $$
> \text{P} \neq \text{NP}.
> $$

> [!info]
> **Věta (nástroj na dokazování NP-těžkosti).** Je-li $A$ NP-těžký a $A \leq_p B$, pak i $B$ je NP-těžký.

---

# 5. Cook-Levinova věta

> [!success]
> **Cookova–Levinova věta:** Problém **SAT** je NP-úplný.

> [!warning]
> Důkaz:
>
> 1. $\text{SAT} \in \text{NP}$
>   - Certifikátem je **ohodnocení proměnných** formule.Verifikátor pouze dosadí toto _ohodnocení do formule_ a v polynomiálním čase zkontroluje, zda _je formule pravdivá_.
> 2. **SAT je NP-těžký**
>   - Abychom dokázali, že je SAT NP-hard, musíme ukázat, že **každý problém z třídy NP lze v polynomiálním čase převést na SAT**. Nechť tedy $L \in \text{NP}$. Z definice třídy $\text{NP}$ existuje nedeterministický Turingův stroj $M$, který rozhoduje jazyk $L$ v polynomiálním čase.
>   - Pro libovolný vstup $x$ uvažujeme výpočet tohoto stroje. Celý jeho výpočet lze zaznamenat do tzv. **tableau**, tedy tabulky, jejíž řádky představují jednotlivé konfigurace stroje v čase a sloupce jednotlivá políčka pásky. Předpokládáme, že stroj běží nejvýše $n^k$ kroků. Má nejvýše $n^k$ řádků, během $n^k$ kroků navštíví nejvýše $n^k$ políček pásky. Celá tabulka má tedy rozměr přibližně $n^k \times n^k$, což je stále polynom.![[019fe1dc-8ad6-76ca-a5a0-1a2035477ed7.png]]
>   - Z této tabulky následně _sestrojíme booleovskou formul_i
>     $$
>     \varphi_{M,x}= \varphi_{\text{cell}} \land \varphi_{\text{start}} \land \varphi_{\text{move}}\land \varphi_{\text{accept}},
>     $$
>     která je **splnitelná** právě tehdy, když _tableau představuje správný přijímací výpočet stroje_.
>   - J_ednotlivé části formule_ zajišťují následující podmínky:
>     - $\varphi_{cell}$ zajišťuje, že každá buňka tableau obsahuje **právě jeden symbol** (symbol pásky nebo symbol reprezentující stav stroje s hlavou na daném políčku).
>     - $\varphi_{start}$ zajišťuje, že **první řádek tableau** odpovídá počáteční konfiguraci Turingova stroje na vstupu $x$.
>     - $\varphi_{move}$ zajišťuje, že **každá následující konfigurace vznikne z předchozí správnou aplikací přechodové funkce**. Jinými slovy, každý řádek tabulky musí odpovídat _jednomu korektnímu kroku výpočt_u.
>     - $\varphi_{accept}$ zajišťuje, že se v tableau objeví **přijímací konfigurace** (obvykle v posledním řádku). Pokud stroj skončí dříve než po maximálním uvažovaném počtu kroků, předpokládá se, že _všechny následující řádky zůstávají stejné_.
>   - Je-li možné _proměnným formule přiřadit hodnoty_ tak, aby byly **všechny tyto podmínky splněny**, _existuje správně vyplněné tableau_, které odpovídá přijímacímu výpočtu Turingova stroje. Platí tedy
>     $$
>     x \in L⟺\varphi_{M,x} \text{ je splnitelná}
>     $$

> [!info]
> Cookova–Levinova věta byla _prvním důkazem existence NP-úplného problému_. Od té doby lze **NP-úplnost dalších problémů** dokazovat **redukcemi ze SAT** nebo _z jiných již známých NP-úplných problémů_.

---

# 6. Třída $\text{coNP}$

> [!success]
> Třída $\text{coNP}$ obsahuje doplňky jazyků z třídy $\text{NP}$.
>
> $$
> \text{coNP} = \set{\overline{L} \mid L \in \text{NP}}
> $$

> [!note]
> Jinými slovy, pokud jazyk $L$ patří do $\text{NP}$, pak jeho doplněk $\overline L$ patří do $\text{coNP}$

> [!info]
> Zatímco u problémů z $\text{NP}$ _lze v polynomiálním čase ověřit správnost odpovědi_ **ANO**, u problémů z $\text{coNP}$ _lze v polynomiálním čase ověřit správnost odpovědi_ **NE**.
>
> Jinými slovy, problémy z $\text{coNP}$ mají **krátký certifikát pro zápornou odpověď**, zatímco problémy z $\text{NP}$ mají _krátký certifikát pro odpověď kladnou_.

**Název:** $\text{UNSAT}$ (problém nesplnitelnosti booleovských formulí)

**Vstup:** Booleovská formule $\varphi$ v _konjunktivní normální formě_.

**Otázka:** Je daná formule ne_splnitelná_?

- Je to doplněk $\text{SAT}$

**Název:** $\text{TAUTOLOGY}$ (problém tautologie booleovských formulí)

**Vstup:** Booleovská formule $\varphi$.

**Otázka:** Je formule $\varphi$ pravdivá pro **každé** ohodnocení výrokových proměnných?

- **Certifikátem pro zápornou odpověď** (tj. že formule **není** tautologií) je **ohodnocení** e výrokových proměnných, pro které je formule nepravdivá.

## 6.1 Vztahy

> [!note]
> - _Platí_
>   $$
>   \text P \sube \text{NP},
>   $$
>   protože každý _problém řešitelný v polynomiálním čase_ lze také _v polynomiálním čase_ **ověřit**.
>
> - _Platí_ také
>   $$
>   \text{P} \sube \text{coNP},
>   $$
>   protože třída $P$ je **uzavřená na doplněk**. Je-li jazyk _rozhodnutelný v polynomiálním čase_, pak je _v polynomiálním čase rozhodnutelný_ i jeho **doplněk**.
>
> - O vztahu _mezi třídami_ NP a coNP _není známo_ jejich vztah
>   $$
>   \text{NP}=\text{coNP} \quad \text{nebo} \quad \text{NP}\neq\text{coNP}
>   $$