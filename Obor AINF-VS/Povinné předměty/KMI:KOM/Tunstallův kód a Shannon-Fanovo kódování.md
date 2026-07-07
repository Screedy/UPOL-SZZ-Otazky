## 1. Tunstallův kód

### 1.1 Popis a princip

- **Tunstallův kód** je _statistická kompresní metoda_.

> [!warning]
> **Vstup:**
>
> - Posloupnost symbolů ze zdrojové abecedy
> - Zdrojová abeceda$A$
> - Číslo $n = |A|$
> - Číslo$k\ ...$pevná délka kódových slov
> - Číslo$m\ ...$velikost kódové abecedy
> - (_Volitelně_) Pravděpodobnostní výskyty jednotlivých symbolů z abecedy
>
> **Výstup:**
>
> - Tabulka s kódovými slovy
> - Komprimovaná data

- Většina kompresních metod přiřazuje _často se vyskytujícím_ symbolům _kratší kódy_ a _vzácným delší_. Tunstallův kód naopak vytváří **často se vyskytující fráze** různé délky a všechny reprezentuje **stejně dlouhými kódovými slovy**.

> [!note]
> **Intuice:** Místo toho, abychom častým symbolům dávali krátké kódy, dáváme **častým symbolům delší zdrojová slova** — symbol s vysokou pravděpodobností se „roztáhne" do delších frází, čímž se za jedno kódové slovo pevné délky zakóduje více vstupních symbolů najednou. To snižuje průměrný počet bitů na symbol.

### 1.2 Požadavky na Tunstallův kód

1. **Jednoznačná kódovatelnost** = Každé kódové slovo musí jednoznačně odpovídat jedné sekvenci zdrojových symbolů. (vytváří prefixový kód)
2. **Optimální kód** = Průměrná délka zdrojových slov je **maximální**. (vybírá se symbol s největší pravděpodobností)
3. **Maximální využití kódových slov**. Je použito maximální množství kódových slov, ideálně všech $m^k$.

### 1.3 Pseudokód (algoritmus na vytvoření slovníku)

```javascript
T ← A            // počáteční množina zdrojových slov = jednotlivé symboly
i ← 0
// zkouška zda by šlo přidat další rozšíření slova
while n + (i+1)(n-1) ≤ m^k  do  
    // Najdi nejpravděpod. slovo
    x ← w ∈ T  takové, že  P(w) ≥ P(w')  pro všechna w' ∈ T 
    // Nahraď ho n rozšířeními    
    T ← (T \ {x}) ∪ {xy | y ∈ A}          
    i ← i + 1
C(T) ← přiřaď kódová slova délky k libovolně
```

**Jak to funguje krok po kroku:**

1. Začni s množinou zdrojových slov $T = A$.
2. Opakuj: vyber slovo s **nejvyšší pravděpodobností** a nahraď ho $n$novými slovy (původní slovo prodloužené o každý symbol abecedy). Tím se počet slov v $T$zvýší o $n - 1$.
3. Pokračuj, dokud novou rozšířenou množinu $T$lze zakódovat$m^k$kódovými slovy.
4. Přiřaď kódová slova libovolně.

> [!info]
> **Proč právě nejpravděpodobnější slovo?** Protože jeho rozšířením se průměrná délka zdrojových slov zvýší nejvíce — časté symboly vytvoří delší fráze, což maximalizuje počet vstupních symbolů zakódovaných jedním kódovým slovem.

### 1.4 Příklad kódování — krok po kroku

#### Příklad

**Vstup:** `barbaraabarboraubaru`, $k = 4$, $A = {a, b, r, u, o}$, $m = 2$(binární kód)

**Pravděpodobnosti symbolů** (z frekvencí ve vstupu, 20 symbolů):

| Symbol | Frekvence | $P$ |
| --- | --- | --- |
| a   | 7   | 7/20 = 0.35 |
| b   | 5   | 5/20 = 0.25 |
| r   | 5   | 5/20 = 0.25 |
| u   | 2   | 2/20 = 0.10 |
| o   | 1   | 1/20 = 0.05 |

**Kapacita:** $m^k = 2^4 = 16$kódových slov

**Počáteční stav:** $T = {a, b, r, u, o}$, $|T| = 5$

**Krok 1:** Podmínka: $5 + 1 \cdot 4 = 9 \leq 16$✓

Nejpravděpodobnější slovo: $a$($P(a) = 7/20$)

$T = {aa, ab, ar, au, ao, b, r, u, o},\ |T| = 9$

**Krok 2:** Podmínka: $5 + 2 \cdot 4 = 13 \leq 16$ ✓

Nyní potřebujeme pravděpodobnosti nových slov. Počítáme z bigram vstupu (19 bigramů v `barbaraabarboraubaru`):

$P(ba) = 4/19$, $P(ar) = 4/19$, $P(ab) = 1/19$, $P(aa) = 1/19$, $P(au) = 1/19$, $P(ao) = 0$, $P(bo) = 1/19$

Nejpravděpodobnější slovo v $T$: $b$ ($P(b) = 5/20$)

$T = {aa, ab, ar, au, ao, ba, bb, br, bu, bo, r, u, o}$, $|T| = 13$

**Krok 3:** Podmínka: $5 + 3 \cdot 4 = 17 > 16$ ✗ → **STOP**

**Výsledný slovník:**

| Symbol | Kódové slovo |
| --- | --- |
| aa  | 0000 |
| ab  | 0001 |
| ar  | 0010 |
| au  | 0011 |
| ao  | 0100 |
| ba  | 0101 |
| bb  | 0110 |
| br  | 0111 |
| bu  | 1000 |
| bo  | 1001 |
| r   | 1010 |
| u   | 1011 |
| o   | 1100 |

**Výstup:** `0101 1010 0101 1010 0000 0101 1010 1001 1010 0011 0101 1010 1011`

52 bitů, průměrně 2.6 b/symbol


### 1.5 Dekódování

- Dekódování je **jednoduché** — přečti $k$bitů, vyhledej v tabulce příslušné zdrojové slovo, zapiš ho na výstup. Díky pevné délce kódových slov se dekodér vždy synchronizuje.

### 1.6 Vlastnosti

- **Prefixový kód**: Jelikož kódová slova mají _pevnou délku_.
- **Robustnost**: Chyby v kódových slovech se při dekódování **nešíří**, protože kódová slova mají pevnou délku a dekodér se vždy synchronizuje po$k$bitech.
- **Modely**: Pouze statický a semi-adaptivní model (nelze snadno adaptovat za běhu)
- **Průměrná délka kódu:**

$$
\bar{l}(C(T)) = \frac{k}{\sum_{i=1}^{t} P(w_i) \cdot l(w_i)}
$$

kde $t$je počet zdrojových slov $w_i$délky $l(w_i)$s pravděpodobností výskytu $P(w_i)$.

---

## 2. Shannon-Fanovo kódování

### 2.1 Popis a princip

- **Shannon-Fanovo kódování** je **první pokus** o konstrukci _optimálního binárního prefixového kódu_.

> [!warning]
> **Vstup:**
>
> - Posloupnost symbolů ze zdrojové abecedy
> - (_Volitelně_) **Seřazené** pravděpodobnostní výskyty jednotlivých symbolů z abecedy
>
> **Výstup:**
>
> - Tabulka s kódovými slovy
> - Komprimovaná data

> [!info]
> Je historicky důležité, ale v praxi bylo překonáno Huffmanovým kódováním, které je skutečně optimální.

- Symboly seřazené podle _klesající pravděpodobnosti výskytu_ se rekurzivně dělí na **dvě skupiny** tak, aby _součty pravděpodobností_ obou skupin byly **co nejbližší**. Symbolům v „horní" skupině se přiřadí bit `0`, symbolům v „dolní" skupině bit `1`. Postup se rekurzivně opakuje, dokud _v každé skupině nezbyde jeden symbol_.

### 2.2 Pseudokód (algoritmus na vytvoření slovníku)

```javascript
function ShannonFano(a, b):
    if a = b then
        C(a_a) ← prázdný řetězec          // Jeden symbol = konec rekurze
    else if a + 1 = b then
        C(a_a) ← 0                         // Dva symboly = triviální dělení
        C(a_b) ← 1
    else
        Najdi j takové, že |Σ(i = a ... j) p_i  -  Σ(i= j+1 ... b) p_i| je minimální
        ShannonFano(a, j)                   // Rekurze pro horní skupinu
        ShannonFano(j+1, b)                 // Rekurze pro dolní skupinu
        C(a_i) ← 0·C(a_i)  pro i = a, ..., j       // Prefix 0
        C(a_i) ← 1·C(a_i)  pro i = j+1, ..., b     // Prefix 1

ShannonFano(1, n)
```

- **Jak funguje krok po kroku**:
  1. Vypočítají se pravděpodobnosti výskytu každého symbolu ve zdrojové abecedě.
  2. Symboly se seřadí podle jejich pravděpodobností výskytu od nejvyšší po nejnižší.
  3. Seznam symbolů se rozdělí na dvě části tak, aby součet pravděpodobností v obou částech byl **co nejvyrovnanější**.
  4. **První části** se přiřadí bit $0$a druhé části se přiřadí bit $1.$
  5. Tento proces se rekurzivně opakuje pro obě části, dokud všechny symboly nemají přiřazené unikátní kódy.

### 2.3 Příklad kódování — krok po kroku

#### Příklad

**Vstup:** `barbaraabarboraubaru`, $A =\set{a, b, r, u, o}$

**Pravděpodobnosti**:

| Index | Symbol | $p$ |
| --- | --- | --- |
| 1   | a   | 7/20 = 0.35 |
| 2   | b   | 5/20 = 0.25 |
| 3   | r   | 5/20 = 0.25 |
| 4   | u   | 2/20 = 0.10 |
| 5   | o   | 1/20 = 0.05 |

**Krok 1 — dělení (1, 5):**

Hledáme $j$, kde je rozdíl součtů nejmenší:

- $j = 1$: $|0.35 - 0.65| = 0.30$
- $j = 2$: $|0.60 - 0.40| = 0.20$ ← **minimum**
- $j = 3$: $|0.85 - 0.15| = 0.70$

Dělíme: ${a, b}$ dostane prefix `0`, ${r, u, o}$ dostane prefix `1`.

(Možné také hledat střed pomocí průběžného počítání sum ze začátku a z konce)

**Krok 2a — dělení (1, 2):**

Dva symboly → $C(a) = 00$, $C(b) = 01$

**Krok 2b — dělení (3, 5):**

- $j = 3$: $|0.25 - 0.15| = 0.10$ ← **minimum**
- $j = 4$: $|0.35 - 0.05| = 0.30$

Dělíme: ${r}$dostane prefix `10`, ${u, o}$dostane prefix `11`.

**Krok 3 — dělení (4, 5):**

Dva symboly → $C(u) = 110$, $C(o) = 111$

**Výsledný kód (tabulka a strom):**

```
          Kořen
         /     \
        0       1
       / \     / \
      0   1   0   1
      a   b   r  / \
                0   1
                u   o
```

| Symbol | Kódové slovo | Délka |
| --- | --- | --- |
| a   | 00  | 2   |
| b   | 01  | 2   |
| r   | 10  | 2   |
| u   | 110 | 3   |
| o   | 111 | 3   |

**Zakódování vstupu** `barbaraabarboraubaru`:

`00 01 00 00 01 00 00 00 00 01 00 01 00 10 00 110 01 00 10 110` → celkem 43 bitů


### 2.4 Podmínka optimality

> [!danger]
> Kód je optimální, právě když v každém dělení platí:
>
> $$
> \sum_{i=a}^{j} p_i = \sum_{i=j+1}^{b} p_i
> $$
>
> Tedy obě skupiny mají přesně stejnou celkovou pravděpodobnost. To je obecně nesplnitelné, proto Shannon-Fanův kód **není vždy optimální** (na rozdíl od Huffmanova).

### 2.5 Dekódování

Dekódování probíhá průchodem kódovým stromem od kořene — čteme bit po bitu a podle hodnoty jdeme doleva (0) nebo doprava (1), dokud nedojdeme do listu. To je možné, protože kód je prefixový.

### 2.6 Vlastnosti Shannon-Fanova kódování

- **Prefixový kód**: Žádné kódové slovo není prefixem jiného, jednoznačně a okamžitě dekódovatelný
- **Není obecně optimální**: Existují rozložení pravděpodobností, kde Huffmanův kód má nižší průměrnou délku. Shannon-Fanovo kódování dělí shora (top-down), Huffmanovo zdola (bottom-up), což zaručuje optimalitu.
- **Splňuje Shannonovu větu o kódování zdroje:** $\frac{H(A)}{\log_2 m} \leq \bar{l}(C(A)) < \frac{H(A)}{\log_2 m} + 1$
- **Složitost:** $O(n \log n)$pro setřídění + $O(n)$pro rekurzivní konstrukci