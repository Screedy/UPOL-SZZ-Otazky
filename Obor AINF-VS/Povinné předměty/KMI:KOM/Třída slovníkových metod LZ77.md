## 1. Slovníkové metody

- Slovníkové metody využívají skutečnosti, že se v datech často _opakují stejné posloupnosti symbolů_ (vzory, fráze). Místo opakovaného ukládání těchto vzorů _ukládají odkazy na jejich dřívější výskyty_.

### 1.1 Základní vlastnosti:

- Nevyužívají _statistický model_ (pravděpodobnosti výskytu symbolů).
- Využívají _opakující se vzory_ (slova, části vět, řetězce znaků).
- Komprese je založena na nahrazování opakovaných vzorů odkazy do slovníku.
- Často dosahují dobré komprese u _dat s mnoha opakováními_. (Oproti přímého kódování vstupu, kódujeme odkaz na místo v slovníku → vyšší míra komprese)

### 1.2 Slovník

- Slovník obsahuje dříve nalezené, často používané, vzory a může být:
  - **implicitní slovník** – slovník je tvořen již zpracovanou částí vstupu (není samostatná struktura), vzory se referencují zpětným odkazem na pozici a délku (např. LZ77).
  - **explicitní slovník** – slovník je samostatná tabulka vzorů budovaná za běhu (samostatná struktura), do výstupu se zapisují indexy do této tabulky (např. LZW).

### 1.3 Aktualizace slovníku

- Podle způsobu vytváření rozlišujeme:
  - **statické** – slovník je _znám_ předem a během komprese se nemění,
  - **semi-adaptivní** – slovník se _vytvoří před kompresí_ ze vstupních dat,
  - **adaptivní** – slovník _vzniká a aktualizuje se_ během komprese.

> [!info]
> Při omezené velikosti slovníku se používají strategie nahrazování vzorů, např. **LRU (Least Recently Used)**.

### 1.4 Výhody

- jednoduchá a rychlá dekomprese,
- nevyžadují odhad pravděpodobností,
- velmi účinné při výskytu opakujících se vzorů.

---

## 2. Kódování n-gramů

- **Kódování n-gramů** je _slovníková metoda_, ve které slovník obsahuje nejčastější n-gramy vybrané pomocí statistického modelu. Komprese probíhá nahrazováním nalezených n-gramů jejich indexy ve slovníku.

### 2.1 Slovník

- Obsahuje:
  - všechny _symboly vstupní abecedy_,
  - nejčastější 2-gramy až n-gramy.
- Položky jsou obvykle seřazeny podle četnosti (pravděpodobnosti) výskytu.
- Slovník je vytvořen pomocí _statického nebo semi-adaptivního statistického modelu_.

### 2.2 Postup kódování

1. Načítej symboly ze vstupu a postupně **vytvářej co nejdelší řetězec**, který _se nachází ve slovníku_.
2. Jakmile po přidání dalšího symbolu vznikne řetězec, který **ve slovníku není**:
  - zakóduj _index dosud nalezeného nejdelšího řetězce_,
  - začni _vytvářet nový_ řetězec od aktuálního symbolu.
3. Po zpracování celého vstupu _zakóduj i poslední nalezený řetězec_.

- Kódování indexů _statickým kódem nebo statistickým kódováním_ (Huffmanovým nebo aritmetickým)

![](/api/files/019ecc86-fe02-703a-a555-69dee02294d8/MacBook-2026-06-15-004767@2x.png)

### 2.3 Výhody

- Využívá často se opakující posloupnosti symbolů.
- Jeden index může reprezentovat více znaků najednou.
- U častých n-gramů může dosahovat lepší komprese než kódování po jednotlivých symbolech.

---

## 3. LZ77

### 3.1 Popis a princip

- **LZ77** je _slovníková kompresní metoda_ z rodiny LZ algoritmů. Tato metoda využívá techniku zvanou **“sliding window”**.

> [!warning]
> **Vstup**:
>
> - Posloupnost symbolů zdrojové abecedy
> - Číslo $K \ ...$velikost search buffer
> - Číslo $L \ ...$velikost look-ahead buffer
>
> **Výstup**:
>
> - Komprimovaná data

#### 3.1.1 Sliding window

- Sliding window se v LZ77 skládá z dvou částí:
  - **Search buffer:**
    - _Velikost_ bufferu je definována **parametrem**$K$
    - Obsahuje již zpracovaná data = _posloupnost_$K$_bezprostředně předchozích symbolů_
    - Slouží jako **adaptivní slovník**, kde algoritmus vyhledává dříve zpracované fráze
  - **Look-ahead buffer**
    - _Velikost_ bufferu je definována **parametrem**$L$
    - Obsahuje _aktuální sekvenci symbolů_ k zpracování
- LZ77 předpokládá, že **opakující se vzory se vyskytují blízko sebe** - do vzdálenosti $K$

### 3.2 Pseudokód

```
x ← prázdný řetězec
o ← 0
while načti symbol a do:
    if se řetězec (x + a) nachází v search bufferu AND délka(x) < L then
        o ← vzdálenost výskytu (x + a) od aktuální pozice
        x ← x + a
    else
        zapiš trojici (o, délka(x), a)
        x ← prázdný řetězec
        o ← 0
if x není prázdný řetězec then
    zapiš dvojici (o, délka(x))
```

- **Postup**:
  1. Udržujeme **search buffer** obsahující již zpracovanou část vstupu.
  2. Hledáme nejdelší řetězec shodný s aktuální pozicí vstupu.
  3. _Dokud lze shodu prodlužovat o další symbol_, pokračujeme v hledání. (Dokud existuje v search bufferu, nebo nám nedošlo místo v look-ahead bufferu)
  4. Jakmile další symbol již nelze přidat:
    - Zapíšeme trojici:
      $$
      (\text{offset}, \text{délka}, \text{další symbol})
      $$
      
    - kde:
      - **offset** = vzdálenost nalezené shody,
      - **délka** = délka nalezené shody,
      - **další symbol** = první symbol za nalezenou shodou.
  5. Pokračujeme za _právě zakódovanou částí vstupu_.
  6. Po zpracování celého vstupu se _případná poslední shoda_ zapíše bez posledního symbolu.
- **Kódování trojic:**
  - _Vzdálenosti, délky a symboly_ se kódují **statickým kódem** nebo **(adaptivním) statistickým kódováním**
  - Alternativně lze kódovat celé trojice najednou místo jednotlivě.

---

### 3.3 Příklad kódování — krok po kroku

#### Příklad

**Vstup:** `barbaraabarboraubaru`, $A = {a, b, r, u, o}$, $K = 10$, $L = 3$

| Krok | Search buffer (max 10) | Look-ahead (max 3) | Přečtené symboly | Nalezeno | Výstup $(o, l, a)$ |
| --- | --- | --- | --- | --- | --- |
| 1   | (prázdný) | `bar` | `b` | nic | $(0, 0, b)$ |
| 2   | `b` | `arb` | `a` | nic | $(0, 0, a)$ |
| 3   | `ba` | `rba` | `r` | nic | $(0, 0, r)$ |
| 4   | `bar` | `bar` | `b`→`ba`→`bar`→`bara` | `bar` na vzdálenosti 3 | $(3, 3, a)$ |
| 5   | `barbara` | `aba` | `a`→`ab` | `a` na vzdálenosti 1 | $(1, 1, b)$ |
| 6   | `barbaraab` | `arb` | `a`→`ar`→`arb`→`arbo` | `arb` na vzdálenosti 8 | $(8, 3, o)$ |
| 7   | `baraabarbo` | `rau` | `r`→`ra`→`rau` | `ra` na vzdálenosti 8 | $(8, 2, u)$ |
| 8   | `aabarborau` | `bar` | `b`→`ba`→`bar`→`baru` | `bar` na vzdálenosti 8 | $(8, 3, u)$ |

**Celkový výstup:** `0,0,b 0,0,a 0,0,r 3,3,a 1,1,b 8,3,o 8,2,u 8,3,u`


---

### 3.4 Dekódování

- Dekodér čte trojice $(o, l, a)$a rekonstruuje výstup:
  - Zkopíruj$l$symbolů ze vzdálenosti$o$od aktuální pozice ve výstupu.
  - Připoj symbol$a$.
- Dekodér **nepotřebuje znát** původní search buffer - ten si rekonstruuje z dosud dekódovaného výstupu.

---

## 4. Varianty LZ77

### 4.1 LZR

- Délky$K$a$L$bufferů jsou **neomezené** (teoreticky).
- V praxi omezena paměťovými možnostmi.

### 4.2 LZSS

- **LZSS** je vylepšení LZ77 — řeší jeho _hlavní neefektivitu_: LZ77 posílá trojici$(\text{offset}, \text{délka}, \text{další symbol})$ i tehdy, když **žádná shoda nebyla nenalezena**, což je plýtvání.
- LZSS místo toho používá **příznakový bit**:
  - **0** → následuje literál (jeden znak přímo)
  - **1** → následuje dvojice$(\text{offset}, \text{délka})$— odkaz do slovníku
- Pokud by bylo kódování odkazu **stejně dlouhé** nebo **delší** než _samotný symbol_, algoritmus místo toho _zapisuje zakódovaný samostatný symbol_.

#### **4.2.1 Varianty LZSS:**

- **LZB**: Varianta, která kóduje vzdálenosti pomocí postupně se zvyšujícího počtu bitů dle aktuální velikosti search bufferu a délky kóduje pomocí Eliasova Gamma kódu.
- **SLH**: Semi-adaptivní varianta, která kóduje vzdálenosti a symboly pomocí Huffmanova kódu.

### 4.3 Deflate

- **Nejúspěšnější varianta** LZ77/LZSS
- Základ formátů ZIP, gzip, zlib, PNG, PDF.

**4.3.1 Hlavní rysy**:

- Výstupem jsou **dvojice**$(\text{délka}, \text{vzdálenost})$nebo **samostatné symboly** (jako LZSS).
- Využívá **lazy matching**.
  - Pokud je nalezena shoda, algoritmus ji nemusí ihned zakódovat, ale porovná ji se shodou začínající o symbol později. Pokud je pozdější shoda delší, použije se ta, protože vede k lepší kompresi.
- Vstup se zpracovává **po blocích**. Každý blok může mít jiný mód — algoritmus vybere ten nejvýhodnější.

**Tři módy bloků:**

- **Mód 1 (bez komprese)**
  - Data se přenesou beze změny + 5 B záhlaví.
  - _Použití_: nekomprimovatelná data (už zkomprimované soubory apod.).
- **Mód 2 (statické kódy):**
  - Předem daný, pevně zakódovaný Huffmanův strom (stejný pro všechny soubory).
  - Rychlé, ale neoptimální pro konkrétní data.
- **Mód 3 (semi-adaptivní kódy):**
  - Huffmanův strom se sestaví z aktuálního bloku → optimální pro daná data.
  - Strom se musí přenést spolu s daty — ukládá se komprimovaně jako seznam délek kódových slov (+ další Huffmanův kód nad nimi).
  - Používá **kanonický Huffmanův kód**: dekodér nepotřebuje celý strom, stačí mu seznam délek — z nich strom jednoznačně rekonstruuje.

---

## 5. Implementační aspekty

### Typické velikosti bufferů

- $K$(search buffer): až **tisíce** symbolů, v Deflate $K = 2^{15} = 32768$B.
- $L$(look-ahead buffer): **desítky až stovky** symbolů.

### Časová složitost

- Hlavní bottleneck je **vyhledávání nejdelšího vzoru** v search bufferu.
- Naivní přístup: $O(K \cdot L)$na jeden krok (S hashovací tabulkou nebo suffix stromem: výrazně rychlejší)
- **Dekomprese je vždy rychlá** — $O(1)$na jeden výstupní symbol (pouhé kopírování + připojení).