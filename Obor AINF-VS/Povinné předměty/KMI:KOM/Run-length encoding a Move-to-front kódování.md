## 1. Run-length encoding (RLE)

### 1.1 Popis a princip

- **Run-length encoding** je jedna z nejjednodušších kompresních technik.

> [!warning]
> **Vstup**:
>
> - Posloupnost symbolů ze zdrojové abecedy
> - Číslo $k$
> - Symbol příznaku
>
> **Výstup**:
>
> - Komprimovaná data

- Jejím základním principem je nahrazení **posloupnosti (run) stejných za sebou jdoucích symbolů** kompaktnějším zápisem. Místo samotných opakujících se symbolů se zapíše trojice informací:
  - **příznak** (flag), že následuje kódovaný run,
  - **délka** posloupnosti (kolik symbolů se opakuje),
  - **symbol**, který se opakuje.

> [!info]
> **Příklad:** Představte si černobílý obrázek — celé řádky obsahují dlouhé sekvence černých nebo bílých pixelů. Místo uložení každého pixelu zvlášť řekneme „150× bílá, 30× černá, 120× bílá…". U textových dat jsou runy kratší, ale princip je stejný.

### 1.2 Parametr číslo $k$

- Aby byla komprese efektivní (tj. aby výstup nebyl delší než vstup), používá se RLE pouze pro posloupnosti delší než **určité číslo** $k$:
  - Pokud $r \leq k$: vypíšeme symbol $r$-krát (bez příznaku, bez komprese).
  - Pokud $r > k$: použijeme kódování s příznakem.
- Typická hodnota $k$ _bývá 3._ (tj. run délky 1, 2 nebo 3 se nekóduje, od délky 4 výš ano)

### 1.3 Problém zaměnitelnosti příznaku

> [!danger]
> Kód příznaku se může shodovat s kódem některého symbolu abecedy.

- Řešení:
  - **Varianta 1 (explicitní příznak):** Použije se speciální znak, který se ve zdrojových datech nevyskytuje.
  - **Varianta 2 (příznak za symboly):** Vypíšeme $k$kopií symbolu a poté kód délky zmenšené o $k$(tj. $r - k$). Dekodér ví, že pokud vidí $k$stejných symbolů za sebou a poté číslo, jedná se o run.

### 1.4 Pseudokód (kompresní algoritmus)

```
r ← 0
while načti ze vstupu symbol a:
    if r = 0:
        x ← a          // zapamatuj si symbol
        r ← 1          // začátek nového runu
    else:
        if a = x:
            r ← r + 1  // run pokračuje
        else:
            // run symbolu x skončil, zapiš výstup
            if r ≤ k:
                zapiš r-krát symbol x
            else:
                zapiš kód příznaku, číslo r, symbol x
                // NEBO: zapiš k-krát symbol x, poté číslo (r − k)
            x ← a
            r ← 1
// na konci nezapomenout zapsat poslední run!
```

### 1.5 Příklad kódování krok po kroku

#### Příklad

**Vstup:** `bbbbaaaarrrbbaaaaara`, $k=3$

Rozložení na runy:

| Run | Symbol | Délka $r$ | $r \leq 3$? | Výstup (varianta 1: příznak `x`) | Výstup (varianta 2) |
| --- | --- | --- | --- | --- | --- |
| bbbb | b   | 4   | Ne  | `x4b` | `bbb1` |
| aaaa | a   | 4   | Ne  | `x4a` | `aaa1` |
| rrr | r   | 3   | Ano | `rrr` | `rrr` |
| bb  | b   | 2   | Ano | `bb` | `bb` |
| aaaaa | a   | 5   | Ne  | `x5a` | `aaa2` |
| r   | r   | 1   | Ano | `r` | `r` |
| a   | a   | 1   | Ano | `a` | `a` |

**Celkový výstup (varianta 1):** `x4bx4arrrbbx5ara`

**Celkový výstup (varianta 2):** `bbb1aaa1rrrbbaaa2ra`

**Původní délka:** 20 symbolů → **Varianta 1:** 17 znaků, **Varianta 2:** 19 znaků.


### 1.6 Vlastnosti RLE

- **==Výhody:==**
  - Jednoduchá implementace
  - Velmi nízká výpočetní náročnost — $O(n)$čas i prostor.
- **==Nevýhoda:==**
  - **Efektivita závisí na datech:** Vynikající pro data s dlouhými runy (binární obrazy BMP, faxové přenosy, jednoduché grafiky). Špatný pro data bez opakování (může výstup dokonce zvětšit!).
- **Aplikace:** Formát obrázků BMP.

---

## 2. Move-to-front (MTF) kódování

### 2.1 Popis a princip

- **Move-to-front (MTF) kódování** je lokálně adaptivní transformace (= přizpůsobuje se lokální četnosti výskytu symbolů)

> [!warning]
> **Vstup**:
>
> - Posloupnost symbolů ze zdrojové abecedy
> - Zdrojová abeceda A
> - _(Volitelně)_ Pravděpodobnostní výskyty jednotlivých symbolů
>
> **Výstup**:
>
> - Zakódované data

- Jejím základním principem je _převedení vstupních symbolů na posloupnost čísel_ (indexů). **Často se opakující symboly** jsou kódovány **malými čísly**, speciálně posloupnost **stejných symbolů** se převede na **posloupnost nul**.

**Formální popis:**

- Udržujeme seznam (permutaci) zdrojové abecedy $A = {a_1, a_2, \ldots, a_n}$.
- _Volitelně_ seznam na začátku setřídíme sestupně podle pravděpodobností výskytu symbolů.
- Pro každý symbol $a$na vstupu:
  1. Najdeme jeho pozici $i$v seznamu.
  2. Na výstup zapíšeme číslo $i$.
  3. Symbol $a$přesuneme na **začátek** seznamu (a ostatní posunu o jedno dozadu).

> [!note]
> **Intuice:** Pokud se symbol právě vyskytl, je na začátku seznamu, příště dostane index 0. Pokud se symbol opakuje mnohokrát za sebou, celá sekvence se změní na řadu nul.
>
> A i v obecnějším případě — když se v datech vyskytují lokální shluky určitých symbolů (což je po BWT typické) — vznikají malá čísla, která se efektivně komprimují.

### 2.2 Pseudokód (kódování)

```
Vstup: zdrojová abeceda A = {a₁, a₂, …, aₙ}
       (volitelně) pravděpodobnosti {p₁, …, pₙ}
       vstupní řetězec

(volitelně) setřiď aᵢ tak, že pᵢ ≥ pⱼ pro i < j

while načti ze vstupu symbol a ∈ A:
    najdi i takové, že aᵢ = a       // pozice v aktuálním seznamu
    zapiš na výstup číslo i  // výstupní index
    if i > 0:
        přesuň aᵢ na začátek seznamu:
            x ← aᵢ
            aⱼ ← aⱼ₋₁  pro j = 1, 2, …, i  // posunování ostatních čísel
            a₁ ← x
```

### 2.3 Dekódování MTF

Dekódování je symetrické — dekodér udržuje stejný seznam a provádí stejné operace:

```
Vstup: zdrojová abeceda A = {a₁, a₂, …, aₙ} (stejné počáteční pořadí jako kodér)

while načti ze vstupu číslo idx:
    i ← idx
    zapiš na výstup symbol aᵢ
    if i > 0:
        přesuň aᵢ na začátek seznamu (stejně jako u kódování)
```

> [!danger]
> **Klíčové:** Dekodér musí začít se **stejným počátečním pořadím seznamu** jako kodér. Pokud kodér setřídil podle pravděpodobností, dekodér musí znát tyto pravděpodobnosti.

### 2.4 Příklady

#### Příklad kódování krok po kroku

**Vstup:** `bbbbaaaarrrbbaaaaara` **Abeceda:** $A = {b, a, r}$, $p(b) = 6/20$, $p(a) = 10/20$, $p(r) = 4/20$

**Varianta 1:** _Počáteční seznam seřazený podle pravděpodobností_ → $[a, b, r]$

| Krok | Vstup | Seznam před | Výstup | Seznam po |
| --- | --- | --- | --- | --- |
| 1   | b   | [a, b, r] | **1** | [b, a, r] |
| 2   | b   | [b, a, r] | **0** | [b, a, r] |
| 3   | b   | [b, a, r] | **0** | [b, a, r] |
| 4   | b   | [b, a, r] | **0** | [b, a, r] |
| 5   | a   | [b, a, r] | **1** | [a, b, r] |
| 6   | a   | [a, b, r] | **0** | [a, b, r] |
| 7   | a   | [a, b, r] | **0** | [a, b, r] |
| 8   | a   | [a, b, r] | **0** | [a, b, r] |
| 9   | r   | [a, b, r] | **2** | [r, a, b] |
| 10  | r   | [r, a, b] | **0** | [r, a, b] |
| 11  | r   | [r, a, b] | **0** | [r, a, b] |
| 12  | b   | [r, a, b] | **2** | [b, r, a] |
| 13  | b   | [b, r, a] | **0** | [b, r, a] |
| 14  | a   | [b, r, a] | **2** | [a, b, r] |
| 15  | a   | [a, b, r] | **0** | [a, b, r] |
| 16  | a   | [a, b, r] | **0** | [a, b, r] |
| 17  | a   | [a, b, r] | **0** | [a, b, r] |
| 18  | a   | [a, b, r] | **0** | [a, b, r] |
| 19  | r   | [a, b, r] | **2** | [r, a, b] |
| 20  | a   | [r, a, b] | **1** | [a, r, b] |

**Celkový výstup:** `1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 1`

Zhuštěně: **1000 1000 200 20 20000 2 1**

**Varianta 2:** _Počáteční seznam podle abecedy_ → $[b, a, r]$ (bez třídění dle pravděpodobností)

Výstup by byl: `0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 1`

- Liší se pouze v prvním čísle (b je nyní na pozici 0, ne 1).

#### Příklad dekódování

**Vstup:** `1, 0, 0, 0, 1, 0, 0, 0` (prvních 8 čísel z předchozího příkladu)

**Počáteční seznam:** $[a, b, r]$

| Krok | Vstup (idx) | Seznam před | Výstup $a_i$ | Seznam po |
| --- | --- | --- | --- | --- |
| 1   | 1   | [a, b, r] | **b** | [b, a, r] |
| 2   | 0   | [b, a, r] | **b** | [b, a, r] |
| 3   | 0   | [b, a, r] | **b** | [b, a, r] |
| 4   | 0   | [b, a, r] | **b** | [b, a, r] |
| 5   | 1   | [b, a, r] | **a** | [a, b, r] |
| 6   | 0   | [a, b, r] | **a** | [a, b, r] |
| 7   | 0   | [a, b, r] | **a** | [a, b, r] |
| 8   | 0   | [a, b, r] | **a** | [a, b, r] |

**Výstup:** `bbbbaaaa` ✓


https://www.youtube.com/watch?v=obbK0scsb98

### 2.6 Vlastnosti MTF

- **Lokálně adaptivní:** Přizpůsobuje se lokálním změnám ve frekvenci symbolů. Nepotřebuje znát pravděpodobnosti předem (stačí dohodnout počáteční pořadí).
- **Není kompresní metoda sama o sobě** — je to **transformace**, která vytváří příznivější vstup pro navazující kódování. Sama o sobě data nezkracuje (výstup má stejný počet symbolů jako vstup).
- **Časová složitost:** $O(n \cdot |A|)$v nejhorším případě (každý symbol může vyžadovat posunutí celého seznamu). Pro malé abecedy zanedbatelné. Pro velké abecedy lze optimalizovat datovými strukturami.
- **Prostorová složitost:** $O(|A|)$na seznam.

### 2.7 Alternativní varianty přesunu

- **Swap (prohození):** Místo přesunu na začátek se symbol prohodí se svým předchůdcem: $x \leftarrow a_i$, $a_i \leftarrow a_1$, $a_1 \leftarrow x$. Méně agresivní adaptace.
- **Postupný posun:** Symbol se neposune na začátek najednou, ale postupně se přesouvá o jednu pozici vpřed, dokud nedosáhne první pozice.

---

## 3. Vztah MTF a RLE — typický kompresní pipeline

> [!info]
> MTF a RLE se v praxi **kombinují** — využívá se například v následující pipeline:
>
> 1. **BWT (Burrows-Wheelerova transformace):** Permutuje vstupní blok tak, aby se vytvořily shluky stejných symbolů (symboly se stejným kontextem se ocitnou vedle sebe).
> 2. **MTF:** Převede shluky stejných symbolů na sekvence nul a malých čísel.
> 3. **RLE:** Zakóduje dlouhé sekvence nul kompaktně.
> 4. **Huffmanovo nebo aritmetické kódování (statické kódování):** Zakóduje výsledná čísla s proměnnou délkou kódových slov podle frekvencí.
>
> Tento pipeline používá například **bzip2**.