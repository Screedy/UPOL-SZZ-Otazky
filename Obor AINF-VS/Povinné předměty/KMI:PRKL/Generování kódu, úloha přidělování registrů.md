> [!success]
> **Generování kódu** (**Back End**) je _poslední fáze překladu_.  
> Jejím úkolem je **převést interní reprezentaci programu** (nejčastěji čtveřice) do _cílového kódu pro konkrétní procesor_.

- Hlavní činnosti při generování kódu jsou:
  - **Statické stanovení pořadí instrukcí**
  - **Přidělování registrů**
  - **Volba formátu instrukcí**
  - Případně **okénková optimalizace**

<div class="joplin-table-wrapper"><table style="min-width: 306px"><tbody><tr><th colspan="1" rowspan="1" colwidth="281"><p data-id="salsxvbbmmno">Forma cílového programu</p></th><th colspan="1" rowspan="1"><p data-id="mqwqikqruwmc">Vlastnosti</p></th></tr><tr><td colspan="1" rowspan="1" colwidth="281"><p data-id="ygfzlngqsdbd"><strong>Kompletní program v jazyce stroje</strong></p></td><td colspan="1" rowspan="1"><p data-id="ikdxhflzkxrm">Přímo spustitelný, ale vhodný jen pro velmi krátké programy.</p><ul><li><p data-id="wlxkjtxbfpfh">historicky u 8-bitových mikropočítačů</p></li></ul></td></tr><tr><td colspan="1" rowspan="1" colwidth="281"><p data-id="fengllryludp"><strong>Modul s relativními adresami</strong></p></td><td colspan="1" rowspan="1"><p data-id="sxwiqxflgoaw"><strong>Nejběžnější.</strong> Interní adresy relativní k začátku modulu, externí adresy nevyplněné + seznam externích odkazů. Doplní je až <strong>sestavovací program (linker)</strong></p></td></tr><tr><td colspan="1" rowspan="1" colwidth="281"><p data-id="uydkyjnacttg"><strong>Program v jazyce symbolických adres</strong></p></td><td colspan="1" rowspan="1"><p data-id="vpohulovnuwb">Generování je jednodušší, ale překlad je celkově delší — je nutný ještě průchod assemblerem</p></td></tr></tbody></table></div>

> [!info]
> _Front-end_ + _strojově nezávislé optimalizace_ mohou být **pro všechny platformy společné**, pro každou **cílovou platformu** se dělá jen _vlastní back-end_.

---

# 1. Statické stanovení pořadí vykonávání instrukcí

> [!info]
> Tato činnost souvisí **s pipeline architekturou procesorů.**

- V ní je _vykonávání strojové instrukce_ rozděleno do **pevného počtu fází**.
- Počet fází je dán architekturou procesoru, _typické je rozdělení_ na **5 fází**:

1. **Načtení** instrukce
2. **Dekódování** operačního kódu
3. **Výpočet** aritmetické/logické operace **nebo** výpočet adresy u instrukcí čtení/zápisu do paměti
4. **Přístup** do paměti
5. **Zápis** výsledku aritmetické/logické operace do registru

- Procesor může vykonávat **všech 5 fází současně**, každou u jiné instrukce — _v ideálním případě_ tedy **zahajuje novou instrukci v každém taktu**.
- Všechny instrukce _procházejí všemi 5 fázemi_, i když je **nevyužijí**.

![[019f9dad-a561-7269-ab50-8afe0e481214.png]]

## 1.1 Datové závislosti

> [!success]
> Operace je **datově závislá** na jiné operaci, jestliže pro své vykonání **potřebuje její výsledek**.

- _Příklad_:

```c
d = (a+b)*c;
z = x-y;
```

- V prvním příkazu je operace `*` datově závislá na operaci `+` → _může proběhnout až po ní_.
- Ve druhém příkazu je `-` datově **nezávislá** na operacích prvního příkazu → _může se vykonat kdykoliv_.

- Je-li _datově závislá instrukce v pipeline hned za instrukcí_, _jejíž výsledek potřebuje_, musí procesor **čekat**.
- Úlohou překladače je **přeuspořádat instrukce tak, aby mezi závislé dvojice vložil nezávislé instrukce** — _sémantika programu se nesmí změnit_. Chce aby _pipeline, byla co nejlépe využita_.

> [!warning]
> **Pozor na kompromis:** Přeuspořádání sice zkrátí čekání, ale **prodlouží oblasti života** hodnot.  
> Plánování instrukcí a přidělování registrů proto **jdou proti sobě** (méně registrů znamená více `store`/`load`, více souběžně živých hodnot znamená větší tlak na registry)

---

# 2. Přidělování registrů

- V interní formě programu je **velký počet proměnných**: _Proměnné ze zdrojového kódu_ **a navíc dočasné proměnné** _vzniklé při generování interní formy_.
- Je-li hodnota v registru, je přístup k ní **výrazně rychlejší**, než když se musí načíst z paměti, ale registrů procesoru je **konečný, malý počet** (typicky jednotky až desítky) → je nutné stanovit uložení proměnných (v registru/v paměti)

> [!success]
> **Úloha přidělování registrů:** rozhodnout, hodnoty kterých proměnných budou uchovány v registrech pro následné použití a které budou uloženy do paměti (i za cenu, že se při dalším použití musí znovu načíst).

> [!danger]
> **Optimální využití registrů je NP-úplný problém** — jeho časová složitost je exponenciální, a tedy časově nepřijatelná.  
> Řeší se proto pouze **heuristickými, časově přijatelnými metodami**.  
> V současnosti se převážně používá metoda založená na **barvení grafu**.

## 2.1 Přidělování registrů v základním bloku metodou barvení grafu

- Výchozí je zde graf interferencí mezi oblastmi života proměnných. Základní pojmy:
  - **Proměnná je definována**, když je jí přiřazena hodnota.
  - **Proměnná je živá**, jestliže byla definována, někde dále je na ni **reference** a mezitím **nebyla znovu definována** (nebyla jí přiřazena nová hodnota).
  - **Oblast života proměnné** je část programu mezi definicí proměnné a referencí.
- Vlastnosti grafu interferencí:
  - **Uzly** = oblasti života proměnných.
  - **Hrana** mezi dvěma uzly ⟺ oblasti života reprezentované těmito uzly se **překrývají**.
  - _Význam hrany_: hodnoty těchto dvou proměnných **nemohou být uchovány ve stejném registru**.

### 2.1.1 Algoritmus přidělování registrů barvením grafu

- **Výchozí podmínky:**
  - Je dán graf interferencí $I$.
  - Je k dispozici $m$ registrů. Registry jsou reprezentovány $m$ barvami, barvám jsou přiřazena čísla $1, \dots, m$.

1. Nechť $G$ je _kopie_ grafu $I$.
2. Odebíráme uzly a ukládáme je na zásobník následovně:   
  **Je v** $G$ **uzel se stupněm** $< m$**?** 
  1. **Ano** … Odebereme ho a _přidáme jej na zásobník_ $Z$_._
  2. **Ne** … Odebereme z $G$ _kterýkoliv uzel_ a uložíme jej na zásobník. A pokračujeme dál s odebíráním uzlů.
3. Po uložení všech uzlů na zásobník, _uzly ze zásobníku odebíráme a barvíme je v grafu_ $I$. Odebereme uzel $u$ ze zásobníku $Z$. Najdeme barvu s nejmenším číslem kterou lze uzel obarvit s ohledem na předtím již obarvené jeho sousedy v grafu $I$.   
  **Existuje taková barva?**
  1. **Ano** … Uzel o_barvíme a pokračujeme_ s dalším uzlem na zásobníku.
  2. **Ne** …  Vezmeme z **doposud neobarvených uzlů** uzel s **největším stupněm** a **odstraníme** ho z grafu. Hodnota reprezentovaná tímto _uzlem bude uložena do paměti_. **Celý proces se znovu opakuje** od kroku 1 s novým grafem $I$. 
4. Pokud _zásobník je prázdný, algoritmus se ukončí._ Po ukončení algoritmu obarvené uzly reprezentují proměnné, jejichž hodnota lze uchovat v registrech.

#### Příklad:

**Uvažujme základní blok** (trojadresný kód; sledujeme proměnné `a`–`f`):

![[019f9ee6-11b3-7689-bc4d-f31eb40ba21e.png]]

**Graf interferencí** $I$:

![[019fd383-2b08-71d6-8236-63668706b847.png]]

Stupně uzlů: $\deg(a)=1,\ \deg(b)=5,\ \deg(c)=4,\ \deg(d)=3,\ \deg(e)=3,\ \deg(f)=2$.

Všimněte si, že ${b,c,d,e}$ tvoří **úplný podgraf** $K_4$ — čtyři proměnné jsou v okamžiku 6–7 živé současně.

#### Fáze 1 — plnění zásobníku (počet registrů $m = 3$)

| Krok | Uzel | Zdůvodnění | Zásobník $Z$ |
| --- | --- | --- | --- |
| 2   | `a` | $\deg(a)=1 < 3$ | `a` |
| 2   | `f` | po odebrání `a`: $\deg(f)=2 < 3$ | `a f` |
| 3   | `b` | zbyly `b,c,d,e` — všechny mají stupeň 3, žádný $< m$→ **libovolný uzel** | `a f b` |
| 2   | `c`,`d`,`e` | po odebrání `b` mají `d e` stupeň 2 | `a f b d e c` |

#### Fáze 2 — obarvování (barvy 1, 2, 3)

- Postupně ze zásobníku odebereme uzly `c, e, d` a obarvíme je:![[019f9ef0-7655-725a-837c-34aeef3ad435.png]]
- Následně uzel `b` obarvit nelze → všechny jeho sousedé jsou obarveni všemi barvami. V grafu $I$ odstraníme uzel `b`.![[019f9ef2-0d3a-7194-9eea-5c79cb433434.png]]
- Znovu odebíráme z grafu $G$ uzly a ukládáme je na zásobník  
  `Z: a d c e f`
- Postupným odebíráním dostaneme:

![[019f9f16-a603-7350-a87b-4545cc94d982.png]]

> [!info]
> **Jedině hodnotu proměnné** `b` **musíme uložit do paměti**, hodnoty ostatních proměnných mohou být uloženy v registrech. Že `a` a `e` sdílí jeden registr, je v pořádku — jejich oblasti života se nepřekrývají.


> [!danger]
> Přidělování registrů také komplikuje skutečnost, že v instrukčních souborech procesorů  
> některé **registry mají specifické použití**. Například v instrukčním souboru x86 se pro  
> násobení a dělení používá dvojice registrů `DX:AX`.

---

# 3.Volba formátu instrukcí

> [!success]
> Po přidělení registrů následuje **volba formátu instrukcí**. Překladač _rozhoduje, zda budou operandy instrukce_ uloženy **v registrech**, nebo **v paměti**.
>
> U procesorů **RISC** je situace jednoduchá, protože _aritmetické a logické instrukce_ mohou pracovat **pouze s registry**. (jen RR)  
> U procesorů **CISC** je možností více, protože _operandy mohou být jak v registrech, tak v paměti_.

## 3.1 Formáty instrukcí

- **RR (Register–Register)** – oba operandy jsou v registrech.
- **RM (Register–Memory)** – první operand je v registru, druhý v paměti.
- **MR (Memory–Register)** – první operand je v paměti, druhý v registru.

Formát **MM (Memory–Memory)** se běžně **nepoužívá**, protože by vyžadoval dva přístupy do paměti pro načtení operandů a další pro uložení výsledku, což by _bylo příliš pomalé a složité_.

## 3.2 RISC vs. CISC

|     | RISC | CISC |
| --- | --- | --- |
| Operandy aritm./log. instrukcí | jen v **registrech** | v registrech i v **paměti** |
| Dostupné formáty | jen **RR** | **RR, RM, MR** |
| Přístup do paměti | jen `load` / `store` (load-store architektura) | libovolná instrukce |
| Volba instrukce překladačem | jednodušší (málo variant) | složitější (volí se i formát) |
| Nároky na registry | **vyšší** (vše musí projít registrem) | nižší |

---

# 4. Okénková (peephole) optimalizace

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