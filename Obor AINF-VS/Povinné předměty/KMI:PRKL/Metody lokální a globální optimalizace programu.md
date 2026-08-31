> [!success]
> **Optimalizace** je _transformace interní formy programu_, která **zachovává sémantiku** programu, ale _zlepšuje jeho kvalitu_ — typicky rychlost vykonávání, případně velikost výsledného kódu.

- Základní dělení optimalizací je na **lokální** a **globální** optimalizace.
- Jde o dělení podle **rozsahu kódu, kterýž překladač uvažuje**

> [!warning]
> **Základní blok programu** je část programu, v níž **uvnitř není žádná instrukce větvení**  
> (podmíněný nebo nepodmíněný skok, volání podprogramu, synchronní přerušení). Instrukce  
> větvení _může být jen poslední instrukcí základního bloku_. Dále _návěští_ určené pro skok do  
> základního bloku _může být jen na jeho začátku_ (u první instrukce bloku).
>
> **Graf toku dat** je _orientovaný graf s vlastnostmi_:  
> • Jeho _uzly_ jsou **základní bloky** programu.  
> • _Hrany_ vyjadřují **přechody** (větvení) **mezi jednotlivými základními bloky**.
>
> Ze základního bloku $B_1$ je hrana do bloku $B_2$, jestliže v programu po ukončení bloku $B_1$  
> může nastat přechod do bloku $B_2$.

# 1. Lokální optimalizace

> [!success]
> **Lokální optimalizace** se provádí _v rámci jednoho základního bloku_. (odděleně jednotlivé bloky)

## 1.1 Vyhodnocení konstantních výrazů

> [!warning]
> **Konstantní výraz** je výraz, jehož _hodnotu lze urči_t již **v době překladu**, protože všechny jeho _operandy mají známé konstantní hodnoty_.

> [!success]
> Překladač tak výraz **vypočítá** _při překladu_ a místo několika instrukcí _vloží přímo výslednou hodnotu_.

**Příklad:**

`b = 5;`  
`c = a + 2*b;`

- Podvýraz `2*b` je konstantní (`b=5` z předchozího přiřazení).

| Neoptimalizující | Optimalizující |
| --- | --- |
| `(*, 2, b, t1)` | `(+, a, 10, t1)` |
| `(+, a, t1, t2)` | `(=, t1, -, c)` |
| `(=, t2, -, c)` |     |

> [!note]
> Ušetřila se jedna instrukce násobení a jedna dočasná proměnná.

## 1.2 Eliminace společných podvýrazů

> [!success]
> Dva výrazy jsou považovány za **společné**, jestliže mají stejnou operaci a jejich operandy mají _prokazatelně stejné hodnoty_.

- Pokud se v jednom základním bloku _několikrát vyskytne stejný výraz_ a jeho hodnota se mezitím **nezměnila**, _není nutné jej znovu počítat_. Překladač **výsledek prvního výpočtu uloží** a _při dalším výskytu jej pouze použije_.

**Příklad:**

```
a = b + c;
d = b;
e = (d + c) * f;
```

- Podvýrazy `b+c` a `d+c` **jsou shodné**, protože _v důsledku přiřazení_ `d = b` mají operandy stejné hodnoty.
- _Optimalizovaně:_

```
t = b + c;   
a = t;   
d = b;   
e = t * f;
```

## 1.3 Algoritmus nalezení společných podvýrazů a vyhodnocení konstantních výrazů

- V algoritmu se u každé proměnné **uvažují dva atributy**:
  - `const` … Atribut určující, zda hodnota proměnné **je konstantní**.
  - `num` … **Atribut hodnoty**. Je číselný. Je volen tak, že tento atribut má _u dvou proměnných_ **stejnou hodnotu** je v případě, že je zaručeno, že **hodnota proměnných je stejná**.
- Dále si zavedeme proměnnou `numval`, kterou budeme používat **pro generování hodnot pro číslování**. 

1. **Počátek**:
  1. `numval = 0`
  2. _Pro každou proměnnou_ `v`, která se _objevuje v základním bloku_ **nastavíme** na začátku bloku _její atributy_:
    1. `v.const = false`
    2. `v.num = ++numval`
2. **Procházíme jednotlivé čtveřice** základního bloku a postupně se _u každé čtveřice provedou kroky_:
  1. Jestliže má čtveřice **tvar přiřazení**: `(=, var1, _ , var)` //var = var1
    1. Nastavíme atributy:
      1. `var.const = var1.const`
      2. `var.num = var1.num`
  2. Jestliže má čtveřice **tvar přiřazení**: `(=, konstanta, _ , var)` // var = 4
    1. Nastavíme atributy:
      1. `var.const = true`
      2. `var.num = ++numval`
  3. Jestliže čtveřice **reprezentuje unární operaci**: `(op, arg, _ , var)` //var = !a
    1. Jestliže má `arg.const` hodnotu `true`, **jedná** se **konstantní výraz**:
      1. _Nahradíme_ čtveřicí: `(=, hodnota, _ , var)`
      2. `var.const = true`
      3. `var.num = ++numval`
    2. **Nejedná-li se o konstantní výraz**, prohledá se _předchozí část základního bloku_, jestli neobsahuje čtveřici `(opx, argx, _ varx)` takovou, že `op = opx` a `arg.num = argx.num`
      1. Jestliže **najdu takovou čtveřici** (byl nalezen společný podvýraz): 
        1. _Nahradíme_ čtveřicí: `(=, varx, _ ,var)`
        2. `var.const = varx.const`
        3. `var.num = varx.num`
      2. _Jinak_:
        1. `var.const = false`
        2. `var.num = ++numval`
  4. Jestliže čtveřice reprezentuje **binární operaci** `(op, arg1, arg2, var)` //var = a + b
    1. Jestliže má `arg1.const` i `arg2.const` hodnotu `true`, **jedná** se **konstantní výraz**:
      1. **Vypočítáme** hodnotu výrazu `(hodnota = arg1 op arg2)`
      2. _Nahradíme_ čtveřicí: `(=, hodnota, _ , var)`
      3. `var.const = true`
      4. `var.num = ++numval`
    2. Jestliže má pouze **jeden argument atribut const** pravdivý
      1. Nahradíme tento operand _ve čtveřici příslušnou hodnotou_ 
    3. **Nejedná-li se o konstantní výraz**, prohledá se _předchozí část základního bloku_, jestli neobsahuje čtveřici `(opx, arg1x, arg2x, varx)` takovou, že `op = opx` a `arg1.num = arg1x.num` a `arg2.num = arg2x.num` (pokud je op komutativní, může to být i do kříže)
      1. Jestliže **najdu takovou čtveřici** (byl nalezen společný podvýraz): 
        1. _Nahradíme_ čtveřicí: `(=, varx, _ ,var)`
        2. `var.const = varx.const`
        3. `var.num = varx.num`
      2. Jinak:
        1. `var.const = false`
        2. `var.num = ++numval`
3. Po provedení těchto optimalizací následuje **odstranění dočasných proměnných**, _které už nejsou potřebné_, a _s nimi spojené přiřazení_.

#### Příklad

Základní blok:

```
a = 4
d = b*c+1
e = 2*a*d
f = b
g = f*c+b*a
```

Na začátku se atributy nastaví:

![[019d7dce-6512-759d-8b57-2ad982f60364.png]]

Interní forma, konstantní výrazy a společné podvýrazy:

![[019d7dce-fb79-7562-87f5-c16927736939.png]]

Po lokální optimalizaci a odstranění zbytečných dočasných proměnných:

![[019d7dcf-5a73-710f-9e76-88d7a0fea801.png]]![[019d7dcf-d740-7733-a32c-ea4d6562c812.png]]


---

# 2. Globální optimalizace

> [!success]
> **Globální optimalizace** na rozdíl od lokální optimalizace _neoptimalizuje pouze jednotlivé základní bloky_, ale také **tok dat mezi nimi**. Díky tomu dokáže nalézt _více možností optimalizac_e, její implementace je však _výrazně složitější._

- Stejně jako lokální optimalizace využívá **vyhodnocení konstantních výrazů** a **eliminaci společných podvýrazů**, avšak již _na úrovni celého programu nebo funkce_. Kromě toho obsahuje **metody specifické pro globální optimalizaci**.

## 2.1 Konstantní výrazy na globální úrovní

- Princip je _stejný jako u lokální optimalizace_ – pokud _lze hodnotu výrazu určit již při překladu_, překladač ji _vypočítá a nahradí výsledkem_.
- Rozdíl spočívá v tom, že se **nepracuje pouze v jednom základním bloku**, ale _využívají se informace z více bloků programu_.

## 2.2 Nalezení společných podvýrazů na globální úrovni

- Metoda číslování hodnot, která je využívána na lokální úrovní je _na globální úrovní obtížně realizovatelná_.

### 2.2.1 SSA (Static Single Assignment)

> [!success]
> **Základní myšlenka**: Každé přiřazení _vytvoří novou verzi proměnné_.

- Je značně složitá. Je potřeba nalézt tzv. **dominátory v grafu toku dat**.

### 2.2.2 Metoda založená na množinách

- Za _společné podvýrazy se považují ty_, které mají:
  - **Stejnou operaci**
  - **Stejné operandy**
  - **Hodnota** žádného z operandů **nebyla** mezi nimi **změněna**
- _Pro každý základní blok se vypočítají množiny:_

| Množina | Význam |
| --- | --- |
| `AvailIn(b)` | Výrazy k dispozici **na začátku** bloku `b` |
| `AvailOut(b)` | Výrazy k dispozici **na konci** bloku `b` |
| `Comp(b)` | Výrazy vypočítané v `b` a stále platné na konci |
| `Kill(b)` | Výrazy z `AvailIn`, které přestaly platit (změna operandu) |

**Rovnice:**

- Uvnitř _základního bloku_:

$$
\tt{AvailOut}(b)=\tt{Comp}(b) \cup (\tt{AvailIn}(b)-\tt{Kill}(b)) \ \ \ \ \ \ \ (I )
$$

- Vyjadřuje, že na konci bloku `b` jsou k dispozici výrazy, jež buďto:
  - byly k dispozici na začátku bloku (`AvailIn`) a nebyly změněny hodnoty jejich operandů (množina `Kill`),
  - nebo byly v bloku vypočítány a jsou na konci bloku (množina `Comp`).

- _Mezi bloky_ :

$$
\tt{AvailIn(b)} = \cap_{p\in \text{Pred}(b)} \tt{AvailOut(p)} \ \ \ \ \ \ \ (II)
$$

- kde `Pred(b)` je množina všech bloků, které jsou předchůdci bloku `b` v grafu toku dat.

> [!note]
> Rovnice vyjadřuje, že výraz _je k dispozici na začátku bloku_ jen pokud je k dispozici na konci **všech** **jeho předchůdců**

Soustava těchto rovnic se počítá **iterativním způsobem**:

1. Na začátku pro všechny bloky `b` stanov `AvailIn(b) = ∅`.
2. Opakovaně počítáme `AvailOut` dle $(\text I)$ a `AvailIn` dle $(\text{II})$, dokud se nedosáhne ustáleného stavu (množiny nepřestanou měnit)

#### Příklad

Uvažujme graf toku dat se 4 bloky:

![[019d95e2-8676-74cd-92b5-077841900f8c.png]]

Množiny `Comp` a `Kill` pro jednotlivé bloky:

![[019d95e3-1693-738b-ad83-ab98eb62f716.png]]![[019d95e3-813f-717f-9e12-0f41120a4451.png]]

Množiny `AvailIn` a `AvailOut` pro ukončení iterativního výpočtu:

![[019d95e4-0257-710d-8d28-eb9ee965807b.png]]

Odtud vyplývá, že v bloku `B4` není nutné generovat kód pro výrazy `u+1` a `x+y`.


### 2.2.3 Optimalizace cyklů

> [!success]
> Optimalizace cyklů se zaměřují na zrychlení vykonávání cyklů. Cílem je odstranit zbytečné výpočty nebo snížit počet prováděných instrukcí při každé iteraci

#### **a)** Přesun invariantních výrazů mimo cyklus

- Výraz, jehož hodnota se v jednotlivých průchodech cyklu nemění, je vyňat a jeho výpočet je dán **před cyklus**.

```c
// Před optimalizací
for (i=0; i<100; ++i) { 
  a[i] = c/d; 
}

// Po optimalizaci
t = c/d;
for (i=0; i<100; ++i) { 
  a[i] = t; 
}
```

#### **b) Induktivní výrazy**

> [!warning]
> - **Induktivní proměnná** je proměnná, jejíž hodnota se _při každém průchodu_ cyklu _zvýší/sníží o hodnotu výrazu_ **nezávislého na cyklu.**
> - **Induktivní výraz** má tvar `a*i + b,`kde
>   - `a, b` jsou na cyklu nezávislé výrazy
>   - `i` je induktivní proměnná.
> - Optimalizace nahradí násobení _přičítáním přírůstku_.

```cpp
// Před optimalizací
for (i=0, j=m; i<n; ++i, j+=k) { 
  c[i] = a*j-b; 
}

// Po optimalizaci
t1 = a*m-b;     // počáteční hodnota
t2 = a*k;       // přírůstek
for (i=0; i<n; ++i) { 
  c[i] = t1; 
  t1 += t2; 
}
```

#### **c) Rozvinutí cyklu (loop unrolling)**

- U cyklů s _malým konstantním počtem průchodů a malým tělem_ se cyklus odstraní a **nahradí příkazy** reprezentujícími jednotlivé průchody.

```cpp
// Před
for (i=0; i<3; ++i) { 
  a[i] = 2*i; 
}

// Po
a[0] = 0;
a[1] = 2;
a[2] = 4;
```

## 2.3 Optimalizace volání funkce

- Funkce volaná **jen v jednom místě** programu se nahradí přímo svým tělem.
- Tím se odstraní časová režie volání (příprava argumentů, uložení návratové adresy, skok, návrat).

## 2.4 Nalezení neinicializovaných proměnných

> [!success]
> Tato metoda zjišťuje proměnné, jejichž hodnota je použita, aniž by jim byla předtím přiřazena hodnota – takový stav vede k nepředvídatelným výsledkům.

- **Základní pojmy:**
  - Proměnná je **definována**, když je jí přiřazena hodnota
  - Proměnná je **živá**, jestliže byla _definována_, dále je na ní _reference_ (její hodnota je použita), a mezitím _nebyla znovu definována_
  - **Oblast života** – část programu _mezi definicí a referencí_
- _Pro každý blok se vypočítají množiny:_

| Množina | Význam |
| --- | --- |
| `LiveIn(b)` | Proměnné živé na **začátku** bloku |
| `LiveOut(b)` | Proměnné živé na **konci** bloku |
| `Use(b)` | Proměnné, na které jsou v `b` reference, aniž byly v `b` předtím definovány |
| `Kill(b)` | Proměnné definované v bloku `b` |

- _Rovnice_**:**

$$
\tt{LiveIn}(b)=\tt{Use}(b) \cup (\tt{LiveOut}(b)-\tt{Kill}(b)) \ \ \ \ \ (I)
$$

> [!note]
> Vyjadřuje, že na začátku bloku je proměnná živá, pokud v tomto bloku obsahuje referenci, aniž by předtím byla v bloku definovaná.

$$
\tt{LiveOut}(b) = \cup_{s \in \text{Succ}(b)} \tt{LiveIn}(s)\ \ \ \ \ (II)
$$

- Kde `Succ(b)` je množina _bloků, které jsou následníci bloku_ `b` v grafu toku dat.

Soustava těchto rovnic se počítá **iterativním způsobem**:

1. Začíná `LiveOut(b) = ∅`.
2. Opakovaně se počítají všechny množiny `LiveIn(b)` dle rovnice $(\text I)$ a množiny `LiveOut(b)` dle rovnice $(\text{II})$, dokud se nedosáhne ustáleného stavu (množiny se přestanou měnit)

> [!info]
> **Detekce neinicializovaných proměnných:** `LiveIn` počátečního bloku by měla být **prázdná**. Pokud není, obsahuje proměnné, u kterých není zaručena inicializace.

#### Příklad:

Uvažujme graf toku dat se 4 bloky:

![[019d95ee-0bd2-76ff-86bb-e3e67c4d1916.png]]

Množiny `Ref` a `Kill` pro jednotlivé bloky jsou:

![[019d95ee-79e6-733a-bbf0-d027726af7ef.png]]

Množiny `AvailIn` a `AvailOut` po ukončení iterativního výpočtu:

![[019d95ee-eb44-728b-b901-5844912f3c56.png]]

- Množina _LiveIn_ počátečního bloku (zde je to _B1_) by měla být prázdná.
  - Pokud není, obsahuje proměnné, u kterých není zaručena inicializace.
  - V tomto příkladu je to proměnná _s_, která v případě, že přechod do bloku _B3_ bude z bloku _B2_, nebude mít přiřazenu počáteční hodnotu.


---

# 4. Superlokální optimalizace

> [!success]
> **Superlokální optimalizace** optimalizuje **rozšířené základní bloky**.

> [!warning]
> Rozšířený základní blok je _tvořen několika základními bloky_, které jsou propojeny tak, že:
>
> - do prvního bloku může vstupovat více cest,
> - všechny ostatní bloky mají právě **jednoho předchůdce**.

> [!info]
> **Princip:** Když optimalizujeme blok, který má jednoho předchůdce, můžeme přebrat informace o atributech proměnných (const, num) z konce předchůdce a pokračovat v jejich aktualizaci. To umožní detekovat společné podvýrazy přes hranice základních bloků.

---

# 5. Okénková (peephole) optimalizace

> [!success]
> Provádí se **na konci**, až _po vygenerování instrukcí cílového kódu_. Jde o úpravy směřující k odstranění zbytečných instrukcí nebo jejich zjednodušení.

**1. Odstranění zbytečných instrukcí:**

```
add AX, 0       // přičtení 0 → odstranit
mul AX, 1       // násobení 1 → odstranit
```

**2. Nahrazení jednoduššími instrukcemi:**

```
add AX, 1       →     inc AX     // inkrementace
sub AX, 1       →     dec AX     // dekrementace
mul AX, 2       →     shl AX, 1  // bitový posun místo násobení
```

> [!info]
> **Název "okénková"** je odvozen od skutečnosti, že při této optimalizaci se uvažuje jen určitý počet za sebou následujících instrukcí, které tvoří **okénko posouvající se** postupně po vygenerovaném kódu.