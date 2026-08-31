# 1. Atributová gramatika

> [!success]
> **Atributová gramatika** je **rozšířením bezkontextové gramatiky** o sémantické informace. _Přidává k_ ní sémantické informace ve formě **atributů** a **sémantických pravidel**.
>
> _Formálně_:
>
> $$
> AG = (G, A, R)
> $$
>
> kde
>
> - $G = (N,T,P,S)$ je výchozí bezkontextová gramatika,
> - $A = \bigcup_{X \in N \cup T} A(X)$ je konečná množina atributů,
> - $R$ je konečná množina sémantických pravidel.

- Sémantická analýza pak spočívá **ve vyhodnocování atributů** **podle sémantických pravidel** _při průchodu derivačním stromem_.

## 1.1 Atributy

> [!success]
> Atribut představuje **sémantickou informaci přiřazenou symbolu gramatiky**.
>
> Je-li $X \in N \cup T$, označujeme _množinu atributů přiřazených symbolu_ $X$ jako
>
> $$
> A(X).
> $$
>
> _Jednotlivý atribut_ zapisujeme ve tvaru
>
> $$
> X.a,\qquad a \in A(X).
> $$

- Typickými atributy používanými při překladu jsou například:
  - datový typ výrazu (`typ`),
  - hodnota konstanty,
  - odkaz na položku v tabulce symbolů,
  - adresa proměnné nebo dočasného výsledku.
- Samotné atributy _uchovávají informace_. Jejich hodnoty _musí být vypočteny pomocí sémantických pravidel_.

> [!danger]
> **Podmínka jednoznačnosti:** V _každém derivačním stromu_ musí pro **každý atribut každého uzlu** existovat **nejvýše jedno sémantické pravidlo**, které _určuje jeho hodnotu_. Tím je zajištěno, že výsledek výpočtu atributů je jednoznačný.

## 1.2 Sémantická pravidla

> [!success]
> **Sémantická pravidla** určují _způsob výpočtu jednotlivých atributů_. Jsou přiřazena pravidlům bezkontextové gramatiky.
>
> _Mějme syntaktické pravidlo:_
>
> $$
> X_0 \rightarrow X_1X_2\dots X_m.
> $$
>
> K němu _mohou být přiřazena sémantická pravidla obecného tvaru:_
>
> $$
> X_i.a=f(X_j.u,X_k.v,\dots,X_r.z).
> $$
>
> Tento zápis vyjadřuje, že **hodnota atributu** $X_i.a$ je **vypočtena funkcí** $f$ z _atributů ostatních symbolů_, které se _nacházejí ve stejném produkčním pravidle_.

- Funkce $f$ může _představovat například_:
  - prosté **přiřazení** hodnoty,
  - aritmetický nebo logický **výpočet**,
  - **kontrolu kompatibility** datových typů,
  - **vyhledání informace** v tabulce symbolů,
  - vytvoření položky v interní reprezentaci programu.

> [!info]
> Sémantická pravidla tedy _představují vlastní algoritmus sémantické analýzy_ – určují, _jaké informace se mají během syntaktické analýzy vypočítat_ a _jak se mají šířit mezi jednotlivými uzly derivačního stromu_.

## 1.3 Klasifikace atributů

- Podle způsobu výpočtu rozlišujeme **syntetizované** a **děděné** atributy.

### 1.3.1 Syntetizované atributy

> [!success]
> **Syntetizovaný atribut** $AS(X)$ je _vypočten_ z atributů **potomků** daného uzlu derivačního stromu. Informace se tedy šíří **zdola nahoru** (od listů směrem ke kořeni).

- Formálně je syntetizovaný atribut atribut symbolu na **levé straně syntaktického pravidla**.

> [!info]
> **Příklad**: Datový typ výrazu vznikne až po výpočtu datových typů obou operandů.
>
> ```
> // Pravidlo
> E → E1 + E2
> 
> // Syntentizovaný atribut
> E.typ =
>     if E1.typ = float or E2.typ = float
>     then float
>     else int
> ```

- Syntetizované atributy _jsou přirozené zejména_ pro **syntaktickou analýzu zdola nahoru (LR)**, protože se _vypočítávají při redukci syntaktických pravidel_.

### 1.3.2 Děděné atributy

> [!success]
> **Děděný atribut** $AI(X)$ je naopak vypočten z atributů **rodiče** nebo **levých sourozenců** daného uzlu. Informace se tedy šíří převážně **shora dolů**.

- Formálně jde o atribut symbolu na **pravé straně syntaktického pravidla**.

> [!info]
> **Příklad**: Předávání datového typu z deklarace na jednotlivé identifikátory.
>
> ```
> // Pravidlo
> DEKLARACE → TYP IDENTIFIKATOR
> 
> // Děděný atribut
> IDENT.typ = TYP.typ
> ```

- Děděné atributy se využívají především při **syntaktické analýze shora dolů (LL)**.

> [!danger]
> _Platí_:
>
> $AS(X) \cup AI(X) = A(X), \qquad AS(X) \cap AI(X) = \varnothing$

### 1.3.3 Intrinsické atributy terminálních symbolů

> [!success]
> **Intrinsické atributy** jsou atributy, jejichž hodnota není vypočítána sémantickými pravidly atributové gramatiky, ale je **přímo určena lexikálním analyzátorem** _při rozpoznání terminálního symbolu_.

```
int x = 5;
```

- Token `int` má intrinsický atribut „klíčové slovo `int`“.
- Token `x` má intrinsický atribut „název `x`“ (a případně odkaz do tabulky symbolů).
- Token `5` má intrinsický atribut „hodnota = 5“.

> [!warning]
> **Obecné atributové gramatiky** umožňují _libovolné závislosti mezi atributy_, jejich vyhodnocení však může být _složité a často vyžaduje sestavení celého derivačního stromu_.
>
> Pro praktickou implementaci překladačů se proto používají jejich omezené varianty – **S-atributové** a **L-atributové gramatiky**, jejichž omezení _odpovídají způsobu syntaktické analýzy_ a _umožňují průběžný výpočet atributů během parsován_í.

---

# 2. S-atributová gramatika

- Při **syntaktické analýze zdola-nahoru (LR)** parser nejprve provádí operace **přesunu (shift)**, při kterých ukládá symboly na zásobník. V této fázi však ještě **není známo syntaktické pravidlo**, podle kterého bude provedena redukce, a proto nelze vyhodnocovat sémantická pravidla ani počítat atributy právě přesouvaných symbolů.
- Syntaktické pravidlo je určeno až při operaci **reduce**, kdy je dokončeno _rozpoznání celé pravé strany pravidla_. Teprve v tomto okamžiku _lze vypočítat atribut symbolu na levé straně redukčního pravidla_.

> [!info]
> Z tohoto důvodu je při **analýze zdola-nahoru** možné pracovat pouze se **syntetizovanými atributy**, zatímco _dědičné atributy nelze průběžně vyhodnocovat_.

- Analýza zdola-nahoru je tedy z hlediska výpočtu atributů méně výhodná než analýza shora-dolů.

> [!success]
> **S-atributová gramatika** je atributová gramatika obsahující **výhradně syntetizované atributy**. Formálně platí
>
> $$
> A_I(X)=\emptyset,\qquad \forall X\in N\cup T.
> $$
>
> **Výpočet** atributů _probíhá průběžně během syntaktické analýzy_, pouze v okamžiku **redukce**, kdy jsou známa _všechna syntaktická i sémantická pravidla_.

- **Implementace S-atributové gramatiky** využívá **jeden zásobník**, na kterém jsou společně uloženy _zásobníkové symboly parseru i jejich syntetizované atributy_.
  - Při operaci **shift** se na _zásobník uloží symbol spolu s jeho množinou syntetizovaných atributů_ (u terminálních symbolů zpravidla převzatých z intrinsických atributů vytvořených lexikálním analyzátorem).
  - Při operaci **reduce** se ze _syntetizovaných atributů symbolů na pravé straně_ **vypočítají** _syntetizované atributy symbolu na levé straně_, atributy pravé strany jsou odstraněny a na zásobník se uloží nový symbol společně s nově vypočtenými atributy.

## 2.1 Příklad analýzy

![[019fcccc-f832-738d-9942-fe65e1d269ee.png]]![[019fcccd-8a02-738e-8f44-5b60777db58d.png]]

---

# 3. L-atributová gramatika

- Na rozdíl od analýzy zdola-nahoru je při **syntaktické analýze shora-dolů (LL)** syntaktické pravidlo známo již **v okamžiku expanze neterminálu**. Současně jsou tedy známa i sémantická pravidla, což umožňuje průběžně _vyhodnocovat atributy jednotlivých symbolů_ během samotného parsování.
- Díky tomu lze používat nejen syntetizované, ale také **dědičné atributy**.

> [!success]
> **L-atributová gramatika** je atributová gramatika umožňující **průběžný výpočet atributů při analýze shora-dolů**. Označení **L** (_Left-to-right_) vyjadřuje, že _dědičné atributy_ mohou být předávány pouze **zleva doprava**.
>
> Pro **každé** syntaktické pravidlo
>
> $$
> X_0 \to X_1 X_2 \ldots X_m \qquad (P)
> $$
>
> platí, že **dědičné atributy každého symbolu** $X_j$ **na pravé straně (** $j \ge 1$ **) jsou přímo závislé jen na**:
>
> - atributech symbolů $X_1, X_2, \ldots, X_{j-1}$ (**levých sourozencích**)
> - **dědičných atributech symbolu** $X_0$ (**rodiče**)
>
> Toto _omezení zajišťuje_, že **všechny** _atributy lze vyhodnotit během_ **jediného průchodu** derivačním stromem

> [!danger]
> Naopak **nesmějí záviset** na _pravých sourozencích_, _na vlastních atributec_h ani n_a syntetizovaných atributech rodiče_, protože ty jsou _vypočítány až po zpracování celé pravé strany pravidla_.

## 3.1 Pořadí výpočtu atributů

- Atributy lze pak počítat v přímočarém pořadí odpovídajícím **průchodu stromem do hloubky zleva doprava**:

$$
A_I(X_0),\ A_I(X_1), A_S(X_1),\ A_I(X_2), A_S(X_2),\ \ldots,\ A_I(X_m), A_S(X_m),\ A_S(X_0)
$$

> [!note]
> **Intuice**: Nejprve jsou tedy _předány dědičné atributy z rodiče,_ následně jsou _postupně zpracovány všechny symboly pravé strany pravidla_ a po jejich dokončení se _vypočítá syntetizovaný atribut symbolu_ na levé straně pravidla.

## 3.2 Deterministický sémantický analyzátor se dvěma zásobníky

- Analyzátor využívá **dva zásobníky**:
  
  - **syntaktický zásobník** – obsahuje symboly parseru (terminály a neterminály),
  - **sémantický zásobník** – obsahuje hodnoty atributů jednotlivých symbolů.
  
  Oba zásobníky se při analýze pohybují společně – ke každému symbolu na syntaktickém zásobníku existují odpovídající atributy na zásobníku sémantickém.

### **Krok 0. — Výchozí stav**

![[019f9366-769c-718b-a41c-82e2e93a864e.png]]

### **Krok 1.** — Výpočet dědičných atributů

- Parser se rozhodne expandovat neterminál podle pravidla

$$
X_0 \to X_1 X_2 \ldots X_m
$$

- Protože je pravidlo již známé, může nejprve vypočítat **dědičné atributy** symbolů na pravé straně pravidla. Ty jsou **odvozeny z atributů rodiče** $X_0$ a případně **z atributů levých sourozenců**. Vypočtené hodnoty se _uloží na sémantický zásobník_. (To je PŘED expanzí)

![[019f9366-c212-75da-b6a3-04e284b767bf.png]]

### **Krok 2.** — Provedeme expanzi pravidla

![[019f9367-265e-730f-8e13-aaa84bf7a1ca.png]]

- Na syntaktickém zásobníku se neterminál $X_0$ **nahradí** _symboly pravé strany pravidla_
- Parser následně začne _jednotlivé symboly zpracovávat zleva doprava_.

### Krok 3. — Zpracování symbolů pravé strany

- Máme dvě možnosti:

#### a) Symbol je terminál

- Pokud je $X_i$ terminální symbol, parser **provede srovnání** _se vstupním tokenem_ a navíc se při této příležitosti **stanoví dědičné atributy** a _uloží na zásobník_.
- Následně se _získají_ jeho **syntetizované atributy**, které jsou obvykle převzaty z **intrinsických atributů** _vytvořených lexikálním analyzátorem_ (například hodnota číselného literálu nebo odkaz na položku tabulky symbolů).
- Tyto atributy uloží na sémantický zásobník.

![[019f9367-d407-75ea-a7c5-c7c470f35a7c.png]]

#### b) Symbol je neterminál

- Pokud je $X_i$ neterminál, nejprve se vypočítají jeho **dědičné atributy** a _uloží se na zásobník_.

![[019f9368-35e5-73cc-9587-b709a00aad20.png]]

- Poté parser tento neterminál expanduje podle odpovídajícího pravidla a stejným způsobem rekurzivně zpracuje celý jeho podstrom.
- Po dokončení zpracování neterminálu _jsou již známy atributy všech jeho potomků_, takže lze vypočítat jeho **syntetizované atributy**, které se uloží na sémantický zásobník.

![[019f9368-a12d-759d-8b76-124dc2a3022b.png]]

### **Krok 4.** — Dokončení pravé strany

- _Stejným způsobem_ pro $X_2, \ldots, X_m$. Na konci je na sémantickém zásobníku:

![[019f9368-f42d-73bc-8729-8fd9d45cfba4.png]]

### **Krok 5. — Výpočet syntetizovaného atributu rodiče**

- Jakmile jsou _zpracovány všechny symboly pravé strany pravidla_, parser vypočítá **syntetizované atributy** neterminálu $X_0$.
- Následně **odstraní** ze sémantického zásobníku **atributy symbolů pravé strany**, protože _již nejsou potřeba_, a uloží pouze **nově vypočtené atributy symbolu** $X_0$.

![[019f9369-334a-72ab-a1f5-9023f2f7def5.png]]

> [!warning]
> **Zapamatuj si tuhle asymetrii.** LR parsery jsou **syntakticky silnější** než LL, ale pro **výpočet atributů jsou slabší**.
>
> _Důvod je časový:_ LR zná pravidlo až _na konci_ (při redukci), LL už _na začátku_ (při expanzi).