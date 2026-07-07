## 1. Aritmetické kódování

### 1.1 Popis a princip

- **Aritmetické kódování** je _entropické kódování_, které reprezentuje celou zprávu jediným číslem z intervalu $\langle 0,1)$.

> [!warning]
> **Vstup**:
>
> - Posloupnost symbolů ze zdrojové abecedy
> - (_Volitelně_) Zdrojová abeceda $A$
> - (_Volitelně_) Pravděpodobnostní výskyty jednotlivých symbolů z abecedy
>
> **Výstup**:
>
> - Komprimovaná data
> - (_Volitelně — nemusí přímo vracet, ale dekodér potřebuje_) Délka zdrojového slova
> - (_Volitelně — nemusí přímo vracet, ale dekodér potřebuje_) Distribuční funkce

**1.1.1 Motivace vzniku**

**Omezení Huffmanova kódování**

- Víme, že pro Huffmanovo kódování platí, že _nikdy nebude lepší jak entropie_ a zároveň **může být až o 1bit horší** —$H(A) \leq \bar{l}(C(A)) < H(A) + 1$. To _zní jako malý rozdíl_, ale někdy je to obrovský.

> [!danger]
> **Problém**: Huffman přiřazuje každému symbolu **celý počet bitů**.

> [!note]
> **Příklad**: Pokud máme tedy zdroj: $p_1=0.95, p_2=0.05$. Entropie je $H(A) ≈ 0.286\ \text{b/symbol}$. Teoreticky by stačilo přenášet asi 0.286 bitu na symbol. Huffman má kódy `A=0, B=1` . Průměrná délka je tedy: $0.95⋅1 + 0.05⋅1 = 1\ \text{b/symbol}$. Což je zde celkem neefektivní$1≫0.286$.

- **Řešení?** Nekóduj jednotlivé symboly, ale bloky symbolů. Počet symbolů v abecedě, ale roste exponenciálně: pro blok délky $k$: $|A^k|$. Exponenciální nárůst Huffmanova stromu.

**Myšlenka aritmetického kódování**

- Místo přiřazování kódového slova **každému symbolu** se kóduje celé **zdrojové slovo (zpráva)** jako **jedno číslo** z podintervalu $\langle 0, 1)$.

> [!success]
> **Výhoda**: Průměrná délka kódu na symbol se blíží entropii **bez nutnosti rozšiřovat abecedu**.

**1.1.2 Kumulativní distribuční funkce (CDF)**

- V aritmetickém kódování se používá _k rozdělení intervalu_$\langle 0, 1)$na **podintervaly odpovídající jednotlivým symbolům** $a_i$.
- Abeceda $A = {a_1, a_2, \ldots, a_n}$s pravděpodobnostmi $p_i = P(a_i)$.
- Kumulativní pravděpodobnost: $F_X(i) = \sum_{k=1}^{i} p_k$, přičemž $F_X(0) = 0$.
- Každý symbol $a_i$odpovídá podintervalu$\langle F_X(i-1), F_X(i))$délky $p_i$.

> [!note]
> - **Intuice:** Čím pravděpodobnější symbol, tím širší podinterval → méně bitů potřeba k jeho specifikaci → lepší komprese.

### 1.2 Pseudokód

```javascript
l ← 0
u ← 1
while (načti ze vstupu symbol a_i ∈ A):
    ll ← l
    l  ← l + (u - l) · F_X(i - 1)     // Vypočítání dolní hranice intervalu
    u  ← ll + (u - ll) · F_X(i)       // Vypočítání horní hranice intervalu

zapiš na výstup binární reprezentaci libovolného čísla z [l, u) s minimem bitů
```

> [!danger]
> Klíčové vzorce pro nový interval při symbolu $a_i$:
>
> - $l_{\text{nový}} = l + (u - l) \cdot F_X(i-1)$
> - $u_{\text{nový}} = l + (u - l) \cdot F_X(i)$

---

### 1.3 Příklad kódování krok po kroku

#### Příklad

**Zadání**

- Vstup: `barbaraabarboraubaru`
- Abeceda: $A = {a, b, r, u, o}$
- Pravděpodobnosti: $p(a) = \frac{7}{20} = 0.35$, $p(b) = \frac{5}{20} = 0.25$, $p(r) = \frac{5}{20} = 0.25$, $p(u) = \frac{2}{20} = 0.10$, $p(o) = \frac{1}{20} = 0.05$

**Kumulativní pravděpodobnosti**

| Symbol | $p_i$ | $F_X(i-1)$ | $F_X(i)$ | Podinterval |
| --- | --- | --- | --- | --- |
| $a = a_1$ | 0.35 | 0.00 | 0.35 | $[0.00, 0.35)$ |
| $b = a_2$ | 0.25 | 0.35 | 0.60 | $[0.35, 0.60)$ |
| $r = a_3$ | 0.25 | 0.60 | 0.85 | $[0.60, 0.85)$ |
| $u = a_4$ | 0.10 | 0.85 | 0.95 | $[0.85, 0.95)$ |
| $o = a_5$ | 0.05 | 0.95 | 1.00 | $[0.95, 1.00)$ |

**Kódování prvních 4 symbolů (**`barb`**)**

**Krok 1: symbol** `b` ($i=2$, $F_X(1)=0.35$, $F_X(2)=0.60$)

- $l = 0 + (1-0) \cdot 0.35 = 0.35$
- $u = 0 + (1-0) \cdot 0.60 = 0.60$
- $[l, u) = [0.35, 0.60)$

**Krok 2: symbol** `a` ( $i=1$, $F_X(0)=0$, $F_X(1)=0.35$)

- $l = 0.35 + (0.60 - 0.35) \cdot 0 = 0.35$
- $u = 0.35 + (0.60 - 0.35) \cdot 0.35 = 0.4375$
- $[l, u) = [0.35, 0.4375)$

**Krok 3: symbol** `r` ($i=3$, $F_X(2)=0.60$, $F_X(3)=0.85$)

- $l = 0.35 + (0.4375 - 0.35) \cdot 0.60 = 0.35 + 0.0525 = 0.4025$
- $u = 0.35 + (0.4375 - 0.35) \cdot 0.85 = 0.35 + 0.074375 = 0.424375$
- $[l, u) = [0.4025, 0.424375)$

**Krok 4: symbol** `b` ($i=2$, $F_X(1)=0.35$, $F_X(2)=0.60$)

- $l = 0.4025 + (0.424375 - 0.4025) \cdot 0.35 = 0.4025 + 0.00765625 = 0.41015625$
- $u = 0.4025 + (0.424375 - 0.4025) \cdot 0.60 = 0.4025 + 0.013125 = 0.415625$
- $[l, u) = [0.41015625, 0.415625)$

A tak dále pro každý další symbol — **interval se stále zmenšuje**.

### Finální výstup

- Po zakódování celé zprávy je výsledný interval velmi úzký. Výstupem je _binární zápis libovolného čísla z tohoto intervalu s minimálním počtem bitů_.
- V příkladu: Výstup je $0.411376953125$, zapsáno binárně jako `011010001010` (12 bitů).


---

### 1.4 Dekódování

- Dekodér zná distribuční funkci $F_X$a délku $L$zdrojového slova.
- Načte binární číslo $x \in [0, 1)$a opakovaně hledá, do kterého podintervalu $x$padne.

```
l ← 0
u ← 1
j ← 0
načti ze vstupu (převedené binární) číslo x ∈ [0, 1)

while j < L:
    najdi i ∈ {1, ..., n} takové, že F_X(i-1) ≤ ((x - l)/(u - l)) < F_X(i)
    zapiš na výstup symbol a_i
    j ← j + 1
    if j < L:
        ll ← l
        l ← l + (u - l) · F_X(i - 1)
        u ← ll + (u - ll) · F_X(i)
```

> [!info]
> Pro nalezení symbolu se spočte **normalizovaná pozice** $\frac{x - l}{u - l}$a zjistí se, do kterého podintervalu $\langle F_X(i-1), F_X(i))$tato hodnota padne.

> [!danger]
> Pro dekódování je nutné znát délku $L$původního zdrojového slova.

#### Příklad

**Zadání**

- Vstup: `011010001010` = $0.411376953125$
- $L=20$
- Abeceda$A = \{a, b, r, u, o\}$, indexy $a_1=a,\ a_2=b,\ a_3=r,\ a_4=u,\ a_5=o$
- Distribuční funkce (kumulativní pravděpodobnost): $F_X(0)=0,\ F_X(1)=0{.}35,\ F_X(2)=0{.}6,\ F_X(3)=0{.}85,\ F_X(4)=0{.}95,\ F_X(5)=1$

**Krok 1**: _Vypočítat_ $\frac{x-l}{u-l}=\frac{0.411376953125-0}{1-0}=0.411376953125 \rightarrow \langle F_X(1), F_X(2)) \rightarrow$`b`

Přepočítám interval: $l=0.35,\ u=0.6$

**Krok 2**: _Vypočítat_ $\frac{x-l}{u-l}=\frac{0.411376953125-0.35}{0.6-0.35}=0.245507812 \rightarrow \langle F_X(0), F_X(1)) \rightarrow$`a`

Přepočítám interval: $l=0.35,\ u=0.4375$

**Krok 3**: _Vypočítat_ $\frac{x-l}{u-l}=\frac{0.411376953125-0.35}{0.4375-0.35}=0.701450892 \rightarrow \langle F_X(2), F_X(3)) \rightarrow$`r`

Přepočítám interval: $l=0.4025,\ u=0.424375$

**Krok 4**: _Vypočítat_ $\frac{x-l}{u-l}=\frac{0.411376953125-0.4025}{0.424375-0.4025}=0.40580357 \rightarrow \langle F_X(1), F_X(2)) \rightarrow$`b`

Přepočítám interval: $l=0.39484375,\ u=0.415625$

…


---

### 1.5 Přeškálování (rescaling) a průběžný výstup

- S každým dalším symbolem se interval $\langle l, u)$zmenšuje → v praxi **podtečení** **aritmetiky** s omezenou přesností (float/double).
- Navíc bez přeškálování _nelze produkovat výstup_ **průběžně** — všechny bity by se vypsaly až na konci.

### Tři případy přeškálování

Přeškálování se provádí vždy, když $l$a $u$leží ve stejné části intervalu $\langle 0, 1)$:

| Případ | Podmínka | Akce | Intuice |
| --- | --- | --- | --- |
| **1** | $u < 0.5$ | $l \leftarrow 2l$, $u \leftarrow 2u$, výstup bit `0` | Oba konce v dolní polovině |
| **2** | $l \geq 0.5$ | $l \leftarrow 2(l - 0.5)$, $u \leftarrow 2(u - 0.5)$, výstup bit `1` | Oba konce v horní polovině |
| **3** | $l \geq 0.25 \wedge u < 0.75$ | $l \leftarrow 2(l - 0.25)$, $u \leftarrow 2(u - 0.25)$, $c \leftarrow c + 1$ | Interval kolem středu |

### Výstup při přeškálování

- Při případu 1: zapíšeme `0` a poté $c$-krát `1` (inverze).
- Při případu 2: zapíšeme `1` a poté $c$-krát `0` (inverze).
- Při případu 3: žádný okamžitý výstup, jen $c \leftarrow c + 1$(odložení rozhodnutí).

> [!note]
> **Důvod:** Případ 3 nastává, když interval „sedí" uprostřed a nemůžeme určit první bit — ale jakmile se interval posune do jedné poloviny (případ 1 nebo 2), dodatečné $c$bitů inverze „doplní" odložená rozhodnutí.

#### Příklad přeškálování

**Zadání**

- Vstup: `barbaraabarboraubaru`
- Abeceda: $A = {a, b, r, u, o}$
- Pravděpodobnosti: $p(a) = \frac{7}{20} = 0.35$, $p(b) = \frac{5}{20} = 0.25$, $p(r) = \frac{5}{20} = 0.25$, $p(u) = \frac{2}{20} = 0.10$, $p(o) = \frac{1}{20} = 0.05$

**Kumulativní pravděpodobnosti**

| Symbol | $p_i$ | $F_X(i-1)$ | $F_X(i)$ | Podinterval |
| --- | --- | --- | --- | --- |
| $a = a_1$ | 0.35 | 0.00 | 0.35 | $[0.00, 0.35)$ |
| $b = a_2$ | 0.25 | 0.35 | 0.60 | $[0.35, 0.60)$ |
| $r = a_3$ | 0.25 | 0.60 | 0.85 | $[0.60, 0.85)$ |
| $u = a_4$ | 0.10 | 0.85 | 0.95 | $[0.85, 0.95)$ |
| $o = a_5$ | 0.05 | 0.95 | 1.00 | $[0.95, 1.00)$ |

**Kódování prvních 4 symbolů (**`barb`**)**

**Krok 1: symbol** `b` ($i=2$, $F_X(1)=0.35$, $F_X(2)=0.60$)

- $l = 0 + (1-0) \cdot 0.35 = 0.35$
- $u = 0 + (1-0) \cdot 0.60 = 0.60$
- $[l, u) = [0.35, 0.60)$

**Kontrola přeškálování**: _Případ 3_ → $l=0.20,\ u=0.70,\ c=1$

**Krok 2: symbol** `a` ($i=1$, $F_X(0)=0$, $F_X(1)=0.35$)

- $l = 0.2 + (0.70-0.20) \cdot 0 = 0.20$
- $u = 0.2 + (0.70-0.20) \cdot 0.35 = 0.375$
- $[l, u) = [0.20, 0.375)$

**Kontrola přeškálování**: _Případ 1_ → $l=0.4,\ u=0.75,\ c=0$→ `01`

**Krok 3: symbol** `r` ($i=3$, $F_X(2)=0.60$, $F_X(3)=0.85$)

- $l = 0.61$
- $u = 0.6975$
- $[l, u) = [0.61, 0.6975 )$

**Kontrola přeškálování**: _Případ 3_ → $l=0.22,\ u=0.395,\ c=1$, _Případ 1_ → $l=0.44,\ u=0.79,\ c=0$→ `01`

…


---

### 1.6 Přeškálování u dekodéru

### Princip

- Dekodér provádí **stejné přeškálování** jako kodér a **navíc přeškáluje i hodnotu** $x$.
- Na začátku načte $\lceil -\log_2 \frac{p_{\min}}{4} \rceil$bitů do $x$.
- Při přeškálování: $x \leftarrow 2(x - d) + b \cdot 2^{-\lceil -\log_2 \frac{p_{\min}}{4} \rceil}$, kde $b$je další načtený bit.

---

### 1.7 Celočíselná implementace

- Celočíselná varianta aritmetického kódování je upravená verze standardního aritmetického kódování, která **používá celočíselné operace** místo operací s plovoucí desetinnou čárkou. Tato úprava _zjednodušuje implementaci_, zejména v prostředích, kde manipulace s plovoucí desetinnou čárkou může být _neefektivní_ nebo _kde je omezená přesnost těchto operací problematická_.

> [!info]
> V praxi se interval $\langle0, 1)$zobrazí na **celočíselný rozsah** $\langle0, M-1)$, kde $M$je typicky $2^8$, $2^{16}$, $2^{32}$nebo $2^{64}$.

---

### 1.8 QM kódování (binární aritmetické kódování)

- Adaptivní varianta aritmetického kódování je vylepšením standardního aritmetického kódování, které _umožňuje kódovat data bez předchozí znalosti jejich pravděpodobnostního rozložení_.
- V adaptivním modelu se pravděpodobnosti symbolů **aktualizují dynamicky během zpracování dat**, což umožňuje efektivněji reagovat na změny v rozložení dat.

---

### 1.9 Vlastnosti aritmetického kódu

#### Prefixový kód

- Aritmetické kódování produkuje **prefixový binární kód** pro zdrojová slova nad abecedou $A$.
- Průměrná délka pro slova délky $k$: $H(A^k) \leq \bar{l}(C(A^k)) < H(A^k) + 1$.

#### Kdy je aritmetické kódování výhodnější?

- **Malé abecedy** (binární, malý počet symbolů)
- **Velké rozdíly v pravděpodobnostech** **symbolů**