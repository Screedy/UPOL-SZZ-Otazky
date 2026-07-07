## 1. Huffmanovo kódování

### 1.1 Popis a princip

- Huffmanovo kódování je _pravděpodobnostní_ kompresní algoritmus, který vytváří **optimální prefixový kód**

> [!warning]
> **Vstup**:
>
> - Posloupnost symbolů ze zdrojové abecedy
> - Číslo $m\ ...$velikost kódové abecedy
>
> **Výstup**:
>
> - Komprimovaná data

> [!danger]
> **Klíčová vlastnost**: Huffmanův kód je **optimální prefixový kód**. Pro daný pravděpodobnostní model neexistuje prefixový kód s menší průměrnou délkou.

**1.1.1 Hlavní výhody a nevýhody adaptivního modelu**

**Výhody:**

- Není třeba předem znát rozdělení symbolů ani posílat tabulku → vhodné pro **streamování** (data přicházejí postupně, neznáme celou délku).
- Kodér i dekodér si udržují **shodný strom** ze stejných dat → strom se nepřenáší.
- Přizpůsobuje se **lokálním změnám statistiky** (např. text mění téma) — na rozdíl od jednoho statického stromu.

**Nevýhody:**

- Na _začátku_, než se nasbírají četnosti, _kóduje hůř_ (krátké soubory).
- **Aktualizace stromu** po každém symbolu je výpočetně _náročnější_.

**1.1.2 Triviální (naivní) přístup**:

- Po každém symbolu kompletně **přestavět** Huffmanův strom z aktuálních četností. Korektní, ale **výpočetně neúnosné.**

**1.1.3 Klíčové principy adaptivního Huffmanova kódování**

**Sourozenecká vlastnost (sibling property)**

> [!success]
> **Definice**: Binární strom s nezápornými váhami uzlů je Huffmanův (tj. odpovídá optimálnímu prefixovému kódu) **právě tehdy**, když lze jeho uzly očíslovat tak, že:
>
> - každý uzel, kromě kořene, má svého **sourozence**,
> - uzly _lze seřadit_ do posloupnosti _podle neklesající váhy_ $w_1 \le w_2 \le \dots \le w_{2n-1}$, ve které **sourozenci sousedí** (uzly$2k-1$a$2k$jsou sourozenci) a každý uzel má **číslo menší** než jeho rodič.

> [!note]
> **Intuice**: V Huffmanově stromu platí, že **čím méně pravděpodobný symbol, tím hlouběji leží** (delší kód). Sibling property je přesné kritérium, jak to ověřit: očíslujeme uzly „odspodu nahoru, zleva doprava" podle vah a musí vyjít, že váhy nikdy neklesají a sourozenci jsou vždy vedle sebe. Pokud po inkrementaci nějakého listu tato vlastnost přestane platit, stačí **prohodit** porušující uzel na správné místo.

- **Jak se využívá v algoritmu:** U každého uzlu:
  
  - **počet výskytů**$n(x)$symbolu$x$ (= váha uzlu),
  - **pořadové číslo**$i(v(x))$uzlu.
  
  Při inkrementaci váhy listu pak postupujeme od listu ke kořeni a kdekoliv by se sibling property porušila, **prohodíme** uzel (i s celým podstromem) s uzlem, který má **nejnižší pořadové číslo mezi uzly stejné váhy**. Tím se sibling property zachová s minimem práce.

**Speciální (escape) symbol ε**

> [!success]
> **Problém:** Na začátku je strom prázdný a kodér postupně narazí na symboly, které ještě nikdy neviděl. Jak **dekodéru sdělit** „tohle je nový symbol"?
>
> **Řešení**: Speciální (escape) **symbol ε**

- V abecedě je navíc symbol$\varepsilon$značící **neexistující / první výskyt** symbolu.
- Strom začíná jako jediný list$\varepsilon$.
- Když kodér potká **nový** symbol$a$(jeho list ve stromu ještě není), pošle:
  1. **kód**$\varepsilon$— cesta stromem k aktuálnímu listu$\varepsilon$ (tj. „pozor, nový symbol)
  2. **doslovné zakódování symbolu** $a$ (např. jeho fixní binární/ASCII zápis nebo raw symbol).
- Když kodér potká **známý** symbol, pošle jen jeho kód (cestu stromem).

> [!danger]
> **Důležitý detail:** Při úplně **prvním** symbolu je$C(\varepsilon)$ještě **prázdný řetězec** (strom má jediný list$\varepsilon$v kořeni), takže se pošle jen doslovné zakódování symbolu. Teprve od druhého symbolu má $\varepsilon$nenulovou cestu.

---

### 1.2 Pseudokód

#### 1.2.1 Inicializace

```
T_H(A) ← ⟨{ vl(ε) }, ∅⟩       // Vytvoří se strom = jediný list ε, žádné hrany
C(ε)   ← prázdný řetězec      // Kód ε = přázný řetězec
n(ε)   ← 0                    // Váha ε = 0
i(vl(ε)) ← 1                  // Pořadové číslo ε = 1
```

#### 1.2.2 Kódovací smyčka (pseudokód)

```
while načti ze vstupu symbol a ∈ A do
    if vl(a) ∉ V_H(A) then          // Symbol ještě není ve stromu
        zapiš na výstup C(ε) a zakódování a
    else                            // Symbol už ve stromu je
        zapiš na výstup C(a)
    zavolej AKTUALIZAČNÍ algoritmus (viz sekce 1.2.3 a 1.2.4)
```

- Aktualizace má **dvě větve**: vkládání nového symbolu a inkrementaci existujícího.

#### 1.2.3 Aktualizace stromu — nový symbol

```
if vl(a) ∉ V_H(A) then
    // Dosavadní list ε se změní na vnitřní uzel x = aε
    V_H(A) ← V_H(A) ∪ { vl(a), v(x = aε) }
    n(a) ← 1;  n(x) ← 0
    i(v(x))  ← i(vl(ε))             // vnitřní uzel přebere pořadové číslo starého ε
    i(vl(a)) ← i(v(x)) + 1        
    i(vl(ε)) ← i(vl(a)) + 1
    // Přepojení hran: pod nový uzel x dáme nový list a (0) a ε (I)
    E_H(A) ← (E_H(A) \ {⟨v(yε), vl(ε)⟩_b})
             ∪ { ⟨v(x), vl(ε)⟩_I, ⟨v(x), vl(a)⟩_0, ⟨v(yx), v(x)⟩_b }
    // Pokračuj inkrementací vah nahoru (viz 1.2.4) od uzlu x
```

- **Nový symbol jde na hranu** `0`**,** $\varepsilon$**zůstává na hraně** `I`

> [!note]
> **Intuice:** Vezmu list$\varepsilon$, „rozdvojím" ho na vnitřní uzel se dvěma potomky: nově viděný symbol$a$(váha 1) a$\varepsilon$(váha 0). Pak je potřeba přičíst jedničku všem předkům až ke kořeni.

#### 1.2.4 Aktualizace stromu — existující symbol

```
else
    v(x) ← vl(a)

// Pokračování inkrementací vah od uzlu x ke kořeni
while v(x) ≠ vr do 
    // Najdi uzel se STEJNOU váhou a NEJNIŽŠÍM pořadovým číslem
    najdi v(y): i(v(y)) ≤ i(v(z)) ∀ v(z) s n(y)=n(z)=n(x)
    if v(y) ≠ v(x) ∧ ⟨v(y), v(x)⟩ ∉ E_H(A) then  // Pokud není stejný uzel a není to rodič
        // Prohození podstromů x a y 
        E_H(A) ← (E_H(A) \ {⟨u, v(x)⟩_b, ⟨t, v(y)⟩_b'})
                 ∪ { ⟨t, v(x)⟩_b, ⟨u, v(y)⟩_b' }
        // Prohození pořadových čísel
        i ← i(v(x));  i(v(x)) ← i(v(y));  i(v(y)) ← i
    n(x) ← n(x) + 1                              // teprve teď inkrementuj
    v(x) ← u,  ⟨u, v(x)⟩ ∈ E_H(A)                // přejdi na rodiče
n(x) ← n(x) + 1                                  // inkrementuj kořen
```

> [!danger]
> - **Klíčová pravidla:**
>   1. **Nejprve prohození, teprve potom inkrementace.** Pokud bychom inkrementovali dřív, prohození by se počítalo se špatnou vahou.
>   2. Prohazujeme s uzlem stejné váhy a **nejmenšího pořadového čísla**, **nikdy s vlastním rodičem**.
>   3. Postupujeme **od listu ke kořeni**, na každé úrovni rozhodneme o přesunu, inkrementujeme, jdeme výš.

---

### 1.3 Příklad kódování — krok po kroku

#### Příklad

`barbaraabarboraubaru`

Abeceda $A = {a, b, r, u, o}$, kódová abeceda binární ($m = 2$). Pořadové číslo uzlu je u něj uvedeno.

**Start:** jediný list `ε` (číslo 1),$C(\varepsilon)=$prázdný.

![](/api/files/019ec66d-5155-730f-b0e3-9ac2bfce776e/MacBook-2026-06-14-004754@2x.png)

**Symbol** `b` (nový, ε prázdné) → výstup `b` (jen doslovný symbol):

![](/api/files/019ec644-adc7-730f-a703-69de778c0d75/MacBook-2026-06-14-004749@2x.png)

Nyní $C(b)=$`0`, $C(\varepsilon)=$`1`.

**Výstup po** `b`**:** `b`

**Symbol** `a` (nový) → výstup `C(ε)`$\cdot$`a` = `1`$\cdot$`a` = `1a`. Rozštěpíme list ε:

![](/api/files/019ec646-df6d-7249-a270-3ee757f3dc84/MacBook-2026-06-14-004750@2x.png)

Nyní$C(b)=$`0`, $C(a)=$`10`, $C(\varepsilon)=$`11`.

**Výstup po** `ba`**:** `b1a`

**Symbol** `r` (nový) → výstup `C(ε)` + `r` = `11` + `r` = `11r`:

![](/api/files/019ec648-2296-7673-99a6-c7beee91e64d/MacBook-2026-06-14-004751@2x.png)

Nyní$C(b)=$`0`, $C(a)=$`10`, $C(r)=$`110`, $C(\varepsilon)=$`111`.

**Výstup po** `bar`**:** `b1a11r`

> [!danger]
> **Pozor!** Změnilo se pořadové číslo pravé a levé větve pod kořenem. Je možné i změnit větve, ale není to potřeba.

**Symbol** `b` (existující) → výstup `0`

![](/api/files/019ec64b-9bbe-7263-bae3-1962cde9051d/MacBook-2026-06-14-004752@2x.png)

Symbol `b` **už ve stromu je**. Žádné prohození není třeba. Inkrementujeme váhu listu `b`.

**Výstup po** `barb`**:** `b1a11r0`

**Symbol** `u` (existující) → výstup `11110`

![](/api/files/019ec695-40ce-723f-a855-d61f50ef7d98/MacBook-2026-06-14-004758@2x.png)

Symbol `u` už ve stromu je. Symbol `o` má stejnou váhu a menší pořadové číslo → dojde k prohození se symbolem `u`. Symbol `a` má stejnou váhu a menší pořadové číslo → dojde k prohození se symbolem `rouε`. Poté inkrementujeme.

**Finální výstup:**

`b1a11r01011010010011010111o11001111u10011011110`


---

### 1.4 Dekódování

```javascript
// Inicializujeme stejný strom jako v kóderu
T_H(A) ← ⟨{ vl(ε) }, ∅⟩
n(ε) ← 0
i(vl(ε)) ← 1

while není konec vstupu do
    v ← vr                              // Počáteční vrchol je kořen

    // Procházej strom podle bitů, dokud nenaražíš na list
    while v ≠ vl(a) do                  
        načti ze vstupu bit b ∈ B
        v ← u,  ⟨v, u⟩_b ∈ E_H(A)

    if a = ε then                      // Došli jsme k listu ε → nový symbol 
        načti ze vstupu zakódování symbolu a ∈ A a zapiš a na výstup
    else                               // Našli jsem konkrétní symbol
        zapiš na výstup symbol a ∈ A

    zavolej STEJNÝ aktualizační algoritmus (sekce 1.2.4)
```

- **Symetrie:** Dekodér používá **identický aktualizační algoritmus** jako kodér. Protože oba vidí stejnou posloupnost symbolů, jejich stromy zůstávají **bit po bitu shodné** → strom se nikdy nepřenáší.

---

### 1.5. Varianty algoritmu

- **FGK (Faller–Gallager–Knuth):**
  - Historicky první praktický inkrementační algoritmus.
  - Při prohazování bere uzel s **nejnižším pořadovým číslem** ve váhové třídě (to, co popisuje přednáškový pseudokód).
  - Strom může být „nevyvážený" — průměrná délka kódu je o něco horší než u Vittera.
- **Vitter (algoritmus Λ / V, 1987):**
  - Vylepšuje FGK pomocí **implicitního číslování** a dodatečné invariantní podmínky (preferuje uzly výše ve stromu).
  - **Garantuje**, že počet bitů adaptivního kódu nepřekročí délku statického Huffmana o více než$O(1)$na symbol; konkrétně dává **nejvýše o jeden bit na symbol více** než ideální statický Huffman.
  - V praxi obvykle o trošku lepší komprese než FGK.
- **Společné:** obě udržují **sibling property**, liší se jen pravidlem výběru uzlu pro prohození a uspořádáním.

---

### 1.6. Složitost a implementační poznámky

- **Časová složitost na symbol:** $O(l)$, kde $l$je délka kódu daného symbolu (= hloubka listu) — aktualizace probíhá po cestě od listu ke kořeni. Pro celý vstup délky $N$tedy $O(N \cdot \bar{l})$.
- **Prostorová složitost:** $O(n)$uzlů pro abecedu velikosti $n$(strom má nejvýše $2n-1$uzlů + uzel ε).