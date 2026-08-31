> [!success]
> Třída $\text{PTIME}$ (Polynomial Time), značená také $\text P$, je _množina všech jazyků rozhodnutelnýc_h **DTS** **v polynomiálním čase**.
>
> $$
> \text{P} = \bigcup_{k \gt 0} \text{DTIME}(n^k)
> $$

> [!note]
> To znamená, že jazyk patří do $\text P$ právě tehdy, když _existuje TS_, který jej **rozhodne v čase** $O(n^k)$ _pro nějaké_ $k$

---

# 1. Log-space redukce $≤_{m}^{\log}$

> [!danger]
> **Proč nemůžeme použít polynomickou redukci?**
>
> Pak by byl každý problém z $\text P$ redukovatelný na libovolný netriviální problém z $\text P$  
> (Netriviální = problém může vrátit odpověď ano i ne)
>
> 1. Nejprve bychom problém vyřešili v polynomiálním čase
> 2. Podle výsledku vrátili jednu ze dvou pevných instancí cílového problému.
>
> Pak by byl téměř každý netriviální problém v P „P-úplný“ → proto se **používá log-space redukce**

> [!warning]
> _Log-space transducer_ je TS pracující v **logaritmickém prostoru**, který je navíc vybaven **výstupní páskou**, jež je **pouze pro zápis**.
>
> Poté, co zapíše na políčko této pásky symbol, posune zapisovací hlavu **doprava** a nikdy ji nemůže posunout doleva (co je jednou zapsáno, už nejde přepsat).

> [!note]
> **Intuice:** Výstup redukce může být **polynomiálně velký** (např. graf konfigurací TS). Kdyby se výstup počítal do paměti, žádná zajímavá redukce by se do $\log n$ nevešla.

> [!warning]
> Funkce $f : \Sigma^* \to \Sigma^*$ je **vyčíslitelná v logaritmickém prostoru**, pokud _existuje log-space transducer_, který pro vstup $x$ zastaví _a na výstupní pásce zůstane_ $f(x)$.

> [!success]
> Jazyk $A$ je **redukovatelný v logaritmickém prostoru** na jazyk $B,$ značeno:
>
> $$
> A \leq_{m}^{\log} B,
> $$
>
> pokud _existuje_ funkce $f$ _vyčíslitelná v logaritmickém prostoru_ taková, že
>
> $$
> x \in A \Lrarr f(x) \in B.
> $$

---

# 2. PTIME-úplnost

> [!success]
> _Jazyk_ $L$ je **PTIME-těžký**, jestliže na něj lze _v logaritmickém prostoru_ převést **každý jazyk** z třídy $\text{P}$
>
> $$
> ∀L' \in \text{P}:\qquad L' \leq_{m}^{\log} L
> $$

> [!note]
> **Intuitivně**_:_ PTIME-těžký problém je **alespoň tak obtížný** _jako všechny problémy z_ **PTIME**.  
> Nemusí však _sám patřit do PTIME_ ani být _rozhodnutelný_.

> [!success]
> Jazyk $L$ je **PTIME-úplný**, pokud:
>
> - je **PTIME-těžký**
> - **patří do třídy** $\text{PTIME}$

> [!note]
> P**TIME-úplné problémy** představují **nejtěžší sekvenční problémy**, které jsou _stále řešitelné v polynomiálním čase_.

> [!info]
> Pokud bychom pro některý z nich _našli velmi efektivní paralelní algoritmus_ (např. v NC), pak by jej díky logaritmicko-prostorovým redukcím _měly všechny problémy z P_.
>
> Proto jsou PTIME-úplné problémy důležité při studiu **paralelizovatelnosti algoritmů**.

---

# 3. Vztah k $\text{NC}$

> [!info]
> Platí:
>
> $$
> \text{NC} \sube \text P
> $$
>
> Není známo, zda
>
> $$
> \text{NC}= \text P \quad \text{nebo} \quad \text{NC}\neq \text P
> $$

> [!note]
> Kdyby $\text{NC}= \text P$
>
> - Každý algoritmus, který dnes umíme řešit v polynomiálním čase, lze také efektivně paralelizovat.
> - Například by bylo možné velmi efektivně paralelizovat:
>   - kompilaci programů,
>   - optimalizační algoritmy v překladačích,
>   - databázové dotazy
>
> Kdyby $\text{NC}\neq \text P$
>
> - To by znamenalo, že existuje **zásadní hranice paralelizace**. Některé výpočty jsou ze své podstaty sekvenční.

---

# 4. CIRCUIT-VALUE

> [!success]
> **Název: CIRCUIT-VALUE**
>
> **Vstup**: Booleovský obvod **bez proměnných** (vstupní brány mají label 0 nebo 1)
>
> **Výstup**: Je obvod pravdivý?

> [!info]
> **Věta:** $\text{CIRCUIT-VALUE}$ je P-úplný.

> [!warning]
> Důkaz:
>
> 1. $\text{CIRCUIT-VALUE} \in P$
>   - Stačí projít brány v topologickém pořadí a spočítat jejich hodnoty.
>   - Časová složitost je lineární vzhledem k velikosti obvodu.
> 2. $\text{CIRCUIT-VALUE}$ je PTIME-těžký
>   - Nechť $L\in P$. Existuje tedy TS $M$, který rozhoduje $L$ v polynomiálním čase.Pro libovolný vstup $x$ _lze v logaritmickém prostoru sestrojit Booleovský obvod_ $C^{x}$, který **simuluje výpočet** stroje $M$ na vstupu $x$. Jednotlivé brány obvodu _reprezentují elementární kroky výpočtu_ a jejich _propojení odpovídá přechodům_ mezi konfiguracemi TS.
>   - Obvod je zkonstruován tak, že jeho výstup má hodnotu 1 právě tehdy, když stroj $M$ přijme vstup $x$.

---

# 5. HORN-SAT

> [!success]
> **Hornova formule** je formule _výrokové logiky v CNF_ taková, že v každé klauzuli je **nejvýše jeden pozitivní literál**.

> [!success]
> **Název**:$\text{HORN-SAT}$
>
> **Vstup**: Hornova formule
>
> **Otázka**: Existuje ohodnocení proměnných, které formuli splňuje?

> [!info]
> **Věta:** $\text{HORN-SAT}$ je P-úplný

> [!warning]
> Důkaz:
>
> $\text{HORN-SAT} \in \text P$
>
> - Algoritmus opakuje následující kroky:
>   1. Pokud $\varphi$ **neobsahuje klauzuli s jedním literálem** → _ohodnotíme_ **všechny proměnné na 0** a přijme.
>   2. Pokud $\varphi$ **obsahuje klauzule** $(x)$ **a** $(¬x)$ pro _nějakou proměnnou_ $x$→ **zamítá**.
>   3. Pokud $\varphi$ **obsahuje klauzuli** $(l)$ _s jedním literálem_ → ohodnotíme příslušnou proměnnou tak, aby $l$ **byl pravdivý**. _Odstraníme klauzuli_ $(l)$ a ze _zbývajících klauzulí odstraníme literá_l $(¬l)$.
> - Algoritmus **pracuje v polynomiálním čase** (v každé iteraci ubude proměnná).
>
> $\text{HORN-SAT}$ je PTIME-těžký
>
> - Ukážeme $\text{CIRCUIT-VALUE} \le^{\log}_m \text{HORN-SAT}$
>
>   1. Víme, že **MCVP je PTIME-úplný**.
>   2. Každé hradlo AND nahradíme klauzulí
>
>   $$
>   (\neg x \lor \neg y \lor z).
>   $$
>
>   3. Každé hradlo OR nahradíme dvěma klauzulemi
>
>   $$
>   (\neg x \lor z),(\neg y \lor z).
>   $$
>   4. Vstupy s hodnotou 1 zapíšeme jako jednotkové klauzule.
>   5. Přidáme jednotkovou klauzuli pro výstup.
>   6. Vznikne Hornova formule splnitelná právě tehdy, když výstup obvodu je 1.

**Důkaz P-těžkosti** — ukážeme `CIRCUIT-VALUE ≤log HORN-SAT`:

- Pro daný obvod $C$ (bez proměnných) vytvoříme Hornovu formuli $\varphi$.
- Pro každou bránu $g$ zavedeme dvě proměnné:$g⁺$ (brána je pravdivá) a $g⁻$ (brána je nepravdivá).
- Přidáme klauzuli $(¬g⁺ ∨ ¬g⁻)$ vylučující, aby byly obě pravdivé zároveň.
- Pro každý typ brány přidáme hornovské klauzule vyjadřující správný výpočet:
  - Brána s labelem 1: klauzule $(g⁺)$
  - Brána s labelem 0: klauzule $(g⁻)$
  - Brána OR $(h₁ ∨ h₂)$:$(g⁺ ∨ ¬h₁⁺)$,$(g⁺ ∨ ¬h₂⁺)$,$(g⁻ ∨ ¬h₁⁻ ∨ ¬h₂⁻)$ — každá je hornová
  - Analogicky pro AND, NOT.
- Celá konstrukce jde provést log-space transducerem.
- $\varphi$ je splnitelná právě tehdy, když je výstupní brána $C$ pravdivá.

**Praktický dopad**: HORN-SAT je důležitý v logickém programování (Prolog, Datalog) a databázové teorii — jeho P-úplnost říká, že vyhodnocení hornových klauzulí je sekvenčně přirozené, ale paralelizovat ho není snadné.

- 
- Přirozenou otázkou je: jsou všechny problémy z $P$ také **efektivně paralelizovatelné**? Tj. platí $P ⊆ NC$?
- **P-úplné problémy** jsou _„nejtěžší"_ problémy v $P$— pokud by bylo možné některý z nich vyřešit v $\text{NC}$ (paralelně efektivně), pak by platilo $P = \text{NC}$.
- P-úplnost tedy charakterizuje problémy, u nichž se předpokládá, že jsou **inherentně sekvenční** — nelze je výrazně zrychlit paralelismem.