# 1. Pravděpodobnostní Turingův stroj (PTS)

> [!success]
> Uvažujme **NTS** $M$ takový, že z **každé nekoncové konfigurace** máme **právě dvě** _nedeterministické volby_.  
> Výpočet $M$ na vstupu $x$ (tj. průchod jednou větví stromu výpočtu) probíhá takto:  
> V konfigurace $c:$
>
> 1. $M$ si hodí **férovou mincí** (s pravděpodobností $0{,}5$ padne orel, s pravděpodobností $0{,}5$ panna),
> 2. _Padne-li orel,_ provede se krok odpovídající **první** **nedeterministické volbě** _přístupné z_ $c$, jinak krok **odpovídající druhé volbě** _přístupné z_ $c$
>
> Předpokládáme, že $M$ **vždy zastaví**.  
> Je-li koncová konfigurace větve výpočtu $v$ v hloubce $h(v)$, pak pravděpodobnost průchodu touto větví je
>
> $$
> \frac{1}{2^{h(v)}}
> $$
>
> Řekneme tedy, že $M$ přijímá $x$ s pravděpodobností
>
> $$
> P[M(x) = 1] = \sum_{v \in S} \frac{1}{2^{h(v)}},
> $$
>
> kde $S$ je množina **přijímacích větví** $M$ pro vstup $x.$
>
> Očividně $M$ zamítá s pravděpodobností
>
> $$
> P[M(x)=0] = 1 - P[M(x)=1].
> $$
> ![[019ff00e-a5ac-77fd-a457-a807800d3b96.png]]

> [!info]
> **Složitost** je u PTS _definována stejně jako u NTS_

> [!note]
> **Intuice:**
>
> - Na rozdíl od NTS, který si "správnou větev" vybírá nedeterministicky, PTS vybírá mezi větvemi **náhodně** _pomocí hodů mincí_. Výsledkem výpočtu proto není pouze ANO nebo NE, ale **pravděpodobnost**, _s jakou stroj vstup přijme_.
> - U NTS stačí, aby existovala **jedna** přijímací větev (i kdyby byla jediná). U PTS nás zajímá, jakou **část** _stromu tvoří přijímací větve_.

## 1.1 Ekvivalentní „offline" pohled

- Na PTS se dá dívat jako na **obyčejný DTS** $M$, který dostane navíc druhý vstup — dostatečně dlouhý řetězec bitů $y$ na speciální pásce, jenž **nahrazuje házení mincí**.
- Pro konkrétní $x$ a konkrétní $y$ je výpočet $M(x,y)$ **deterministický**.
- Pravděpodobnost, že $M$ se složitostí $T(n)$ přijímá $x$ definujeme jako

$$
P_y[M(x,y)=1] = \frac{|\set{y \in \set{0,1}^k \mid M(x,y)=1}|}{2^k}
$$

kde $k$ je libovolné číslo větší než $T(|x|)$ (stroj se složitostí $T(n)$ nestihne přečíst víc než $T(n)$ náhodných bitů).

> [!note]
> **Intuice**: Pravděpodobnost přijetí pak získáme jednoduše tak, že spočítáme, pro _kolik možných řetězců_ $y$ algoritmus **přijme**, a _vydělíme jejich počet celkovým počtem možností_ $2^k$

---

# 2. Třída $\text{RP}$ a $\text{coRP}$

> [!success]
> $L \in \textbf{RP}$, pokud existuje PTS $M$ s **polynomiální časovou složitostí** tak, že
>
> - $x \in L \implies P[M(x)=1] \geq 3/4$
> - $x \notin L \implies P[M(x)=1] = 0$
> - Pokud **přijímá**, **máme jistotu**, že $x\in L$. Pokud **zamítá**, mohl by (s pravděpodobností nejvýše $1/4$) být $x\in L$.
>
> $L \in \textbf{coRP}$— chyba je přesunuta na druhou stranu:
>
> - $x \in L \implies P[M(x)=0] = 0$
> - $x \notin L \implies P[M(x)=0] \geq 3/4$
> - Pokud **zamítá**, **máme jistotu**, že $x\notin L$. Pokud **přijímá**, mohl by (s pravděpodobností nejvýše $1/4$) být $x \notin L$.
>
> Ekvivalentně můžeme napsat pomocí pravděpodobnosti přijetí:
>
> - $x \in L \implies P[M(x)=1] = 1$
> - $x \notin L \implies P[M(x)=1] \leq 1/4$
>
> Obě definice jsou stejné protože:
>
> - $P[M(x)=0] = 1 - P[M(x)=1]$

> [!danger]
> **Konstanta není podstatná!**
>
> Důvodem je, že **opakovaným spuštěním algoritmu lze pravděpodobnost chyby výrazně snížit.**

---

# 3. Třída $\text{BPP}$

> [!success]
> **Třída BPP** obsahuje všechny jazyky, které _lze rozhodnout PTS_ v polynomiálním čase s **oboustrannou omezenou chybou**.
>
> Řekneme, že $L \in \textbf{BPP}$, pokud existuje PTS $M$ s polynomiální časovou složitostí tak, že
>
> - $x \in L \implies P[M(x)=1] \geq 3/4$
> - $x \notin L \implies P[M(x)=1] \leq 1/4$

> [!note]
> **Intuice:**
>
> - $M$ **dělá chyby na obě strany**, ale obě jsou omezené konstantou $1/4$
> - Stejně jako u $\text{RP}$ není ani zde hodnota $3/4$ nijak výjimečná. Opakováním algoritmu a rozhodnutím podle **většinového hlasování** _lze pravděpodobnost chyby zmenšit_.

## 3.1 Základní vlastnosti

- **BPP je uzavřená na doplněk**, tj.$\text{BPP} = \text{coBPP}$. Plyne přímo z definice: definice je symetrická, stačí prohodit přijetí a zamítnutí.
- $\text{RP} \subseteq \text{BPP}$ a $\text{coRP} \subseteq \text{BPP}$— RP je speciální případ, kde je jedna z chyb rovna nule.
- Známé inkluze:$\text{P} \subseteq \text{RP} \subseteq \text{NP}$, dále $\text{RP} \subseteq \text{BPP}$,$\text{coRP} \subseteq \text{BPP}$.
  - $\text{P} \subseteq \text{RP}$: deterministický stroj je PTS, který mincí háže, ale výsledek ignoruje.
  - $\text{RP} \subseteq \text{NP}$: v offline pohledu je posloupnost náhodných bitů $y$, na které $M$ přijme, **certifikát**. Protože v NE-případě žádné takové $y$ neexistuje ($P = 0$), je verifikace korektní.

---

# 4. Věta o amplifikaci

> [!info]
> **Věta:** Pokud $A \in \text{BPP}$, pak pro **libovolný polynom** $n^d$ existuje PTS $N$ s polynomiální časovou složitostí tak, že pro $x$ délky $n$ platí
>
> $$
> P[N(x) \neq A(x)] \leq \frac{1}{2^{n^d}}.
> $$
>
> (Pravděpodobnost, že $N$ vrátí špatnou odpověď je…)

> [!warning]
> **Důkaz**:
>
> 1. Z $A \in \text{BPP}$ máme PTS $M$ s pol. čas. složitostí rozhodující $A$ s chybou omezenou $1/4$.
> 2. Sestavíme PTS $N$, který **simuluje** $M$ **na vstupu** $x$ **opakovaně, a to** $n^{d+1}\text{-krát}$ (s nezávislými náhodnými bity).
> 3. $N$ spočítá četnost přijetí a zamítnutí a **přijímá, pokud ve více než polovině případů** $M$ **přijímal** (většinové hlasování).
> 4. Složitost $M$ je polynomická, počet opakování je polynomický $\Rightarrow$ složitost $N$ je polynomická.
> 5. Pravděpodobnost, že $N$ udělá chybu (tj. že více než polovina simulací skončila chybou), omezíme součtem binomických členů:
>
> $$
> \sum_{k=0}^{n^{d+1}/2} \binom{n^{d+1}}{k} \left(\frac{3}{4}\right)^{k} \left(\frac{1}{4}\right)^{n^{d+1}-k} \leq \frac{1}{2^{n^d}}.
> $$

---

# 5. Věta:$\text{BPP} \subseteq \Sigma_2^p$

> [!info]
> Věta:
>
> $$
> \text{BPP} \subseteq \Sigma_2^p
> $$

- Protože BPP je uzavřená na doplněk, plyne odsud rovnou i $\text{BPP} \subseteq \Pi_2^p$, tedy $\text{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$.

---

# 6. Přirozené problémy v $\text{BPP}$

## 6.1 Testování prvočíselnosti

- Dnes **triviální**, protože víme, že problém patří do $\text P$ (AKS algoritmus).
- Nicméně i kdyby do $\text{P}$ nepatřil, patřil by do $\text{BPP}$: existují efektivní pravděpodobnostní algoritmy (**Miller–Rabinův test**, **Solovay–Strassenův test**)

## 6.2 Testování polynomických identit (PIT)

> [!success]
> **Název**: Testování polynomických identit
>
> **Vstup:** Polynom nad proměnnými $x_1, \dots, x_n$ s _celočíselnými koeficienty zadaný ve formě_ **aritmetického obvodu** (definice je analogická booleovskému obvodu, jen brány místo logických operací počítají $+$, $-$, $*$).
>
> **Otázka:** Je tento obvod roven $0$ pro všechna ohodnocení proměnných?