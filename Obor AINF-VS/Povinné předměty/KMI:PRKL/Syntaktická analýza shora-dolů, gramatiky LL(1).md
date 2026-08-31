> [!success]
> **Syntaktický analyzátor (parser)** _využívá lexikální analýzu, je také součástí části Front-End_. Jeho úkolem je _rozpoznávat_ **syntaktické celky programu** (např. deklarace, výrazy nebo příkazy) a následně je předat k sémantické analýze.

- Syntaxi běžného programovacího jazyka **nelze popsat regulární gramatikou**.
  - Typickým příkladem jsou _závorkové struktury_, kde je potřeba zajistit _stejný počet otevíracích a uzavíracích závorek_, což **regulární gramatika nedokáže vyjádřit**.
  - Proto se syntaxe popisuje **bezkontextovou gramatikou (CFG)** $G = (N, T, P, S).$
- Syntaktický analyzátor je realizován jako **deterministický zásobníkový automat**. Během analýzy se sestavuje **derivační strom** odpovídající vstupnímu programu. Existují dva základní směry jeho sestavování:
  - **Shora-dolů** — strom se staví od kořene (počáteční symbol $S$) směrem k listům (terminální symboly)
  - **Zdola-nahoru** — strom se staví od listů směrem ke kořeni (od terminálních symbolů k počátečnímu)
- Deterministickou syntaktickou analýzu lze provádět pouze pro určité podtřídy bezkontextových gramatik:
  - **LL(k)** gramatiky – používají se při analýze **shora-dolů**,
  - **LR(k)** gramatiky – používají se při analýze **zdola-nahoru**.

> [!info]
> V praxi se z LL(k) tříd používá výhradně **LL(1)**.

---

# 1. Princip zásobníkového automatu pro analýzu shora-dolů

> [!success]
> Při syntaktické analýze shora-dolů se používá **deterministický zásobníkový automat**, který pracuje pouze se **zásobníkem** (nevyužívá stavy). Na zásobníku se nacházejí terminální i neterminální symboly gramatiky a analýza **vždy pracuje pouze s jeho vrcholem** (odebírá se právě jeden symbol)

- Zásobníkovými symboly je množina $N \cup T$ výchozí gramatiky.
- Během analýzy automat provádí dvě základní operace:

| Operace | Kdy se provádí | Co dělá |
| --- | --- | --- |
| **Expanze** | na vrcholu zásobníku je neterminál $A$ | **nahradí** $A$ _pravou stranou pravidla_ $A \to X_1 X_2 \dots X_k$ |
| **Srovnání** | na vrcholu zásobníku je terminál $t$ | **porovná** $t$ se symbolem na vstupu:   _jsou-li shodné_, odstraní oba   _jsou-li neshodné_, syntaktická chyba |

- Na začátku analýzy obsahuje zásobník pouze **počáteční symbol gramatiky** a _na vstupu se nachází posloupnost terminálních symbolů_ vytvořená lexikálním analyzátorem. Parser opakovaně provádí expanze a srovnání.
- Automat přijme zdrojový program jako syntakticky správný, pokud je **přijat celý vstup a zásobník je na konci prázdný**.

## 1.1 Ukázkový příklad (princip, ne ještě tabulkově řízený automat)

#### Příklad

Gramatika jazyka aritmetických výrazů:  
$T=\set{+,-,,/,i,(,)}\\ N=\set {E}\\ P=\set{E \to E{+}E \mid E{-}E \mid E{}E \mid E{/}E \mid i \mid (E)}$

Průběh pro vstup `(i+i)*i-i` (vrchol zásobníku vlevo):

```
Vstup           Zásobník     Akce
(i+i)*i-i       E            expanze dle E→E*E
(i+i)*i-i       E*E          expanze dle E→(E)
(i+i)*i-i       (E)*E        srovnání symbolu (
i+i)*i-i        E)*E         expanze dle E→E+E
i+i)*i-i        E+E)*E       expanze dle E→i
i+i)*i-i        i+E)*E       srovnání i
+i)*i-i         +E)*E        srovnání +
i)*i-i          E)*E         expanze dle E→i
i)*i-i          i)*E         srovnání i
)*i-i           )*E          srovnání )
*i-i            *E           srovnání *
...             ...          (analogicky dále)
```

> [!info]
> Tento příklad jen ilustruje operace expanze/srovnání — volba pravidla při expanzi je zde dělána „ručně". Tato gramatika je navíc **nejednoznačná a s levou rekurzí**, tedy **není LL(1)**. Aby automat mohl rozhodovat deterministicky (bez ručního zásahu), je potřeba gramatiku vhodně upravit a řízení expanze svěřit **LL(1) tabulce**.


---

# 2. Gramatiky LL(1)

- Pro deterministickou syntaktickou analýzu shora-dolů se používají **gramatiky LL(k)**.
- V praxi se však téměř výhradně používají **gramatiky LL(1)**, protože umožňují jednoduchou a efektivní implementaci parseru.

## **2.1 Význam názvu LL(1)**

- **první L (Left to right)** — vstupní řetězec se čte **zleva doprava**.
- **druhé L (Leftmost derivation)** — používá se **levá derivace** (derivuje se vždy nejlevější neterminál).
- **1** — parser potřebuje pro rozhodnutí pouze **jeden vstupní symbol dopředu (lookahead)**. Podle něj _jednoznačně určí, které produkční pravidlo použije_.

> [!danger]
> Každé rozhodnutí je **deterministické**.

## 2.2 Podmínka LL(1) gramatiky

> [!note]
> Ne každá bezkontextová gramatika je současně gramatikou LL(1).

> [!success]
> Bezkontextová gramatika je **LL(1)** právě tehdy, když pro každá dvě pravidla se stejným neterminálním symbolem na levé straně
>
> $$
> A→α\newline A→β
> $$
>
> platí **podmínka disjunktnosti množin** **First-Follow**:
>
> $$
> \text{First}(\alpha, \text{Follow}(A)) \cap \text{First}(\beta, \text{Follow}(A)) = \emptyset
> $$

> [!info]
> To znamená, že parser musí být schopen **na základě jediného vstupního symbolu jednoznačně určit, které pravidlo použít**. Pokud by se _množiny překrývaly, parser by nevěděl, kterou produkci zvolit_, a gramatika by nebyla LL(1).

(Zápis $\text{First}(\alpha,\text{Follow}(A))$ znamená: spočti First řetězce, kde za $\alpha$ následně dosadíš možné symboly z $\text{Follow}(A)$— používá se hlavně tehdy, když $\alpha \Rightarrow^* \varepsilon$.)

## 2.3 Množina FIRST

> [!note]
> Množina **FIRST** obsahuje _všechny terminální symboly_, kterými _může začínat řetězec odvozený z daného symbolu nebo posloupnosti symbolů_. Pokud lze odvodit prázdný řetězec, obsahuje také symbol $\varepsilon.$

> [!success]
> $$
> \text{First}(\alpha) = \set{t \mid \alpha \Rightarrow^* t\mu,\ t \in T} \cup \set{\varepsilon \mid \alpha \Rightarrow^* \varepsilon}
> $$

### 2.3.1 Algoritmus výpočtu First($\alpha$)

1. Jestliže řetězec $\alpha$ **začíná** _terminálem_ $t$
  1. $\text{First}(\alpha) = \set{t}$
2. Jestliže řetězec $\alpha$ **začíná** _neterminálem_ $B$, vezmeme všechna pravidla se symbolem $B$ na levé straně $B \to \beta_1 \mid \dots \mid \beta_k$ a výpočet převedeme na rekurzivní volání:
  1. $\text{First}(\alpha) = \text{First}(\beta_1) \cup \dots \cup \text{First}(\beta_k)$
3. Je-li argument rekurze prázdný řetězec položíme
  1. $\text{First}(\varepsilon) = \set{\varepsilon}$.

### 2.3.2 Příklad výpočtu First

Gramatika:  
$S \to A \mid B \mid d\\ A \to aA \mid \varepsilon\\ B \to b \mid \varepsilon$

Chceme $\text{First}(ABd)$. Postupným odvozováním:

```
ABd ⇒ aABd     (A → aA)
ABd ⇒ Bd ⇒ bd  (A → ε, B → b)
ABd ⇒ Bd ⇒ d   (A → ε, B → ε)
Firtst(ABd) = {a, b, d}
```

## 2.4 Množina FOLLOW

> [!note]
> Množina **FOLLOW** obsahuje všechny _terminální symboly_, které se _mohou ve správně vytvořené větě_ objevit **bezprostředně za daným neterminálem**. Pokud může být _neterminál na konci věty_, obsahuje také symbol označující konec vstupu $\varepsilon.$

> [!success]
> $$
> \text{Follow}(A) = \set{t \mid S \Rightarrow^* \mu A \nu,\ \nu \neq \varepsilon,\ t \in \text{First}(\nu)} \cup \set{\varepsilon \mid S \Rightarrow^* \mu A}
> $$

### 2.4.1 Algoritmus výpočtu Follow(A)

- Využívají se dvě množiny:
  - $H$… množina _neterminálních symbolů, které jsme již uvažovali_ (aby se výpočet nezacyklil)
  - $Y$… aktuální uvažovaný symbol

1. $H = \emptyset$,$Y = A$.
2. Byl symbol $Y$ uvažován?
  1. Ano … konec této větve
  2. Ne … $H = H \cup {Y}$ a nastavíme $\text{Follow}(Y) = \emptyset$
3. Je $Y = S$ (startovní symbol)
  1. Ano … přidej $\varepsilon$ do $\text{Follow}(Y)$
4. Vezmeme _všechna pravidla s_ $Y$ na **pravé straně** $X \to \mu Y \nu$ a pro ně uvažujeme:
  1. je-li $\nu \neq \varepsilon$: spočti $G = \text{First}(\nu)$.
    1. Pokud $\varepsilon \notin G$, přidej $G$ do $\text{Follow}(Y)$.
    2. Pokud $\varepsilon \in G$, přidej $G - {\varepsilon}$ a navíc rekurzivně spočti $\text{Follow}(X)$ a přidej ho také.
  2. je-li $\nu = \varepsilon$: rekurzivně spočti a přidej $\text{Follow}(X)$.

### 2.4.2 Příklad výpočtu Follow

Gramatika:  
$S \to AB\\ A \to Ca\\ B \to Bb \mid cC\\ C \to d$

Chceme $Follow(C)$:

```
1. Y = C
A → Ca -> First(a) = a -> Follow(C) = Follow(C)∪{a}
B → cC -> Follow(C)=Follow(C)∪Follow(B)
2. Y = B
B → Bb -> First(b) = b -> Follow(B)=Follow(B)∪{b}
S → AB -> Follow(B)=Follow(B)∪Follow(S)
3. Y = S
startovavní symbol -> Follow(S) = Follow(S)∪{ε}

Follow(C)={a,b,ε}
```

---

# 3. Konstrukce LL(1) tabulky a činnost automatu

- Jakmile jsou vypočteny množiny **FIRST** a **FOLLOW**, lze sestavit **LL(1) tabulku**, podle které parser _při syntaktické analýze rozhoduje, jaké produkční pravidlo použije_.

## 3.1 Konstrukce LL(1) tabulky

1. Očíslujeme všechna pravidla gramatiky.
2. Pro každé pravidlo $A \to \alpha$ spočítáme množinu $\text{First}(\alpha \ \text{Follow}(A))$.
3. Sestavíme tabulku:
  1. Řádky = neterminály
  2. Sloupce = terminály $\cup \ {\varepsilon}$
  3. Do pozice $[A, t]$ zapiš **číslo pravidla** $A \to \alpha$ právě tehdy, když $t \in \text{First}(\alpha,\text{Follow}(A))$. Není-li žádné takové pravidlo, pozice zůstává prázdná (= syntaktická chyba, pokud tam analýza dojde).

## 3.2 Kompletní příklad

LL(1) gramatika popisující výrazy se sčítáním a závorkami (operandy zastupuje $i$):

$1.\ E \to TF \\ 2.\ F \to {+}TF \\ 3.\ F \to \varepsilon\\ 4.\ T \to (E) \\ 5.\ T \to i$

Výpočet First-Follow množin pro každé pravidlo:

| číslo pravidla | pravidlo | First-Follow množina |
| --- | --- | --- |
| 1   | $E \to TF$ | $\text{First}(TF) = \set{(, i}$ |
| 2   | $F \to {+}TF$ | $\text{First}({+}TF) = \set{+}$ |
| 3   | $F \to \varepsilon$ | $\text{Follow}(F) = \set{),\varepsilon}$ |
| 4   | $T \to (E)$ | $\text{First}((E)) = \set{(}$ |
| 5   | $T \to i$ | $\text{First}(i) = \set{i}$ |

_Tabulka automatu:_

![[019f864e-daeb-748e-8bde-17d7272a13a7.png]]

## 3.3 Činnost automatu s tabulkou

1. Na začátku analýzy se na zásobník vloží **počáteční symbol gramatiky** a na vstupu je posloupnost tokenů vytvořená lexikálním analyzátorem.
2. V každém kroku:
  1. Je-li na vrcholu zásobníku neterminál $A$ a na vstupu terminál $x$, vyhledá se v tabulce pozice $[A, x]$:
    - obsahuje-li číslo pravidla → provede se **expanze**;
    - je-li prázdná → **syntaktická chyba**.
  2. Je-li na vrcholu zásobníku terminál → provede se **srovnání** se vstupem (úspěch = odstranění obou, neúspěch = chyba).
3. Konec: _vstup vyčerpán a zásobník prázdný_ → zdrojový **kód je syntakticky správný.**

Průběh pro vstup `i+(i+i)`:

```
Vstup       Zásobník   Akce
i+(i+i)     E          expanze dle 1: E→TF
i+(i+i)     TF         expanze dle 5: T→i
i+(i+i)     iF         srovnání i
+(i+i)      F          expanze dle 2: F→+TF
+(i+i)      +TF        srovnání +
(i+i)       TF         expanze dle 4: T→(E)
(i+i)       (E)F       srovnání (
i+i)        E)F        expanze dle 1: E→TF
i+i)        TF)F       expanze dle 5: T→i
i+i)        iF)F       srovnání i
+i)         F)F        expanze dle 2: F→+TF
+i)         +TF)F      srovnání +
i)          TF)F       expanze dle 5: T→i
i)          iF)F       srovnání i
)           F)F        expanze dle 3: F→ε
)           )F         srovnání )
            F          expanze dle 3: F→ε
            prázdný    ✓ analýza úspěšná
```

## 3.4 Konstrukce syntaktického analyzátoru metodou rekurzivního sestupu

> [!success]
> LL(1) tabulka může být místo explicitní datové struktury implementována přímo jako **sada vzájemně volajících se funkcí** (jedna funkce na neterminál), kde `switch` podle vstupního symbolu rozhoduje o pravidle — tzv. **rekurzivní sestup**.

> [!info]
> Tomuto tématu (implementace, generování kódu funkcí) se podrobně věnuje **samostatný okruh 4**.

---

# 4. Transformace gramatik na LL(1) tvar

- Ne každá bezkontextová gramatika _splňuje podmínky gramatiky_ **LL(1)**. Pokud parser _nedokáže podle jednoho vstupního symbolu jednoznačně rozhodnout_, které pravidlo použít, vznikají v LL(1) tabulce **konflikty**. V mnoha případech je lze odstranit vhodnou **transformací gramatiky**, aniž by se změnil jazyk, který gramatika popisuje..

## 4.1 Levá faktorizace

> [!success]
> Odstraňuje konflikt **First-First** — více pravidel se stejným neterminálem má stejný začátek pravé strany: $A \to \alpha\alpha_1 \mid \alpha\alpha_2 \mid \dots \mid \alpha\alpha_k$

- Nahradí se:  
  $A \to \alpha A'\\ A' \to \alpha_1 \mid \alpha_2 \mid \dots \mid \alpha_k$

> [!info]
> **Příklad:** $A \to abc \mid abd$ ⟶ $A \to abA'$, $A' \to c \mid d$.

## 4.2 Pohlcení řetězce

> [!success]
> Odstraňuje konflikt **First-Follow**, typický u pravidel tvaru  
> $A \to \alpha B \omega\gamma\\ B \to \omega \mid \varepsilon$  
> kde $\text{First}(\omega) \cap \text{Follow}(B) \neq \emptyset$, protože $\omega$ se vyskytuje i za $B$ v $A$.

> [!note]
> **Intuice**: Když na vrcholu _zásobníku bude_ $B$ _a na vstupu_ $w$ _nevíme_, jestli pokračovat v pravidle $A$ (expandovali bychom podle $B \to\varepsilon$) nebo expandovat podle $B \to \omega$

- Zavede se nový neterminál $B'$ nahrazující $B\omega$:  
  $A \to \alpha B'\\B' \to \omega\omega \mid \omega \xrightarrow{\text{lev. faktorizace}} B' \to \omega B$

> [!info]
> **Příklad:**  
> $A \to Babu\\ B \to a \mid \varepsilon$  
> (pohlcovaný řetězec je $a$):  
> $A \to B'bu\\ B' \to aa \mid a\xrightarrow{\text{lev. faktorizace}} B' \to aB\\ B \to a \mid \varepsilon$

## 4.3 Odstranění levé rekurze

> [!danger]
> Gramatika obsahující **levou rekurzi** **není gramatikou LL(1)**, protože parser by se při _rekurzivním sestupu dostal do nekonečné rekurze_. Proto je před konstrukcí LL(1) parseru nutné levou rekurzi odstranit.

### **4.3.1 Přímá levá rekurze**

> [!success]
> Přímá rekurze má tvar
>
> $A \to A\alpha \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_s$ kde produkce **začíná stejným neterminálem**, který je _na levé straně pravidla_.
>
> Takovou gramatiku lze **převést na pravou rekurzi** zavedením nového neterminálu:  
> $A \to \beta_1 A' \mid \beta_2 A' \mid \dots \mid \beta_s A'\\ A' \to \alpha A' \mid \varepsilon$

> [!info]
> **Příklad:** $A \to Aa, A \to b \mid cc$ ⟶ $A \to bA' \mid ccA'$, $A' \to aA' \mid \varepsilon$.

### **4.3.2 Nepřímá levá rekurze**

> [!success]
> Nepřímá levá rekurze nastává tehdy, když se _neterminál_ **_odkazuje sám na sebe_** _přes jeden nebo více dalších neterminálů_, například
>
> $$
> A→Bα,B→Aβ.
> $$
>
> Nejprve se provede **substituce** pravidel tak, aby _vznikla přímá levá rekurze_, a následně se _odstraní stejným postupem jako v předchozím případě_.

## 4.4 Substituce

> [!success]
> Substituce je _pomocná transformace_, při níž se **pravá strana** jednoho pravidla **dosadí do jiného pravidla**.

- Používá se zejména tehdy, když _konflikt není na první pohled patrný_, ale vzniká **až přes jiný neterminál**. Po substituci lze zpravidla _použít levou faktorizaci nebo odstranit levou rekurzi_.

> [!info]
> **Příklad:** $A \to aa \mid Bb$, $B \to a \mid b$
>
> $\text{First}(aa) = {a}$,$\text{First}(Bb) = {a,b}$— konflikt First-First, ale skrytý za $B$.
>
> Substitucí $B$ do $A \to Bb$ dostaneme $A \to aa \mid ab \mid bb$, a levou faktorizací:  
> $A \to aA' \mid bb\\ A' \to a \mid b$

---

# 5. Nejednoznačnost gramatiky — problém „dangling else"

> [!info]
> Transformace z oddílu 4 **neopraví nejednoznačnou gramatiku** — jen _odstraňují technické konflikty_ v LL(1) tabulce.

- **Klasický příklad** je podmínkový příkaz:

$Z \to S\\ S \to \texttt{if(C)}S\ \texttt{else}\ S \mid \texttt{if(C)}S \mid \text{ostatní příkazy}$

- _Levá faktorizace_ dá:

$S \to \texttt{if(C)}S \ S'\\ S' \to \texttt{else} \ S \mid \varepsilon$

> [!danger]
> I po faktorizaci ale $\text{First}(\texttt{else} \ S) = \set{\texttt{else}}$ a zároveň $\texttt{else} \in \text{Follow}(S')$→ konflikt zůstává, protože gramatika je skutečně **nejednoznačný!**
>
> Pro vstup:
>
> ```
> if (C) if (C) S else S
> ```
>
> existují dva různé derivační stromy podle toho, ke kterému `if` patří `else` :
>
> ![[019f8907-77cd-739e-b3b4-93bcda31bc1f.png]]
>
> ![[019f8907-ab17-771a-9193-614fc0b14cc1.png]]

- _Řešení v praxi_:
  - Konvence, že `else` patří **nejbližšímu** předchozímu `if` (tak to řeší většina jazyků — konflikt se v tabulce/parseru vyřeší ve prospěch delšího výrazu),
  - Konflikt ošetřit ručně přímo ve funkcích rekurzivního sestupu,
  - V některých jazycích (Visual Basic) se `if` explicitně ukončuje `end if`, čímž nejednoznačnost úplně mizí
  - Případně **přejít na analýzu zdola-nahoru**.

---

# 6. Zotavení z chyby při analýze shora-dolů

> [!success]
> Chyba syntaktické analýzy se **snadno zjistí** — automat se zastaví, pokud:
>
> - **srovnání selže** (terminál na zásobníku ≠ terminál na vstupu)
> - pro _neterminál na vrcholu zásobníku_ a aktuální vstupní symbol **není** v tabulce **žádné pravidlo expanze**.

> [!danger]
> Obtížnější je **zotavení** — synchronizace vstupu s automatem tak, aby mohl pokračovat.

## 6.1 Obecné metody zotavení

- **Oprava zdrojového kódu** (vynechání/vložení/náhrada symbolů) — přesná, ale riskantní.
  - Špatná oprava může vyvolat novou chybu.
  - Při vkládání symbolů může kód „nekontrolovaně růst".
- **Panický mód (panic mode)** — bezpečnější.
  - Po chybě se vynechává vstup až po nejbližší **význačný symbol** k **_omezovačům_** (typicky `;`, `{`, `}`, `#`).
  - **Nevýhoda**: může se vynechat i syntakticky správná část kódu.

## 6.2 Metoda zotavení specifická pro analýzu shora-dolů

1. Pro symboly aktuálně na zásobníku sestav **množinu přípustných symbolů** = sjednocení množin First těchto symbolů $\cup \ \set{\#}$ (# = konec programu).
2. Ve zdrojovém textu přeskakuj symboly, dokud nenarazíš na symbol z této množiny.
3. Synchronizuj automat pomocí algoritmu:

```
synchronizován = false
while not synchronizován
  if na vrcholu zásobníku je terminální symbol t
    uděláme srovnání
    if srovnání není úspěšné
      odebereme symbol t ze zásobníku (má to stejný efekt jako kdybychom ho
      vložili do zdrojového programu a provedli úspěšné srovnání)
    else // srovnání je úspěšné
      odstraníme symbol t ze zásobníku a ze vstupu
       synchronizován = true
  else // na vrcholu zásobníku je neterminální symbol A
    if není pravidlo expanze pro A při daném symbolu na vstupu
      odebereme neterminální symbol a nahradíme ho na zásobníku nejkratším
      řetězcem terminálních symbolů, které lze v gramatice z něho odvodit
    else // je pravidlo expanze pro A
      uděláme expanzi
```

### Příklad

Gramatika:

```
P → B
B → { C }
C → B | S C | ε
S → i=E; | while (E) S | ;
E → E+E | i
```

Vstup: `{ while (+i } #`

```
Vstup             Zásobník          Akce
{while(+i}#       P                 expanze P→B
{while(+i}#       B                 expanze B→{C}
{while(+i}#       {C}               srovnání {
while(+i}#        C}                expanze C→SC
while(+i}#        SC}               expanze S→while(E)S
while(+i}#        while(E)SC}       srovnání while
(+i}#             (E)SC}            srovnání (
+i}#              E)SC}             ✗ není pravidlo pro expanzi E
```

Množina přípustných symbolů = First(E) ∪ First()) ∪ First(S) ∪ First(C) ∪ {#} = `{ ( i ) ; while { } # }`.

```
Vstup     Zásobník    Akce
+i}#      E)SC}       vynech symboly po nejbližší přípustný (+ se vynechá)
i}#       E)SC}       nyní je pravidlo E→i → expanze
i}#       i)SC}       srovnání i — úspěšné
}#        )SC}        obnovení normální analýzy
```

- Analýza dále pokračuje standardně (expanze/srovnání), dokud nenarazí na další chybu nebo neskončí s prázdným zásobníkem a vstupem.