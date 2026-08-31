# 1. Úloha lexikální analýzy v překladači

> [!success]
> Lexikální analýza je **první část překladače**, která je součástí tzv. **front-endu**. Lexikální analyzátor čte zdrojový program znak po znaku a vykonává tyto činnosti:
>
> - **Rozpoznává lexikální symboly** (tokeny) zdrojového programu a převádí program do **1. interní formy** — _posloupnosti symbolů_.
> - **Vynechává bílé znaky** — mezery, tabulátory, konce řádků — které slouží **jen** k čitelnosti kódu.
> - **Vynechává komentáře** (v jazycích C/C++ to dělá preprocesor).

## 1.1 Proč je lexikální analýza oddělena od syntaktické

- Analýza syntaxe je rozdělena na lexikální a syntaktickou ze dvou praktických důvodů:
  - **Jednoduchost popisu:** Lexikální symboly _mají jednoduchou strukturu_ — dají se popsat **regulárními gramatikami** a realizovat **konečným automatem**. _Není potřeba síla bezkontextové gramatiky_.
  - **Zjednodušení syntaktického analyzátoru:** Syntaktický analyzátor _pracuje s posloupností tokenů_ (1. interní formou), **nemusí se zabývat strukturou** _jednotlivých atomů_. Tím se _zjednodušuje návrh bezkontextové gramatiky_ pro syntaxi jazyka.

## 1.2 Začlenění lexikálního analyzátoru do překladače

- Lexikální analyzátor je první částí překladače a tvoří rozhraní mezi zdrojovým kódem a syntaktickým analyzátorem.
- Jeho úkolem je postupně číst zdrojový program, _rozpoznávat jednotlivé tokeny a předávat je syntaktickému analyzátoru_. Bývá implementován jako **jedna funkce**, která je _volána pokaždé_, když syntaktický analyzátor **potřebuje další lexikální symbol**.

> [!info]
> Nejčastěji je tato funkce označována jako `lex()` nebo `yylex()` (u nástroje Lex/Flex)

> [!danger]
> Důležité je pochopit, že **lexikální analyzátor neprochází celý program dopředu a nevytvoří seznam všech tokenů**. Místo toho pracuje **postupně**.

- _Typický průběh je následující_:
  1. Syntaktický analyzátor _analyzuje program_
  2. **Potřebuje token**
  3. **Zavolá funkci** `lex()`,
  4. Lexikální analyzátor _přečte znaky až do konce prvního tokenu_
  5. **Vrátí tento token** syntaktickému analyzátoru
  6. Syntaktický analyzátor _pokračuje v analýz_e
  7. _Kdykoliv potřebuje další token, znovu zavolá_ `lex()`.

```
Zdrojový program → [Lexikální analyzátor] ← volání lex() → [Syntaktický analyzátor]
```

## 1.3 Dva způsoby realizace

- Dva základní způsoby realizace lexikálního analyzátoru:
  - **Ruční sestavení** — programátor napíše lexer ručně (stavový automat implementovaný pomocí `switch`/`case` nebo tabulky přechodů).
  - **Generátor lexikálních analyzátorů** — nejznámější je **Lex**, jeho volně dostupnou variantou je **Flex** (Fast Lexical Analyzer Generator, projekt GNU).

![[019f853f-4bc7-7221-92fe-8e22a369b802.png]]

---

# 2. Lexikální symboly (tokeny) a lexémy

> [!success]
> - **Lexém** je _konkrétní posloupnost znaků_ ve zdrojovém programu, kterou lexikální analyzátor **rozpozná jako jednu jednotku**.
> - **Lexikální symbol (token)** představuje **typ** _tohoto lexému_. Kromě typu může _obsahovat také jeho hodnotu_ (např. název identifikátoru nebo hodnotu konstanty).

## 2.1 Druhy lexikálních symbolů

- Tokeny (lexikální symboly) zdrojového programu zahrnují:

| Druh | Příklady |
| --- | --- |
| Klíčová slova | `int`, `typedef`, `enum`, `class`, `if`, `for`, `return` |
| Identifikátory | `i`, `suma`, `pocet`, `Zamestnanec` |
| Konstanty | `12`, `1.5E5`, `"Eva"`, `'&'` |
| Oddělovače | `,` (čárka) |
| Omezovače | `{`, `}`, `[`, `]`, `(`, `)`, `;` |
| Operátory | `+`, `-`, `*`, `%`, `++`, `<=`, `=`, `>>=` |

## 2.2 Interní forma — posloupnost symbolů

- Výstupem lexikální analýzy je **první interní forma programu**, označovaná jako **posloupnost symbolů (tokenů)**.

> [!info]
> Každému druhu lexikálního symbolu je přiřazeno **celé číslo** (kód tokenu).
>
> Typicky se používá následující způsob:
>
> - **Jednoznakové symboly** používají _přímo ASCII hodnotu znaku_ (např. `)` → 41, `+` → 43).
> - **Víceznakové symboly** mají vlastní číselné kódy, _zpravidla větší než 255_. Např. celé číslo → 261, operátor `==` → 280.
>
> U tokenů, které kromě typu nesou také hodnotu (identifikátory a konstanty), lexer předává obě informace.
>
> - Číslo `12` (typ `int`) → binární forma (typicky 32 bitů).
> - Číslo `1.5` (typ `double`) → 64bitový formát IEEE 754.
> - Znak `'A'` → ASCII kód 65 (1 byte), resp. při Unicode na 2 nebo 4 byty.

> [!note]
> **Příklad.** Program v Pascalu:
>
> ```pascal
> program Matice;
> var i,j of integer;
> ...
> ```
>
> Lexer rozpozná tokeny: `program` `Matice` `;` `var` `i` `,` `j` `of` `integer` `;` …

---

# 3. Rozpoznání konce lexikálního symbolu

- Ve zdrojovém programu jsou jednotlivé lexémy zapsány za sebou a často mezi nimi nejsou žádné mezery. Úkolem lexikálního analyzátoru je proto určit, **kde jeden lexém končí a kde začíná další**.
- K tomu používá pravidlo **nejdelší shody** (_longest match_ nebo také _maximal munch_).

> [!success]
> Lexikální analyzátor se snaží k právě rozpoznávanému tokenu **přidávat další znaky tak dlouho**, dokud tím _vzniká delší platný token_. Jakmile další _znak již do tokenu nepatří_, _token ukončí a začne rozpoznávat následující_. Pokud je tímto znakem whitespace, _následně jej přeskočí_ a _začne rozpoznávat další token_.

**Příklad 1.** V jazyce C: při rozpoznání `!` se podívá na další znak — je-li to `=`, přidá ho a rozpozná `!=`.

**Příklad 2.** Výraz `b+++c` je rozdělen na `b` `++` `+` `c` (interpretace `b++ + c`), protože `++` je delší než `+`.

**Příklad 3.** Výraz `b+++++c` je rozdělen na `b` `++` `++` `+` `c`, což způsobí chybu. (syntaktickém analyzátoru)

**Příklad 4.** Naopak `b+++ ++c` se rozdělí na `b ++ + ++ c`, což je korektní.

---

# 4. Rozpoznávání klíčových slov

- Ve většině programovacích jazyků (např. C, C++, Java) mají **klíčová slova stejnou syntaxi jako identifikátory**. Z pohledu lexikálního analyzátoru tedy nelze podle samotného tvaru okamžitě poznat, zda se jedná o klíčové slovo nebo běžný identifikátor.

```
if
while
return
pocet
suma
```

## 4.1 Rozpoznávání klíčových slov lexikálním analyzátorem

1. Lexer nejdřív běžným způsobem rozpozná identifikátor.
2. Poté jeho text vyhledá v **hashovací tabulce klíčových slov**.
  1. Pokud je _nalezen_, vrátí **token příslušného klíčového slova,**
  2. Pokud _nalezen není_, vrátí **token identifikátoru**.

> [!info]
> **Příklad.** Pro klíčová slova jazyka C se používá specifická hashovací funkce:
>
> $$
> h(z_1 z_2 \ldots z_k) = \text{kod}(z_1) + \text{kod}(z_k) + k
> $$
>
> kde `kod` je speciální kódovací tabulka. Výsledkem je tabulka 32 řádků, kde každé klíčové slovo má unikátní pozici.
>
> ![[019fbed8-993e-717e-98b3-224583936003.png]]

## 4.2 Rozpoznávání klíčových slov syntaktickým analyzátorem

- Lexer předává klíčová slova jako _běžné identifikátory_, **rozlišení** provede **až parser** (syntaktický analyzátor)
- Tento přístup je jednodušší pro lexer, ale komplikuje syntaktickou analýzu.

---

# 5. Regulární gramatiky a regulární výrazy

- Tokeny mají poměrně jednoduchou strukturu, a proto je lze popsat **regulárními gramatikami**. Ty jsou ekvivalentní **konečným automatům**, díky čemuž lze podle nich efektivně sestavit lexikální analyzátor.
- V praxi se však _regulární gramatiky používají jen výjimečně_. Mnohem častěji se stejné jazyky popisují pomocí **regulárních výrazů**, které jsou výrazně stručnější.

## 5.1 Regulární gramatiky

- Regulární gramatiky jsou **gramatiky typu 3 v Chomského hierarchii**. Používají se k popisu **regulárních jazyků**, tedy _jazyků, které lze rozpoznat konečným automatem_.

> [!success]
> Regulární gramatika $G = (N, T, P, S)$ má pravidla tvaru:
>
> $A \to aB \quad A, B \in N\\A \to a \quad \ \ \ a \in T$

> [!info]
> **Věta.**
>
> _Ke každé regulární gramatice_ existuje **deterministický konečný automa**t, který **rozpoznává stejný jazyk**.
>
> _Ke každému deterministickému konečnému automatu_ lze vytvořit **ekvivalentní regulární gramatiku**.

**Příklad.**

- Uvažujme _identifikátor programovacího jazyka_.
- Pravidlo říká:
  - první znak musí být písmeno nebo podtržítko,
  - další znaky mohou být písmena, číslice nebo podtržítka.
- Regulární gramatika by musela obsahovat pravidlo pro **každé možné písmeno, číslici i podtržítko**. Taková gramatika je velmi rozsáhlá a nepřehledná.
- Proto se v praxi **používají regulární výrazy**.

## 5.2 Regulární výrazy

- Regulární výraz je _kompaktní způsob zápisu regulárního jazyka_. Popisuje stejný jazyk jako regulární gramatika, ale mnohem stručněji.
- _Regulární výrazy se používají_ například **při tvorbě lexikálních analyzátorů** v nástrojích **Lex** nebo **Flex**, kde se pomocí nich _zapisují pravidla pro jednotlivé tokeny_.

> [!success]
> **Pravidla pro sestavení** regulárních výrazů nad abecedou $T$:
>
> - Každý symbol $x \in T$ je regulární výraz.
> - Prázdný řetězec $\varepsilon$ je regulární výraz.
> - Jsou-li $\alpha$ a $\beta$ regulární výrazy, pak jsou i regulární výrazy:
>   - $\alpha\beta$— **zřetězení**
>   - $\alpha \mid \beta$— **alternativa** ($\alpha$ anebo $\beta$)
>   - $\alpha^+$— **pozitivní uzávěr**
>   - $(\alpha)$— **závorky** pro prioritu
>
> **Priorita operátorů** (od nejvyšší): uzávěr ($*$,$+$) > zřetězení > alternativa ($\mid$).

**Příklad.**

- Místo rozsáhlé regulární gramatiky lze identifikátor zapsat jednoduše

```
[A-Za-z_][A-Za-z0-9_]*
```

---

# 6. Chyby rozpoznávané při lexikální analýze

> [!danger]
> Lexikální analyzátor kontroluje pouze **správnost zápisu jednotlivých tokenů**. Neřeší jejich význam ani správnost programu jako celku – to je úkolem syntaktické a sémantické analýzy.

Lexikální analyzátor rozpozná tyto druhy chyb:

- **Příliš dlouhý identifikátor** — překročení maximální povolené délky (např. ve Fortranu max 6 znaků).
- **Chybný zápis čísla** — např. `1E` (chybí exponent), `1.2.3` (dvě desetinné tečky).
- **Číslo mimo rozsah** — hodnota přesahuje kapacitu datového typu.
- **Chybný zápis znaku** — např. `'AB'` (více než jeden znak v znakové konstantě).
- **Neukončený řetězec** — např. `"AB` (chybí uzavírací `"`).
- **Řetězec příliš dlouhý** — překročení maximální délky (v Pascalu max 255).
- **Neplatný znak** — na vstupu je znak, který netvoří žádný platný lexikální symbol. Např. v jazyce C znaky `$` a `@`.

---

# 7. Vstup a výstup lexikální analýzy

|     | Popis |
| --- | --- |
| **Vstup** | Zdrojový kód — proud znaků (ASCII / Unicode) |
| **Výstup** | 1. interní forma — posloupnost tokenů (typ + případná hodnota) |
| **Konzument** | Syntaktický analyzátor (parser), který volá `lex()` pro další token |
| **Vedlejší výstupy** | Chybová hlášení; naplnění tabulky symbolů (záznamy o identifikátorech a konstantách) |