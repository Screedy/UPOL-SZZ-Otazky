- **Rekurzivní sestup (recursive descent)** je konkrétní implementace **prediktivního LL(1) syntaktického analyzátoru**, tedy analýzy **shora-dolů** s jedním vstupním symbolem dopředu (_lookahead_).

> [!info]
> Označení **prediktivní** znamená, že analyzátor _dokáže podle jediného vstupního symbolu_ (lookahead) **jednoznačně předpovědět**, které _pravidlo gramatiky_ **použije**, aniž by musel _zkoušet více možností nebo se vracet zpět_.

- Místo tabulkou řízeného zásobníkového automatu je parser realizován jako **sada vzájemně se volajících funkcí**, přičemž _každému neterminálu gramatiky odpovídá jedna funkce_. Zásobník analyzátoru je zde **implicitní** – je _tvořen zásobníkem volání funkcí_.
- Parser přijímá posloupnost _tokenů vytvořenou lexikálním analyzátorem_ a během analýzy **vytváří derivační strom** a může _současně provádět sémantické akce_.
- Výstupem je zjištění, zda program **je/není syntakticky správný**

---

# 1. Princip metody

> [!success]
> Pro _každý neterminální symbol_ $A$ gramatiky **sestavíme jednu funkci** `ParseA()`, která _provádí analýzu podle všech pravidel gramatiky_, jež mají symbol $A$ **na levé straně**.

> [!note]
> **Intuice:**
>
> Každá funkce představuje rozpoznání jednoho neterminálu. Podle **aktuálního vstupního tokenu (lookahead)** rozhodne, které pravidlo použije, a následně zpracuje pravou stranu tohoto pravidla.
>
> Při průchodu pravou stranou pravidla:
>
> - pokud narazí na **neterminál**, zavolá odpovídající funkci (`ParseB()`), čímž se provede **expanze**,
> - pokud narazí na **terminál**, _porovná jej s aktuálním vstupním tokenem_ (**srovnání**). Jsou-li shodné, načte _další token,_ jinak _oznámí syntaktickou chybu_.
>
> **Rekurze** _v gramatických pravidlech_ se tak přímo promítá _do rekurzivního volání funkcí_.

**Dvě základní operace**:

| Operace | Kdy se provádí | Co dělá |
| --- | --- | --- |
| **Expanze** | na vrcholu zásobníku je neterminál $B$ | nahradí $B$ pravou stranou pravidla zavoláním `ParseB()` |
| **Srovnání** | na vrcholu zásobníku je terminál $t$ | porovná $t$ se symbolem na vstupu; jsou-li shodné, odstraní oba (jinak chyba) |

- Analyzátor nikdy nezkouší více pravidel ani se nevrací zpět (_backtracking_).
- Rozhodnutí je **vždy jednoznačné** _na základě jediného vstupního symbol_u, což je možné pouze pro **LL(1) gramatiky**.

---

# 2. Předpoklady

- Rekurzivní sestup předpokládá, že _gramatika je_ **LL(1)**.
- Množiny **FIRST** a **FOLLOW** umožňují parseru **jednoznačně rozhodnout, které produkční pravidlo daného neterminálu se má použít**, a to pouze podle jediného vstupního symbolu.
- Výpočet těchto množin i podmínky LL(1) byly popsány v předchozí kapitole.

---

# 3. Obecný algoritmus konstrukce

- Předpokládejme:
  - `u` — aktuální vstupní token (aktuální lookahead).
  - `lex()` — funkce lexikálního analyzátoru, vrací další token.
  - `chyba()` — obsluha syntaktické chyby.

1. **Pro každé** pravidlo $A \to \alpha$ vypočítáme jeho **First-Folow množinu**:

$A \to \alpha_1 \quad \text{FIRST}(\alpha_1,\text{FOLLOW}(A)) = \set{a_{11}, a_{12}, \dots, a_{1p}}\\ A \to \alpha_2 \quad \text{FIRST}(\alpha_2,\text{FOLLOW}(A)) = \set{a_{21}, a_{22}, \dots, a_{2q}}\\ \vdots \\ A \to \alpha_k \quad \text{FIRST}(\alpha_k,\text{FOLLOW}(A)) = \set{a_{k1}, a_{k2}, \dots, a_{kr}}$

2. Pro každý neterminální symbol $A$ gramatiky sestavíme jednu funkci, která dělá _analýzu podle všech pravidel gramatiky s tímto symbolem na levé straně_. **Bude mít tvar:**

![[019f89af-bc6b-707e-9a4f-209a7d34bbf1.png]]

- Části akce pro $\alpha_i$ obsahují **operace expanze nebo srovnání** _pro jednotlivé symboly pravé strany_ $\alpha_i$ pravidla $A \to \alpha_i$
  - Pro každý **neterminál** $B \in \alpha_i$→ zavoláme `ParseB();`
  - Pro každý **terminál** $t \in \alpha_i$→ provedeme **srovnání**. Je-li úspěšné načteme další lexikální symbol pomocí `lex()`, jinak `chyba()`.
- Pomocná _funkce pro srovnání terminálů_ může mít například tvar:

```c
Srovnani(v)
{
    if (u == v) u = lex();
    else chyba();
}
```

---

# 4. Kompletní příklad

- Uvažujme gramatiku:

$1.\quad E \to T \ F\\ 2.\quad F \to {+}\ T\ F\\ 3.\quad F \to \varepsilon\\ 4.\quad T \to (E)\\ 5.\quad T \to i$

Počáteční symbol je $E$.

## 4.1 Výpočet FIRST a FOLLOW

| Číslo | Pravidlo | Množina First–Follow |
| --- | --- | --- |
| 1   | $E \to TF$ | $\text{FIRST}(TF) = \set{(,\ i }$ |
| 2   | $F \to +TF$ | $\text{FIRST}(+TF) = \set{+}$ |
| 3   | $F \to \varepsilon$ | $\text{FOLLOW}(F) = \set{),\ \varepsilon }$ |
| 4   | $T \to (E)$ | $\text{FIRST}((E)) = \set{(}$ |
| 5   | $T \to i$ | $\text{FIRST}(i) = \set{i }$ |

> [!info]
> Tato gramatika je LL(1).

### **4.2.1 Výpočet jednotlivých hodnot**

#### Výpočet

1. $\text{FIRST}(TF)$: $T$ začíná buď `(` (pravidlo 4) nebo `i` (pravidlo 5) → $\set{(, i}$.
2. $\text{FIRST}(+TF) = \set{+}$ — začíná terminálem `+`. (podobně výpočet 4 a 5)
3. $\text{FOLLOW}(F)$: kde stojí $F$ na pravé straně? V pravidle 1 ($E\to TF$) je $F$ na konci → do $\text{FOLLOW}(F)$ jde $\text{FOLLOW}(E)$; v pravidle 2 ($F\to +TF$) je $F$ opět na konci → $\text{FOLLOW}(F)$ (rekurze, nic nepřidá navíc).
  - $\text{FOLLOW}(E)$: $E$ je počáteční → obsahuje `ε`; v pravidle 4 ($T \to (E)$) stojí za $E$ terminál `)` → přidáme `)`. Celkem $\text{FOLLOW}(E) = \set{), \varepsilon}$.


## 4.3 Sestavení funkcí

Symbol `#` značí konec analyzovaného programu. (Náhrada za ε)

```c
ParseE()
{
    switch (u) {
        case '(':
        case 'i':  ParseT(); ParseF(); return;   // E → TF   (FIRST = {(, i})
        default:   chyba();
    }
}

ParseF()
{
    switch (u) {
        case '+':  u = lex(); ParseT(); ParseF(); return;  // F → +TF  (FIRST = {+})
        case ')':
        case '#':  return;                                 // F → ε    (FOLLOW(F) = {), #})
        default:   chyba();
    }
}

ParseT()
{
    switch (u) {
        case 'i':  u = lex(); return;                       // T → i    (FIRST = {i})
        case '(':  u = lex(); ParseE(); Srovnani(')');       // T → (E)  (FIRST = {(})
                   return;
        default:   chyba();
    }
}
```

## 4.4 Průběh analýzy na vstupu `i+(i+i)`

```
ParseE                       // u='i'
├─ ParseT                    // u='i' → T→i, u=lex() → u='+'
└─ ParseF                    // u='+' → F→+TF
   ├─ (match '+')            // u=lex() → u='('
   ├─ ParseT                 // u='(' → T→(E)
   │  ├─ (match '(')         // u=lex() → u='i'
   │  ├─ ParseE              // u='i'
   │  │  ├─ ParseT           // u='i' → T→i, u=lex() → u='+'
   │  │  └─ ParseF           // u='+' → F→+TF
   │  │     ├─ (match '+')   // u=lex() → u='i'
   │  │     ├─ ParseT        // u='i' → T→i, u=lex() → u=')'
   │  │     └─ ParseF        // u=')' → F→ε (return)
   │  └─ Srovnani(')')       // u=lex() → u='#'
   └─ ParseF                 // u='#' → F→ε (return)
```

---

# 5. Vztah k tabulkové LL(1) analýze

Dělají totéž, pouze jiným způsobem:

| Aspekt | Tabulkový LL(1) parser | Rekurzivní sestup |
| --- | --- | --- |
| Zásobník | **explicitní** datová struktura | **implicitní** (zásobník volání) |
| Rozhodnutí o pravidle | vyhledání buňky $M[A, u]$ v tabulce | `switch (u)` uvnitř `ParseA()` |
| Řízení | jeden univerzální řídicí cyklus + tabulka | kód _„zadrátovaný"_ do funkcí |
| Expanze | pop neterminálu, push pravé strany | volání `ParseB()` |
| Srovnání | pop terminálu = match se vstupem | `Srovnani(t)` / `u==t; u=lex()` |
| Změna gramatiky | přegenerovat tabulku | přepsat funkce |
| Sémantické akce | vkládají se hůř | vkládají se **přirozeně** přímo do kódu |
| Čitelnost / ladění | horší | **lepší** (parser vypadá jako gramatika) |

## **5.1 Kdy se co používá:**

- _Rekurzivní sestup_ se často píše **ručně** — je čitelný, snadno se do něj vkládají sémantické akce a zotavení z chyb, hodí se **pro menší jazyky**.
- Tabulkový parser se spíš **generuje** **nástrojem**.