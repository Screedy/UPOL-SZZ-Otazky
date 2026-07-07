## 1. Blokové třídění

### 1.1 Popis a princip

- **Blokové třídění** je _transformační technika_ bezeztrátové komprese.

> [!warning]
> **Vstup**:
>
> - Posloupnost symbolů zdrojové abecedy
> - Číslo$K \ ...$maximální velikost bloku
> - (_Volitelně_) Zdrojová abeceda$A$
>
> **Výstup**:
>
> - Číslo$k \ ...$použitá velikost bloku ( často$K$, ale text nemusí vyjít přesně)
> - Transformovaný blok velikosti$k$(posloupnost **posledních symbolů** setříděných rotací)
> - Číslo$i \ ...$pozice originálního bloku

> [!info]
> Jde o **Burrows-Wheeler transformaci** — zkráceně **BWT**.

- **Klíčová vlastnost**: BWT sama o sobě nekomprimuje. Provádí _reverzibilní permutaci_ vstupního bloku dat tak, že výstup **obsahuje shluky stejných symbolů**. Tyto shluky lze pak snadno komprimovat navazujícími metodami (MTF, RLE, statistické kódování).
- BWT **nepoužívá pravděpodobnostní model** ani slovníkový přístup. Pracuje čistě na principu třídění cyklických rotací bloku. Implicitně **využívá kontextové závislosti** v datech — proto se řadí mezi _kontextové metody_.

---

### 1.2 Pseudokód

```
while načti ze vstupu nejvýše K symbolů jako blok b_k do
    zapiš na výstup číslo k // Načtený text by mohl být kratší
    i ← 2
    while i ≤ k do
        b_i^k ← rotace b_{i-1}^k o 1 symbol doleva // Posun jednoho symbolu do leva
        i ← i + 1
    setřiď b_1^k, ..., b_k^k lexikograficky // Setřiď jednotlivé řádky (posuny)
    i ← 1
    while i ≤ k do
        zapiš na výstup poslední symbol b_i^k
        i ← i + 1
    zapiš na výstup číslo i, kde b^k = b_i^k // Kde je originílní řetězec
```

> [!note]
> **Intuice: Proč to funguje?**
>
> _Seřazením cyklických rotací_ se vedle sebe dostanou řádky se **stejným** nebo **podobným kontextem**. Znaky, které těmto kontextům **předcházejí**, _bývají často stejné_, a proto se v posledním sloupci BWT _vytvářejí shluky stejných symbolů_, které lze následně efektivně komprimovat.

**Popis**:

1. Načti blok$b^k = b_1^k$délky$k$ze vstupní posloupnosti. Nejvýše bude mít délku$K$symbolů.
2. Vytvoř$k$_cyklických rotací_ bloku$b^k$:
  - $b_1^k =$původní blok
  - $b_i^k =$rotace $b_{i-1}^k$o 1 symbol doleva (první symbol se přesune na konec)
3. Setřiď všech$k$rotací **lexikograficky**.
4. Výstupem je:
  - číslo$k$(délka bloku)
  - posloupnost **posledních symbolů** setříděných rotací: $L_1, L_2, \ldots, L_k$
  - index$i$řádku, ve kterém se nachází původní (nerotovaný) blok $b^k$

### 1.3 Příklad kódování — krok po kroku

![](/api/files/019ecba4-20d6-7518-be7b-a0736bcf52d2/MacBook-2026-05-14-004638@2x.png)

---

### 1.4 Dekódování (inverzní transformace)

```
načti ze vstupu číslo k
načti ze vstupu k symbolů L_1, ..., L_k
F_i ← L_i pro i = 1, ..., k
setřiď F_1, ..., F_k lexikograficky

// Spočítej počáteční indexy prvního výskytu symbolů ve sloupci F
a ← F_1;  i_F(a) ← 1
for i = 2 to k do
    if F_i ≠ a then
        a ← F_i;  i_F(a) ← i

// Konstrukce mapování mezi stejnými výskyty symbolů v F a L sloupci
// V druhém sloupci se hledá stejný symbol se stejným pořadím výskytu
for i = 1 to k do
    φ^{-1}(i_F(L_i)) ← i 
    i_F(L_i) ← i_F(L_i) + 1

// Rekonstruuj blok
načti ze vstupu číslo i // číslo i = index původního bloku
for j = 1 to k do
    zapiš na výstup symbol F_i
    i ← φ^{-1}(i)
```

![](/api/files/019ecba4-20a7-71b2-879e-20da15aa49d7/MacBook-2026-06-15-004763@2x.png)

> [!info]
> Při ručním výpočtu na papíře je dobrý postup tento:
>
> 1. Zapsat sloupce$F$a$L$HNED vedle sebe. Dopsat sloupec s indexy.
> 2. Přidat sloupec$\varphi^{-1}$. Tedy pro každý symbol v$F$najít stejný symbol v$L$se stejným pořadím výskytu.

---

### 1.5 Implementační aspekty

- **Maximální délka bloku** $K$**:** v praxi až statisíce symbolů (bytů). Větší blok → lepší komprese (delší kontexty), ale vyšší paměťová náročnost.
- **Časová složitost:**
  - Kódování: $O(k \cdot \log k)$ v průměru (závisí na algoritmu třídění suffixů)
  - Dekódování: $O(k)$ (setřídění counting sortem + lineární průchod)
- **Paměťová složitost:** $O(k)$ — pole ukazatelů + originální blok

---

### 1.6 Kompresní pipeline: BWT → MTF → RLE → statistické kódování

BWT se v praxi nikdy nepoužívá samostatně. Typický řetězec zpracování:

1. **BWT (Burrows-Wheelerova transformace):** Permutuje vstupní blok tak, aby se vytvořily shluky stejných symbolů (symboly se stejným kontextem se ocitnou vedle sebe).
2. **MTF:** Převede shluky stejných symbolů na sekvence nul a malých čísel.
3. **RLE:** Zakóduje dlouhé sekvence nul kompaktně.
4. **Huffmanovo nebo aritmetické kódování (statické kódování):** Zakóduje výsledná čísla s proměnnou délkou kódových slov podle frekvencí.

> [!info]
> Tento pipeline je základem kompresoru **bzip2**.