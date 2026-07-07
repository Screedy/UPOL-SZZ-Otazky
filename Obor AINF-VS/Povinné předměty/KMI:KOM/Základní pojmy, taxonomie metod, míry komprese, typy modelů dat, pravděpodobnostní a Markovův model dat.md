## 1. Komprese dat — Co to je a proč ji děláme?

> [!success]
> **Definice:** Komprese dat je zmenšení velikosti reprezentace informačního obsahu (dat) při zachování dané míry obsažené informace.

> [!info]
> Jde o jeden z účelů kódování dat.

**Dvě fáze komprese:**

- **Identifikace a modelování struktury dat**
  - Analyzujeme opakující se vzory, četnost výskytu vzorů nebo vztahy mezi jednotlivými vzory.
  - U některých typů dat lze vytvářet i model procesu, který data generuje (například u zvuku či obrazu lze odhadovat hodnoty na základě předchozích).
  - Pro různé časti dat mohou být použity různé modely.
- **Zakódování dat podle nalezeného modelu**.
  - Převedení do efektivnější podoby, často pomocí binárního kódu.
  - Případně se kóduje i samotný model (u semi-adaptivních metod).

> [!note]
> **Intuice:** Komprese funguje proto, že reálná data nejsou náhodná (obsahují pravidelnosti, opakování a závislosti). Čím víc struktury v datech najdeme, tím víc místa ušetříme.

#### Příklad z přednášky

$2, 2, 4, 6, 7, 7, 7, 10, 10, 11, 11, 14 \ \ (x_1, x_2, …, x_{12})$

_Popis struktury dat_:

1. Jedná se o číslo 2–14.
  1. Na převod do dvojkové soustavy jsou potřeba 4 bity / číslo → $4 \times 12 = 48$b
2. Jedná se o 7 různých hodnot.
  1. Na převod stačí 3 bity / číslo → $3 \times 12 = 36$b
3. Častěji opakované čísla kratším kódem (proměnná délka)
  1. $\tt{01=7, 111=11, 110=10,101=2,100=14,000=4,001=6}$ → 33 b = 2,75 b / číslo
  2. Pozor: Musí být jednoznačně dekódovatelný kód (prefixový kód)
4. Kódování opakování čísla
  1. $\tt{0=žádné, 10=jedno, 11=2 }$→ 32 b = $2.\overline{6}$b/číslo
5. Mezi sousedy jsou malé rozdíly (predikce, kódování rozdílu)
  1. $d_1=x_1=2$, $d_i=x_i-x_{i-1}$
  2. $0,2,2,1,0,0,3,0,1,0,3$→ 4b + 2b / číslo → 26 b = $2.1\overline{6}$b/číslo
6. Vztah mezi čísli a posloupností (predikce, kódování rozdílu)
  1. $\hat{x}_i = i + 1$, $d_i = x_i - \hat{x}_i$
  2. $0,-1,0,1,1,0,-1,1,0,0,-1,1$→ $\tt{0=0,10=-1, 11=1}$→ 19 b = $1.58\overline{3}$b/číslo


**Historické příklady:** Morseovka a Braillovo písmo.

---

## 2. Taxonomie (rozdělení) kompresních metod

> [!warning]
> **Kompresní algoritmus** — originální data → komprimovaná data
>
> **Dekompresní algoritmus** — komprimovaná data → dekomprimovaná data

### 2.1 Bezeztrátové (lossless) metody

> [!success]
> **Definice:** _Dekomprimovaná data_ jsou **identická** s _originálními daty._ Nedochází k žádná ztrátě informace.

- **Statistické metody:** Huffmanovo kódování, aritmetické kódování — využívají frekvence symbolů.
- **Kontextové metody:** PPM (Prediction by Partial Matching) — pravděpodobnost symbolu závisí na předchozích symbolech (kontextu).
- **Slovníkové metody:** LZ77, LZ78, LZW — nahrazují opakující se fráze odkazem do slovníku.
- **Jiné / transformační:** BWT (Burrows-Wheeler Transform), MTF, ACB; obrazové (JPEG-LS, JBIG).

> [!info]
> **Použití:** text, programové soubory, citlivé záznamy (bankovní, zdravotní), nereprodukovatelná data.

### 2.2 Ztrátové (lossy) metody

> [!success]
> **Definice:** _Dekomprimovaná data_ jsou **odlišná** jako _data originální_. Dochází k vynechaní informace z originálních dat (vyšší míra komprese), což vede ke _zkreslení_ _dat_. Využívá se omezení lidského vnímání (zraku, sluchu).

- **Vzorkování a kvantizace:** skalární a vektorová.
- **Diferenční kódování:** DPCM, delta modulace.
- **Transformační a podpásmové kódování:** Fourierova transformace, Z a kosinová transformace, wavelety.

> [!info]
> **Aplikace:** JPEG (obraz), H.264/H.265 (video), MP3/AAC (zvuk).

> [!danger]
> **Klíčový rozdíl:** Bezeztrátová komprese odstraňuje **_redundanci_** (nadbytečnost), ztrátová navíc odstraňuje **_irelevanci_** (informaci, která je pro příjemce nepodstatná).

---

## 3. Míry kompresních algoritmů

### 3.1 Kompresní poměr (compression ratio)

> [!success]
> **Definice:** Kompresní poměr je poměr velikosti originálních a komprimovaných dat.
>
> $$
> \text{CR} = \frac{\text{velikost originálních dat}}{\text{velikost komprimovaných dat}}
> $$

- Pokud **CR > 1**, tak _došlo ke kompresi_ (data se zmenšila).
- Často se udává i jako _procento_: $\frac{\text{komprimovaná}}{\text{originální}} \times 100%$.

> [!info]
> **Příklad**: originál 1000 B, komprimovaný 400 B → CR = 2,5 (neboli komprimovaná data jsou 40 % originálu).

### 3.2 Compression rate (bitová rychlost)

> [!success]
> **Definice:** Průměrná velikost komprimovaných dat na vzorek originálních dat.

> [!info]
> **Příklad:** U obrazu se měří v bitech/pixel, u videa a zvuku v bitech/sekundu.

### 3.3 Míry zkreslení (u ztrátové komprese)

> [!success]
> **Definice:** Rozdíl mezi originálními a dekomprimovanými daty.

- Existuje více způsobů měření “přesnosti” a “kvality obsahu.
- Měří se na referenčních datech.

> [!info]
> **Příklad:** MSE, PSNR, SSIM aj.

### 3.4 Asymptotická složitost a experimentální složitost

- Časová a paměťová složitost algoritmů komprese a dekomprese.
- Experimentální se měří na referenčních datech (benchmarky).

---

## 4. Shannonova teorie informace — entropie a její význam pro kompresi

### 4.1 Informace

> [!success]
> **Definice:** Informace asociovaná s výskytem jevu $A$je
>
> $$
> i(A) = \log_b \frac{1}{P(A)} = -\log_b P(A)
> $$
>
> kde $P(A)$je pravděpodobnost jevu $A$.

- **Vlastnosti**:
  - Pokud je pravděpodobnost události 1 (je jistá), informace je 0. Informace události roste s klesající pravděpodobností.
  - Pro dvě nezávislé události $A,B$platí, že $i(AB) = i(A) + i(B)$.
- **Jednotky informace**:
  - **Bit** — pro základ logaritmu $b = 2$
  - **Nat** — pro základ logaritmu $b = e$
  - **Hartley** — pro základ logaritmu $b = 10$

> [!note]
> **Intuice:** Čím méně pravděpodobná událost, tím víc informace nese její výskyt.

### 4.2 Entropie (H)

> [!success]
> **Definice (Shannon, 1948):** Entropie měří průměrnou míru informace (vážený průměr informací všech jevů):
>
> $$
> H(A)=\sum_{i=1}^{n} P(A_i) i(A_i) = -\sum_{i=1}^{n} P(A_i) \log_2 P(A_i)
> $$
>
> kde $A_i$jsou možné jevy a $P(A_i)$jejich pravděpodobnosti výskytu.

Shannon ukázal, že tento _vzorec přirozeně vyplývá_ z několika **základních požadavků** na měření informace:

1. $H$ je **spojitá funkce** pravděpodobností $p_i$. Tedy _malá změna pravděpodobností_ způsobí pouze _malou změnu entropie_.
2. $H$ je **monotónně rostoucí** vzhledem k počtu $m$ stejně pravděpodobných jevů (při $p_i = 1/m$). Čím více _stejně pravděpodobných jevů_, tím více _informace získáme_ po zjištění jevu. Proto **entropie roste**.
3. $H$ je **konzistentní při rozdělení experimentu** na pod-experimenty (řetězové pravidlo). Informace získaná ve více krocích musí odpovídat informaci získané jedním krokem.

> [!note]
> **Intuice:** Entropie měří „průměrnou překvapivost" zdroje. Maxima dosahuje při uniformním rozložení (všechny symboly stejně pravděpodobné — maximální nejistota), minima (= 0) když je jeden symbol jistý a ostatní nemožné.

### 4.3 Entropie zdroje a podmíněná entropie

> [!success]
> Zdroj informace$Z$obvykle negeneruje pouze jeden symbol, ale celou posloupnost symbolů:
>
> $$
> X_1, X_2, \ldots, X_n
> $$
>
> Entropie zdroje proto vyjadřuje průměrné množství informace připadající na jeden symbol dlouhé posloupnosti:
>
> $$
> H(Z)=lim_{n→∞}\frac{​1}{n}​G_n
> $$
>
> kde:
>
> $$
> G_n = -\sum P(X_1 = i_1, \ldots, X_n = i_n) \log P(X_1 = i_1, \ldots, X_n = i_n)
> $$
>
> a $G_n$představuje entropii celé posloupnosti délky $n$.

#### 4.3.1 Nezávislé symboly (entropie 1. řádu)

- Pokud jsou symboly **nezávislé a mají stejné pravděpodobnostní rozložení**, pak znalost předchozích symbolů nijak nepomáhá při odhadu dalšího symbolu. Entropie zdroje je potom rovna entropii jednoho symbolu:

$$
H(Z) = H(A_i) = -\sum P(A_i) \log P(A_i)
$$

- Tato hodnota se označuje jako **entropie 1. řádu**.

#### 4.3.2 Podmíněná entropie

- V reálných datech však symboly často nejsou nezávislé.

> [!info]
> **Například:** V textu po písmenu “q” téměř vždy následuje “u”.

- Znalost předchozího symbolu tedy snižuje neurčitost dalšího symbolu.
- Míru této neurčitosti popisuje podmíněná entropie:

$$
H(X_1 | X_2) = \sum_{i_2} P(a_{i_2}) H(X_1 | X_2 = i_2)
$$

- Podmíněná entropie vyjadřuje průměrné množství informace o symbolu $X_1$za předpokladu, že se vyskytuje za symbolem $X_2$.

#### 4.3.3 Markovovy modely

- V Markovových modelech je podmíněná entropie zapisována jako:

$$
H(X | S)
$$

- kde $S$představuje aktuální stav systému (kontext).

> [!danger]
> **Klíčová vlastnost:** Entropie při uvažování závislostí je **vždy menší nebo rovna** entropii při nezávislém modelu.

#### Příklad výpočtu entropie

$x_1,x_2,...,x_{10}=\text{aababbabaa}$

_Výpočet entropie:_

1. Nezávislé symboly (entropie 1. řádu):
  1. $P(a)=\frac{6}{10},P(b)=\frac{4}{10}$
  2. $H=-P(a)\log_2P(a)-P(b)\log_2P(b) = 0.971 \text{ b/symbol}$
2. Markovův model 1.řádu:
  1. $P(a)=\frac{5}{9}, P(b)=\frac{4}{9}$
  2. $P(a|a)=\frac{2}{5}, P(b|a)=\frac{3}{5},P(a|b)=\frac{3}{4}, P(b|b)\frac{1}{4}$
  3. $H=P(a)H(X|a)+P(b)H(X|b)=P(a)(-P(a|a)\log_2P(a|a)-P(b|a)\log_2P(b|a))+P(b)(-P(a|b)\log_2P(a|b)-P(b|b)\log_2P(b|b))=\text{0.9b/symbol}$
3. Markovův model 2.řádu:
  1. $P(aa)=\frac{1}{8},P(ab)=\frac{3}{8},P(ba)=\frac{3}{8},P(bb)=\frac{1}{8}$
  2. $P(a|aa) = 0, P(b|aa) = 1, P(a|ab)=\frac{2}{3}, P(b|ab)=\frac{1}{3}, P(a|ba)=\frac{1}{3}, P(b|ba)=\frac{2}{3}, P(a|bb) = 1, P(b|bb) = 0$
  3. $H=\sum_{x_1x_2=aa}^{bb}P(x_1x_2)H(X|x_1x_2)= \sum_{x_1x_2=aa}^{bb}P(x_1x_2)(-\sum_{y=a,b}P(y|x_1x_2)\log_2P(y|x_1x_2))= \text{0.689 b/symbol}$

> [!info]
> Vidíme, že s rostoucím řádem modelu (více závislostí) entropie klesá — model lépe zachycuje strukturu dat.


### 4.5 Algoritmická teorie informace (Kolmogorovova složitost)

> [!success]
> **Definice:** Kolmogorovova složitost dat $x$= je **délka** nejkratšího algoritmu (včetně parametrů) nebo nejkratšího počítačového programu (v jakémkoliv programovacím jazyce), jehož výstupem jsou data $x$.

> [!note]
> **Intuice:** Vyjadřuje, jak “jednoduše” lze daná data popsat.

- Přesnou Kolmogorovovu složitost obecně **nelze vypočítat** — neexistuje algoritmus, který by pro libovolná data vždy nalezl _nejkratší možný program_.

- V praxi se proto používají aproximace, například _princip minimální délky popisu_ (**MDL — Minimum Description Length**) navržený Rissanenem.
- $\text{MDL}(x) = \min_j (D_{M_j} + R_{M_j}(x))$
  - kde $D_{M_j}$je délka popisu modelu,
  - $R_{M_j}(x)$ je délka zakódovaných dat pomocí modelu $M_j$.
- MDL tedy _představuje kompromis_ mezi složitostí modelu a přesností reprezentace dat.

---

## 5. Základní pojmy o kódování

> [!warning]
> Máme zdrojovou abecedu $A=\{a_1, a_2, \ldots ,a_n\}$, kde $a_i$= symboly ($A$je množina symbolů, které chceme zakódovat)

### 5.1 Kódování a dekódování

> [!success]
> **Definice:** Kódování je injektivní zobrazení $C: A \mapsto B^+$, kde $A$ je zdrojová abeceda a $B^+$je množina všech konečných neprázdných slov nad kódovou abecedou $B$(často $B = {0, 1}$).

- $C(a_i) \in B^+$ je **kódové slovo** pro symbol $a_i$.
- $l(a_i)$ je **délka** kódového slova $C(a_i)$.

> [!success]
> **Definice:** Dekódování je zobrazení $D:C(A) \mapsto A$, kde $C(A)$je množina kódových slov a $A$ je zdrojová abeceda.

- **Blokový kód** (kód pevné délky): všechna kódová slova (pro všechny symboly) mají **stejnou délku**

> [!info]
> Například: ASCII

### 5.2 Jednoznačně dekódovatelný kód

> [!success]
> **Definice:** Každá (neprázdná) posloupnost symbolů z kódové abecedy je zřetězením nejvýše jedné posloupnosti kódových slov.
>
> **Kódování**: $C^+: A^+ \mapsto B^+$je injektivní.
>
> **Dekódování**: $D^+: C^+(A^+) \mapsto A^+$

- **Test jednoznačné dekódovatelnosti** (Sardinasův–Pattersonův algoritmus)
  - Test ověřuje, zda může _být stejný zakódovaný řetězec dekódován více způsoby_.
  - Algoritmus hledá překryvy mezi kódovými slovy:
    - je-li jedno slovo prefixem druhého,
    - do množiny $S$ se přidá zbytek řetězce.
  - Proces se opakuje pro nové zbytky.
    - Pokud se v $S$objeví celé kódové slovo, kód není jednoznačně dekódovatelný.
    - Pokud už nové zbytky nevznikají, kód je jednoznačně dekódovatelný.

#### Příklad jednoznačné dekódovatelnosti

$C(A)=\{0,01,011,111\}$

- $01 = 0\cdot1 →$zbytek $1$
- $011 = 0\cdot1 →$zbytek $11$
- $S=\{1,11\}$.

- Další iterace nevytvoří konflikt ani nové zbytky, proto je kód jednoznačně dekódovatelný.

#### Příklad **NE**-jednoznačné dekódovatelnosti

$C(A)=\{0,01,10,11\}$

- $01 = 0\cdot1 →$zbytek $1$
- $S=\{1\}$
- $10 = 1\cdot0 →$zbytek $0$
- Protože $0 \in C(A)$, **vznikl konflikt**!

> [!danger]
> Řetězec $010$ má dva rozklady!


### 5.3 Prefixový kód

> [!success]
> **Definice:** Žádné kódové slovo není prefixem jiného kódového slova.

> [!note]
> **Intuice:** Každý prefixový kód je jednoznačně dekódovatelný.

- **Výhoda**: dekódování je **okamžité** — jakmile přečteme celé kódové slovo, ihned ho dekódujeme, aniž bychom museli číst dál.

> [!info]
> Příklad: ${0, 10, 110, 111}$ je prefixový. ${0, 01, 011, 111}$ je JD, ale není prefixový.

### 5.4 Kraftova nerovnost

> [!success]
> **Věta (Kraftova):**  
> Prefixový kód s $k$ kódovými slovy délek $l_1, l_2, \ldots, l_k$ nad kódovou abecedou velikosti $m$existuje právě když:
>
> $$
> \sum_{i=1}^{k} m^{-l_i} \leq 1
> $$

> [!success]
> **Věta (McMillanova):**  
> McMillanova věta rozšiřuje Kraftovu nerovnost na obecnější podmínku pro jednoznačně dekódovatelné kódy.

> [!note]
> **Intuice:** Kraftova nerovnost říká, že krátká kódová slova „zabírají velký podíl" kódového prostoru. Chceme-li jeden symbol zakódovat velmi krátce, musíme jiné zakódovat delšími slovy. Nerovnost vymezuje, jaké kombinace délek jsou vůbec možné.

---

## 6. Optimální kód a Shannonova věta

### 6.1 Průměrná délka kódu (na symbol)

> [!success]
> **Definice:** Průměrná délka kódu se vypočítá jako vážený průměr délek kódových slov, kde váhami jsou pravděpodobnosti výskytu symbolů.
>
> $$
> \bar{l}(C(A)) = \sum_{i=1}^{n} P(a_i) \cdot l(a_i)
> $$
>
> $P(a_i)$je pravděpodobnost výskytu symbolu $a_i$
>
> $l(a_i)$je délka jeho kódového slova

> [!warning]
> **Optimální kód** má minimální průměrnou délku v rámci dané třídy kódů (typicky prefixové).

### 6.2 Shannonova věta o kódování zdroje (1. Shannonova věta, noiseless coding theorem)

> [!success]
> **Definice:** Pro optimální prefixový kód $C(A)$ ze zdrojové abecedy $A$ do kódové abecedy $B$ platí:
>
> $$
> \frac{H(A)}{\log_b m} \leq \bar{l}(C(A)) < \frac{H(A)}{\log_b m} + 1
> $$
>
> $H(A)$je entropie zdroje symbolů z A
>
> $b$je stejný jak pro výpočet informace v entropii (většinou 2 = bit)
>
> $m$je velikost kódové abecedy B

- **Dolní mez:** Průměrná délka kódu nemůže být menší než entropie.
- **Horní mez:** Existuje prefixový kód, jehož průměrná délka překračuje dolní mez nejvýše o 1.

> [!note]
> **Intuice:** Shannonova věta stanovuje limity pro průměrnou délku optimálního kódu.

- Rovnost $\bar{l}(C(A)) = \frac{H(A)}{log_b m}$nastane právě když $P(a_i) = m^{-l(a_i)}$pro všechny symboly. Poté se jedná o tzv. **absolutně optimální kód**.

### 6.3 Redundance kódu

> [!success]
> **Definice:** Redundance kódu je rozdíl mezi skutečnou průměrnou délkou kódu a teoretickým minimem průměrné délky kódu.
>
> $$
> R = \bar{l}(C(A)) - \frac{H(A)}{\log_b m}
> $$

### 6.4 Rozšíření zdrojové abecedy (source extension)

> [!success]
> **Problém**: Shannonova věta dává mezeru až 1 bit.
>
> Změnou zdrojové abecedy na k-tice (nezávislých) symbolů z původní abecedy A lze průměrnou délku kódu $\bar{l}(C(A))$přiblížit k teoretickému minimu $\frac{H(A)}{\log_b m}$.
>
> $$
> \frac{H(A^k)}{\log_b m} \leq \bar{l}(C(A^k)) < \frac{H(A^k)}{\log_b m}+1 \\[1em] \frac{kH(A)}{\log_b m} \leq k\bar{l}(C(A)) < \frac{kH(A)}{\log_b m}+1 \\[1em] \frac{H(A)}{\log_b m} \leq \bar{l}(C(A)) < \frac{H(A)}{\log_b m} + \frac{1}{k}
> $$

> [!danger]
> S rostoucím $k$se průměrná délka na symbol libovolně blíží entropii. **Ale pozor:** abeceda $A^k$může mít velikost až $n^k$, což je v praxi problém (obrovský strom, obrovský slovník).

---

## 7. Typy modelů dat

> [!warning]
> Model dat je matematický popis zdroje dat. Určuje pravděpodobnosti symbolů nebo jejich závislosti a poskytuje informace potřebné pro efektivní kompresi.

### 7.1 Fyzický model

- _Fyzický model_ popisuje **zdroj nebo proces generování dat**. Zaměřuje se na fyzické nebo skutečné aspekty, které vedou ke vzniku dat.
- Obecně je tento model **příliš složitý** nebo nemožný.

### 7.2 Pravděpodobnostní model

- _Pravděpodobnostní model_ popisuje pravděpodobnost výskytu symbolů **nezávisle** se vyskytujících na ostatních symbolech.
- Použití pro statické bezeztrátové kompresní metody.

- **Ignorantní model:** Všechny symboly jsou stejně pravděpodobné.
- **Klasický model:** Pravděpodobnosti se získají z frekvencí výskytu.

> [!info]
> **Zajímavost:** _Problém nulové pravděpodobnosti (zero frequency problem)_. Kompresní metody vyžadují nenulové pravděpodobnosti pro všechny uvažované symboly. Symbol, který se dosud neobjevil, má frekvenci 0, ale nulovou pravděpodobnost mu přiřadit nesmíme (jinak bychom ho nemohli zakódovat).
>
> _Řešení_: nastavíme velmi malou pravděpodobnost.

### 7.3 Markovův model

- _Markovův model_ popisuje pravděpodobnost výskytu symbolu **závisle** na (konečně mnoha) předchozích symbolech (na **kontextu**).
- Použití pro kontextové metody.

- Podle řádu je určen na kolika předchozích symbolech výskyt nového záleží:
  - **Model 1. řádu:** $P(x_j | x_{j-1})$— Pravděpodobnost výskytu symbolu $x_{j}$ závisí pouze na předchozím symbolu $x_{j-1}$.
  - **Markovův model** $k$**-tého řádu:** $P(x_j | x_{j-1}, \ldots, x_{j-k})$— Pravděpodobnost výskytu symbolu $x_{j}$ závisí pouze na předchozích symbolech $x_{j-1}, \ldots, x_{j-k}$.

> [!note]
> **Intuice:** V běžném textu po písmenu „q" téměř jistě následuje „u" — kontext dramaticky ovlivňuje pravděpodobnosti. Markovův model toto zachycuje. Čím vyšší řád, tím **přesnější predikce**, ale **tím víc stavů** ($|A|^k$) a tím víc dat potřebujeme k odhadu pravděpodobností.

#### Příklad

$x_1,x_2,...,x_{10}=\text{aababbabaa}$

  
**stavy modelu 1. řádu** = posloupnosti (bezprostředně) předchozích symbolů délky 1 pro všechny symboly: $a,b$

$P(a)=\frac{5}{9},P(b)=\frac{4}{9},$

$P(a|a)=\frac{2}{5},P(b|a)=\frac{3}{5},P(a|b)=\frac{3}{4}, P(b|b)=\frac{1}{4}$

  
**stavy modelu 2. řád** = posloupnosti (bezprostředně) předchozích symbolů délky 2 pro všechny symbolu: aa, ab, ba, bb

$P(aa)=\frac{1}{8},P(ab)=\frac{3}{8},P(ba)=\frac{3}{8},P(bb)=\frac{1}{8}$

$P(a|aa) \rightarrow 0, P(b|aa) \rightarrow 1, P(a|ab)=\frac{2}{3},P(b|ab)=\frac{1}{3},P(a|ba)=\frac{1}{3},P(b|ba)=\frac{2}{3}, P(a|bb) \rightarrow 1, P(b|bb) \rightarrow 0$


### 7.4 Další modely

- **Slovníkový model:** Paměť _často se vyskytujících vzorů_ (frází) z předchozích dat. Použití pro slovníkové metody (LZ77, LZ78, LZW).
- **Prediktivní model:** Predikce symbolu na základě předchozích. Kódování rozdílu (residua) mezi predikcí a skutečností.
- Modely lze **kombinovat** (např. context mixing v PAQ).

### 7.5 Typy modelů podle adaptivity

| Typ | Popis | Výhody | Nevýhody |
| --- | --- | --- | --- |
| **Statický** | Neměnný, známý předem kompresoru i dekompresoru | Jednoduchost, rychlost | Neoptimální pro konkrétní data |
| **Semi-adaptivní** | Vytvořen z dat (1. průchod), pak neměnný (2. průchod) a předán dekompresoru | Optimální pro daná data | Dva průchody, nutnost přenášet model |
| **Adaptivní** | Dynamicky budován/modifikován za běhu z doposud zpracovaných dat | Jeden průchod, model se nemusí přenášet | Složitější, pomalejší |

> [!danger]
> **Klíčové:** U adaptivního modelu musí kompresor i dekompresor budovat model **stejným způsobem** — dekompresor má k dispozici pouze data, která dosud dekódoval.