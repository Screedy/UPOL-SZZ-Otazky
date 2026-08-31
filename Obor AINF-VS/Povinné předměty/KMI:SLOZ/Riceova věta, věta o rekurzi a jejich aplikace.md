> [!warning]
> **Many-one redukce** $A \leq_m B$
>
> - Existuje **vyčíslitelná** funkce $f$ taková, že $\forall x:\quad x \in A \iff f(x) \in B.$
> - **Intuice**: _Každou instanci problému_ $A$ pouze **přepočítáme** na _instanci problému_ $B$ a oba musí vrátit stejnou odpověď
> - **Důsledek**:
>   - Jestli $B$ je (částečně) rozhodnutelný →$A$ je (částečně) rozhodnutelný
>   - Jestli $A$ je (částečně) nerozhodnutelný →$B$ je (částečně) nerozhodnutelný
>
> **Oracle pro jazyk** $L$ je externí zařízení, které _umí rozhodnout jazyk_.
>
> **Turingova redukce** $A \leq_T B$
>
> - Existuje oracle TS s oracle pro B $(M^B)$, který rozhoduje $A$.
> - **Intuice**: Řešení problému $A$ umíme postavit za předpokladu, že máme _„kouzelnou černou skříňku"_ řešící $B$.
> - **Důsledek**:
>   - Jestli $B$ je rozhodnutelný →$A$ je rozhodnutelný
>   - Jestli $A$ je nerozhodnutelné →$B$ je nerozhodnutelné.
>   - ==Neplatí pro rozpoznatelnost!!== (částečně rozhodnutelný)

> [!info]
> Platí $A \leq_m B \Rightarrow A \leq_T B$.

---

# 2. Věta o rekurzi

- Zabývá se otázkou, zda může _Turingův stroj během svého výpočtu_ **_pracovat se svým vlastním zakódováním_**. Běžný Turingův stroj **svůj vlastní popis nezná** – po spuštění má _k dispozici pouze vstup_.

> [!note]
> **Intuice:** Věta o rekurzi však ukazuje, že **pro libovolný Turingův stroj** $T$ **lze sestrojit nový Turingův stroj** $R$**, který při svém výpočtu automaticky předá stroji** $T$ **své vlastní zakódování** $⟨R⟩$.

- Aby bylo možné takový stroj sestrojit, je nejprve potřeba zavést několik pomocných konstrukcí.

## 2.1 Pomocné Turingovy stroje

- Pro každé $x \in \Sigma^*$ existují:

| Stroj | Vstup | Co udělá |
| --- | --- | --- |
| $\text{PRINT} [x]$ | $w$ | Smaže $w$, zapíše na pásku $x$, hlavu nastaví na první políčko |
| $\text{PRINTSKIP}[x]$ | $w$ | **Nesmaže** $w$, zapíše $x$ **za** něj, hlavu nastaví na první znak $w$ |
| $\text{MACRO}$ | $x$ | Zapíše na pásku $\langle \text{PRINT}[x]\rangle$ |
| $\text{MACROSKIP}$ | $x$ | Zapíše na pásku $\langle \text{PRINTSKIP}[x]\rangle$ |

- Další potřebnou konstrukcí je možnost _spojit dva Turingovy stroje do jednoho_.
  - Pro TS $A, B$ značíme $A \to B$ stroj, který:
    1. Provede $A$ na vstupu $x$,
    2. Jakmile $A$ zastaví, pokračuje výpočtem $B$, přičemž **zdědí obsah pásky i pozici hlavy**.

## 2.2 Konstrukce stroje $\text{SELF}$

- Než přejdeme _k vlastní větě o rekurzi_, ukážeme si _jednodušší konstrukci_ stroje **SELF**, jehož úkolem je **pro libovolný vstup vytisknout své vlastní zakódování**.

- Toho dosáhneme _pomocí dvou pomocných strojů_ $A$ a $B$.
  - TS $A$, který **pro jakýkoliv vstup** $w$:
    1. Provede $\text{PRINT}[<B>]$
  - TS $B$, který obecně pro vstup $<M>$ udělá: (později bude $<B>$)
    1. Spustí $\text{MACRO}$ pro $<M>$, potom má na pásce $<\text{PRINT}[<M>]>$
    2. Sestaví TS (spojí dohromady) z _popisu TS na_ **_vstupu_** a _z popisu_ **z kroku 1**. _Popis tohoto TS vypíše_. (Na pásce bude $<\text{PRINT}[<M>] → M>$)

- **Co se stane při běhu TS** $A$ **→** $B$**, tedy TS** $\text{PRINT}[<B>] → B$**?**
  1. $\text{PRINT}[\langle B\rangle]$ zapíše na pásku $\langle B\rangle$.
  2. Spustí se $B$ se vstupem $\langle B\rangle$→ z bodu 1 jeho definice má $\langle \text{PRINT}[\langle B\rangle]\rangle$,
  3. → z bodu 2 sestaví $\langle \text{PRINT}[\langle B\rangle] \to B \rangle = \langle \text{SELF}\rangle$.
- Na pásce **zůstal vlastní popis**.

> [!note]
> **Intuice**_:_
>
> - Stroj se skládá ze **dvou půlek**: první půlka („data“) obsahuje popis druhé půlky
> - Druhá půlka („kód“) umí z dat zrekonstruovat popis první půlky (protože první půlka je jen tiskárna těch dat) a slepit obojí.

> [!danger]
> Tato konstrukce však zatím **neumí zpracovávat běžný vstup**. Proto ji _mírně upravíme a získáme obecnou větu o rekurzi_.

## 2.3 Věta o rekurzi

> [!info]
> **Věta (o rekurzi).**  
> Nechť $T$ je TS vyčíslující funkci $t : \Sigma^* \times \Sigma^* \to \Sigma^*$_. Potom existuje TS_ $R$ _vyčíslující funkci_ $r : \Sigma^* \to \Sigma^*$ _tak, že pro všechna_ $w \in \Sigma^*$ platí $r(w) = t(w, \langle R\rangle).$

> [!note]
> **Intuice / jak se věta používá v praxi:** _„Při konstrukci Turingova stroje si smím do popisu napsat řádek_ **_‚získej_** $\langle$ **_vlastní popis_** $\rangle$ **_‘_** _a dál s ním pracovat jako s jakýmkoli jiným řetězcem.“_

### **2.3.1 Důkaz**

(drobná úprava konstrukce $\text{SELF}$, aby přežil vstup)

- TS $A$, který pro jakýkoliv vstup $w$:
  1. Provede $\text{PRINTSKIP}[<B→T>]$
- TS $B$, který obecně pro vstup $w<M>$ udělá: (později bude $<B→T>$)
  1. Spustí $\text{MACROSKIP}$ pro $<M>$, potom má na pásce $<\text{PRINTSKIP}[<M>]>$
  2. Sestaví TS (spojí dohromady) z popisu TS na vstupu a z popisu z kroku 1. Popis tohoto TS vypíše. (Na pásce bude $w<\text{PRINTSKIP}[<M>] → M>$)

- **Co dělá náš stroj** $R$ **je** $\text{PRINTSKIP}[<B→T>] → (B→T)$ **pro vstup** $w$**?**
  - Zavolá se $\text{PRINTSKIP}[<B→T>]$, na pásce bude $w<B→T>$
  - (Zbývá vykonat $B→T$)
  - Vykoná se $B$, na pásce bude $w<\text{PRINTSKIP}[<B→T>]→(B→T)>$
  - (Zbývá vykonat $T$)
  - Pro vstup $w$ je v momentě, kdy spouštíme $T$ na pásce $w<R>$

---

# 3. Aplikace věty o rekurzi

> [!info]
> Jakmile program _zná svůj vlastní kód, může dělat věci jako_:
>
> - **zjistit délku** svého programu,
> - vytisknout svůj program,
> - **vytvořit svou kopii**,
> - rozhodovat podle svého vlastního popisu.

### 3.1 Důkaz nerozhodnutelnosti $A_{TM}$

- Předpokládejme sporem TS $H$ rozhodující $A_{TM}$. Sestrojíme TS $B$, který pro vstup $w$:
  1. **Získá svůj vlastní popis** $\langle B\rangle$ (věta o rekurzi),
  2. Spustí $H$ na $(\langle B\rangle, w)$,
  3. Udělá **opak** — pokud $H$ přijme,$B$ zamítne; pokud $H$ zamítne,$B$ přijme.
- Pak pro každé $w$:$B$ přijímá$w$$\iff $ $ H $říká, že$ B $nepřijímá$ w$. **Spor**.

## 3.2 $MIN_{TM}$ není rozpoznatelný

> [!success]
> TS $M$ je **minimální**, pokud neexistuje ekvivalentní TS $N$ (přijímá a zamítá stejně) s **kratším zakódováním**.
>
> Položme $MIN_{TM} = \set{\langle M\rangle \mid M \text{ je minimální}}.$

> [!info]
> **Věta:** $MIN_{TM}$ **není rozpoznatelný**.

#### **Důkaz**

Kdyby byl $MIN_{TM}$ rozpoznatelný, existuje enumerátor $E$ s $L(E) = MIN_{TM}$. Sestrojíme TS $C$, který pro vstup $x$:

1. **Zjistí délku svého vlastního zakódování** $|\langle C\rangle|$ (věta o rekurzi),
2. Simuluje $E$, dokud nevytiskne nějaké $\langle D\rangle$ s $|\langle D\rangle| > |\langle C\rangle|$,
3. Simuluje $D$ na $x$ a “chová se stejně”.

Protože $MIN_{TM}$ je **nekonečná** množina, takové $\langle D\rangle$ se dřív nebo později objeví, takže krok 2 skončí. Pak je ale $C$ ekvivalentní $D$ a přitom $|\langle C\rangle| < |\langle D\rangle|$—$D$ tedy není minimální, spor s $\langle D\rangle \in MIN_{TM}$. ∎


---

# 4. Riceova věta

> [!note]
> **Intuice**: Jejím hlavním smyslem je určit, **které otázky o TS nelze algoritmicky rozhodnout**. Nezabývá se však vlastnostmi samotných TS, ale vlastnostmi **jazyků**, které tyto stroje rozpoznávají.

## 4.1 Vlastnost rozpoznatelných jazyků

- Aby bylo možné Riceovu větu formulovat, je nejprve potřeba definovat pojem **vlastnost rozpoznatelných jazyků**.

> [!success]
> Uvažme **zobrazení** $P : \Sigma^* \to \set{0,1}$.
>
> Řekneme, že $P$ je **vlastnost rozpoznatelných jazyků**, pokud pro _libovolné dva TS_ $M_1, M_2$ platí:
>
> $$
> L(M_1) = L(M_2) \quad \Longrightarrow \quad P(\langle M_1\rangle) = P(\langle M_2\rangle).
> $$

> [!note]
> **Intuice**: Pokud dva různé Turingovy stroje rozpoznávají stejný jazyk, musí mít vůči této vlastnosti stejnou hodnotu.

> [!success]
> Vlastnost $P$ je **netriviální**, pokud existují $M_1,M_2$ tak, že $P(\langle M_1 \rangle) \neq P(\langle M_2 \rangle)$

**Příklady:**

| Otázka | Je to vlastnost jazyků? | Netriviální? |
| --- | --- | --- |
| „Přijímá $M$ konečný jazyk?“ | ✅ ano | ✅ ano |
| „Je $L(M) = \emptyset$?“ | ✅ ano | ✅ ano |
| „Je $L(M)$ regulární?“ | ✅ ano | ✅ ano |
| „Přijímá $M$ slovo $011$?“ | ✅ ano | ✅ ano |
| **„Má** $M$ **méně než 100 stavů?“** | ❌ **ne** — ke každému stroji lze vyrobit ekvivalentní stroj s víc stavy | —   |
| **„Zastaví** $M$ **na každém vstupu?“** | ❌ **ne** — dva stroje se stejným jazykem se mohou lišit v tom, zda mimo jazyk cyklí, nebo zamítají | —   |
| „Je $L(M)$ rozpoznatelný?“ | ✅ ano, ale **triviální** (vždy 1) | ❌ ne |

> [!info]
> **Věta (Riceova).** Nechť $P$ je **netriviální vlastnost rozpoznatelných jazyků**. Potom jazyk $L_P = \set{w \mid P(w) = 1}$ je **nerozhodnutelný.** (Potom jazyk $L_P$ je množina popisů TS, které mají vlastnost je nerozhodnutelný)

## 4.2 Důkaz z přednášky

#### Důkaz

1. Předpokládejme, že $P(\langle M_\emptyset\rangle) = 0$ pro každý stroj $M_\emptyset$ s $L(M_\emptyset) = \emptyset$. (Předpokládáme vlastnost, kterou nemají stroje, které přijímají prázdný jazyk)
2. Protože $P$ **je netriviální**, _existuje rozpoznatelný jazy_k $A$ takový, že pro **každý** TS $T$ s $L(T) = A$ máme $P(\langle T\rangle) = 1$.  
  Protože $A$ je _rozpoznatelný_, tak nějaký TS $M$ **musí existovat**.
3. Sestrojíme TS $R$, který pro vstup $(\langle M\rangle, w)$ vypíše popis stroje $M'$, kde $M'$ pro vstup $x$:
  1. Simuluje $M$ na $w$. Pokud $M$ **zamítne**,$M'$ zamítne,
  2. Simuluje $T$ na $x$ a chová se stejně jako $T$.
4. Vidíme, že:
  - Pokud $M$ přijímá $w$, poté $L(M’) = L(T)$, tedy $P(<M’>)=1$
  - Pokud $M$ zacyklí pro $w$ nebo zamítá $w$, pak $L(M’) = \varnothing$, tedy $P(<M’>)=0$

Tedy $(\langle M\rangle, w) \in A_{TM} \iff \langle M'\rangle \in L_P.$

> [!note]
> **Intuice**: Protože předpokládáme, že **jazyk** $A$ **vlastnost** $P$ **má, zatímco prázdný jazyk ji nemá**, stačí se _zeptat rozhodovacího algoritmu pro_ $L_P$, zda má stroj $M'$ vlastnost $P$. Jeho odpověď **nám přímo řekne, zda** $M$ **přijímá vstup** $w$**.** _Tím bychom rozhodli jazyk_ $A_{TM}$, což je **spor**. Proto žádný algoritmus rozhodující $L_P$ nemůže existovat.


## 4.3 Co Riceova věta **neříká**

- **Neříká nic o rozpoznatelnosti.** Riceova věta dává jen nerozhodnutelnost. Některé $L_P$ jsou rozpoznatelné (např.${\langle M\rangle \mid 011 \in L(M)}$— simuluj $M$ na $011$), jiné ne (např.$EMPTY$).
- **Neplatí pro jiné výpočetní modely s omezenou silou** — např. _„přijímá tento DFA prázdný jazyk?“_ je rozhodnutelné. Riceova věta stojí a padá s existencí univerzálního stroje a plnou Turingovskou silou.

## 4.4 Jak Riceovu větu používat

Při aplikaci Riceovy věty stačí vždy ověřit dvě podmínky:

1. Zda se jedná o **vlastnost rozpoznávaného jazyka**, nikoliv o vlastnost implementace Turingova stroje.
2. Zda je tato vlastnost **netriviální**, tedy existují jazyky, které ji mají, i jazyky, které ji nemají.

Jsou-li obě podmínky splněny, Riceova věta okamžitě říká, že daný problém je nerozhodnutelný.