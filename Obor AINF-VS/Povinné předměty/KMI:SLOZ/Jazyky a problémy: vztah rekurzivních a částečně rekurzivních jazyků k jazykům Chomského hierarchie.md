> [!success]
> **Jazyk:**
>
> Nechť $\Sigma$ je _konečná abeceda_. Potom jazyk $L$ je _libovolná podmnožina množiny všech_ **_konečných_** _slov_ nad touto abecedou:
>
> $$
> L⊆Σ^∗.
> $$
>
> kde $\Sigma^*$ označuje _množinu všech konečných slov_ nad abecedou $\Sigma$, včetně prázdného slova $\varepsilon$.

> [!success]
> **Problém** je _trojice_ $(\text{IN}, \text{OUT}, \text{p})$, kde:
>
> - $\text{IN}$ je množina (přípustných) vstupů,
> - $\text{OUT}$ je množina výstupů a
> - $p: \mathrm{IN} \to \mathrm{OUT}$ je funkce _přiřazující každému vstupu odpovídající výstup._
>
> Algoritmus $A$ _řeší problém_ $P$ zadaný trojicí $(\text{IN}, \text{OUT}, \text{p})$ **spolu s dohodnutým kódováním vstupů a výstupů**, jestliže je _schopen přijmou_t (přečíst) kód jakéhokoli vstupu $x$ z množiny $\text{IN}$ a vydat k němu **po konečném počtu kroků** kód výstupu $y$ z množiny $\text{OUT}$, pro nějž $y = p(x)$.
>
> **Rozhodovací (ANO/NE) problém** je speciální případ, kde $\mathrm{OUT} = \set{\text{Ano}, \text{Ne}} = \set{1, 0}$

> [!note]
> **Intuice**: Jazyk a rozhodovací problém jsou dvě různá vyjádření téže věci:
>
> - **jazyk** říká, která slova jsou správná,
> - **rozhodovací problém** se ptá, zda konkrétní slovo do tohoto jazyka patří.

# 1. Rekurzivní a částečně rekurzivní jazyky

> [!warning]
> **Turingův stroj** je _šestice_ $M = (Q, \Sigma, \Gamma, \delta, q_0, F)$, kde
>
> - $Q$ je konečná neprázdná množina **stavů**,
> - $\Sigma$ je konečná neprázdná množina **vstupních symbolů**,
> - $\Gamma$ je **pásková abeceda**,$\Sigma \subseteq \Gamma$, a $\Gamma - \Sigma$ obsahuje alespoň prázdný znak $\sqcup$,
> - $q_0 \in Q$ je **počáteční stav**,
> - $F \subseteq Q$ je **koncové stavy**; _u rozhodovacích problémů_ $F = {q_{accept}, q_{reject}}$,
> - $\delta: (Q - F) \times \Gamma \to Q \times \Gamma \times \set{-1, 0, +1}$ je **přechodová funkce**.
>   - Instrukce $(q, a) \to (q', a', m)$
>
> **Konfigurace** je _trojice_ $(u, q, v)$, kde $u, v ∈ Γ^*$ a $q ∈ Q$  
> (obsah pásky vlevo od hlavy, aktuální stav, obsah pásky od hlavy doprava)
>
> Relaci _„jeden krok"_ značíme $c_1 \vdash c_2$, její tranzitivní uzávěr $\vdash^+$, reflexivně-tranzitivní $\vdash^*$. (TS přejde z konfigurace $c_1$ do $c_2$)
>
> Turingův stroj $M$ přijímá slovo $w$ pokud z počáteční konfigurace se po konečném počtu kroků dostane do přijímající konfigurace: $c_{start} \vdash^* c_{accept}$

> [!warning]
> **Nedeterministický TS** se liší pouze přechodovou funkcí
>
> $$
> \delta: Q \times \Gamma \to 2^{Q \times \Gamma \times \set{-1,0,+1}}
> $$
>
> Výpočet je **strom konfigurací**. NTS **přijímá**, pokud _alespoň jedna_ větev přijímá; zamítá, pokud _žádná_ větev nepřijímá.

> [!success]
> Množinu všech slov $w ∈ Σ^*$, které TS $T$ **přijímá**, značíme $L(T)$. Jazyk $L(T)$ nazýváme **jazyk částečně rekurzivní (RE)** a říkáme, že TS $T$ **rozpoznává jazyk** $L(T)$
>
> Pokud navíc platí, že TS $T$ **zamítá** _každé slovo, které nepatří_ do $L(T)$, nazýváme jazyk $L(T)$ jazyk **rekurzivní (R)** a říkáme, že TS $T$ **rozhoduje jazyk** $L(T)$

> [!info]
> **Vztah**:
>
> Každý r_ekurzivní jazyk je zároveň částečně rekurzivní_. Platí tedy:
>
> $$
> \text{rekurzivní}\subsetneq \text{částečně rekurzivní }
> $$
>
> **Opačná inkluze neplatí**. Existují jazyky (například HALT), které _lze pouze rozpoznat, ale nelze je rozhodnout_.

## 1.1 Enumerátorová charakterizace RE

> [!success]
> **Enumerátor** $E$ je TS _obohacený o možnost tisku řetězců_. 
>
> - _Ignoruje vstup_ (smaže pásku a vrátí se na začátek), _nemusí zastavit_
> - $L(E) = \set{ w | E \text{ vytiskne } w }$ (množina řetězců, které vytiskne)

> [!info]
> **Věta.** $L$ je rozpoznatelný $\iff$ existuje enumerátor $E$ s $L = L(E)$.

> [!warning]
> Důkaz:
>
> $\Rightarrow:$
>
> - Použijeme **paralelní simulaci** všech výpočtů.
>
> ![[019fd79d-b8cd-73ad-b3a6-d492c650d2bf.png]]
>
> $\Leftarrow:$
>
> 1. Spustíme enumerátor.
> 2. Sledujeme, co tiskne.
> 3. Jakmile vytiskne hledané slovo x, přijmeme.

## 1.2 Existence nerozpoznatelných jazyků

> [!info]
> **Věta**. Existují jazyky, které nejsou rozpoznatelné Turingovým strojem.

> [!warning]
> Důkaz:
>
> _Turingových strojů_ je **spočetně mnoho**. Každý stroj má konečný počet stavů, konečný počet pravidel, …  
> Lze jej tedy zapsat jako konečný řetězec znaků.
>
> _Jazyků_ je **nespočetně mnoho**. Dokazuje se _Cantorovou diagonalizační metodou_.
>
> ![[019fd7a6-67ae-7569-9203-3cb2af413eab.png]]

> [!note]
> **Důsledek:** Existují jazyky, které **nejsou rozpoznatelné** (natož rozhodnutelné)

### 1.2.1 Konkrétní příklad $A_{TM}$

Jazyk:$A_{TM} = \set{(\langle M \rangle, w) \mid M \text{ přijímá } w}$

- Je rozpoznatelný. Pro vstup $(<M>, w)$ simuluje TS $M$ pro vstup $w$, a přijímá, pokud $M$ přijímá. 
- Bývá označován jako **Halt problém**.

> [!info]
> **Věta**. $A_{TM}$ není rozhodnutelný.

> [!warning]
> **Důkaz: Sporem**. Předpokládáme, že existuje TS $H$, který rozhoduje $A_{TM}$. 
>
> Sestavíme TS $D$, který pro vstup $<X>$ provede:
>
> 1. _Simuluje_ $H$ pro $(<X>, <X>)$.
> 2. **Vrátí opačný výsledek**. ($H$ přijme →$D$ zamítne a naopak)
>
> Nyní se podívejme, co se stane, když na $D$ dáme vstup $<D>$. Pokud $D$ přijímá $<D>$, pak $H$ přijímá $(<D>, <D>)$, což ovšem znamená, že $D$ zamítá $<D>$. Spor nastane, i když $D$ zamítá $<D>$.

## 1.3 Postova věta

> [!info]
> **Věta (Postova věta).** Jsou-li $L$ i $\overline{L}$ rozpoznatelné, pak jsou **rozhodnutelné**.

> [!warning]
> **Důkaz**_:_ Pustím oba stroje **zároveň, střídavě po krocích.** Jeden z nich musí jednou přijmout.

> [!note]
> _Důsledek:_ $\mathrm{R} = \mathrm{RE} \cap \mathrm{coRE}$, a $\overline{A_{TM}}$ není ani rozpoznatelný.

## 1.5 Další nerozhodnutelné jazyky

- $\mathrm{EMPTY} = \set{\langle M \rangle \mid L(M) = \emptyset}$
- $\mathrm{EQUAL} = \set{(\langle M_1\rangle, \langle M_2\rangle) \mid L(M_1) = L(M_2)}$

---

# 2. Gramatiky a Chomského hierarchie

> [!success]
> **Gramatika** je čtveřice $G = (N, \Sigma, P, S)$:
>
> - $N$ je konečná neprázdná množina **neterminálů** (velká písmena),
> - $\Sigma$ je konečná množina **terminálů**, a platí $\Sigma \cap N = \emptyset$,$V = N \cup \Sigma$,
> - $P \subseteq \set{\alpha \to \beta \mid \alpha, \beta \in (N \cup \Sigma)^*,\ \alpha \neq \varepsilon}$ je konečná množina **pravidel**,
> - $S \in N$ je **počáteční neterminál**.

- Řetězec z $(N \cup \Sigma)^*$ nazýváme **větná forma**.
- **Přímé odvození:** $\gamma\alpha\omega \vdash \gamma\beta\omega$, existuje-li pravidlo $\alpha \to \beta$.
- Jazyk _generovaný gramatikou_:$L(G) = \set{w \in \Sigma^* \mid S \vdash^* w}$

## 2.1 Chomského hierarchie

![[019fd7b8-d2e4-7723-b022-28f4b175a6df.png]]

| Typ | Název | Omezení na pravidla |
| --- | --- | --- |
| **0** | **Neomezená** | Jen $\alpha \neq \varepsilon$ |
| **1** | **Kontextová** (context-sensitive), _nezkracující_ | $\lvert \alpha \rvert \le \lvert \beta \rvert$ |
| **2** | **Bezkontextová** (context-free) | $A \to \alpha$, kde $A \in N$ |
| **3** | **Regulární** | $A \to \alpha B$ nebo $A \to a$ |

> [!danger]
> Každý typ je speciálním případem předchozího, takže $\text{typ 3} \subseteq \text{typ 2} \subseteq \text{typ 1} \subseteq \text{typ 0}$ **na úrovni gramatik**.

## 2.3 Odpovídající výpočetní modely

| Typ | Třída jazyků | Automat | Rozhodnutelnost příslušnosti |
| --- | --- | --- | --- |
| 0   | částečně rekurzivní (RE) | Turingův stroj | **nerozhodnutelná** |
| 1   | kontextové (CS) | **Lineárně omezený automat (LBA)** = NTS s páskou velikosti vstupu | rozhodnutelná v $\mathrm{NSPACE}(n)$ |
| 2   | bezkontextové (CF) | zásobníkový automat | rozhodnutelná, dokonce v $\mathrm{P}$ |
| 3   | regulární (REG) | konečný automat | rozhodnutelná, v čase $O(n)$/ prostoru $O(1)$, tedy v $\mathrm{L}$ |

---

# 3. Typ 0 (částečně rekurzivní jazyky)

> [!info]
> **Věta 12.** Je-li $G$ gramatika typu 0, pak je $L(G)$ **rozpoznatelný**.

- **Nedeterministický** TS má na _jedné pásce vstup, na druhé větnou formu_.  
  **Nedeterministicky vybírá** pozici a pravidlo, _aplikuje ho_, a když se _větná forma rovná vstupu, přijme_. → **Stroj hádá odvození.**

#### _Důkaz_

Sestavíme **dvoupáskový NTS** $R$ s $L(R) = L(G)$. Pro vstup $w$:

1. Na první pásce je $w$, na druhou pásku zapíše $S$ (aktuální větná forma).
2. **Nedeterministicky vybere pozici** ve větné formě na druhé pásce.
3. **Nedeterministicky vybere pravidlo** z $G$.
4. Ověří, zda lze pravidlo na vybraném místě aplikovat; pokud ano, aplikuje ho.
5. Porovná větnou formu s $w$; při shodě **přijme**, jinak zpět na krok 2.


> [!info]
> **Věta 13.** Je-li $L$ _rozpoznatelný_, pak **existuje gramatika** $G$ typu 0 s $L(G) = L$.

- Gramatika odvozováním **simuluje kroky TS**.

#### _Důkaz (nečtu)_

Nechť $L = L(M)$ pro $M = (Q, \Sigma, \Gamma, \delta, q_0, F)$. Sestavíme gramatiku, jejíž **odvozování simuluje kroky TS** — větná forma zhruba odpovídá konfiguraci stroje. Terminály $= \Sigma$. Neterminály:

$N = (\Sigma \cup \set{\varepsilon}) \times \Gamma \ \cup\ \set{A_1, A_2, A_3}\ \cup\ Q$

Ve složeném symbolu $[a, X]$ si první složka pamatuje **původní vstupní symbol** a druhá **aktuální obsah políčka pásky**. Symbol z $Q$ značí stav a jeho pozice ve větné formě značí pozici hlavy.

**a) Vygenerování počáteční konfigurace:**

$A_1 \to q_0 A_2 \qquad A_2 \to [a,a]A_2 \ (\forall a \in \Sigma) \qquad A_2 \to A_3 \qquad A_3 \to [\varepsilon, \sqcup]A_3 \qquad A_3 \to \varepsilon$

Pro vstup $w = w_1\dots w_n$ se odvodí větná forma $q_0[w_1,w_1][w_2,w_2]\dots[w_n,w_n][\varepsilon,\sqcup]\dots[\varepsilon,\sqcup]$ kde poslední pravidlo _„nafoukne"_ tolik prázdné pásky, kolik bude přijímající výpočet potřebovat. _(Gramatika si množství pásky hádá dopředu — to je v pořádku, generuje-li se nedeterministicky.)_

**b) Simulace výpočtu:**

$q[a,X] \to [a,Y]q' \quad \text{pro } \delta(q,X)=(q',Y,\text{right})$  
$[b,Z],q,[a,X] \to q',[b,Z],[a,Y] \quad \text{pro } \delta(q,X)=(q',Y,\text{left})$

(Předpokládáme, že se stroj nepokusí jít doleva z prvního políčka — to lze vždy zařídit.)

**c) Úklid — odvození přijímaného slova:**

$[a,X]q \to qaq, \qquad q[a,X] \to qaq \quad (a \in \Sigma \cup {\varepsilon},\ X \in \Gamma,\ q \in Q)$  
$q \to \varepsilon \quad \text{pouze pro } q = q_{accept}$

Složené symboly se _„rozpustí"_ a nechají za sebou původní vstupní písmena. Stavové symboly zmizí **jen tehdy, je-li stav přijímající**. Čistě terminální větná forma tedy vznikne **právě když** $M$ příslušný řetězec přijal.

**Klíčová myšlenka k zapamatování:** první složka složeného symbolu je _paměť původního vstupu_ — pásku stroj přepisuje, ale gramatika musí nakonec vygenerovat původní slovo, ne obsah pásky na konci výpočtu.


## 3.1 Závěr

$\text{gramatika typu 0} = \text{částečně rekurzivní (RE) jazyky}$

---

# 4. Lineárně omezený automat a kontextové gramatiky

> [!success]
> **Lineárně omezený automat (LBA)** je nedeterministický TS, kde:
>
> - pásková abeceda obsahuje speciální **zarážky** $\rhd$ a $\lhd$ (nepatří do $\Sigma$) označující začátek a konec pásky,
> - stroj je **nesmí přepsat**,
> - na políčku s $\rhd$ se nesmí posunout doleva, na políčku s $\lhd$ doprava.
>
> $L(A) = \set{x \in \Sigma^* \mid \rhd x \lhd \ \vdash^*\ w,q_{accept},w' \text{ pro nějaká } w, w'}$

> [!note]
> **Intuice:** LBA je TS, který smí použít **přesně tolik pásky, kolik je dlouhý vstup** (odtud _„lineárně omezený"_).  
> Je to přesně nedeterministický stroj pracující v prostoru $O(n)$, tedy $\mathrm{NSPACE}(n)$.

> [!info]
> **Věta 14.** Pro každou kontextově závislou gramatiku $G$ existuje LBA $A$ s $L(G) = L(A)$.

#### _Důkaz_ _(analogie Věty 12, dvě technické překážky)__:_

1. **Nemáme dvě pásky** → Vyřešíme pomocí dobře zvolené páskové abecedy:  
  Ve dvojici $[a, K]$ je $a$ _„na první pásce"_ (původní vstup),$K$ _„na druhé pásce"_ (aktuální větná forma).  
  Práce se dvěma páskami se tak simuluje prací s _„dvoupáskovými"_ symboly.
2. **Máme jen** $n$ **políček** → nevadí, protože $G$ je **nezkracující**: žádná větná forma vedoucí k odvození řetězce délky $n$ nemůže být delší než $n$. Zjistí-li větev výpočtu, že by potřebovala víc místa, **zamítne**.

Na začátku LBA upraví pásku na $\rhd,[w_1, S],[w_2, \sqcup]\ \dots\ [w_n, \sqcup],\lhd$ a dále nedeterministicky vybírá pozici a pravidlo, aplikuje, a při shodě „druhé pásky" s „první" přijímá.


> [!info]
> **Věta 15.** Pro každý LBA $A$ existuje kontextově závislá gramatika $G$ s $L(A) - {\varepsilon} = L(G)$.

#### _Důkaz:_ (analogicky Větě 13 simulace výpočtu odvozováním).

Technické problémy navíc:

- symboly $\rhd$,$\lhd$ a symbol aktuálního stavu je nutné **zapracovat do složených symbolů** — cílová gramatika musí zůstat **nezkracující**, takže nesmíme použít mazací pravidla typu $q \to \varepsilon$ z Věty 13, ale musíme stav _„vstřebat"_ do sousedního složeného symbolu.
- **Rozdíl** $-{\varepsilon}$ není kosmetika: nezkracující gramatika nikdy neodvodí $\varepsilon$, zatímco LBA prázdné slovo přijmout může.


## 4.1 Závěr

$\text{gramatika typu 1 (kontextové)} = \text{jazyky přijímané LBA} = \mathrm{NSPACE}(n) \text{ (až na } \varepsilon)$

---

# 5. Kontextové vs. rozhodnutelné jazyky

> [!info]
> **Věta 16.** Pro každou kontextově závislou gramatiku $G$ je $L(G)$ **rozhodnutelný**.

- Sestavím **graf všech větných forem délky nejvýše** $n$ (je jich konečně mnoho, protože gramatika nezkracuje) a ověřím, jestli z $S$ vede cesta do $x$. Konečný graf → dosažitelnost umím rozhodnout.

#### _Důkaz_

Rozhodující TS pro vstup $x$ délky $n$ sestaví graf větných forem:

- **vrcholy** = všechny větné formy $G$ délky **nejvýše** $n$ (jejich počet je konečný, nanejvýš $\lvert N \cup \Sigma\rvert^{n+1}$ — proto konstrukce končí),
- **hrana** $\alpha \to \beta$, právě když $\alpha \vdash \beta$,
- TS ověří **existenci cesty ze** $S$ **do** $x$ (např. tranzitivním uzávěrem / BFS — dosažitelnost v konečném grafu je rozhodnutelná).


> [!info]
> **Věta 17.** Existuje rozhodnutelný jazyk $L$ takový, že pro každou kontextově závislou gramatiku $G$ platí $L \neq L(G)$.

- **Existuje rozhodnutelný jazyk, který kontextový není.**  
  _Diagonalizace:_ kontextových gramatik je spočetně mnoho, tak vezmu $L = \{x_i \mid x_i \notin L(G_i)\}$. Ten se _liší od každé gramatiky_, a _přesto je rozhodnutelný_.

#### _Důkaz (opět diagonalizace, ale konstruktivní):_

1. Každá kontextově závislá gramatika je konečný objekt, existuje její zakódování $\langle G \rangle$ a TS umí o řetězci rozhodnout, zda gramatiku kóduje. Kontextově závislých gramatik je tedy **spočetně mnoho**:$G_1, G_2, \dots$ Podobně máme enumeraci všech řetězců $x_1, x_2, \dots$
2. Definujeme $L = {x_i \mid x_i \notin L(G_i)}$— **doplněk diagonály**.
3. Pro každé $i$ se $L$ liší od $L(G_i)$ v řetězci $x_i$, takže $L$ **není** kontextový.
4. $L$ je přitom **rozhodnutelný**: TS pro vstup $x$ (1) najde index $i$ s $x = x_i$ (enumerátor pro $\Sigma^*$), (2) vygeneruje $\langle G_i \rangle$ (enumerátor gramatik), (3) rozhodne $x_i \in L(G_i)$ postupem z Věty 16 a odpoví **opačně**.

Krok (3) je možný **jen díky Větě 16** — diagonalizace potřebuje, aby testování příslušnosti bylo rozhodnutelné. Právě proto stejný trik nefunguje proti RE (nemohli bychom v kroku (3) vždy zastavit) a proto $\mathrm{R} \subsetneq \mathrm{RE}$ musíme dokazovat jinak — přes $A_{TM}$.


## 5.1 Závěr

$\text{CS} \subsetneq \text{R} \subsetneq \text{RE} = \text{typ 0}$