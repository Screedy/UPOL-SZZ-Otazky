> [!success]
> **Syntaktická analýza zdola-nahoru (bottom-up parsing)** sestavuje derivační strom od **listů** (terminály = tokeny z lexikálního analyzátoru) směrem ke **kořeni** (počáteční symbol gramatiky).  
> Parser tedy postupně rozpoznává _stále větší syntaktické celky_, až vznikne _počáteční symbol gramatiky_.

- Používá se **deterministický zásobníkový automat**, který (na rozdíl od LL analýzy) pracuje s **celým zásobníkem** — při jednom přechodu může odebrat _různý počet_ zásobníkových symbolů (tolik, kolik je symbolů na pravé straně redukovaného pravidla).
- _Na začátku_ je **zásobník prázdný**.
- _Na konci_ analýzy obsahuje pouze **počáteční symbol gramatiky**, _pokud je vstup syntakticky správný_.

**Základní operace:**

- **Přesun (shift)** — _Přesune jeden symbol_ ze vstupu na vrchol zásobníku.
- **Redukce (reduce)** — Na vrcholu zásobníku _nahradí řetězec_ odpovídající _pravé straně_ pravidla neterminálem z _levé strany_ téhož pravidla ($A \to \beta$⇒ na zásobníku se $\beta$ nahradí za $A$).

#### Ruční příklad — Shift/Reduce

Gramatika aritmetických výrazů:

$E \to E{+}E \mid E{-}E \mid E{*}E \mid E{/}E \mid i \mid (E)$

kde $T = \set{+,-,*,/,i,(,)}$, $N = {E}$. Analyzujeme výraz `(i+i)*i-i`.

Vrchol zásobníku je **vpravo**.

| Vstup | Zásobník | Akce |
| --- | --- | --- |
| `(i+i)*i-i` | _(prázdný)_ | přesun `(` |
| `i+i)*i-i` | `(` | přesun `i` |
| `+i)*i-i` | `(i` | redukce dle $E\to i$ |
| `+i)*i-i` | `(E` | přesun `+` |
| `i)*i-i` | `(E+` | přesun `i` |
| `)*i-i` | `(E+i` | redukce dle $E\to i$ |
| `)*i-i` | `(E+E` | redukce dle $E\to E{+}E$ |
| `)*i-i` | `(E` | přesun `)` |
| `*i-i` | `(E)` | redukce dle $E\to (E)$ |
| `*i-i` | `E` | přesun `*` |
| `i-i` | `E*` | přesun `i` |
| `-i` | `E*i` | redukce dle $E\to i$ |
| `-i` | `E*E` | redukce dle $E\to E{*}E$ |
| `-i` | `E` | přesun `-` |
| `i` | `E-` | přesun `i` |
|     | `E-i` | redukce dle $E\to i$ |
|     | `E-E` | redukce dle $E\to E{-}E$ |
|     | `E` | _(hotovo)_ |

> [!danger]
> **Pozor:** tato gramatika je _nejednoznačná_ — trasa výše je jen jedna z možných. V reálném automatu by na několika místech vznikly konflikty, které je nutné vyřešit (asociativita, precedence).


---

# 1. Rodina LR gramatik

- _Deterministickou analýzu zdola-nahoru_ umožňuje třída **LR gramatik**, které se dělí _do čtyř podtříd_:

$$
\text{LR(0)} \subset \text{SLR(1)} \subset \text{LALR(1)} \subset \text{LR(1)}
$$

- Čím je třída gramatik silnější, tím dokáže zpracovat větší množinu jazyků, ale parser je zároveň složitější a má více stavů.

| Podtřída | Charakteristika |
| --- | --- |
| **LR(0)** | Nejjednodušší parser, rozhoduje bez lookahead. |
| **SLR(1)** | Reduce se rozhoduje podle **Follow** množin. |
| **LALR(1)** | Kompromis _mezi velikostí parseru a jeho schopnostmi_.   V praxi **nejčastěji používaná varianta**. |
| **LR(1)** | _Nejsilnější_ třída LR parserů, ale automaty mají _nejvíce stavů_ a _jsou největší_. |

## 1.1 Význam písmen LR(k)

- **L** **(Left-to-right)** — vstupní řetězec se čte **zleva doprava**.
- **R (Rightmost derivation)** — činnost je založena na **pravé derivaci**, rekonstruované pozpátku.
- **k** (typicky 1) — počet symbolů **lookahead** (kolik symbolů vstupu vpředu stačí znát pro deterministické rozhodnutí).

> [!info]
> V praxi se nejčastěji používají **LALR(1)** gramatiky. Ve srovnání _s LR(1) vytvářejí výrazně menší automaty_, přitom dokážou zpracovat většinu programovacích jazyků. Proto je používají generátory parserů, jako jsou **Yacc** nebo **Bison**.

---

# 2. Základ konstrukce automatu

- Konstrukce deterministických automatů pro analýzu zdola-nahoru je _celkově výrazně složitější_ než automatů pro analýzu shora-dolů.

## 2.1 Rozšířená gramatika

- Před konstrukcí vytvoříme **rozšířenou gramatiku** $G' = (N \cup {S'}, T, P \cup {S' \to S}, S')$

> [!info]
> Přidání pravidla $S' \to S$ (s novým startovním symbolem) **usnadňuje detekci konce** analýzy.

## 2.2 LR položky(items)

> [!info]
> U analýzy **shora-dolů** parser vždy ví, podle _kterého pravidla postupuje_, protože pravidla **sám rozvíjí**. Proto _mu stačí na zásobníku uchovávat pouze terminály a neterminály_.
>
> U analýzy **zdola-nahoru** je situace _opačná_ – parser _postupně skládá symboly do větších celků_ a musí rozhodnout, **kdy provést redukci a podle kterého pravidla**. Samotné _terminály a neterminály k tomu nestačí_. Proto se používají **LR položky**, které **zachycují aktuální stav** rozpoznávání pravidel.

> [!success]
> **LR položka (item)** je _pravidlo gramatiky_, ve kterém je pomocí **tečky (•)** vyznačeno, jaká _část pravé strany pravidla již byla při analýze rozpoznána_.
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

#### Příklad

Pravidlo $A \to aBc$ má 4 položky:

| Položka | Význam |
| --- | --- |
| $[A \to .aBc]$ | ještě nebyl rozpoznán žádný symbol |
| $[A \to a.Bc]$ | byl rozpoznán symbol `a` |
| $[A \to aB.c]$ | byly rozpoznány symboly `aB` |
| $[A \to aBc.]$ | byla rozpoznána celá pravá strana pravidla – lze provést **redukci**. |


> [!warning]
> Pokud je **tečka na konci pravidla**, jedná se o **redukční položku**.
>
> Parser již _rozpoznal celou pravou stranu pravidla_ a _může ji nahradit neterminálem z levé strany pravidla_.

> [!note]
> **Navíc info — LR(1) položky:**
>
> - Při konstrukci **LALR(1)** se používají položky ve tvaru
>
> $$
> [A \to \mu . \nu; \ ω]
> $$
>
> kde **ω** je **prediktivní** **(lookahead)** **množina symbolů**, která určuje, pro _které vstupní symboly je dovoleno provést redukci_.

## 2.3 Uzávěr (closure)

> [!success]
> Při _konstruování nového zásobníkového symbolu_ se **vytváří uzávěr U(M)** _výchozí množiny položek gramatiky M_.
>
> Do uzávěru se **zahrnou počáteční položky** _všech možných pravidel_, jež mají **na levé straně** _neterminální symbo_l, který je v některé _z výchozích položek množiny M_ **právě za tečkou**. Výpočet uzávěru má _rekurzivní charakter_.
>
> $$
> U(M) = M \cup \set{[B \to .\beta] \mid [A \to \mu . B \nu] \in U(M),\ B \to \beta \in P}
> $$

> [!info]
> **Uzávěr (closure)** _rozšiřuje množinu LR položek_ o všechny položky, které _mohou být v daném stavu parseru potřeba_.

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

## 2.5 Postup sestavení automatu

1. Vytvoří se _rozšířená gramatika_.
2. Zkonstruujeme **počáteční zásobníkový symbol** $z_0 = U({[S' \to .S]})$ a _zařadíme jej do množiny zásobníkových symbolů_ $Z = {z_0}$
3. **Průběžný krok:** Pro každý dosud nezpracovaný symbol $z \in Z$ proveď krok 4.
4. Pro každý symbol $x \in N \cup T$ spočítej $M = \set{[A \to \mu x . \nu] \mid [A \to \mu . x \nu] \in z}$.
  1. Je-li $M \neq \emptyset$, vytvoř $z' = U(M)$
  2. Pokud $z' \notin Z$, přidej ho a definuj $z' = \text{goto}(z, x)$.
5. **Tabulka:**
  1. **Sloupce** jsou _terminální symboly, symbol #_ (konec vstupního analyzovaného kódu), _neterminální symboly_ _(nedáváme tam rozšířený S’)_,
  2. **Řádky** jsou _čísla jednotlivých zásobníkových symbolů_ z množiny Z
6. **Doplnění přesunů**. Pro každý přesun $z_k = \text{goto}(z_i, x)$ napíšeme na **řádek i**, ve **sloupci x**, napíšeme **číslo k**.
7. **Doplnění redukcí:**
  1. Pravidla očíslujeme.
  2. Pro každou redukční položku $[A \to \alpha .]$ ve stavu $z_k$ zapiš do řádku $k$ **do sloupců podle rozhodovacího kritéria** hodnotu `+číslo pravidla`.
  3. U **SLR(1)** je kritérium: sloupce $x \in \text{Follow}(A)$.
8. **Ukončení:** do buňky pro redukční položku $[S' \to S.]$ a sloupec `#` zapiš `H` (Halt).

> [!warning]
> Výsledkem konstrukce je **deterministický automat**, jehož stavy tvoří množiny LR položek. Parser pak podle tohoto automatu rozhoduje, zda provede **přesun (Shift)**, **redukci (Reduce)** nebo přijme vstup.

---

# 3. Konflikty

- Při sestavování **LR tabulky** může nastat situace, kdy pro stejný stav a vstupní symbol existuje **více možných akcí**. Parser pak nedokáže jednoznačně rozhodnout, jak pokračovat. Taková situace se označuje jako **konflikt**.
- Rozlišují se dva základní typy konfliktů:

## 3.1 Přesun-redukce (shift-reduce)

- Nastává, když parser může buď:
  - **provést přesun (Shift)** dalšího vstupního symbolu, nebo
  - **provést redukci (Reduce)** podle některého pravidla.
- Parser tedy neví, zda má pokračovat ve čtení vstupu, nebo již rozpoznal pravou stranu pravidla a má provést redukci.

## 3.2 Redukce-redukce (reduce-reduce)

- Nastává, když lze ve stejném okamžiku provést **redukci podle dvou různých pravidel**.
- Parser tedy nedokáže určit, které pravidlo je správné.

## 3.3 Řešení konfliktů

1. **Použitím silnějšího typu LR parseru** — jen teoreticky, generátory LR(1) nejsou běžně dostupné.
2. **Úpravou gramatiky**, aby byla jednoznačná. Spolehlivé, ale pracné a obvykle vede k větší gramatice.
3. **Vyřešit konflikt ručně** — v každé konfliktní buňce podle sémantiky jazyka (asociativita, precedence) ponechat _jednu_ akci a ostatní smazat.

## 3.4 Příklad

```
E' → E
E  → E+E
E  → E*E
E  → (E)
E  → i
```

- Tato gramatika je **nejednoznačná**, takže konflikty budou v _libovolném_ LR automatu.
- Pro jednoduchost se volí **SLR(1)** konstrukce.
- `Follow(E) = {+, *, ), #}`, redukce se doplní do sloupců podle Follow.
- Vzniklá tabulka má konflikty (výřez pro `+` a `*`):

| Stav | `+` | `*` |
| --- | --- | --- |
| 7   | `4 +2` | `5 +2` |
| 8   | `4 +3` | `5 +3` |

- Konflikty se vyřeší podle **asociativity** a **precedence** operátorů:
  - **Konflikt 4/+2 ve stavu 7 (vstup** `+`**)** — nastane u `i+i+i`. Volba _redukce_ dá strom `(i+i)+i` (levá asociativita `+`), volba _přesunu_ dá `i+(i+i)`. Součet je levě asociativní ⇒ v tabulce ponecháme **redukci** (`+2`).
  - **Konflikt 5/+2 ve stavu 7 (vstup** `*`**)** — nastane u `i+i*i`. _Přesun_ dá `i+(i*i)`, _redukce_ dá `(i+i)*i`. Součin má vyšší precedenci ⇒ ponecháme **přesun** (`5`).
  - **Konflikt 4/+3 ve stavu 8 (vstup** `+`**)** — nastane u `i*i+i`. Součin má vyšší precedenci ⇒ redukovat `i*i` dřív ⇒ ponecháme **redukci** (`+3`).

> [!info]
> **Alternativa: přepis gramatiky** — Konflikty lze odstranit i přepsáním na jednoznačnou gramatiku.

---

# 4. Zotavení z chyby při analýze zdola-nahoru

> [!success]
> Chyba syntaktické analýzy se **snadno zjistí** — automat se zastaví, pokud:
>
> - v _tabulce automatu_ **není** pro současný symbol _na vrcholu zásobníku_ a symbol _na vstupu_ **žádná akce** (ani přesun, ani redukce)

> [!danger]
> Obtížnější je **zotavení** — synchronizace vstupu s automatem tak, aby mohl pokračovat.

## 4.1 Obecné metody zotavení

- **Oprava zdrojového kódu** (vynechání/vložení/náhrada symbolů) — přesná, ale riskantní.
  - Špatná oprava může vyvolat novou chybu.
  - Při vkládání symbolů může kód „nekontrolovaně růst".
- **Panický mód (panic mode)** — bezpečnější.
  - Po chybě se vynechává vstup až po nejbližší **význačný symbol** k **_omezovačům_** (typicky `;`, `{`, `}`, `#`).
  - **Nevýhoda**: může se vynechat i syntakticky správná část kódu.

## 4.2 Metoda pro analýzu zdola nahoru

1. Stanovíme **význačné neterminální symboly** (např. z pravidel pro deklarace, příkazy, výrazy atd.) Pro každý z těchto symbolů přidáme do gramatiky pravidlo pro chybový stav:  
  $A → \text{chyba}$
2. Při chybě _odstraníme ze zásobníku_ zásobníkové symboly tak dlouho, až **najdeme zásobníkový**  
  **symbol s položkou** ve tvaru  
  $[B→\alpha.A\beta]$  
  kde $A$ je _některý ze stanovených význačných neterminálních symbolů_.
3. Použitím _redukce_ podle pravidla  
  $A → \text{chyba}$  
  se na _zásobník přidá zásobníkový symbol_ s položkou  
  $[B→\alpha A.\beta]$  
  který najdeme v tabulce automatu **na řádku zásobníkového symbolu**, _který je právě na vrcholu_  
  _zásobníku_, a **ve sloupci pro symbol** $A$.
4. Dále ze vstupu **odstraníme symboly**, _dokud se nedostaneme k symbolu_, který **patří do množiny**  
  $\text{Follow}(A)$.
#### Příklad
  
  _Máme gramatiku:_
  
  ```
  E' → E
  E  → E+E
  E  → E*E
  E  → (E)
  E  → i
  ```
  
  **Tabulka** a **přidané pravidlo**:
  
  ![[019fdb51-df01-7137-9cc6-fabd0133402c.png]]
  
  _Průběh_:
  
  ![[019fdb52-cf98-76e9-8275-a8f2d4832aba.png]]
  