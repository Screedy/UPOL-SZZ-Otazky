> [!success]
> **Syntaktická analýza zdola-nahoru (bottom-up parsing)** sestavuje derivační strom od **listů** (terminály = tokeny z lexikálního analyzátoru) směrem ke **kořeni** (počáteční symbol gramatiky).  
> Parser tedy postupně rozpoznává _stále větší syntaktické celky_, až vznikne _počáteční symbol gramatiky_.

- Používá se **deterministický zásobníkový automat**, který (na rozdíl od LL analýzy) pracuje s **celým zásobníkem** — při jednom přechodu může odebrat _různý počet_ zásobníkových symbolů (tolik, kolik je symbolů na pravé straně redukovaného pravidla).
- _Na začátku_ je **zásobník prázdný**.
- _Na konci_ analýzy obsahuje pouze **počáteční symbol gramatiky**, _pokud je vstup syntakticky správný_.

**Základní operace:**

- **Přesun (shift)** — _Přesune jeden symbol_ ze vstupu na vrchol zásobníku.
- **Redukce (reduce)** — Na vrcholu zásobníku _nahradí řetězec_ odpovídající _pravé straně_ pravidla neterminálem z _levé strany_ téhož pravidla ($A \to \beta$⇒ na zásobníku se $\beta$ nahradí za $A$).

---

# 1. Rodina LR gramatik

- **SLR(1) (Simple LR)** je jedna z metod **deterministické syntaktické analýzy zdola-nahoru**. Patří do rodiny LR parserů:

$$
\text{LR(0)} \subset \text{SLR(1)} \subset \text{LALR(1)} \subset \text{LR(1)}
$$

> [!info]
> **SLR(1)** se jmenuje _Simple LR_, protože **používá jednodušší LR(0)** _položky_ bez _uloženého lookaheadu._ Číslo (1) ale zůstává, protože **parser stále rozhoduje podle jednoho vstupního symbolu** (lookahead), který _porovnává s množinami FOLLOW_.

---

# 2. Konstrukce automatu pro SLR(1)

## 2.1 Rozšířená gramatika

- Před konstrukcí vytvoříme **rozšířenou gramatiku** $G' = (N \cup {S'}, T, P \cup {S' \to S}, S')$

> [!info]
> Přidání pravidla $S' \to S$ (s novým startovním symbolem) **usnadňuje detekci konce** analýzy.

## 2.2 Konstrukce LR(0) položek

> [!info]
> U analýzy **shora-dolů** parser vždy ví, podle _kterého pravidla postupuje_, protože pravidla **sám rozvíjí**. Proto _mu stačí na zásobníku uchovávat pouze terminály a neterminály_.
>
> U analýzy **zdola-nahoru** je situace _opačná_ – parser _postupně skládá symboly do větších celků_ a musí rozhodnout, **kdy provést redukci a podle kterého pravidla**. Samotné _terminály a neterminály k tomu nestačí_. Proto se používají **LR položky**, které **zachycují aktuální stav** rozpoznávání pravidel.

> [!success]
> **LR(0) položka (item)** je _pravidlo gramatiky_, ve kterém je pomocí **tečky (•)** vyznačeno, jaká _část pravé strany pravidla již byla při analýze rozpoznána_.
>
> _Obecný tvar_ položky je:
>
> $$
> [A \to \mu . \nu]
> $$
>
> kde:
>
> - $\mu$ představuje již **rozpoznanou** (přesunutou) část pravé strany pravidla,
> - $\nu$ představuje část, kterou parser **teprve očekává**.
>
> Tečka tedy odděluje **již zpracované symboly** od **symbolů, které ještě zbývá zpracovat**.
>
> Toto jsou **LR(0) položky**, protože _neobsahují prediktivní část_.

> [!warning]
> Pokud je **tečka na konci pravidla**, jedná se o **redukční položku**.
>
> Parser již _rozpoznal celou pravou stranu pravidla_ a _může ji nahradit neterminálem z levé strany pravidla_.

## 2.3 Výpočet uzávěru (closure)

> [!success]
> Pokud je za tečkou **neterminál**, musí _parser přidat počáteční položky všech jeho pravidel_.
>
> Do uzávěru se **zahrnou počáteční položky** _všech možných pravidel_, jež mají **na levé straně** _neterminální symbo_l, který je v některé _z výchozích položek množiny M_ **právě za tečkou**. Výpočet uzávěru má _rekurzivní charakter_.
>
> $$
> U(M) = M \cup \set{[B \to .\beta] \mid [A \to \mu . B \nu] \in U(M),\ B \to \beta \in P}
> $$

> [!info]
> **Uzávěr (closure)** _rozšiřuje množinu LR položek_ o všechny položky, které _mohou být v daném stavu parseru potřeba_.

> [!note]
> **Intuice:** je-li tečka **před neterminálem** $B$, znamená to, že teď musíme rozpoznat nějakou pravou stranu pravidla pro $B$. Do stavu proto přidáme _počáteční_ položky všech pravidel $B \to \beta$ (tečka na začátku). Výpočet je **rekurzivní** — nově přidaná položka může mít za tečkou zase neterminál.

## 2.4 Přechod (goto)

> [!success]
> **Přechod (goto)** určuje, _do jakého stavu se parser dostane po zpracování určitého symbolu_.
>
> $$
> \text{goto}(z, x) = U\big({[A \to \mu x . \nu] \mid [A \to \mu . x \nu] \in z}\big)
> $$
>
> Vznikne tak, že se ve všech položkách aktuálního stavu **posune tečka přes zvolený symbol** a následně se z nově vzniklých položek **vypočítá uzávěr (closure)**.

> [!info]
> - Přechod po **terminálu** odpovídá operaci **Shift (přesun)**.
> - Přechod po **neterminálu** nastává po provedení **Reduce (redukce)**.

> [!note]
> **Intuice:** goto = „posuň tečku přes $x$" u všech položek, kde to jde, a udělej uzávěr.

## 2.5 Postup sestavení automatu

1. Vytvoří se _rozšířená gramatika_.
2. Zkonstruujeme **počáteční zásobníkový symbol** $z_0 = U({[S' \to .S]})$ a _zařadíme jej do množiny zásobníkových symbolů_ $Z = {z_0}$
3. **Průběžný krok:** Pro každý dosud nezpracovaný symbol $z \in Z$ proveď krok 4.
4. Pro každý symbol $x \in N \cup T$ spočítej $M = \set{[A \to \mu x . \nu] \mid [A \to \mu . x \nu] \in z}$.
  1. Je-li $M \neq \emptyset$, vytvoř $z' = U(M)$
  2. pokud $z' \notin Z$, přidej ho a definuj $z' = \text{goto}(z, x)$.
5. **Tabulka:**
  1. **Sloupce** jsou _terminální symboly, symbol #_ (konec vstupního analyzovaného kódu), _neterminální symboly_ _(nedáváme tam rozšířený S’)_,
  2. **Řádky** jsou _čísla jednotlivých zásobníkových symbolů_ z množiny Z
6. **Doplnění přesunů**. Pro každý přesun $z_k = \text{goto}(z_i, x)$ napíšeme na **řádek i**, ve **sloupci x**, napíšeme **číslo k**.
7. **Doplnění redukcí:**
  1. Pravidla očíslujeme.
  2. Pro každou redukční položku $[A \to \alpha .]$ ve stavu $z_k$ zapiš do řádku $k$ **do sloupců podle rozhodovacího kritéria** hodnotu `+číslo pravidla`.
  3. U **SLR(1)** je _kritérium_: sloupce $x \in \text{Follow}(A)$.
8. **Ukončení:** do buňky pro redukční položku $[S' \to S.]$ a sloupec `#` zapiš `H` (Halt).

## 2.6 Kompletní příklad SLR(1)

$(1)\ E' \rightarrow E\\ (2)\ E \rightarrow E+i\\ (3)\ E \rightarrow i$

- Výpočet _zásobníkových symbolů a přechodů_

| $z'$ | $z$ | $N \cup T$ | $M\\ ----\\ U(M)$ |
| --- | --- | --- | --- |
| 0   |     |     | $[E' \rightarrow .E]\\ ----\\ [E \rightarrow.E+i]\\ [E \rightarrow .i]$ |
| 1   | 0   | $E$ | $[E' \rightarrow E.]\\ [E \rightarrow E.+i]\\$ |
| **==2==** | 0   | $i$ | $[E \rightarrow i.]$ |
| 3   | 1   | $+$ | $[E \rightarrow E+.i]\\$ |
| **==4==** | 3   | $i$ | $[E \rightarrow E+i.]\\$ |

- _Výpočet tabulky_:
  - Nejprve výpočet **Follow množiny**: $\text{Follow}(E)=\set{+,\#}$

|     | $+$ | $i$ | $\#$ | $E$ |
| --- | --- | --- | --- | --- |
| 0   |     | 2   |     | 1   |
| 1   | 3   |     | H   |     |
| 2   | +3  |     | +3  |     |
| 3   |     | 4   |     |     |
| 4   | +2  |     | +2  |     |

---

# 3. Realizace analyzátoru a generátory

- Bottom-up parser **nelze rozumně psát ručně** (na rozdíl od rekurzivního sestupu u LL). Ručně schůdná je jen analýza shora-dolů.
- **Generátory parserů** berou CFG s akcemi a vygenerují automat:
  - **yacc** (Yet Another Compiler Compiler) — součást Unixu, generuje **LALR(1)** automat.
  - **bison** — volně dostupná GNU alternativa yacc.
- Generátory obvykle umí **konflikty řešit deklarovanou precedencí/asociativitou** (`%left`, `%right`, `%prec`) místo přepisu gramatiky.