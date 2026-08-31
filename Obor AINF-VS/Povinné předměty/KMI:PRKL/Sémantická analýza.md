> [!success]
> **Sémantická analýza** je fáze překladu, která _následuje po syntaktické analýze_. Syntaktický analyzátor rozpozná syntaktické celky programu (deklarace, výrazy, příkazy) a předá je sémantickému analyzátoru
>
> Jejím cílem je ověřit, že program má **správný význam (sémantiku)** – tedy že _není jen syntakticky správný, ale že je i logicky korektní_. Jejím výstupem je **2. interní forma programu**.

- Sémantický analyzátor zejména zjišťuje:
  - zda proměnné použité v příkazech byly vůbec **deklarovány**,
  - _správnost deklarací_ proměnných
  - zda mají **odpovídající datový typ** pro místo, kde jsou použity,
  - pokud mají jiný datový typ, zda v daném jazyce existuje **konverze** na požadovaný typ,
  - pravidla rozsahu platnosti

> [!info]
> V praxi **neběží jako oddělený průchod nad hotovým stromem**, ale je zaklíněná do syntaktické analýzy. Syntaktický analyzátor v průběhu analýzy volá **sémantické funkce**, které _analyzují právě rozpoznanou část_ programu a _generují pro ni 2. interní formu_.

---

# 1. Formální popisy sémantiky

- _Na rozdíl od syntaktické analýzy_ se **nepodařilo vytvořit** obecnou metodu, která by z formálního popisu **automaticky vygenerovala sémantický analyzátor**.

> [!info]
> Existují tři způsoby formálního popisu sémantiky:
>
> 1. **axiomatická sémantika**
> 2. **operační sémantika**
> 3. **denotační sémantika**
>
> Tyto přístupy _přesně popisují význam programů_, ale ukázalo se, že **nejsou vhodné pro automatické generování** _sémantických analyzátorů_.
>
> **Důvod**: Zatímco syntaktická část programovacích jazyků je poměrně podobná (identifikátory, klíčová slova, konstanty, operátory atd.), jejich **sémantika se značně liší** (imperativní jazyky, funkcionální jazyky, logické jazyky, simulační jazyky atd.).

- Po neúspěšných pokusech _o automatické generování sémantických analyzátorů z formálních popisů sémantiky_ se _v implementaci překladačů začaly používat_ **atributové gramatiky**. Ty představují praktický mechanismus pro realizaci sémantické analýzy – _rozšiřují bezkontextovou gramatiku_ o sémantické informace a pravidla pro **jejich vyhodnocování během syntaktické analýzy.**

---

# 2. Atributová gramatika jako nástroj sémantické analýzy

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

## 2.1 Atributy

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

## 2.2 Sémantická pravidla

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

## 2.3 Klasifikace atributů

- Podle způsobu výpočtu rozlišujeme **syntetizované** a **děděné** atributy.

### 2.3.1 Syntetizované atributy

> [!success]
> **Syntetizovaný atribut** **(** $AS(X)$ **)** je _vypočten_ z atributů **potomků** daného uzlu derivačního stromu. Informace se tedy šíří **zdola nahoru** (od listů směrem ke kořeni).

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

### 2.3.2 Děděné atributy

> [!success]
> **Děděný atribut (** $AI(X)$ **)** je naopak vypočten z atributů **rodiče** nebo **levých sourozenců** daného uzlu. Informace se tedy šíří převážně **shora dolů**.

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

### 2.3.3 Intrinsické atributy terminálních symbolů

> [!success]
> **Intrinsické atributy** jsou atributy, jejichž hodnota není vypočítána sémantickými pravidly atributové gramatiky, ale je **přímo určena lexikálním analyzátorem** _při rozpoznání terminálního symbolu_.

```
int x = 5;
```

- Token `int` má intrinsický atribut „_klíčové slovo_ `int`_“._
- Token `x` má intrinsický atribut _„název_ `x`_“_ (a případně odkaz do tabulky symbolů).
- Token `5` má intrinsický atribut _„hodnota = 5“_.

---

# 3. Dobře definovaná atributová gramatika

- Atributová gramatika je **dobře definovaná**, jestliže

1. v **každém** derivačním stromu _existuje_ pro **každý** atribut **právě jedno pravidlo** _určující jeho hodnotu_,
2. gramatika je **acyklická**.

> [!note]
> **Intuice**: První podmínka zajišťuje _jednoznačnost výpočtu atributů_. Druhá podmínka zajišťuje, že atributy lze _skutečně vypočítat_.

> [!success]
> Je **acyklická** pokud v každém derivačním stromu _lze nalézt_ takové **_pořadí_** _výpočtu atributů_, ve kterém je _každý atribut vypočten až poté_, co jsou _známy všechny atributy_, na nichž **závisí**.

## 3.1 Graf závislostí

- Vzájemné závislosti mezi atributy lze znázornit pomocí **grafu závislostí**.V tomto grafu:
  - **vrcholy** představují jednotlivé atributy,
  - **orientovaná hrana** $A \rightarrow B$ znamená, že atribut $B$ **závisí na atributu** $A$, tedy že atribut $A$ musí být vypočten dříve.
- Pokud graf obsahuje orientovaný cyklus, atributy nelze jednoznačně vyhodnotit a atributová gramatika není dobře definovaná.
- Jestliže je graf acyklický, lze nalézt pořadí výpočtu všech atributů.

## 3.2 Silná acykličnost

> [!warning]
> **Problém:** Ověřit acykličnost je _obtížné_. museli bychom dokázat, že **v žádném derivačním stromu nemůže být cyklus**, přitom gramatiky _mají běžně rekurzivní pravidla a generovaný jazyk je nekonečný_ (nelze projít všechny stromy).
>
> **Řešení:** Ověřuje se silnější (a snadněji rozhodnutelná) vlastnost — **silná acykličnost**.

> [!success]
> Atributová gramatika je **silně acyklická**, jestliže pro každý symbol $X \in N \cup T$ je stanoveno pořadí výpočtu jeho atributů $X.a_1, X.a_2, \ldots, X.a_k$ (značíme $O(A(X))$, _order_), splňující podmínku:
>
> Graf sestavený pro **každé** pravidlo $X_0 \to X_1X_2\ldots X_m$, ve kterém
>
> - uzly jsou atributy z množin $A(X_0), A(X_1), \ldots, A(X_m)$,
> - hrany jsou:
>   - z $X_j.b$ do $X_i.a$, jestliže $X_i.a$ **závisí** na $X_j.b$,
>   - z $X_j.b$ do $X_i.a$, jestliže v uspořádání $O(A(X))$ je $X_j.b$ **někde před** $X_i.a$,
>
> je **acyklický**.

> [!danger]
> **Vztah:** silně acyklická $\Rightarrow$ acyklická.

> [!note]
> **Intuice:** Silná acykličnost říká, že si můžeme zvolit **jedno pevné pořadí** _vyhodnocování atributů_ **pro každý symbol**, které funguje _ve všech derivačních stromech_.

### 3.2.1 Příklad — sestavení grafu závislostí a pořadí výpočtu

#### Příklad

Gramatika:

```
A → BC       C.c = f11(B.b)
             A.a = f12(C.c, C.m)
             B.q = A.q

B → DxE      B.b = f21(D.d, E.e)
             E.e = f22(x.x)

C → y        C.m = f3(y.y)

D → wC       C.c = f41(w.w)
             D.d = f42(C.m)

E → e
```

**Postup:** projdeme pravidla a vyznačíme přímé závislosti (šipka = „potřebuji nejdřív“):

```
A.q ──► B.q
w.w ──► C.c(v D)
y.y ──► C.m
C.m ──► D.d
x.x ──► E.e
D.d ─┐
     ├──► B.b ──► C.c(v A)
E.e ─┘
C.c ─┐
     ├──► A.a
C.m ─┘
```

**Odvozené pořadí výpočtu atributů:**

$A.q,\ B.q,\ x.x,\ E.e,\ y.y,\ C.m,\ D.d,\ B.b,\ w.w,\ C.c,\ A.a$

**Kontrola:** graf je acyklický ⇒ gramatika je (pro tento strom) dobře definovaná a výpočet lze provést.


---

# 4. Tabulky symbolů v sémantické analýze

- Při sémantické analýze je _nutné uchovávat informace o identifikátorech_ (proměnných, funkcích, datových typech apod.), aby bylo možné **ověřovat jejich správné použití**. K tomuto účelu slouží **tabulka symbolů**.

> [!success]
> **Tabulka symbolů** je _datová struktura obsahující informace získané z deklarací a definic programu_. Během sémantické analýzy se do ní _ukládají nové symboly_ a současně se z ní _vyhledávají informace_ potřebné pro kontrolu sémantických pravidel.

- V tabulce symbolů jsou obvykle uloženy například:
  - názvy proměnných a jejich datové typy,
  - počáteční hodnoty proměnných,
  - informace o polích (počet dimenzí a jejich rozsahy),
  - informace o strukturách (`struct`, `union`),
  - hlavičky funkcí (návratový typ, parametry),
  - uživatelsky definované datové typy (`typedef`).

---

# 5. Sémantické chyby a jejich hlášení

- Sémantické chyby představují _porušení pravidel programovacího jazyka_, která nelze odhalit lexikální ani syntaktickou analýzou. Jsou zjišťovány během sémantické analýzy _na základě informací uložených v tabulce symbolů a vyhodnocených atributů_.
- _Při nalezení sémantické chyby_ by měl překladač:
  - **uvést místo**, kde byla chyba nalezena,
  - **popsat** charakter chyby,
  - **pokud možno pokračovat v analýze** programu a neukončit překlad po první nalezené chybě.

## 5.1 Zotavení ze sémantických chyb

- Překladač obvykle místo chybné hodnoty dosadí **speciální atribut označující chybu** nebo vytvoří **fiktivní záznam v tabulce symbolů**. Díky tomu _lze pokračovat v analýze programu_ a zabránit vzniku velkého množství navazujících chybových hlášení.

> [!info]
> **Například:** Pokud je použita _nedeklarovaná proměnná desetkrát_, překladač _by měl ohlásit jedinou chybu_ „nedeklarovaný identifikátor“ a _další použití již pouze pracují s fiktivním záznamem,_ místo aby byla stejná chyba hlášena opakovaně.

## 5.2 Typické sémantické chyby

- Mezi nejčastější sémantické chyby patří:

| Chyba | Kontrola |
| --- | --- |
| **undeclared identifier** | identifikátor není nalezen v tabulce symbolů |
| **redefinition of identifier** | opakovaná deklarace ve stejném rozsahu platnosti |
| **incompatible types in assignment** | nekompatibilní datové typy při přiřazení |
| **invalid operands** | nepovolené datové typy operandů operace |
| **too few / too many arguments** | nesouhlasí počet parametrů funkce |
| **break outside of loop** | příkaz `break` použit mimo cyklus |

## 5.3 Chyby, které sémantická analýza neodhalí

- Sémantická analýza je **statická analýza**, a proto _nedokáže odhalit chyby závislé_ **na konkrétních hodnotách** během běhu programu.
- Patří mezi ně například:
  - dělení nulou,
  - přístup mimo rozsah pole,
  - dereference nulového ukazatele,
  - přetečení číselných typů.
- Tyto chyby jsou obvykle odhaleny **až při vykonávání programu** nebo pomocí dalších nástrojů pro statickou analýzu.