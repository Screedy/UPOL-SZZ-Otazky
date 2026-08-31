- Abychom mohli porovnávat algoritmy z hlediska využité paměti, potřebujeme měřit množství paměti, které využívají během výpočtu. Tím se zabývá **paměťová složitost algoritmů**.

> [!success]
> **Paměťová složitost** **DTS** $M$ je funkce $S_M: \mathbb{N} \to \mathbb{N}$, kde $S_M(n)$ je _velikost potřebné paměti při výpočtu_ $M$ nad vstupem délky $n$ **v nejhorším případě** (worst case).
>
>
> Pro NTS jsou _definice analogické_.

- Prostorovou složitost formalizujeme pomocí tříd **DSPACE** a **NSPACE**, které omezují množství pracovní paměti použité deterministickým, resp. nedeterministickým Turingovým strojem.

- Formálně: pro funkci $f: \mathbb{N} \rightarrow \mathbb{N}$ definujeme třídy:
  - $\text{DSPACE}(f(n)) = \{ L(M)\ |\ M$ je DTS s paměťovou složitostí $O(f(n))\}$
  - $\text{NSPACE}(f(n))=\{ L(M)\ |\ M$ je NTS s paměťovou složitostí $O(f(n))\}$

> [!note]
> _Jak to správně říct_:
>
> Pro **paměťovou složitost** $S(n)$ definujeme $\text{DSPACE}(S(n))$ jako _množinu všech jazyků_ rozhodnutelných **deterministickým** Turingovým strojem, jehož _časová složitost_ je $O(S(n))$.

# 1. Model Turingova stroje pro paměťovou složitost

> [!info]
> Chceme mluvit _o paměťové složitosti_ $O(\log n)$. Jenže **samotný vstup má délku** $n$, takže na standardním jednopáskovém TS bychom si už jen přečtením vstupu _„utratili"_ $n$ buněk paměti.

- Používá se vícepáskový TS (resp. NTS):
  - **Vstupní páska**
    - _pouze pro čtení,_
    - její délka je $n$,
    - _nezapočítává se do paměti._
  - **Pracovní páska**
    - lze _číst i zapisovat_,
    - na začátku výpočtu je **prázdná,**
    - právě její velikost _měří paměťovou složitost_.
- To je _důležité_ u logaritmické paměti

> [!note]
> **Intuice:** Stroj s $O(\log n)$ pracovní pamětí si může pamatovat jen **konstantní počet ukazatelů/čítačů** do vstupu (každý zabere $O(\log n)$ bitů). **Nemůže** si zkopírovat vstup, nemůže si držet seznam navštívených vrcholů grafu, nemůže si pamatovat cestu.

---

# 2. Třídy L a NL

> [!success]
> $L$ je množina jazyků **rozhodnutelných DTS** _používajícím nejvýše_ $O(\log n)$ buněk _pracovní_ pásky.
>
> $$
> L = \text{DSPACE}(\log n)
> $$

- Příklady problémů v $L$:
  - $\text{DFA-ACCEPTANCE}$- konečný deterministický automat $D$ přijímá slovo $w$?
    - Stačí si pamatovat aktuální stav (číslo) a pozici čtecí hlavy.
  - $\text{UPATH}$- neorientovaný graf, uzly $s,t$. Existuje cesta z $s$ do $t$?

> [!success]
> $NL$ je množina jazyků **rozhodnutelných NTS** _používajícím nejvýše_ $O(\log n)$ buněk _pracovní_ pásky.
>
> $$
> NL = \text{NSPACE}(\log n)
> $$

> [!note]
> **Intuice:**
>
> _Stejná velikost_ paměti jako u $L$
>
> Rozdíl je pouze v tom, že stroj může v každém kroku **nedeterministicky vybírat jednu z více možností**.
>
> Stačí, aby **existovala jedna přijímající výpočetní větev**.

---

# 3. Problém $\text{PATH}$

> [!success]
> **Název:** $\text{PATH (ST-CONNECTIVITY)}$
>
> **Vstup:** $(G,s,t),$ kde $G$ je **orientovaný** graf, $s,t$ jsou jeho uzly.
>
> **Otázka:** Existuje v $G$ **orientovaná cesta** z $s$ do $t$?

> [!info]
> Věta: $\text{PATH} \in NL$

> [!note]
> **Intuice:** Dosažitelnost v orientovaném grafu lze rozhodnout _nedeterministickým TS_ v _logaritmickém prostoru_.

> [!warning]
> **Důkaz:**
>
> Sestavíme NTS $M$, který potřebuje pouze log. paměť. Vstup je $(G=(V,E),s,t).$
>
> 1. $M$ má na pracovní pásce zapsán **aktuální uzel** — na začátku tam zapíše $s$
> 2. Opakovaně **nedeterministicky vybere souseda** aktuálního uzlu a považuje ho za nový aktuální uzel.
> 3. Současně si na pásce **pamatuje počet provedených výběrů** (délku dosud _“ušlé”_ cesty).
> 4. Pokud je na pracovní pásce $t$, **přijímá**.
> 5. Pokud už provedl **tolik výběrů, kolik je uzlů v grafu**, **zamítá**.
>
> **Paměťová analýza:**
>
> - M reprezentuje uzly jako **čísla v binární soustavě** → na jeden uzel stačí $\lceil \log_2 |V| \rceil$ bitů.
> - Čítač počtu voleb _má hodnotu nejvýše_ $|V|$→ opět stačí $\lceil \log_2 |V| \rceil$ bitů.
> - Celkem:$O(\log n)$ pracovní paměti.

> [!info]
> **Poznámka (otevřená otázka):** Nevíme, zda $\text{PATH} \in L$.  
> **Zajímavě:** verze pro **neorientované grafy** $(\text{UPATH})$ v $L$ **je** — dokázal Reingold (2005).

> [!danger]
> **Proč čítač kroků?** Bez něj by stroj mohl **cyklit** v cyklu grafu a nikdy nezastavit. Pokud cesta z $s$ do $t$ existuje, existuje i cesta **jednoduchá**, ta má nejvýše $|V| - 1$ hran. Delší hledání je tedy zbytečné.
>
> **Proč to nejde deterministicky (zjevně)?** Deterministický průchod (BFS/DFS) potřebuje pole `visited` velikosti $|V|$, tedy **lineární** paměť. Nedeterministický stroj si _nic pamatovat nemusí_ — prostě **_„uhodne"_** správnou cestu krok za krokem.

---

# 4. Log-space redukce a NL-úplnost

> [!warning]
> _Log-space transducer_ je TS pracující v **logaritmickém prostoru**, který je navíc vybaven **výstupní páskou**, jež je **pouze pro zápis**.
>
> Poté, co zapíše na políčko této pásky symbol, posune zapisovací hlavu **doprava** a nikdy ji nemůže posunout doleva (co je jednou zapsáno, už nejde přepsat).

> [!note]
> **Intuice:** Výstup redukce může být **polynomiálně velký** (např. graf konfigurací TS). Kdyby se výstup počítal do paměti, žádná zajímavá redukce by se do $\log n$ nevešla.

> [!warning]
> Funkce $f : \Sigma^* \to \Sigma^*$ je **vyčíslitelná v logaritmickém prostoru**, pokud _existuje log-space transducer_, který pro vstup $x$ zastaví _a na výstupní pásce zůstane_ $f(x)$.

## 4.1 Log-space redukce $≤^{\log}_m$

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

> [!info]
> **Vztah k polynomiální redukci:**
>
> Pokud $A \leq_{m}^{\log} B$, pak $A \leq_p B$.
>
> - **Proč:** log-space transducer má nejvýše $2^{O(\log n)} = n^{O(1)}$ různých konfigurací, _takže pokud zastaví_, **běží polynomiálně dlouho**.
> - **Opačná implikace není známa.**

## 4.2 NL-těžkost a NL-úplnost

> [!success]
> _Jazyk_ $L$ je **NL-těžký**, jestliže na něj lze _v logaritmickém prostoru_ převést **každý jazyk** z třídy $\text{NL}$
>
> $$
> ∀L' \in \text{NL}:\qquad L' \leq_{m}^{\log} L
> $$

> [!note]
> **Intuitivně**_:_ NL-těžký problém je **alespoň tak obtížný** _jako všechny problémy z_ **NL**.  
> Nemusí však _sám patřit do NL_ ani být _rozhodnutelný_.

> [!success]
> Jazyk $L$ je **NL-úplný**, pokud:
>
> - je **NL-těžký**
> - **patří do třídy** $\text{NL}$

> [!info]
> **Věta.** PATH je NL-úplný.

> [!warning]
> **Důkaz:**
>
> Každý problém z NL lze převést na PATH pomocí **logaritmické redukce**.
>
> Nechť $A \in \text{NL}$ a $M$ je NTS rozhodující $A$ v logaritmické paměťové složitosti $s(n) \in O(\log n)$.
>
> Sestrojíme orientovaný graf konfigurací:
>
> - **vrcholy** představují konfigurace stroje,
> - **hrana** vede z konfigurace $c_1$ do $c_2$, pokud lze z $c_1$ přejít do $c_2$ jedním krokem.
>
> Potom platí:
>
> - $x \in A ⟺$ v $G$ existuje cesta z počáteční konfigurace do konfigurace $\text{ACCEPT} ⟺ (\text{G}, \text{ START}, \text{ ACCEPT}) \in \text{PATH}$.

---

# 5. Třída $\text{coNL}$

> [!success]
> Třída $\text{coNL}$ obsahuje doplňky jazyků třídy z $\text{NL}$
>
> $$
> \text{coNL} = \set{ L̄ | L ∈ NL }.
> $$
>
> kde
>
> $$
> \overline L=Σ^∗∖L
> $$
>
> je doplněk jazyka $L$

> [!info]
> **Název:** $\overline{\text{PATH}}$
>
> **Vstup:** $(G,s,t),$ kde $G$ je **orientovaný** graf, $s,t$ jsou jeho uzly.
>
> **Otázka:** **Neexistuje** v $G$ **orientovaná cesta** z $s$ do $t$?

## 5.1 Immermanova-Szelepcsényiho věta

> [!info]
> Pro každou prostorově zkonstruovatelnou funkci $s(n) ≥ \log n$ platí
>
> $$
> \text{NSPACE}(s(n)) = \text{coNSPACE}(s(n)).
> $$
>
> Speciálně potom
>
> $$
> \text{NL} = \text{coNL}.
> $$

> [!note]
> **Intuice:** Nedeterministické prostorové třídy jsou uzavřené na doplněk.

> [!warning]
> **Důkaz**:
>
> Nechť $L\in \text{coNSPACE}(s(n))$. Chceme dokázat, že $L\in \text{NSPACE}(s(n))$.  
> Nechť $M$ je NTS používající $O(s(n))$ paměti, který _rozhoduje doplněk jazyka_ $L$.
>
> **Vstup**: Pro _pevný vstup_ $x$ uvažujeme **graf konfigurací** stroje $M$. Vrcholy _grafu představují konfigurace stroje_ a _hrana vede z konfigurace_ $c_1$ do konfigurace $c_2$, pokud lze z $c_1$ _přejít jedním krokem výpočtu_.
>
> Protože $M$ _používá_ $O(s(n))$ paměti, má **graf konfigurací nejvýše** $2^{O(s(n))}$ _vrcholů_.  
> **Označíme** $R_i$ množinu konfigurací _dosažitelných z počáteční konfigurace nejvýše v_ $i$ _krocích_ a $c_i=|R_i|$
>
> **Na začátku** známe $c_0=1$, protože _dosažitelná je pouze_ **počáteční konfigurace**.  
> **Induktivně** předpokládáme, že _známe hodnotu_ $c_i$, a _chceme spočítat_ $c_i+1$.
>
> Postupně procházíme **všechny konfigurace grafu** a _pro každou ověřujeme_, zda patří do $R_i+1$. _Konfigurace patří_ do $R_i+1$, pokud **již patří** do $R_i$ nebo **má předchůdce** v $R_i$.
>
> Aby nedeterministický _stroj nemohl „hádat“ nesprávně_, **kontroluje** se, že _počet konfigurací označených jako dosažitelných_ z $R_i$ **je přesně** $c_i$. Pokud počet nesouhlasí, výpočet se **zamítne**.  
> Tím _lze korektně spočítat hodnotu_ $c_i+1$.
>
> Postup _opakujeme_, dokud nedojdeme **ke všem dosažitelným konfiguracím.** **Nejvýše** po $2^{O(s(n))}$ iteracích se _již množina dosažitelných konfigurací nemění._
>
> Nakonec **stačí ověřit**, zda je mezi _dosažitelnými konfiguracemi_ některá **přijímací konfigurace**.  
> Pokud _přijímací konfigurace dosažitelná není_, vstup **patří do jazyka** $L$; pokud _dosažitelná je_, vstup do $L$ **nepatří**.
>
> Algoritmus si po celou dobu **uchovává pouze** _několik čítačů_, _aktuální konfiguraci a hodnoty_ $c_i$, takže **spotřebuje pouze** $O(s(n))$ paměti.
>
> Tím jsme ukázali, že $\text{coNSPACE}(s(n)) \sube \text{NSPACE}(s(n))$. _Opačná inkluze se dokáže stejným argumentem_ po záměně jazyka za jeho doplněk.