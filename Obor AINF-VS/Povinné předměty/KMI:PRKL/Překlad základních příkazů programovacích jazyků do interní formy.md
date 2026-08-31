# 1. Kde probíhá překlad příkazů

- _Překlad základních příkazů programovacího jazyka_ probíhá během **syntaktické a sémantické analýzy**. Syntaktický analyzátor _rozpoznává jednotlivé konstrukce programu_ (např. výrazy, přiřazení, podmínky nebo cykly) a v příslušných místech gramatických pravidel volá **sémantické funkce**.
- Tyto funkce současně provádějí **sémantickou kontrolu** programu (například ověření typové správnosti nebo kontrolu deklarací identifikátorů) a vytvářejí **interní reprezentaci programu**.
- Do interní formy se překládají pouze **imperativní části programu**, tedy příkazy a výrazy. Naproti tomu **deklarace a definice** se nevyjadřují pomocí instrukcí interní reprezentace, ale ukládají se do **tabulky symbolů**, která obsahuje _informace o identifikátorech, jejich typech, rozsahu platnosti a dalších vlastnostech_.

## 1.1 Proč se používá interní forma

- Odděluje **front-end** od **back-endu**: pro _m_ jazyků a _n_ platforem stačí $m + n$ překladačů místo $m \cdot n$
- Je vhodným vstupem pro **optimalizaci** — nad lineární formou se dobře hledají základní bloky, společné podvýrazy, konstantní výrazy.
- Je dostatečně nízkoúrovňová (jedna operace na instrukci), ale ještě strojově nezávislá (neomezený počet dočasných proměnných, symbolická návěští místo adres).

---

# 2. Pomocné prostředky při generování interní formy

## 2.1 Pomocné funkce

- Při generování interní formy používají sémantické funkce _několik pomocných funkcí_:

| Funkce | Co dělá |
| --- | --- |
| `newtemp()` | vytvoří **novou dočasnou proměnnou** (`t1`, `t2`, …) a vrátí referenci na ni |
| `newlabel()` | vytvoří **nové návěští** (`L1`, `L2`, …) a vrátí ho |
| `gen(op, arg1, arg2, res)` | **vygeneruje jednu čtveřici** a připojí ji na konec dosud vygenerované interní formy |

## 2.2 Atributy

- Sémantické funkce pracují s _atributy_ přidruženými symbolům gramatiky:

| Atribut | Význam |
| --- | --- |
| `E.ref` | **reference na operand nebo výsledek** operace.   Může ukazovat na:   (a) proměnnou deklarovanou ve zdrojovém programu,   (b) dočasnou proměnnou s výsledkem podvýrazu,   (c) literál (hodnotu) |
| `X.begin` | návěští umístěné **před** výrazem / příkazem |
| `X.lab` | návěští umístěné **uvnitř** výrazu / příkazu |
| `X.end` | návěští umístěné **za** výrazem / příkazem |

## 2.3 Notace `<sem>` a číslování symbolů

- V syntaktických pravidlech označuje zápis `<sem>` místo, ve kterém **parser zavolá odpovídající sémantickou funkci**. Toto volání _nemusí být pouze na konci pravidla_ – může se nacházet i uprostřed, což je důležité například _při překladu cyklů_ nebo _při zkráceném vyhodnocování logických výrazů_.

- Vyskytuje-li se týž symbol v pravidle vícekrát, indexuje se **v pořadí zápisu, včetně levé strany**:

$$
E_1 \to E_2 + E_3
$$

## 2.4 Použité operace čtveřic

- Při generování interní formy se používají následující operace:

| Operace | Význam |
| --- | --- |
| `+ - * /` | aritmetické operace |
| `=` | přiřazení: `(=, zdroj, -, cíl)` |
| `cmp` | srovnání dvou operandů (nastaví příznaky) |
| `jeq`, `jne` | podmíněný skok — jump equal / jump not equal |
| `jlt`, `jle`, `jgt`, `jge` | podmíněný skok — menší / menší nebo rovno / větší / větší nebo rovno |
| `jmp` | nepodmíněný skok |
| `lab` | **umístění návěští** na dané místo v kódu: `(lab, -, -, L)` |

---

# 3. Aritmetické výrazy a přiřazení

| Pravidlo | Sémantická akce |
| --- | --- |
| `E → E + E <sem>` | `E1.ref = newtemp()`   `gen('+', E2.ref, E3.ref, E1.ref)` |
| `E → E * E <sem>` | `E1.ref = newtemp()`   `gen('*', E2.ref, E3.ref, E1.ref)` |
| `E → (E) <sem>` | `E1.ref = E2.ref` (kopie reference) |
| `E → var <sem>` | `E.ref = var.ref` (kopie reference) |
| `E → const <sem>` | `E.ref = const.ref` (kopie reference) |
| `E → var = E <sem>` | `gen('=', E2.ref, -, var.ref)`   `E1.ref = E2.ref` |

```
E → E + E   <sem>
    sem:  E1.ref = newtemp()            // proměnná pro uložení výsledku
          gen('+', E2.ref, E3.ref, E1.ref)

E → E * E   <sem>
    sem:  E1.ref = newtemp()
          gen('*', E2.ref, E3.ref, E1.ref)

E → ( E )   <sem>
    sem:  E1.ref = E2.ref               // kopie reference — negeneruje se nic!

E → var     <sem>
    sem:  E.ref = var.ref               // kopie reference

E → const   <sem>
    sem:  E.ref = const.ref             // kopie reference

E → var = E <sem>
    sem:  gen('=', E2.ref, -, var.ref)
          E1.ref = E2.ref               // kopie reference
```

- Sémantická funkce se volá **až po vygenerování kódu všech (max obou) operandů**.
- **Závorky negenerují nic** — jejich role skončila při syntaktické analýze
- Pravidlo `E → var = E` ukazuje, že v jazycích C/C++ je **přiřazení výraz**, který má hodnotu
  - proto `E1.ref = E2.ref` (umožní zápis `a = b = c`).

---

# 4. Logické výrazy

- Logické výrazy lze při překladu převést do interní formy dvěma způsoby:
  - **stejně jako aritmetické výrazy**, kdy se vyhodnotí oba operandy a výsledek logické operace se uloží do dočasné proměnné (např. Pascal nebo Visual Basic),
  - pomocí **zkráceného vyhodnocování (short-circuit evaluation)**, které využívají jazyky C, C++ nebo C#.

## 4.1 Princip zkráceného vyhodnocování

> [!info]
> Při zkráceném vyhodnocování se pravý operand vyhodnocuje pouze tehdy, pokud je to nutné pro určení výsledku celého výrazu.
>
> - **logický součin** `&&` — pravý operand se nevyhodnotí, je-li levý `0` (false),
> - **logický součet** `||` — pravý operand se nevyhodnotí, je-li levý `≠0` (true).

## 4.2 Pravidlo pro `&&`

```
E → E <sem1> && E <sem2>

    // kód pro výpočet levého operandu E2
    sem1: E1.ref = newtemp()
          E1.end = newlabel()
          gen(=,   0, -, E1.ref)      // předpoklad: výsledek je 0 (false)
          gen(cmp, E2.ref, 0, -)
          gen(jeq, -, -, E1.end)      // levý je 0 → hotovo, výsledek 0

    // kód pro výpočet pravého operandu E3
    sem2: gen(cmp, E3.ref, 0, -)
          gen(jeq, -, -, E1.end)      // pravý je 0 → výsledek zůstane 0
          gen(=,   1, -, E1.ref)      // oba nenulové → výsledek 1 (true)
          gen(lab, -, -, E1.end)
```

> [!info]
> **Trik konstrukce:** do výsledku se **předem uloží „pesimistická" hodnota 0** a mění se na 1 jen tehdy, když se program dostane přes obě kontroly. Ušetří se tím jeden nepodmíněný skok.

## 4.3 Pravidlo pro `||`

```
E → E <sem1> || E <sem2>

    // kód pro výpočet levého operandu E2
    sem1: E1.ref = newtemp()
          E1.end = newlabel()
          gen(=,   1, -, E1.ref)      // předpoklad: výsledek je 1 (true)
          gen(cmp, E2.ref, 0, -)
          gen(jne, -, -, E1.end)      // levý ≠ 0 → hotovo, výsledek 1

    // kód pro výpočet pravého operandu E3
    sem2: gen(cmp, E3.ref, 0, -)
          gen(jne, -, -, E1.end)      // pravý ≠ 0 → výsledek zůstane 1
          gen(=,   0, -, E1.ref)      // oba nulové → výsledek 0 (false)
          gen(lab, -, -, E1.end)
```

> [!info]
> Je to **přesně duální** schéma k `&&`: předvyplní se 1 a skáče se při `jne`.

## 4.4 Pravidlo pro negaci `!`

```
E → ! E <sem>
    sem: E1.ref = newtemp()
         E1.end = newlabel()
         gen(=,   1, -, E1.ref)     // předpoklad: !E je 1
         gen(cmp, E2.ref, 0, -)
         gen(jeq, -, -, E1.end)     // E je 0 → výsledek 1, hotovo
         gen(=,   0, -, E1.ref)     // E je ≠ 0 → výsledek 0
         gen(lab, -, -, E1.end)
```

---

# 5. Podmínkový příkaz `if` a `if-else`

## 5.1 Neúplný podmínkový příkaz (`if` bez `else`)

```
S → if ( E ) <sem1> S <sem2>

    // kód pro výpočet výrazu E podmínky
    sem1: S1.end = newlabel()
          gen(cmp, E.ref, 0, -)
          gen(jeq, -, -, S1.end)     // podmínka nesplněna → přeskoč tělo

          // kód pro S2
    
    sem2: gen(lab, -, -, S1.end)
```

## 5.2 Úplný podmínkový příkaz (`if-else`)

```
S → if ( E ) <sem1> S <sem2> else <sem3> S <sem4>

    // kód pro výpočet výrazu E podmínky
    sem1: S3.begin = newlabel()       // návěští začátku else-větve
          S1.end   = newlabel()       // návěští za celým příkazem
          gen(cmp, E.ref, 0, -)
          gen(jeq, -, -, S3.begin)

          // kód pro S2 (then-větev)
    sem2: gen(jmp, -, -, S1.end)      // přeskočení else-větve!
    sem3: gen(lab, -, -, S3.begin)

          // kód pro S3 (else-větev)
    sem4: gen(lab, -, -, S1.end)
```

---

# 6. Cykly

## 6.1 Cyklus s podmínkou na začátku `while`

```
S → <sem1> while ( E ) <sem2> S <sem3>

    sem1: S1.begin = newlabel()
          S1.end   = newlabel()
          gen(lab, -, -, S1.begin)      // návěští PŘED podmínkou

          // kód pro výpočet výrazu E podmínky
    sem2: gen(cmp, E.ref, 0, -)
          gen(jeq, -, -, S1.end)

          // kód pro S2 (tělo cyklu)
    sem3: gen(jmp, -, -, S1.begin)      // návrat na test podmínky
          gen(lab, -, -, S1.end)
```

> [!warning]
> Pozor na umístění `<sem1>` — je **před klíčovým slovem** `while`, protože návěští začátku musí být vygenerováno **před kódem podmínky** (podmínka se testuje v každém průchodu).

## 6.2 Cyklus s podmínkou na konci `do-while`

```
S → <sem1> do S while ( E ) <sem2> ;

    sem1: S1.begin = newlabel()
          gen(lab, -, -, S1.begin)

          // kód pro S2 (tělo cyklu)
          // kód pro výpočet výrazu E podmínky
    sem2: gen(cmp, E.ref, 0, -)
          gen(jne, -, -, S1.begin)      // podmínka splněna → opakuj
```

## 6.3 Cyklus `for`

```
S → <sem1> for ( E ; E ; E ) <sem2> S <sem3>

          // kód pro výpočet výrazu E1 (inicializace)
    sem1: S1.lab = newlabel()
          S1.end = newlabel()
          gen(lab, -, -, S1.lab)

          // kód pro výpočet E2 (podmínka)
    sem2: gen(cmp, E2.ref, 0, -)
          gen(jeq, -, -, S1.end)

          // kód pro S2 (tělo cyklu)
          // kód pro výpočet výrazu E3 (krok / inkrementace)
    sem3: gen(jmp, -, -, S1.lab)
          gen(lab, -, -, S1.end)
```

**Dvě věci, které je nutné pochopit:**

1. **Návěští** `S1.lab` **musí být až za kódem inicializace** `E1`**.** Inicializace se provede právě jednou, mimo cyklus. Zápis pravidla s `<sem1>` úplně vlevo je zkratka — v reálné implementaci se sémantická akce vkládá až _za_ první `E`, tedy `for ( E ; <sem1> E ; E ) …`.
2. **Kód pro** `E3` **(krok) je ve zdrojovém textu _před_ tělem, ale v interní formě musí být _za_ tělem.** Jednoprůchodový generátor to řeší tak, že čtveřice pro `E3` **negeneruje přímo do výstupu**, ale do **pomocného bufferu**, a v `sem3` je z bufferu přepíše za kód těla.