## 3. LZ78

### **3.1 Popis a princip**

- **LZ78** je _slovníková kompresní metoda_ z rodiny LZ algoritmů. LZ78 navazuje na LZ77, ale nahrazuje implicitní slovník **explicitním slovníkem** _vzorů_. (Řeší jeho problém s mazání starých symbolů, kvůli délce jeho bufferu)

> [!warning]
> **Vstup**:
>
> - Posloupnost symbolů ze zdrojové abecedy
>
> **Výstup**:
>
> - Komprimovaná data

- Slovník je **adaptivní** a **na začátku je prázdný**. Během komprese se do něj _postupně ukládají nové vzory_, které ve slovníku zůstávají _po celou dobu komprese_.
- Protože **kodér i dekodér** vytvářejí _slovník stejným způsobem_, není nutné slovník přenášet spolu s komprimovanými daty.

#### 3.1.**1 Hlavní principy**

- Při kódování se ve slovníku _hledá nejdelší slovo odpovídající aktuální pozici vstupu_. Nalezené slovo se spojí s následujícím symbolem a tato dvojice tvoří nový vzor.
- Na výstup se zapisuje dvojice **(index, symbol)**, kde index určuje _nalezené slovo ve slovníku_ a _symbol představuje první znak_ následující za tímto slovem.

#### **3.1.2 Nevýhody**:

- **Pomalá adaptace na vstup** - do slovníku se přidávají slova jen o **1 symbol delší** než slovo již ve slovníku. Takže to trvá než se naučí kódovat dlouhé fráze.

### 3.2 Pseudokód

```
x ← prázdný řetězec
while načti ze vstupu symbol a ∈ A do
    if xa je ve slovníku then
        x ← xa                   // prodlužuj shodu
    else
        ulož xa jako další položku do slovníku
        zapiš na výstup: (index x ve slovníku, a)
        // index x počínaje 1, pro x = prázdný řetězec index 0
        x ← prázdný řetězec
if x ≠ prázdný řetězec then
    zapiš na výstup: (index x ve slovníku)
```

1. Čteme ze vstupu symbol po symbolu.
2. Snažíme se najít **nejdelší řetězec** $x$, který už ve slovníku máme.
3. Jakmile řetězec $xa$(tj. $x$prodloužený o další symbol $a$) ve slovníku **není**, zapíšeme dvojici (index $x$, $a$) na výstup a uložíme $xa$do slovníku jako novou položku.
4. Začneme hledat znovu od prázdného řetězce.

#### 3.2.1 Kódování indexů a symbolů

- Indexy a symboly se kódují buď **statickým kódem** (např. pevný počet bitů), nebo **(adaptivním) statistickým kódováním** (Huffmanovým nebo aritmetickým).

### 3.3 Příklad kódování krok po kroku

#### Příklad

**Vstup:** `barbaraabarboraubaru`, $A = \set{a, b, r, u, o}$

| Krok | Načítám | $x$před | $xa$ ve slovníku? | Výstup (index, symbol) | Nová položka slovníku |
| --- | --- | --- | --- | --- | --- |
| 1   | b   | ε   | ne  | (0, b) | 1: **b** |
| 2   | a   | ε   | ne  | (0, a) | 2: **a** |
| 3   | r   | ε   | ne  | (0, r) | 3: **r** |
| 4   | b→a | b (=idx 1) → ba ne | —   | (1, a) | 4: **ba** |
| 5   | r→a | r (=idx 3) → ra ne | —   | (3, a) | 5: **ra** |
| 6   | a→b | a (=idx 2) → ab ne | —   | (2, b) | 6: **ab** |
| 7   | a→r | a (=idx 2) → ar ne | —   | (2, r) | 7: **ar** |
| 8   | b→o | b (=idx 1) → bo ne | —   | (1, o) | 8: **bo** |
| 9   | r→a→u | r→ra (=idx 5)→rau ne | —   | (5, u) | 9: **rau** |
| 10  | b→a→r | b→ba (=idx 4)→bar ne | —   | (4, r) | 10: **bar** |
| 11  | u   | ε   | ne  | (0, u) | 11: **u** |

**Výstup:** `(0,b) (0,a) (0,r) (1,a) (3,a) (2,b) (2,r) (1,o) (5,u) (4,r) (0,u)`

#### Slovník po kódování:

| Index | Slovo |
| --- | --- |
| 1   | b   |
| 2   | a   |
| 3   | r   |
| 4   | ba  |
| 5   | ra  |
| 6   | ab  |
| 7   | ar  |
| 8   | bo  |
| 9   | rau |
| 10  | bar |
| 11  | u   |



---

### 3.4 Dekódování

```
while načti ze vstupu a dekóduj kód indexu i ve slovníku do
    x ← prázdný řetězec
    if i ≠ 0 then
        x ← slovo na indexu i ve slovníku
        zapiš na výstup slovo x
    if načti ze vstupu a dekóduj kód symbolu a ∈ A then
        ulož xa jako další položku do slovníku
        zapiš na výstup symbol a
```

1. Přečteme index $i$- pokud $i \neq 0$, vypíšeme slovo na pozici $i$ve slovníku.
2. Přečteme symbol $a$- vypíšeme $a$.
3. Uložíme $xa$(slovo z indexu $i$+ nový symbol $a$) do slovníku jako novou položku.
4. Slovník se buduje **identicky** jako při kódování → dekodér nepotřebuje slovník dopředu.

#### Ruční ověření dekódování (zkráceno)

Vstup: `(0,b) (0,a) (0,r) (1,a) (3,a) (2,b) (2,r) (1,o) (5,u) (4,r) (0,u)`

| Krok | (index, symbol) | Vypíšu | Uložím do slovníku |
| --- | --- | --- | --- |
| 1   | (0, b) | b   | 1: b |
| 2   | (0, a) | a   | 2: a |
| 3   | (0, r) | r   | 3: r |
| 4   | (1, a) | b + a | 4: ba |
| 5   | (3, a) | r + a | 5: ra |
| 6   | (2, b) | a + b | 6: ab |
| 7   | (2, r) | a + r | 7: ar |
| 8   | (1, o) | b + o | 8: bo |
| 9   | (5, u) | ra + u | 9: rau |
| 10  | (4, r) | ba + r | 10: bar |
| 11  | (0, u) | u   | 11: u |

**Dekódovaný výstup:** `b a r ba ra ab ar bo rau bar u` = `barbaraabarboraubaru` ✓


### 3.5 Varianty LZ78

#### 3.5.1 LZFG

- Řadí se mezi **varianty LZ78**, ale podstatou je **hybrid LZ77 + LZ78**:
  - z **LZ77** přebírá myšlenku **search bufferu** — fráze se kódují odkazem (délka + pozice) na dřívější výskyt v již zpracovaném textu.
  - z **LZ78** přebírá **explicitní slovníkovou/stromovou strukturu** a kódování pomocí **kódů dvojic**.
- **Cíl hybridizace:** odstranit hlavní slabiny obou rodičů.
  - LZ77 plýtvá tím, že každý odkaz vždy obsahuje i **explicitní symbol** a kóduje pozici/délku do **pevného počtu bitů**.
  - LZ78 adaptuje pomalu a indexy bývají dlouhé.
  - LZFG kóduje **délku + pozici** úsporně a explicitní symbol uvádí **jen když je nutný**.

#### 3.5.2 Další

- LZRW1
- LZRW4

---

## 4. Datová reprezentace slovníku

### 4.1 Trie

- _Explicitní slovník_ LZ78 lze efektivně reprezentovat pomocí **trie (prefixového stromu)**
- $n\text{-ární strom}$$T = \langle V, E \rangle$, kde $n = |A|$(velikost abecedy)

- **Uzel** je reprezentován jako dvojice **klíč-hodnota**. Klíč je _index fráze_ ve slovníku. Hodnota je _symbol části fráze uložené ve slovníku_.
- **Kořen** reprezentuje _prázdný řetězec ε_ a má _index 0_.
- **Hrana** vede od rodiče k potomkovi. Je označena symbolem rozšiřujícího rodiče. Rodič $x$, hrana $a$, potomek $xa$
- Cesta _od kořene k danému uzlu_ pak dává dohromady _celou frázi_

> [!info]
> Slovo _trie_ pochází z anglického „re**trie**val“

### 4.2 Tabulková reprezentace

#### 4.2.1 Tabulka pro kódování

- Sloupce: **index slova** $xa$, **symbol** $a$, **index prvního potomka** $xab$, a pro sourozence $xab, xac, \ldots$indexy dalšího **sourozence** $xac, xad, \ldots$

#### 4.2.2 Tabulka pro dekódování

- Při dekódování slova na indexu$i$čteme symbol a následujeme ukazatel na rodiče, dokud nedojdeme ke kořeni. Tím získáme slovo **pozpátku** - musíme ho obrátit (nebo uložit do zásobníku a pak vypsat).

![](/api/files/019ee5f9-6040-7539-9e66-24cea46aa23d/MacBook-2026-06-20-004799@2x.png)