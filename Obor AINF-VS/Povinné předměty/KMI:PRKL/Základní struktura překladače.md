> [!success]
> **Překladač** _je program_, který převádí **zdrojový program** napsaný _ve zdrojovém jazyce_ na **cílový program** v jiném _cílovém jazyce_, typicky do _strojového kódu nebo mezikódu_.

_Základní pojmy:_

- **Zdrojový jazyk** — jazyk překládaného programu (C, C++, Java, Pascal, …).
- **Zdrojový kód** — konkrétní zápis programu ve zdrojovém jazyce.
- **Cílový jazyk** — jazyk, do kterého se překládá.
- **Cílový kód** — výstup překladače v cílovém jazyce.

![[019caa55-52d8-75bd-9a4f-cf1f3ce14650.png]]

---

# 1. Formy cílového programu

> [!success]
> _Cílový program_ je **výstup překladače** (nemusí však být vždy přímo spustitelný program)  
> Jeho _konkrétní podoba závisí na architektuře_ systému překladu (kompilace, linkování, interpretace, JIT) a _požadavcích_ na přenositelnost, efektivitu a modularitu.

## **1.1 Kompletní program ve strojovém kódu**

- Přímo **spustitelný program ve strojovém jazyce**, který _může procesor okamžitě vykonávat_ (binární instrukce)
- Vhodný _pouze pro krátké programy_ (spíše už minulost)
- Výhody:
  - Není potřeba _žádný další překlad_ ani _spojování modulů_
- Nevýhody:
  - **Obtížná údržba** a **opakované použití kódu**.
  - **Závislost** na _konkrétní paměťové organizac_i.

## **1.2 Objektový modul s relativními adresami**

- Překladač přeloží každý zdrojový soubor do samostatného objektového modulu.
- Ten obsahuje:
  - přeložené _instrukce ve strojovém kódu_,
  - **exportované symboly** – seznam poskytovaných symbolů (např. funkce nedeklarované jako static)
  - **importované symboly** – seznam symbolů použitých v tomto souboru
  - **relokačních informací**, které umožní správně přepočítat adresy při spojování modulů.
- Výstupem je **objektový soubor** (např. `.o`, `.obj`).
- _Interní adresy_ jsou _relativní k začátku modulu_, **externí adresy** se _doplní až při sestavení_ (linkování).
- **Linker** _spojí všechny objektové moduly, vyřeší vzájemné odkazy mezi nimi_ a _vytvoří jeden_ **_spustitelný program_** (binární soubor).

![[019caa70-3df4-772a-a373-e71b352454e2.png]]

## **1.3 Program v jazyce symbolických adres**

- Překladač (místo strojového kódu) **generuje kód v jazyce symbolických adres**.
- Následně je tento _kód přeložen assemblerem_ do **_objektových modulů_**.
- Výhody:
  - **Jednodušší** implementace překladače.
  - _Čitelnost_ výstupu (vhodné pro ladění a analýzu generovaného kódu).
- Nevýhody:
  - **Delší fáze** překladu.
  - V praxi méně _efektivní než přímé generování obj. kódu_.

![[019caa73-504b-76a8-b3a7-a09da4dd2c6c.png]]

## **1.4 Program v jiném programovacím jazyce**

- Zdrojový jazyk je _přeložen do jiného vysokoúrovňového jazyka_.

> [!info]
> Typicky např. Pascal → C, COBOL → C++.

- Motivace:
  - Znovupoužití existujících optimalizovaných překladačů.
  - Migrace starých jazyků na moderní platformy.
  - Zjednodušení portování.

## **1.5 Specifické interní reprezentace**

- Moderní přístup založený na **virtuálním stroji**.
- Překladač vytvoří _platformně nezávislou reprezentaci programu_
- **Bytecode (Java)**
  - Spouští se nad **JVM** (Java Virtual Machine).
  - Obsahuje instrukce nezávislé na konkrétní architektuře.
- **CIL (Common Intermediate Language)**
  - Používán v .NET ekosystému.
  - Spouštěn pomocí **CLR** (.NET runtime).
- **Princip běhu**
  - Překlad do mezikódu (Bytecode/CLI)
  - Za běhu probíhá JIT kompilace:
    - _Převod mezikódu na nativní strojový kód_.
    - Optimalizace podle konkrétní platformy.
- **Výhody**
  - Vysoká _přenositelnos_t
  - Bezpečnostní mechanismy (verifikace kódu)
  - Možnost runtime optimalizací (např. často používané metody může vložit inline)
- **Nevýhody**
  - _Nutnost běhového prostředí_ (bez toho nelze spustit)
  - Počáteční režim při JIT kompilaci (start programu bývá o něco pomalejší)

---

# 2. Fáze překladu

- Překlad programu se dělí na n_ěkolik logicky oddělených fází_. Každá fáze přijímá **výstup předchozí fáze** a **produkuje vstup pro následující**.

## 2.1 Front-end (analýza)

- Front-end představuje první část překladače.
- Je **závislý na zdrojovém programovacím jazyce**, protože musí rozumět jeho syntaxi i sémantice.
- Front-end _se skládá ze tří částí_:
  - lexikální analýza,
  - syntaktická analýza,
  - sémantická analýza.

### 2.1.1 Lexikální analýza (Lexer / Scanner)

- Jejím úkolem je přečíst zdrojový program jako posloupnost znaků a rozdělit jej na **lexikální symboly (tokeny)** (kategorie + hodnota)**.** Ty představují _nejmenší významové jednotky programovacího jazyka_.

> [!info]
> např. `<ID, "x">`, `<NUM, 42>`, `<KEYWORD, "while">`

- Lexikální analyzátor rozpoznává například:
  - klíčová slova (`if`, `while`, `return`),
  - identifikátory (názvy proměnných a funkcí),
  - konstanty,
  - operátory,
  - oddělovače a omezovače (čárky, závorky, středníky).
- Současně **odstraňuje části** zdrojového programu, které **nejsou pro překlad důležité** → vynechává bílé znaky (mezery, tabulátory, konce řádků) a komentáře.
- **Výstupem** je **1. interní forma** — posloupnost symbolů (tokenů).

> [!warning]
> Lexikální analyzátor také _odhaluje první chyby ve zdrojovém programu_, například špatně zapsaná čísla nebo neplatné znaky.

> [!note]
> U jazyků C/C++ _zpracování direktiv preprocesoru_ předchází lexikální analýze (provádí preprocesor).

### 2.1.2 Syntaktická analýza (Parser)

- Místo jednotlivých znaků již pracuje s tokeny a ověřuje, zda tvoří **syntakticky správný program podle gramatiky programovacího jazyka**.
- Rozpoznává vyšší konstrukce programu, například:
  - deklarace,
  - výrazy,
  - příkazy,
  - bloky programu,
  - definice funkcí.
- Pro popis syntaxe programovacích jazyků se používají **bezkontextové gramatiky** (regulární gramatiky nestačí například pro popis vnořených závorek)
- Výstupem je **derivační strom** (parse tree)
- Metody: _shora-dolů_ nebo _zdola-nahoru_.

### 2.1.2 Sémantická analýza

- Sémantická analýza kontroluje, zda má program **správný význam**. Program může být syntakticky správný, ale přesto obsahovat sémantické chyby.
- _Ověřuje například_:
  - zda jsou **všechny proměnné deklarovány**,
  - zda _nejsou proměnné použity před deklarací_,
  - zda **souhlasí datové typy** při přiřazování nebo ve výrazech,
  - zda jsou **správně volány funkce** (počet a typ parametrů),
  - zda jsou dodržena další pravidla daného programovacího jazyka.
- K popisu sémantiky se používají **atributové gramatiky**, které rozšiřují bezkontextovou gramatiku o **atributy** a **sémantická pravidla**.
- Generuje **2. interní formu** (např. anotovaný AST, trojadresný kód ve formě čtveřic).

## 2.2 Optimalizace

- Optimalizace je fáze překladu, jejímž cílem je **zlepšit vlastnosti programu**, _aniž by se změnila jeho funkčnost_. Překladač tedy upravuje interní reprezentaci programu tak, aby _výsledný program běžel rychleji, zabíral méně paměti nebo měl menší velikost_.
- Základní dělení:
  1. _Platformě nezávislé optimalizace_ — nad **interní reprezentací programu**
    - Odstranění mrtvého kódu (nikdy se nevykoná, nebo nepoužije)
    - Konstantní propagace (nahrazení proměnných známými konstantami)
    - Dostupné výrazy (opakovaně vypočítaný výraz se spočítá pouze jednou a výsledek se znovu využije)
    - Živost proměnných (zjišťuje, které proměnné budou ještě použity)
  2. _Platformě závislé optimalizace_ — až při **generování strojového kódu**
    - **Volba instrukcí**
    - **Přidělování registrů**
  3. _Okénková optimalizace_ — **až po vygenerování cílového kódu**
    - Překladač prochází _krátké úseky instrukc_í ("okénka") a _nahrazuje je efektivnějšími nebo odstraňuje zbytečné instrukce_.

## 2.3 Back-end (Generování cílového kódu)

- Jeho úkolem je _převést optimalizovanou interní reprezentaci_ programu na **cílový kód**.
- Back-end je **závislý na cílové platformě** (musí generovat instrukce konkrétní architektury procesoru)
- Zahrnuje:
  - **Statické stanovení pořadí instrukcí**
  - **Přidělování registrů**
  - **Volba formátu instrukcí**

> [!warning]
> Pokud _překladač vytváří mezikód_ (například Java Bytecode nebo .NET CIL), je v_ýsledkem právě tato platformně nezávislá reprezentace_. V opačném případě je výsledkem _strojový kód nebo objektový modul_.

- Po generování kódu může následovat ještě _strojově závislá okénková optimalizace_.

## 2.4 Výpis chyb (volitelná fáze)

- U **dávkového (neinteraktivního) překladu** může překladač po skončení překladu vypsat zdrojový program společně se seznamem nalezených chyb.
- V dnešních _integrovaných vývojových prostředích_ (IDE) se tato činnost většinou neprovádí samostatně, protože _editor zobrazuje chyby přímo ve zdrojovém kódu_.

---

# 3. Interní formy programu

- Překladač během práce používá dvě základní interní formy:

## 3.1 1. interní forma — posloupnost symbolů

- Výstup lexikální analýzy.
- Zdrojový kód převedený na posloupnost tokenů, zbavený bílých znaků a komentářů.
- Slouží jako vstup pro syntaktický analyzátor.

## 3.2. 2 interní forma — strukturální reprezentace

- Výstup sémantické analýzy.
- _Nejběžnější podoby_:
  - **AST (abstraktní syntaktický strom)** — stromová reprezentace programu bez redundantních uzlů.
  - **Lineární forma — čtveřice (quadruples):** $(op, arg_1, arg_2, result)$
  - **Lineární forma — trojice (triples):** $(op, arg_1, arg_2)$ (výsledek je identifikován pozicí instrukce)

---

# 4. Průchody (passes)

- **Průchod (pass)** = jedno čtení celého vstupu (zdrojového kódu nebo mezikódu).
- **Jednoprůchodový překladač** — provede vše v jednom čtení. Jednodušší, ale omezenější (např. nemůže optimalizovat přes celý program).
- **Víceprůchodový překladač** — Provede více čtení. umožňuje sofistikovanější analýzy a optimalizace.
- Typicky má překlad **tři hlavní průchody (fáze):**
  1. **Front-end** — analýza zdrojového programu → 2. interní forma.
  2. **Optimalizace** — transformace IR.
  3. **Back-end** — generování cílového kódu.
- U dávkového (neinteraktivního) překladu bývá ještě 4. fáze — výpis zdrojového kódu s oznámením nalezených chyb.

---

# 5. Tabulky symbolů

> [!success]
> **Tabulka symbolů** je datová struktura, ve které překladač _uchovává informace o identifikátorech použitých ve zdrojovém programu_.
>
> Vytváří se především během lexikální a sémantické analýzy a využívá se při kontrole správnosti programu i při generování kódu.

> [!note]
> Překladač převádí _imperativní části programu do interní reprezentace_, zatímco _informace z deklarací ukládá do tabulky symbolů_.

- Obsahuje zejména:
  - Jména a datové typy proměnných.
  - U polí: počet dimenzí a jejich rozsahy.
  - U strukturovaných typů (`struct`, `union`, `class`): deklarace členů.
  - U funkcí: hlavičky (parametry, návratový typ).
  - Odvozené typy (`typedef`).

---

# 6. Správa chyb (Error Handling)

- Chyby mohou být odhaleny ve **všech fázích** analýzy — lexikální, syntaktické i sémantické.
- Při nalezení chyby by měl překladač:
  1. **Lokalizovat chybu** — Uvést číslo řádku a sloupce, případně zvýraznit v IDE.
  2. **Popsat druh chyby** — Konzervativně. Lépe obecný popis než chybná diagnóza.
  3. **Zotavit se z chyby** — Pokračovat v analýze, aby bylo možné najít i další chyby.
- Zotavení z chyby je nejobtížnější u syntaktické analýzy. Metody:
  - **Panický mód** — vynechá zdrojový kód až po nejbližší význačný symbol (`;`, `}`, …). Jednoduché, ale může přeskočit velkou část kódu.
  - **Oprava zdrojového programu** — vynechání, vložení nebo nahrazení symbolů. Obtížné na implementaci; špatná oprava může vyvolat další chyby.

---

# 7. Překladač vs. interpret

|     | Překladač (compiler) | Interpret (interpreter) |
| --- | --- | --- |
| **Princip** | Zdrojový kód → cílový kód (strojový) → spuštění | Zdrojový kód → interní forma → přímá interpretace (výpočet) |
| **Výstup** | Spustitelný program | Výsledky výpočtu (žádný cílový kód) |
| **Rychlost běhu** | Rychlý | Pomalejší |
| **Složitost** | Složitější konstrukce | Jednodušší konstrukce |

**Hybridní přístup (Java, C#):** Program se přeloží do mezikódu (bytecode / CIL), který se před spuštěním přeloží JIT překladačem do strojového kódu. Kombinuje přenositelnost s výkonem.

---

# 8. Speciální typy překladačů

- **Křížový překladač (cross-compiler)** — generuje **cílový kód pro jinou platformu**, než _na které překlad běží_. Typické použití: vývoj _pro vestavěné systémy_ (embedded), kdy program napíšeme a zkompilujeme na výkonném PC a přeneseme do cílového zařízení.
- **Preprocesor** — _zpracovává direktivy před vlastním překladem_ (C/C++: `#include`, `#define`, `#ifdef`, …). Modifikuje zdrojový kód, který teprve vstupuje do lexikálního analyzátoru.
- **Assembler** — překládá _jazyk symbolických adres do strojového kódu._ Vztah 1:1 mezi instrukcí v assembleru a strojovou instrukcí.
- **Linker (sestavovací program)** — spojuje _moduly s relativními adresami do výsledného spustitelného programu_; doplňuje externí adresy.