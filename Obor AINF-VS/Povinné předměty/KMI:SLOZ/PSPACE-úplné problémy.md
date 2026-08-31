> [!success]
> Třída $\text{PSPACE}$ je množina všech jazyků rozhodnutelných **DTS s polynomiální prostorovou složitostí**.
>
> $$
> \text{PSPACE}=\bigcup_{k\gt0}\text{DSPACE}(n^k)
> $$

> [!note]
> Jinými slovy, jazyk patří do $\text{PSPACE}$ právě tehdy, když _existuje DTS_, který jej rozhoduje a při výpočtu používá **nejvýše polynomiální množství pracovní paměti**.

> [!danger]
> Na rozdíl od časových tříd zde není _nijak omezen počet vykonaných kroků_. Algoritmus může běžet i **exponenciálně dlouho**, pokud během celého výpočtu nepřekročí povolenou velikost pracovní paměti.

---

# 1. PSPACE-úplný

> [!success]
> _Jazyk_ $L$ je **PSPACE-těžký**, jestliže na něj lze _v polynomiálním čase_ převést **každý jazyk** z třídy $\text{PSPACE}$
>
> $$
> ∀L' \in \text{PSPACE}:\qquad L' \leq_p L
> $$

> [!note]
> **Intuitivně**_:_ PSPACE-těžký problém je **alespoň tak obtížný** _jako všechny problémy z_ **PSPACE**.  
> Nemusí však _sám patřit do PSPACE_ ani být _rozhodnutelný_.

> [!success]
> Jazyk $L$ je **PSPACE-úplný**, pokud:
>
> - je **PSPACE-těžký**
> - **patří do třídy** $\text{PSPACE}$

> [!note]
> **Intuice:** PSPACE-úplné problémy jsou v jistém smyslu _„nejtěžší"_ v celé třídě PSPACE

---

# 2. Typické PSPACE-úplné problémy

## 2.1 TQBF (QBF)

> [!success]
> **Název:** QBF (Quantified Boolean Formula)
>
> **Vstup:** Formule tvaru $\varphi = (Q_1x_1)(Q_2x_2) … (Q_nx_n)\psi$
>
> - kde:
>   - $Q_i \in \set{\forall, ∃}$ jsou kvantifikátory
>   - $\psi$ je výroková formule v CNF nad proměnnými $x_1, …, x_n$
>
> **Otázka:** Je formule $\varphi$ pravdivá?

### 2.1.1 Speciální případy

- Jen **existenční** kvantifikátory:$(\exists x_1)\dots(\exists x_n)\psi$— to je $\text{SAT}$, tedy problém patří do **NP**.
- Jen **univerzální** kvantifikátory:$(\forall x_1)\dots(\forall x_n)\psi$— to je $\text{TAUTOLOGIE}$, tedy problém patří do **coNP**.

> [!info]
> **Věta:** $\text{QBF} \in \text{PSPACE}$

> [!warning]
> **Důkaz**:
>
> Sestavíme **alternující TS** pro vstup $(Q_1x_1)…(Q_nx_n)\psi$:
>
> 1. _Střídavě ohodnocuje proměnné_ $x_1, …, x_n$:
>   - Je-li $Q_i = \exists$→ **existenciální alternace** (stačí jedna větev přijmout)
>   - Je-li $Q_i = \forall$→ **univerzální alternace** (všechny větve musí přijmout)
> 2. Po dosazení všech hodnot **spočítá pravdivost** $\psi$ v polynomickém čase (deterministicky).
>
> _Časová složitost_ ATS **je polynomiální**.  
> **Protože** $\text{APTIME} = \text{PSPACE}$, dostaneme $\text{QBF} \in \text{PSPACE}$.

> [!info]
> **Věta:** $\text{QBF}$ je PSPACE-těžký

> [!warning]
> **Důkaz:**
>
> Vezmeme libovolný $L \in \text{PSPACE}$. Existuje ATS $M$ běžící v čase $m = n^k$ tak, že $L = L(M)$
>
> Předpokládáme (bez ztráty na obecnosti, lze dosáhnout úpravami):
>
> - Počáteční konfigurace je **existenciálně alternující**
> - Z každé nekoncové konfigurace vedou **právě dvě konfigurace** (pro popis true/false)
> - **Alternace se pravidelně střídají**.
>
> _Analogií Cook-Levinovi věty,_ kdy pro vstup $x$:
>
> 1. Vytvoříme formuli $\psi$ nad proměnnými $y_1, …, y_n$ (kde $y_i$ odpovídá volbě výpočetní větve při provádění i-tého kroku výpočtu) 
> 2. Vytvoříme formuli $\varphi = (\exists y_1)(\forall y_2)(\exists y_3)(\forall y_4) . . . (Q_my_m)\psi$, ve které se pravidelně střídají kvantifikátory
>
> Díky předpokladům o $M$ platí, že $\varphi$ je pravdivá, právě když $x \in L$.   
> Celá redukce je v polynomickém čase, protože $|\varphi|$ a tedy i m jsou polynomické k $|x|$.
>
> QBF je **PSPACE-úplný**

# 2.2 Generalized Geography (GG)

> [!success]
> **Název:** GG — zobecněná geografie (Generalized Geography)
>
> - Je hra hrána **dvěma hráči** na **orientovaném** _grafu_ $G$, začínající v **uzlu** $b$.
> - **Vstup**:
>   - orientovaný graf $G=(V,E)$,
>   - počáteční vrchol $b$.
> - _Průběh hry_: 
>   - Existuje **jeden token**, který je _na začátku_ hry **v uzlu** $b$.
>   - Hráči se **střídají v tazích**, _začíná hráč_ $p_0$. 
>   - V jednom tahu hráč přesune token _po hraně do sousedního_, ve hře **dosud nenavštíveného uzlu**. Pokud takový **uzel neexistuje**, _hráč, který je na tahu_ **prohrává**.
>
> **Otázka: _Má první hráč_** $(p_0)$ **_vítěznou strategii?_**

> [!note]
> Všimněme si, že každá hra má **nejvýše tolik tahů**, **kolik je vrcholů** v grafu $G$.

> [!warning]
> **Konfigurace hry** je trojice $(A, p, x)$, kde
>
> - $A$ je množina _dosud navštívených uzlů_,
> - $p \in \set{p_0, p_1}$ je _hráč na tahu_,
> - $x$ je _uzel_, kde je _token_ právě teď.
>
> Z _konfigurace_ $(A, p, x)$ hra **jedním tahem přejde** do _konfigurace_ $(B, q, y)$, značíme $(A, p, x) ⊢ (B, q, y)$ pokud:
>
> - $y \notin A$ je soused $x$
> - $B = A ∪ {x}$
> - $q = p \quad (\text{kde }p_0=p_1, p_1=p_0)$
>
> **Predikát** $\text{WIN}(p', (A, p, x))$, který je pravdivý pokud:
>
> - $p' = p$ a **existuje konfigurace** $(B, q, y)$ taková, že $(A, p, x) ⊢ (B, q, y)$ a $WIN(p', (B, q, y))$ je pravdivý.
> - $p' \ne p$ a pro **každou konfiguraci** $(B, q, y)$ takovou, že $(A, p, x) ⊢ (B, q, y)$ je predikát $\text{WIN}(p', (B, q, y))$ pravdivý.
>
> Zavedeme jazyk $\text{GG} = \set{(G, b) | \text{WIN}(p_0, (\empty,p_0,b)) \text{ je pravdivý}}$

> [!info]
> **Věta:** GG je PSPACE-úplný

> [!warning]
> **Důkaz**:
>
> 1. $\text{GG} \in \text{PSPACE}$
>   - Během hry si stačí pamatovat:
>
>     - aktuální vrchol,
>     - které vrcholy již byly navštíveny,
>     - kdo je na tahu.
>
>     To vše zabírá pouze **polynomiální prostor** vzhledem k velikosti grafu.
> 2. $\mathrm{QBF} \leq_p \mathrm{GG}$— GG je PSPACE-těžký
>
>   - Lze na něj polynomiálně převést problém **QBF (TQBF)**. Myšlenkou redukce je vytvořit graf, ve kterém:
>     - **existenční** kvantifikátory odpovídají tahům **prvního** hráče,
>     - **univerzální** kvantifikátory odpovídají tahům **druhého** hráče,
>     - struktura grafu simuluje vyhodnocování kvantifikované formule.
>
>   Proto platí, že první hráč má vítěznou strategii právě tehdy, když je daná QBF formule pravdivá.
>
> _Příklad_:
>
> $(\exists x_1)(\forall x_2)(\exists x_3)(\forall x_4)(x_1 \lor x_2 \lor \neg x_3) \land (\neg x_1 \lor x_3 \lor \neg x_4)$
>
> ![[019fe338-72c8-722c-91a8-eff383768a25.png]]

---

# 3. Další PSPACE-úplné problémy

- **Ekvivalence nedeterministických konečných automatů (NFA):**Jsou jazyky $L(A₁)$ a $L(A₂)$ totožné?
- **Ekvivalence regulárních výrazů:**Popisují dva regulární výrazy stejný jazyk?
- **Minimalizace NFA:**Je daný NFA minimální?
- **Vítězná strategie v zobecněné dámě (Generalized Checkers / Chess):**
  - Varianty deskových her na $n\times n$ desce jsou PSPACE-úplné.
  - Klíčový rys: oba hráči alternují tahy → přirozená korespondence s střídajícími se kvantifikátory.