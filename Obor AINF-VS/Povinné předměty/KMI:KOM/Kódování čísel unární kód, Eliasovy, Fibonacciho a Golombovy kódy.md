## 1. Úvod

- Kódování čísel představuje _skupinu metod_ pro převod **přirozených čísel** (typicky $i \geq 0$nebo $i \geq 1$) na **binární kódová slova s proměnnou délkou**. Celá čísla (i záporná) lze vždy bijektivně zobrazit na přirozená.

> [!danger]
> **Klíčový předpoklad:** Větší čísla se vyskytují s nižší pravděpodobností. Proto kódy přiřazují kratší kódová slova menším číslům.

> [!info]
> **Kde se kódy čísel používají:**
>
> - Kódování délek v RLE
> - Kódování indexů a vzdáleností ve slovníkových metodách (LZ77, LZ78, LZW)
> - Kódování výstupů MTF

**Základní pojmy pro orientaci:**

- **Prefixový kód** — žádné kódové slovo není prefixem jiného (jednoznačně dekódovatelný)
- **Univerzální kód** — kód, jehož průměrná délka je asymptoticky optimální pro širokou třídu rozložení pravděpodobností (bez znalosti konkrétního rozložení)
- Binární reprezentace čísla $i$se značí $\beta(i)$, její délka $l(\beta(i)) = \lfloor \log_2 i \rfloor + 1$

---

## 1. Unární kód

> [!success]
> **Definice:** Pro $i \geq 0$:
>
> $$
> \text{unární}(i) = \underbrace{1 \ldots 1}_{i} \cdot 0
> $$

- Tedy $i$**jedniček** následovaných **jednou nulou**.

### Příklady

| $i$ | Kódové slovo | Délka |
| --- | --- | --- |
| 0   | `0` | 1   |
| 1   | `10` | 2   |
| 2   | `110` | 3   |
| 3   | `1110` | 4   |
| 5   | `111110` | 6   |

### Vlastnosti

- **Prefixový** — ukončovací bit `0` zajistí, že žádné slovo není prefixem jiného
- **Délka kódového slova:** $i + 1$bitů
- **Optimální** při geometrickém rozložení $P(i) = \frac{1}{2^{i+1}}$ (pro $i \geq 0$) — tedy když se pravděpodobnost s každým dalším číslem přesně půlí
- **Velmi neefektivní** pro větší čísla — délka roste lineárně s hodnotou
- **Použití:** jako součást složitějších kódů (Eliasovy, Golombovy), kódování velmi malých čísel

> [!note]
> **Intuice:** Unární kód je nejjednodušší možný prefixový kód. Je to „čárkový" systém — kolik čárek, takové číslo. Pro data, kde převažují malé hodnoty (0, 1, 2) a velké jsou vzácné, funguje dobře. Jakmile se ale vyskytují i středně velká čísla (řekněme 20–100), je katastrofálně dlouhý.

---

## 2. Eliasovy kódy

- Eliasovy kódy jsou rodinou **univerzálních prefixových kódů** pro kladná celá čísla.

### Pomocné kódy

- $\alpha(i)$— **Alpha kód**
  - _(Obrácený)_ unární kód čísla $i$, pro $i \geq 0$— s jedničkou na konci
  - $\alpha(i) = \underbrace{0 \ldots 0}_{i} \cdot1$
- $\beta(i)$— **Beta kód**
  - Binární reprezentace čísla $i$, pro $i \geq 0$.
  - **Není prefixový**, proto se nepoužívá samostatně

- $l(\beta(i)) = \lfloor \log_2 i \rfloor + 1$— délka binární reprezentace

> [!danger]
> Alfa a beta kód nejsou samostatné Eliasovy kódy, ale **tvoří základ pro konstrukci** Eliasových gamma, delta a omega kódů.

---

### 2.1 Eliasův Gamma kód ($\gamma$)

> [!success]
> **Definice:** Pro $i \geq 1$:
>
> $$
> \gamma(i) = \underbrace{0 \ldots 0}_{l(\beta(i)) - 1} \cdot \beta(i)
> $$

- Tedy$(l(\beta(i)) - 1)$**nul**, následovaných **binární reprezentací** $\beta(i)$.

#### Postup kódování (krok po kroku)

1. Spočti $l(\beta(i)) = \lfloor \log_2 i \rfloor + 1$
2. Zapiš $(l(\beta(i)) - 1)$ nul
3. Zapiš $\beta(i)$

#### Příklad kódování

Zakódujme $i = 5$:

1. $\beta(5) = 101$, tedy $l(\beta(5)) = 3$
2. Zapíšeme $3 - 1 = 2$nul: `00`
3. Zapíšeme $\beta(5) = 101$
4. Výsledek: `00101`

#### Dekódování

1. Čti nuly, dokud nepřečteš jedničku — počet nul = $n$
2. Přečti dalších $n$ bitů
3. Úvodní jednička + těchto $n$ bitů = $\beta(i)$, převeď na číslo

**Příklad dekódování** `00101`

1. Přečteme dvě nuly → $n = 2$
2. Přečteme jedničku (ta je součástí $\beta$) a dalších 2 bitů: `101`
3. $\beta^{-1}(101) = 5$

#### Vlastnosti

- **Prefixový** — úvodní nuly jednoznačně určují délku zbytku
- **Délka:** $2\lfloor \log_2 i \rfloor + 1$bitů
- **Optimální** při $P(i) = \frac{1}{2i^2}$
- **Vhodný** pro malá čísla (do cca 100–1000); pro větší čísla je výhodnější Delta

---

### 2.2 Eliasův Delta kód ($\delta$)

> [!success]
> **Definice**: Pro $i \geq 1$:
>
> $$
> \delta(i) = \gamma(l(\beta(i))) \cdot\beta(i) \text{ bez první jedničky}
> $$

- Tedy zakódujeme tuto **délku**$\beta(i)$**Gamma kódem**, a pak připojíme **zbytek binární reprezentace** $\beta(i)$bez úvodní jedničky.

#### Postup kódování

1. Spočti $l(\beta(i)) = \lfloor \log_2 i \rfloor + 1$
2. Zakóduj $l(\beta(i))$Gamma kódem: $\gamma(l(\beta(i)))$
3. Připoj $\beta(i)$bez úvodní jedničky

#### Příklad kódování

Zakódujme $i = 5$:

1. $\beta(5) = 101, l(\beta(5)) = 3$
2. $\gamma(3) = 011$
3. $\beta(5)$bez úvodní jedničky = `01`
4. Výsledek: `01101`

#### Dekódování

1. Dekóduj Gamma kód → získáš $l = l(\beta(i))$
2. Přečti dalších $l - 1$bitů
3. Předřaď jedničku → $\beta(i)$, převeď na číslo

**Příklad dekódování** `01101`

1. Přečteme jednu nulu → $n = 1$
2. Přečteme jedničku (ta je součástí $\beta$) a dalších 1 bit: `11`
3. $\beta^{-1}(11) = 3$ → $l = 3$
4. Přečtěme další 2 bity: `01`
5. Předřadíme jedničku → $\beta^{-1}(101) = 5$

#### Vlastnosti

- **Prefixový**
- **Délka:** $2\lfloor \log_2(\lfloor \log_2 i \rfloor + 1) \rfloor + \lfloor \log_2 i \rfloor + 1$bitů
- **Optimální** při $P(i) = \frac{1}{2i(\log_2 2i)^2}$
- **Výhodnější než Gamma** pro větší čísla (cca od $i \geq 32$), protože „délku délky" kóduje úsporněji

---

### 2.3 Eliasův Omega kód ($\omega$) — rekurzivní

> [!success]
> Definice: Pro $i \geq 1$:
>
> Pro $i = 1:\ \omega(1) = 0$(ukončovací podmínka)
>
> Pro $i \geq 2$: kód se sestavuje **odzadu**:
>
> 1. Začni zápisem bitu `0` (ukončovací bit)
> 2. Nastav $k := i$
> 3. Dokud $k \geq 2$:
>   1. Zapiš **před** dosavadní kód $\beta(k)$
>   2. Nastav $k := l(\beta(k)) - 1$

#### Příklad kódování

Zakódujeme $i = 5$

1. Začínáme: `0`
2. $k = 5$, $\beta(5) = 101$, zapíšeme: `101`$\cdot$`0` = `101 0`
3. $k = l(\beta(5)) - 1 = 3 - 1 = 2$, $\beta(2) = 10$, zapíšeme před: `10`$\cdot$`101 0` = `10 101 0`
4. $k = l(\beta(2)) - 1 = 2 - 1 = 1,\ k < 2$ → _konec_
5. Výsledek: `101010`

#### Dekódování

1. Nastav $i := 1$
2. Přečti další bit:
  - Pokud je `0` → konec, výsledek je $i$
  - Pokud je `1` → přečti dalších $i$ bitů; tato jednička + přečtené bity = $\beta(i)$; dekóduj jako nové $i$
3. Opakuj od kroku 2

**Příklad dekódování** `101010`:

1. $i = 1$.
  1. Další bit = `1` → přečteme $i = 1$ dalších bitů: `0`.
  2. Dohromady `10` → $\beta^{-1}(10) = 2$ → $i = 2$
2. $i = 2$.
  1. Další bit = `1` → přečteme $i = 2$ dalších bitů: `01`.
  2. Dohromady `101` → $\beta^{-1}(101) = 5$ → $i = 5$
3. $i = 5$.
  1. Další bit = `0` → konec.
  2. Výsledek: $i = 5$

#### Vlastnosti

- **Prefixový**
- **Délka:** $\sum_{j=1}^{k}(\lfloor \log_2 i \rfloor_j + 1) + 1$, kde $\lfloor \log_2 i \rfloor_k = 1$ (iterovaný logaritmus)
- Nejefektivnější z Eliasových kódů pro **velmi velká čísla**

---

### 2.4 Porovnání Eliasových kódů

| $i$ | Gamma $\gamma$ | Delta $\delta$ | Omega $\omega$ |
| --- | --- | --- | --- |
| 1   | 1   | 1   | 0   |
| 3   | 011 | 0101 | 110 |
| 5   | 00101 | 01101 | 101010 |
| 10  | 0001010 (7b) | 01000010 (8b) | 1010010100 (10b) |
| 100 | 13 bitů | 12 bitů | 12 bitů |
| 1000 | 19 bitů | 16 bitů | 15 bitů |

> [!info]
> - $i \leq 30$: Gamma je nejkratší (nebo srovnatelné s Delta)
> - $30 < i \leq 1000$: Delta je výhodnější
> - $i > 1000$: Omega začíná vyhrávat

---

## 3. Fibonacciho kód a Zeckendorfova reprezentace

> [!warning]
> **Fibonacciho posloupnost:** $F_0 = 0, F_1 = 1, F_j = F_{j-1} + F_{j-2}$
>
> Tedy: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …

> [!success]
> **Zeckendorfova věta:** Každé přirozené číslo $i \geq 1$ lze **jednoznačně** zapsat jako součet **nesousedních** Fibonacciho čísel.

- Tato reprezentace se nazývá _Fibonacciho (Zeckendorfova) reprezentace_.

### Fibonacciho (Zeckendorfova_)_ reprezentace

> [!success]
> **Definice**: Pro $i \geq 1$:
>
> $$
> \text{Fib}(i) = a_0 a_1 \ldots a_{k} \cdot 1
> $$

- Tedy Fibonacciho reprezentace čísla $i$zřetězená s jednou jedničkou navíc. Kód vždy **končí dvěma jedničkami**, protože Fibonacciho reprezentace neobsahuje sousední jedničky.
- Začínáme v Fibonacciho posloupnosti **od třetí pozice**
  - 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …

#### Postup kódování

1. Najdi Zeckendorfovu reprezentaci čísla $i$:
  1. Rozkládej $i$ na součet Fibonacciho čísel, vždy od největšího možného
2. Zapiš koeficienty $a_1, a_2, \ldots$
3. Připoj `1` na konec

#### Příklad kódování

Zakódujeme $i = 5$

1. $F_5 = 5$
2. Koeficienty:
  - $a_0 = 0$ (pro $F_2=1$)
  - $a_1 = 0$ (pro $F_3=2$)
  - $a_2 = 0$ (pro $F_4=3$)
  - $a_3 = 1$ (pro $F_5=5$)
3. Zápis: `0001`$\cdot$ukončovací `1` = `00011`

Zakóduj $i = 10$

1. $10 = 8 + 2 = F_6 + F_3$
2. Koeficienty:
  - $a_0 = 0$ ($F_2=1$)
  - $a_1 = 1$ ($F_3=2$)
  - $a_2 = 0$ ($F_4=3$)
  - $a_3 = 0$ ($F_5=5$)
  - $a_4 = 1$ ( $F_6=8$)
3. Zápis: `01001` + ukončovací `1` = `010011`

#### Dekódování

1. Čti bity, dokud nenarazíš na `11`.
2. Poslední jedničku odstraň.
3. Zbylé bity interpretuj jako Fibonacciho reprezentaci: $i = \sum a_j F_{j+1}$

**Příklad dekódování** `010011`:

1. Čteme `0, 1, 0, 0, 1, 1` — nalezeno `11` → konec.
2. Odstraníme ukončovací `1`. Koeficienty = `01001`
3. $a_0=0, a_1=1, a_2=0, a_3=0, a_4=1$  
  $i = 1 \cdot F_3 + 1 \cdot F_6 = 2 + 8 = 10$

### Vlastnosti

- **Prefixový** — ukončovací `11` zajistí jednoznačnost.
- **Délka:** $\leq \lfloor \log_\varphi \sqrt{5} \cdot n \rfloor + 1$, kde $\varphi = \frac{1+\sqrt{5}}{2} \approx 1{,}618$ (zlatý řez).
- **Robustnější** než Eliasovy kódy — chyba v jednom bitu neovlivní dekódování dalších čísel tak snadno, protože ukončovací `11` slouží jako synchronizační značka. U Eliasových kódů se chyba v bitu délky propaguje a zničí dekódování celého zbytku.
- **Nevýhoda:** delší než Eliasovy kódy pro stejná čísla.

---

## 4. Golombovy kódy

> [!success]
> **Definice**: Pro $i \geq 0$a **parametr** $\mathbf{j}$:
>
> 1. _Spočítáme_ $\mathbf{b}=\lceil \log_2 j \rceil$
> 2. _Spočítáme_ $\mathbf{q} = \lfloor i / j \rfloor$(podíl)
> 3. _Spočítáme_ $\mathbf{r} = i - q \cdot j = i \mod j$(zbytek po dělení)
> 4. _Uložíme_ $\mathbf{q}$jako **unární kód**
> 5. _Určíme_ si **délku binární podoby**$\mathbf{r}$na základě následující podmínky:
>   1. Když je $r<2^b-j\text{,}$ulož $r$binárně o délce $b -1$
>   2. Jinak ulož $r = r + 2^b-j$binárně o délce $b$
> 6. _Na výstup_ napiš hodnoty $q\cdot r$

> [!danger]
> Parametr$j$určuje kompromis mezi délkou unární části (podílu$q$) a binární části (zbytku$r$). Jeho vhodná volba má zásadní vliv na efektivitu Golombova kódu.
>
> - Když se zvolí moc **malé** $j \rightarrow$bude _velký unární kód_ $q$
> - Když se zvolí moc **velké** $j \rightarrow$zbytek $r$_potřebuje_ více bitů

#### Příklad kódování

Zakódujeme$j = 5,\ i=3$

1. $b = \lceil \log_2 5 \rceil = 3$
2. $q=\lfloor 3/5 \rfloor = 0$
3. $r= 3 \mod 5=3$
4. Unární kód$q$:`0`
5. $3<2^3-5 \rightarrow$**Není pravda!** Ukládáme $r = 3 + 2^3-5$binárně v délce $b=3$:`110`
6. Výstup: $q\cdot r =$`0110`.

Zakódujeme$j = 5,\ i=9$

1. $b = \lceil \log_2 5 \rceil = 3$
2. $q=\lfloor 9/5 \rfloor = 1$
3. $r= 9 \mod 5=4$
4. Unární kód$q$:`10`
5. $9<2^3-5 \rightarrow$**Není pravda!** Ukládáme $r = 4 + 2^3-5$binárně v délce $b=3$:`111`
6. Výstup: $q\cdot r =$`10111`.

#### Dekódování

1. **Načti** $q$_z unárního kódu_
2. _Spočti_ $b=\lceil \log_2{j} \rceil$
3. _Načti_ $b-1$_bitů_$\rightarrow r'$
4. Pokud $r' < 2^b-j:$$r=r'$  
  _Jinak_: **načti ještě** $1$**bit** $\rightarrow r''$  
  $r=r''-2^b+j$
5. $i=q \times j+r$

**Příklad dekódování** $j=5$a `10111`**:**

1. Výsledné $q$z unárního kódu: `10` $\rightarrow 1$
2. $b=\lceil \log_2{j} \rceil = 3$
3. Načti $b-1$bitů$\rightarrow r' =$`11` $=3$
4. Neplatí$3< 2^3-5 \rightarrow$načítám ještě $1$bit $\rightarrow r''=$`111` $=7$a$r=7-2^3+5=4$
5. $i=1 \times 5+4 =9$

### Optimalita a geometrické rozložení

- Golombův kód s parametrem $j$je **optimální prefixový kód** pro **geometrické rozložení pravděpodobnosti:**

$$
P(i) = p^{i-1}(1-p), \quad i \geq 1
$$

kde optimální parametr je $j = \left\lceil -\frac{1}{\log_2 p} \right\rceil$.

### Riceovy kódy (Golomb-Riceovy kódy)

- Riceovy kódy jsou **speciální případ Golombových kódů** pro $j = 2^k$, kde $k \geq 0$je celé číslo.