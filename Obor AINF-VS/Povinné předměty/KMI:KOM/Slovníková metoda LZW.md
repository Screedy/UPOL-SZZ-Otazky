## 3. LZW

### 3.1 Popis a princip

- **LZW** je _slovníková kompresní metoda_ z rodiny LZ algoritmů. Přesněji patří _do rodiny LZ78_ a její **nejpopulárnější variantou**.

> [!warning]
> **Vstup:**
>
> - Posloupnost symbolů ze zdrojové abecedy
> - Zdrojová abeceda$A$
>
> **Výstup**:
>
> - Komprimovaná data

#### 3.1.1 Klíčový rozdíl oproti LZ78

- **LZ78** na výstupu zapisuje **dvojici (index, symbol)** - index nejdelšího nalezeného slova ve slovníku + další symbol za ním.
- **LZW** na výstupu zapisuje **pouze index** - žádný extra symbol. To je možné díky tomu, že slovník je inicializován všemi symboly vstupní abecedy (ne prázdný jako u LZ78).

---

## 3.2 Pseudokód

```
Inicializuj slovník D: pro každý symbol a ∈ A přidej slovo „a" s indexem.
x ← prázdný řetězec

while načti ze vstupu symbol a ∈ A do
    if xa je ve slovníku then
        x ← xa                          // prodluž aktuální slovo
    else
        ulož xa jako další položku do slovníku
        zapiš na výstup kód indexu x ve slovníku
        x ← a                           // začni nové slovo od symbolu a

if x ≠ prázdný řetězec then
    zapiš na výstup kód indexu x ve slovníku   // poslední slovo
```

- Algoritmus čte vstup symbol po symbolu a snaží se najít **nejdelší slovo** (řetězec), které už má ve slovníku. Jakmile narazí na situaci, kdy by přidání dalšího symbolu vedlo ke slovu, které ve slovníku není:
  1. **Zapíše na výstup index** dosud nalezeného nejdelšího slova.
  2. **Přidá do slovníku** nové slovo = dosavadní slovo + nový symbol.
  3. **Začne od nového symbolu** jako od začátku nového hledání.

---

## 3.3 Příklad kódování — krok po kroku

#### Příklad

**Vstup:** `barbaraabarboraubaru`  
**Abeceda:** $A = \set{a, b, r, u, o}$

**Počáteční slovník:**

| Index | Slovo |
| --- | --- |
| 1   | a   |
| 2   | b   |
| 3   | r   |
| 4   | u   |
| 5   | o   |

**Krok po kroku:**

| Krok | Čtený symbol | x (aktuální) | xa  | xa ve slovníku? | Akce |
| --- | --- | --- | --- | --- | --- |
| 1   | b   | ""  | b   | ANO | x ← `b` |
| 2   | a   | `b` | ba  | NE  | výstup: **2** (b), slovník[6]=ba, x ← `a` |
| 3   | r   | `a` | ar  | NE  | výstup: **1** (a), slovník[7]=ar, x ← `r` |
| 4   | b   | `r` | rb  | NE  | výstup: **3** (r), slovník[8]=rb, x ← `b` |
| 5   | a   | `b` | ba  | ANO | x ← `ba` |
| 6   | r   | `ba` | bar | NE  | výstup: **6** (ba), slovník[9]=bar, x ← `r` |
| 7   | a   | `r` | ra  | NE  | výstup: **3** (r), slovník[10]=ra, x ← `a` |
| 8   | a   | `a` | aa  | NE  | výstup: **1** (a), slovník[11]=aa, x ← `a` |
| 9   | b   | `a` | ab  | NE  | výstup: **1** (a), slovník[12]=ab, x ← `b` |
| 10  | a   | `b` | ba  | ANO | x ← `ba` |
| 11  | r   | `ba` | bar | ANO | x ← `bar` |
| 12  | b   | `bar` | barb | NE  | výstup: **9** (bar), slovník[13]=barb, x←`b` |
| 13  | o   | `b` | bo  | NE  | výstup: **2** (b), slovník[14]=bo, x ← `o` |
| 14  | r   | `o` | or  | NE  | výstup: **5** (o), slovník[15]=or, x ← `r` |
| 15  | a   | `r` | ra  | ANO | x ← `ra` |
| 16  | u   | `ra` | rau | NE  | výstup: **10** (ra), slovník[16]=rau, x←`u` |
| 17  | b   | `u` | ub  | NE  | výstup: **4** (u), slovník[17]=ub, x ← `b` |
| 18  | a   | `b` | ba  | ANO | x ← `ba` |
| 19  | r   | `ba` | bar | ANO | x ← `bar` |
| 20  | u   | `bar` | baru | NE  | výstup: **9** (bar), slovník[18]=baru, x←`u` |
| konec | —   | `u` | —   | —   | výstup: **4** (u) |

**Výstup:** `2 1 3 6 3 1 1 9 2 5 10 4 9 4`

**Výsledný slovník (nové položky):**

| Index | Slovo |
| --- | --- |
| 6   | ba  |
| 7   | ar  |
| 8   | rb  |
| 9   | bar |
| 10  | ra  |
| 11  | aa  |
| 12  | ab  |
| 13  | barb |
| 14  | bo  |
| 15  | or  |
| 16  | rau |
| 17  | ub  |
| 18  | baru |


---

## 3.4 Dekódování

- Dekodér musí rekonstruovat **stejný slovník**, jaký vytvořil kodér, aniž by dostal slovník jako vstup.

```
Inicializuj slovník D: pro každý symbol a ∈ A přidej slovo „a" s indexem.
xp ← prázdný řetězec

while načti ze vstupu a dekóduj kód indexu i ve slovníku do
    if i je index další položky ve slovníku then // Dosud neuložené
        x ← xp
    else
        x ← slovo na indexu i ve slovníku

    if xp ≠ prázdný řetězec then       //Ukládání nové položky do slovníku
        a ← první symbol x
        ulož xp·a jako další položku do slovníku

    xp ← x
    zapiš na výstup slovo x
```

### Příklad dekódování - krok po kroku

#### Příklad

**Vstup:** `2 1 3 6 3 1 1 9 2 5 10 4 9 4`  
**Počáteční slovník:**

| Index | Slovo |
| --- | --- |
| 1   | a   |
| 2   | b   |
| 3   | r   |
| 4   | u   |
| 5   | o   |

| Krok | Index i | Slovo x (výstup) | xp (předchozí) | Nová položka |
| --- | --- | --- | --- | --- |
| 1   | 2   | `b` | ""  | —   |
| 2   | 1   | `a` | b   | 6: b+a = `ba` |
| 3   | 3   | `r` | a   | 7: a+r = `ar` |
| 4   | 6   | `ba` | r   | 8: r+b = `rb` |
| 5   | 3   | `r` | ba  | 9: ba+r = `bar` |
| 6   | 1   | `a` | r   | 10: r+a = `ra` |
| 7   | 1   | `a` | a   | 11: a+a = `aa` |
| 8   | 9   | `bar` | a   | 12: a+b = `ab` |
| 9   | 2   | `b` | bar | 13: bar+b = `barb` |
| 10  | 5   | `o` | b   | 14: b+o = `bo` |
| 11  | 10  | `ra` | o   | 15: o+r = `or` |
| 12  | 4   | `u` | ra  | 16: ra+u = `rau` |
| 13  | 9   | `bar` | u   | 17: u+b = `ub` |
| 14  | 4   | `u` | bar | 18: bar+u = `baru` |

**Dekódovaný výstup:** `b a r ba r a a bar b o ra u bar u` = `barbaraabarboraubaru` ✓


---

## 3.5 Datová reprezentace slovníku

### Trie (n-ární strom)

Slovník LZW lze přirozeně reprezentovat jako **trie** (prefixový strom), stejně jako u LZ78:

- Kořen odpovídá prázdnému řetězci.
- Děti kořene jsou symboly abecedy $A$(počáteční slovník).
- Každý uzel odpovídá jednomu slovu ve slovníku.
- Hrana je označena symbolem, uzel nese index slova.

**Výhoda trie:** Vyhledávání nejdelšího slova ve slovníku je jednoduché - procházíme strom po hranách podle čtených symbolů, dokud existuje odpovídající hrana.

### Hashovací tabulka

V praxi se pro **kódování** používá **hešovací tabulka** pro rychlé vyhledávání, zda slovo$xa$je ve slovníku:

- **Klíč**: dvojice (index slova$x$, symbol$a$).
- **Hodnota**: index slova$xa$ve slovníku.
- Časová složitost vyhledávání: $O(1)$amortizovaně.

Pro **dekódování** stačí **tabulka (pole)** s řádky slovníku, kde každý řádek ukládá:

- Index rodičovského slova (prefix$x$).
- Symbol$a$(poslední symbol slova$xa$).

Při rekonstrukci slova se prochází řetěz rodičů od daného indexu zpět ke kořeni - slovo se čte pozpátku. Velikost slovníku bývá typicky jednotky až desítky tisíc položek (běžně $2^{16} = 65536$).

#### Příklad

| klíč (index rodiče, symbol) | hodnota (index slova) |
| --- | --- |
| (2, a) | 6   |
| (1, r) | 7   |
| (3, b) | 8   |
| (6, r) | 9   |
| (3, a) | 10  |
| (1, a) | 11  |
| (1, b) | 12  |
| (9, b) | 13  |
| (2, o) | 14  |
| (5, r) | 15  |
| (10, u) | 16  |
| (4, b) | 17  |
| (9, u) | 18  |


---

## 3.6 Varianty LZW

- **LZC**:
  - **Proměnná šířka indexu** – velikost slovníku se postupně **zdvojnásobuje** od `512`až po `2^16`.
  - **Po naplnění** slovníku se slovník stává **statickým** (přestane se přidávat).
  - Při **poklesu kompresního poměru pod mez** se slovník **vymaže** a začíná se nanovo.
  - **Vylepšení – Exclusion principle** využívá informaci o předchozím dekódovaném slovu. Ze seznamu možných kandidátů se _vyloučí položky, které nemohou následovat_, a index se pak kóduje _vzhledem k menší množině_ zbývajících slov. Tím lze snížit počet bitů potřebných pro kódování indexů.**u.**
- **LZT**:
  - Varianta LZC.
  - **Po naplnění** slovníku se nezmrazuje ani nemaže celý slovník, ale **vyřadí se slovo s nejméně kódovaným indexem**.
  - Kromě slovníku se vede **seznam slov setříděný podle počtu kódování jejich indexu.**
  - Podobné **LZ77**, ale „posuvné okno“ je nad slovy seřazenými **podle kódování indexu**, ne podle pořadí slov na vstupu.
- **LZMW**:
  - **Po naplnění** slovníku se vyřadí slovo _s nejméně kódovaným indexem,_ které **není prefixem jiného slova**
  - **Do slovníku se ukládá zřetězení** _předchozího a aktuálního zakódovaného slova_. Nové položky tak rostou rychleji než o jeden symbol, což umožňuje rychlejší naučení dlouhých opakujících se vzorů.
  - Slovník **nemůže být trie** – ne každý prefix slova ve slovníku tam musí být. Řeší se **příznakem platnosti** u záznamů; při vyhledávání se od neplatných záznamů **vrací zpět**.
- **LZAP**:
  - Varianta LZMW.
  - Zřetězení se neukládá jen s celým dalším slovem, ale se **všemi jeho neprázdnými prefixy**.
  - Důsledky: **větší slovník**, ale protože je každý prefix přítomen, **není třeba se při vyhledávání vracet** (lze reprezentovat jako trie).

---

## 7. Implementace a praktické aspekty

### Časová složitost

- **Kódování:** Pro každý vstupní symbol se provede jedno vyhledávání ve slovníku. S hashovací tabulkou je to $O(1)$amortizovaně → celková složitost $O(n)$pro vstup délky $n$.
- **Dekódování:** Podobně $O(n)$, ale rekonstrukce slova z tabulky vyžaduje průchod řetězu rodičů (délka slova) → v praxi stále velmi rychlé.

### Prostorová složitost

- Slovník: $O(S)$, kde $S$je maximální počet položek slovníku.
- Každá položka: index rodiče + symbol → konstantní velikost na položku.

### Výhody LZW

- Jednoduchá a rychlá komprese i dekomprese.
- Adaptivní - slovník se buduje za běhu, nepotřebuje předběžný průchod daty.
- Na výstupu jsou **pouze indexy** (žádné symboly navíc jako u LZ78) - úspornější výstup.
- Dekodér nepotřebuje dostat slovník jako vstup - rekonstruuje si ho sám.

### Nevýhody LZW

- **Pomalá adaptace** (zděděno z LZ78): do slovníku se přidávají slova jen o 1 symbol delší než slovo již ve slovníku.
- Při naplnění slovníku je nutná strategie (zmrazení, vymazání, LRU…).

---

## 3.6 Kódování indexů

Výstupem LZW kodéru je posloupnost celočíselných indexů. Ty je potřeba zakódovat do bitového řetězce. Možnosti:

- **Pevná délka kódu:** Pokud je maximální velikost slovníku$2^k$, každý index se kóduje do$k$bitů. Jednoduché, ale neefektivní na začátku, kdy slovník je malý.
- **Postupně rostoucí délka:** Na začátku se kóduje menším počtem bitů (odpovídajícím aktuální velikosti slovníku), délka se zvyšuje, jakmile počet položek slovníku překročí aktuální kapacitu - používá varianta **LZC**.
- **Statistické kódování:** Indexy se kódují Huffmanovým nebo aritmetickým kódováním - pro ještě vyšší kompresi, ale složitější implementace.