## 1. Huffmanovo kódování

### 1.1 Popis a princip

- Huffmanovo kódování je _pravděpodobnostní_ kompresní algoritmus, který vytváří **optimální prefixový kód**

> [!warning]
> Vstup:
>
> - Posloupnost symbolů ze zdrojové abecedy
> - Číslo $m\ ...$velikost kódové abecedy
> - (_Volitelně_) Seřazené pravděpodobnostní výskyty jednotlivých symbolů z abecedy (od nejmenší po největší)
>
> Výstup:
>
> - Tabulka s kódovými slovy
> - Komprimovaná data

> [!danger]
> **Klíčová vlastnost**: Huffmanův kód je **optimální prefixový kód**. Pro daný pravděpodobnostní model neexistuje prefixový kód s menší průměrnou délkou.

**1.1.1 Podmínka optimality, na kterých Huffmanův algoritmus založen:**

- Pokud sloučíme nejméně pravděpodobné symboly do jednoho nového symbolu, _optimální kód_ pro **zmenšenou abecedu** lze rozšířit na _optimální kód_ **původní abecedy**.
- V optimálním prefixovém kódu mají _pravděpodobnější symboly_ **kratší kódová slova**. _Nejméně pravděpodobné symboly_ mají **stejnou délku kódu** a jejich kódová slova se **liší pouze v posledním symbolu**.

**1.1.2 Základní myšlenka:**

Huffmanovo kódování konstruuje kód **„zdola nahoru"** — od _nejméně pravděpodobných symbolů_:

1. Seřaď symboly podle pravděpodobností (sestupně).
2. Vezmi$m$ symbolů s nejmenšími pravděpodobnostmi a spoj je do jednoho „pseudosymbolu"$m'$se součtovou pravděpodobností.
3. Rekurzivně pokračuj, dokud nezbude jediný symbol (kořen stromu).
4. Kódová slova vzniknou procházením stromu od kořene k listům — na každé hraně přiřadíme symbol kódové abecedy.

**1.1.3 Proč**$m$**a ne**$m'$**?**

- Při binárním kódování$m = 2$ je v prvním kroku vždy $m' = 2$(spojujeme dva symboly). U obecné$m\text{-ární}$kódové abecedy je v **prvním** kroku potřeba $m' = (n - 2) \bmod (m - 1) + 2$symbolů, v dalších krocích pak vždy$m$symbolů.

> [!danger]
> **Důvod:** Chceme, aby všechny kratší kódová slova (všechny vnitřní uzly stromu) měly plný počet$m$potomků. Kdyby první krok sloučil jiný počet symbolů, **vznikly by neobsazené větve** a kód by nebyl optimální.

**1.1.4 Huffmanův strom**

> [!success]
> **Definice:** Huffmanův strom $T_H(A) = \langle V_H(A), E_H(A) \rangle$je $m\text{-ární}$strom, kde:
>
> - **Listové uzly** $v_l(a_i)$odpovídají zdrojovým symbolům $a_i \in A$.
> - **Vnitřní uzly** $v(a'_{n'})$odpovídají pseudosymbolům vytvořeným sloučením v rekurzi.
> - **Kořenový uzel** $v_r$je výsledek posledního sloučení.
> - **Hrany** jsou označeny symboly kódové abecedy $b_1, \dots, b_{m'}$.
> - **Kódové slovo** $C(a)$= zřetězení označení hran na cestě z kořene $v_r$do listu $v_l(a)$.

### 1.2 Typy modelů dat (kontext Huffmanova kódování)

| Model | Jak funguje | Poznámka |
| --- | --- | --- |
| **Statický** | Pravděpodobnosti jsou pevně dané předem (např. ze standardu, z předchozí analýzy). | Kodér i dekodér znají stejný kód bez přenosu modelu. |
| **Semi-adaptivní** | Nejprve se projdou vstupní data (1. průchod), spočtou se frekvence, vytvoří se kód, pak se data zakódují (2. průchod). | Model (strom/tabulka) se musí přenést spolu s daty. |
| **Adaptivní** | Kód se mění průběžně po každém zpracovaném symbolu; kodér i dekodér si udržují stejný strom. | Není potřeba přenášet model — oba ho budují identicky. |

### 1.3 Pseudokód (semi-adaptivní Huffmanovo kódování)

#### Algoritmus

```shell
function HuffmanSemiAdapt (A, P, start):
  // Jestli je méně znaků v abecedě než velikost kódové abecedy, tak stačí pouze        
  // přiřadit indexy jako kód
  if n ≤ m then
      C(aᵢ) ← bᵢ pro i = 1, ..., n    
  else
      if první = true then // Když m není rovno 2, první velikost sloučení je jiné
          m' ← (n − 2) mod (m − 1) + 2
      else
          m' ← m
      
      // Slučovní symbolů s nejmenší pravděpodobností
      A' ← (A \ {aₙ₋ₘ'+1, ..., aₙ}) ∪ {a'ₙ' = aₙ₋ₘ'+1 ... aₙ}
      p'ₙ' ← Σ pᵢ  (pro i = n−m'+1, ..., n, kde toto jsou nejmenší pravděpodobnosti)
      
      // Zavolej se rekurzivně s A', příslušnými pravděpodobnostmi a false
      HuffmanSemiAdapt (A', P', false)
      
      // Vezmi kód nového sloučeného symbolu a připoj k němu různé symboly kódové abecedy.
      C(aₙ₋ₘ'+ᵢ) ← C(a'ₙ') bᵢ  pro i = 1, ..., m'
  
  HuffmanSemiAdapt (A = {a₁, ..., aₙ}, {p₁, ..., pₙ}, true)
```


- **Jak funguje krok po kroku:**

1. **Spočítáme frekvence** jednotlivých symbolů ve zdroji dat. Každý symbol s jeho frekvencí vložte do prioritní fronty, která je _seřazena podle frekvence_ (nejméně časté symboly mají prioritu).
2. Z prioritní fronty postupně _odstraňujeme m symbolů_ (první průchod může být jiný) _s nejnižší frekvencí_, sloučíme je do jednoho **nového "symbolu"**, jehož frekvence je součtem frekvencí původních symbolů, a vložíme tento nový symbol zpět do fronty.
3. Po dokončení procesu slévání by měla prioritní fronta _obsahovat pouze jeden "symbol"_, který **reprezentuje celý soubor** symbolů.
4. Ze seznamu zaznamenaných sloučení **vytvoříme kódová slova**. Při každém sloučení  
  přiřadíme vzniklým větvím symboly kódové abecedy (např. 0 a 1). Kód každého  
  symbolu vznikne z posloupnosti symbolů na cestě od kořene k danému symbolu.

### 1.4 Příklad kódování — binární kód ($m = 2$)

#### Příklad

**Vstup:** `barbaraabarboraubaru`

**Frekvence a pravděpodobnosti:**

| Symbol | Frekvence | Pravděpodobnost |
| --- | --- | --- |
| a   | 7   | 7/20 = 0.35 |
| b   | 5   | 5/20 = 0.25 |
| r   | 5   | 5/20 = 0.25 |
| u   | 2   | 2/20 = 0.10 |
| o   | 1   | 1/20 = 0.05 |

**Kroky konstrukce (zdola nahoru):**

```
Krok 1: Spojíme u (2) a o (1) → pseudosymbol "uo" (3)
        Zbylé: {a:7, b:5, r:5, uo:3}

Krok 2: Spojíme r (5) a uo (3) → pseudosymbol "ruo" (8)
        Zbylé: {ruo:8, a:7, b:5}

Krok 3: Spojíme a (7) a b (5) → pseudosymbol "ab" (12)
        Zbylé: {ab:12, ruo:8}

Krok 4: Spojíme ab (12) a ruo (8) → kořen (20)
```

**Výsledný strom:**

![](/api/files/019ec2d8-b712-74ac-a4dd-7c03af00adbb/MacBook-2026-05-13-004634@2x.png)

**Výsledné kódy:**

| Symbol | Kód | Délka |
| --- | --- | --- |
| a   | 00  | 2   |
| b   | 01  | 2   |
| r   | 10  | 2   |
| u   | 110 | 3   |
| o   | 111 | 3   |


### 1.5 Příklad kódování — ternární kód ($m=3$)

#### Příklad

Tentýž vstup `barbaraabarboraubaru`, $A = {a, b, r, u, o}$, $n = 5$, $m = 3$.

**Výpočet** $m'$**:** $m' = (5 - 2) \bmod (3 - 1) + 2 = 3 \bmod 2 + 2 = 1 + 2 = 3.$

```
Krok 1: Spojíme 3 symboly s nejmenšími p: r(5), u(2), o(1) → "ruo"(8)
        Zbylé: {ruo:8, a:7, b:5}

Krok 2: |A'| = 3 ≤ m = 3 → přiřadíme přímo:
        C(a) = 0,  C(b) = 1,  C(ruo) = 2
```

**Výsledné kódy:**

| Symbol | Kód | Délka |
| --- | --- | --- |
| a   | 0   | 1   |
| b   | 1   | 1   |
| r   | 20  | 2   |
| u   | 21  | 2   |
| o   | 22  | 2   |

**Zakódovaný vstup:**

`b a r b a r a a b a r b o r a u b a r u` → `1 0 20 1 0 20 0 0 1 0 20 1 22 20 0 21 1 0 20 21`


### **1.6 Dekódování**

1. Načti model z hlavičky komprimovaných dat.
2. Čti bity a procházej strom od kořene; při dosažení listu vypiš symbol a začni znovu od kořene.

---

## 2. Speciální případy Huffmanova kódu

### 2.1 Unární kód jako Huffmanův

- Pokud _každý symbol_ je **výrazně pravděpodobnější** než _všechny následující symboly dohromady_. Vznikne velmi nevyvážený strom, což v podstatě vytvoří unární kód.

![](/api/files/019ec2d8-b6fa-7289-8ad2-6097756c1417/MacBook-2026-06-13-004746@2x.png)

### 2.2 Blokový kód jako Huffmanův

- V případě _rovnoměrného rozdělení pravděpodobností_ se Huffmanův kód degeneruje na **blokový kód,** ve kterém mají všechna kódová slova stejnou délku.

![](/api/files/019ec2d8-b70b-7249-bfc4-cd9d3a6cef8f/MacBook-2026-06-13-004748@2x.png)

### 2.3 Minimální rozdíly v délkách kódových slov

- Říká, že pokud při konstrukci Huffmanova stromu _vhodně rozhoduješ mezi symboly se stejnou pravděpodobností_, můžeš získat kód, kde se délky kódových slov liší co nejméně.
- **Příklad**: Oba kódy mají stejnou průměrnou délku, takže jsou optimální. První je ale "vyváženější", protože délky se liší méně.

![](/api/files/019ec2d8-b705-756e-95ab-bedc2f1967a0/MacBook-2026-06-13-004745@2x.png)

---

## 3. Aplikace Huffmanova kódování

- **Komprese obrazu:** JPEG (starší standardy)
- **Komprese dat:** Deflate (ZIP, gzip, PNG)
- **Kombinace s jinými metodami:** Často v návaznosti na diferenční kódování (obraz, zvuk), RLE, nebo BWT+MTF.

---

## 4. Složitost a praktické aspekty

### 4.1 Časová složitost

- **Konstrukce stromu:** $O(n \log n)$
- **Kódování/dekódování:** $O(N \cdot l_{\max})$kde $N$je délka vstupu a $l_{\max}$maximální délka kódového slova.

### 4.2 Prostorová složitost

- **Strom:** $O(n)$uzlů. Přesně $2n - 1$uzlů pro binární strom, kde $n$je počet symbolů.
- **Tabulka kódů:** $O(n)$pro uložení kódových slov.