> [!success]
> **Interní forma programu** je způsob, **jakým překladač reprezentuje program uvnitř sebe během překladu**. Je určena _pro jednotlivé fáze překladače_, kdy místo práce s původním textem programu pracují _další části překladače právě s touto interní reprezentací_.

- Je potřeba proto, že zdrojový program je **pouze text** (lineární posloupnost znaků bez struktury), zatímco interní forma umožňuje překladači _jednoduše_ _analyzovat strukturu programu, kontrolovat jeho správnost, provádět optimalizace a generovat cílový kód._
- Je **nezávislá na jazyce** a na **cílovém stroji**

- Překladače používají _dvě základní interní formy_:

|     | Kdo ji generuje | Kdo ji konzumuje | Podoba |
| --- | --- | --- | --- |
| **1. interní forma (1. IF)** | lexikální analyzátor | syntaktický analyzátor | posloupnost symbolů (tokenů) |
| **2. interní forma (2. IF)** | sémantický analyzátor | optimalizátor, generátor kódu | AST nebo lineární forma (čtveřice / trojice) |

---

# 1. První interní forma

- Vzniká při **lexikální analýze**.
- Zdrojový program je převeden na **posloupnost lexikálních symbolů (tokenů)**.

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

## 1.1 Vlastnosti

- Je **lineární** — stejné pořadí jako ve zdrojovém kódu, jen bez bílých znaků a komentářů.
- **Neobsahuje strukturu**
- Pro parser jsou tokeny 1. IF **terminálními symboly gramatiky**.

---

# 2. Druhá interní forma

- Vzniká při **sémantické analýze**. Používá se pro optimalizace a následné generování cílového kódu. Existují dvě nejčastější podoby:
  - **Stromová**
  - **Lineární**

> [!info]
> Druhá interní forma může být reprezentována _jedním nebo více způsoby_ **současně**. Překladač může využívat například abstraktní syntaktický strom, lineární interní formu nebo jejich kombinaci. Jednotlivé reprezentace se používají podle toho, která je **vhodnější pro danou fázi překladu**.

## 2.1 Stromová interní forma

> [!success]
> **AST (Abstract Syntax Tree)** je _stromová reprezentace programu_ odvozená z derivačního stromu _vytvořeného při syntaktické analýze_. Obsahuje **pouze** _informace důležité pro další překlad_, zatímco _zbytečné syntaktické prvky jsou odstraněny_.

- Struktura
  - **vnitřní uzly** představují _operace_ nebo _konstrukce jazyka_ (např. `+`, `*`, `if`, `while`),
  - **listy** představují _operandy_, například identifikátory nebo konstanty.
- Vynechává se zejména:
  - **uzly s neterminály** — slouží jen k vyjádření priority a asociativity
  - **závorky** — jejich úloha (změna priority) je už zachycena tvarem stromu
  - **oddělovače a omezovače** — `;`, `,`, `{`, `}`, `then`, `do` …

Zůstávají: **operátory jako vnitřní uzly** a **operandy (identifikátory, konstanty) jako listy**.

#### Příklad

Gramatika:

$E \to E + T \mid T\\ T \to T * F \mid F\\ F \to (,E,) \mid i$

- Výraz `a+b*(c+d)`

**Derivační strom** (uzly s neterminály, závorky, řetězová pravidla):

![[019f9522-2e11-70e5-8070-86ff0844fee4.png]]

**Odvozený AST:**

![[019f9522-684c-71af-b833-15e59e962b9f.png]]

Vynechány byly **všechny uzly s neterminály** a navíc i některé uzly s terminály (závorky).


### 2.1.1 Vlastnosti a použití

- **Strom nese prioritu i asociativitu implicitně svým tvarem**
- _Vhodný_ pro **optimalizace na úrovni výrazů** — konstantní skládání, algebraické úpravy, přeuspořádání operandů komutativních operací
- _Nevhodný_ pro **řízení toku a přidělování registrů** — tam je potřeba lineární posloupnost instrukcí.

## 3.2 Lineární interní forma

> [!success]
> **Lineární interní forma** je uložena jako **posloupnost jednoduchých instrukcí**, které lze snadno analyzovat, optimalizovat a převést na cílový kód.
>
> Nejběžnější lineární reprezentace jsou:
>
> - **trojice (triples)**,
> - **čtveřice (quadruples)**.

### 3.2.1 Trojice

> [!success]
> Každá instrukce má tvar:
>
> $$
> (\text{operace}, \text{operand1}, \text{operand2})
> $$
>
> Výsledek se **neukládá do pojmenované proměnné**, ale odkazuje se na něj číslem předchozí instrukce.

```
// Příkaz
x = a + b * c

// Trojice
(0) (*, b, c)
(1) (+, a, (0))
(2) (=, (1), x)
```

- Není potřeba vytvářet dočasné proměnné, ale _při přesouvání nebo optimalizaci instrukcí_ je **nutné upravovat všechny odkazy na jejich čísla**.

### 3.2.2 Čtveřice

> [!success]
> Každá instrukce má čtyři položky:
>
> $$
> (\text{operace}, \text{operand1}, \text{operand2}, \text{výsledek})
> $$
>
> - **operace** — jakou _operaci čtveřice reprezentuje_: aritmetická, logická, srovnání, větvení, přiřazení, umístění návěští, …
> - **operandy** — pokud je _operace má_
> - **výsledek** — _kam se ukládá výsledek_ (u aritmetiky), _na jaké návěští se skáče_ (u větvení), apod.

#### 3.2.2.1 Dočasné proměnné

> [!success]
> Protože každá instrukce smí obsahovat nejvýše jeden operátor, mezivýsledky se ukládají do **dočasných (temporary) proměnných** — konvenčně `t1, t2, t3, …`.

```clojure
// Příkaz
x = a + b * c

// Čtveřice
(*, b, c, t1)
(+, a, t1, t2)
(=, t2, -, x)
```

#### 3.2.2.2 Vlastnosti čtveřic

- **Instrukce jsou samostatné a nezávislé na pozici** — čtveřice se odkazují na operandy **jménem** (`t1`, `b`), ne pořadovým číslem. Proto lze čtveřice **přesouvat, mazat a vkládat** bez přepočítávání odkazů → **ideální pro optimalizaci**.
- Snadno se z nich staví **základní bloky a graf toku**.
- **Cena:** _vyšší paměťová náročnost_.

> [!warning]
> **Závěr:** _Forma trojic je sice úspornější, ale není vhodná pro překladače s optimalizací._ Při optimalizaci dochází ke změně pořadí instrukcí, což je u čtveřic mnohem jednodušší. **Proto reálné optimalizující překladače používají čtveřice.**