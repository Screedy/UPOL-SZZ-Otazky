# 1. Úvod

- _Zjednodušeně řečeno:_ **Požadavky na software** popisují, _co má systém dělat_ a _jaké vlastnosti má mít_.
- Jsou **základem celého vývoje** - špatně definované požadavky vedou k problémům v návrhu, implementaci i testování.
- V celém vývoji software _určování požadavků_ je _součástí_ **specifikace software**, která má několik základních fází:
  1. **Studie proveditelnosti**
    - Jsou zákazníkovi potřeby _uskutečnitelné s HW a SW možnostmi_?
    - Je možné SW _vyvinout s daným rozpočtem_?
  2. **Zjišťování a analýza požadavků**
    - _Diskuze_ s (budoucími) uživateli, vedoucími, manažery
    - Pozorování existujících systémů
  3. **Specifikace požadavků** (sumarizace předchozích fází)
    - Výstupem je _dokument s definovanými požadavky_ (uživatelské a systémové)
  4. **Validace požadavků** (kontrola předchozích fází)
    - Jsou _požadavky realizovatelné_?
    - Je _specifikace kompletní_?
    - Zjištěné chyby je _potřeba opravit_

## 1.1 Rozdělení požadavků

### 1.1.1 Podle obsahu

**Funkční požadavky**

- Popisují _služby a funkce_, které má systém poskytovat.
- Odpovídají na otázku **„Co má systém dělat?“**
- Např. „Uživatel bude moci rezervovat knihu.“

**Nefunkční požadavky**

- Popisují _vlastnosti systému jako celku_.
- Odpovídají na otázku **„Jak dobře to má systém dělat?“**
- Např. výkon, bezpečnost, spolehlivost nebo dostupnost.

### 1.1.2 Podle úrovně abstrakce

**Podnikatelské požadavky**

- To jsou **cíle organizace**, tedy proč se systém vůbec vytváří. Jsou to požadavky z pohledu managementu — nevystihují detaily chování systému, ale stanovují kontext a cíl.
- Např. Knihovna chce umožnit online správu výpůjček.

**Uživatelské požadavky**

- Funční a nefunkční požadavky **popisují potřeby uživatelů**.
- Např. Uživatel bude moci rezervovat knihu.

**Systémové požadavky**

- Jsou **detailním rozpracováním** uživatelských požadavků
- Např. Systém umožní prodloužit výpůjčku o 30 dní, pokud není kniha rezervována jiným uživatelem.

# 2. Uživatelské požadavky

> [!success]
> **Uživatelské požadavky** _popisují funkční a nefunkční požadavky_ **v přirozeném jazyce**. Tedy jazykem srozumitelným pro zákazníka, koncové uživatele, manažery (bez odborných slov, …). Často jsou **doplněny diagramy**.

- Popisují pouze _externí chování systému s co nejméně návrhových specifik_ (Uživatele nemusí zajímat v jakém jazyce je systém implementován. Nepotřebuje vědět, na kolika pevných discích v RAID poli je databáze uložena.)

> [!info]
> _Příklad_ funkčního uživatelského požadavku:
>
> - Uživatel bude moci vyhledávat knihy podle autora.
>
> _Příklad_ nefunkčního požadavku:
>
> - Systém by měl být snadno ovladatelný.

- Nejčastěji používaným diagramem pro tyto požadavky je “**Diagram případu užití**” (Use case diagram)

## 2.1 Typické problémy uživatelských požadavků

- **Nízká srozumitelnost** (nejednoznačnost)
  - Bývá složité _jednoduše a jednoznačně_ popsat požadavky, aniž bychom psali dlouhé a náročné věty
- **Míchání typů požadavků**
  - Jasně by měly být _rozlišeny_ funkční a nefunkční požadavky
- **Slučování více požadavků**
  - Jednotlivé požadavky by měly být jasně odděleny

## 2.2 Doporučení při zápisu

- Standardní formát:
  - Jednoznačný _popis_
  - _Zdůvodnění_ (proč je potřeba)
  - _Zdroj_ požadavku (s kým diskutovat změny)
- Konzistentní používání jazyka (rozlišovat povinné a volitelné funkcionality)
  - _Povinné_ — slova ty “musí poskytovat”, “bude poskytovat”
  - _Nepovinné_ — “měl by poskytovat!”

# 3. Systémové požadavky

> [!success]
> **Systémové požadavky** jsou _detailním rozpracováním uživatelských požadavků_. **Přesně popisují** funkcionalitu a vlastnosti systému tak, aby podle nich bylo možné _software navrhnout, implementovat a otestovat_. Musí být _jednoznačné_, _úplné_, _konzistentní_ a _ověřitelné_. Určené pro _vývojáře, analytiky, architekty, testery_. Jsou doplněny **vhodnými diagramy, tabulkami, vzorečky**.

- Jsou často součástí smluv.
- Opět psány v přirozeném jazyce (ale přesněji).

## 3.1 Vztah k uživatelským požadavkům

**Uživatelský požadavek**:

- Uživatel bude moci vyhledávat knihy.

**Systémový požadavek:**

- Systém umožní vyhledávání knih _podle názvu, autora nebo ISBN_. Uživatel může vyplnit jedno nebo více polí. Po stisknutí tlačítka Vyhledat se provede dotaz do databáze a systém zobrazí všechny knihy odpovídající zadaným kritériím.

## 3.2 Struktura systémového požadavku

1. **Funkce** — _Název požadavku a popis funkcionality_ či specifikované entity
2. **Vstupy** — Popis vstupů a jejich původ
3. **Výstupy** — Popis zamýšlených výstupů a jak budou využity
4. **Závislosti** — Které entity jsou pro funkcionality potřeba
5. **Akce** — Popis samotné provedené akce
6. **Vstupní podmínky** — Které musí být splněny před akcí
7. **Výstupní podmínky** — Které musí být splněny po akci
8. **Vedlejší efekty a jejich popis**

- Taková struktura jasně vymezí úseky, ke kterým by se měl přirozený jazyk vyjadřovat
- Velmi často se používá “**Sekvenční diagramy**”.

> [!info]
> _Příklad_:
>
> **Funkce**: Vyhledávání knih.
>
> **Vstupy**: Název knihy, autor, ISBN. Uživatel může vyplnit dané informace. Musí alespoň jednu informaci.
>
> **Výstupy**: Seznam nalezených knih.
>
> **Závislosti**: Databáze knih.
>
> **Akce**: Po vyplnění alespoň jednoho vstupu a stisknutí tlačítka vyhledat, se provede dotaz na databázi a poté systém zobrazí všechny odpovídající knihy.
>
> **Vstupní podmínka:** Uživatel má přístup do knihovního systému.
>
> **Výstupní podmínka:** Jsou zobrazeny všechny knihy odpovídající zadaným kritériím.
>
> **Vedlejší efekty:** Žádné.

# 4. Parametrické požadavky

- Parametrické požadavky nepopisují konkrétní funkce systému, ale určují **pravidla, vlastnosti, rozhraní a omezení**, která musí systém splňovat.
- Lze je rozdělit do čtyř skupin.

## 4.1 Podnikatelská pravidla (Business Rules)

- Podnikatelská pravidla definují **pravidla fungování organizace** nebo domény, **která musí systém respektovat**.

**Příklady:**

- Výpůjčka knihy může trvat maximálně 30 dní.
- Student může mít současně vypůjčeno nejvýše 10 knih.
- Pokuta za pozdní vrácení činí 5 Kč za každý den prodlení.

---

## 4.2 Kvalitativní parametry

- Kvalitativní parametry určují požadovanou **kvalitu systému**.

**Příklady:**

- Odezva systému bude kratší než 2 sekundy.
- Dostupnost systému bude alespoň 99,9 %.
- Aplikace bude snadno použitelná.
- Systém bude snadno udržovatelný a testovatelný.

---

## 4.3 Vnější rozhraní

- Požadavky **na komunikaci systému s okolím** – s uživateli, hardwarem nebo jinými informačními systémy.

**Příklady:**

- Systém bude komunikovat s platební bránou pomocí REST API.
- Aplikace bude podporovat export dat do PDF.
- Systém bude spolupracovat se čtečkou čárových kódů.
- Webová aplikace bude podporovat nejnovější verze prohlížečů Chrome, Firefox a Edge.

---

## 4.4 Omezení

- Omezení představují podmínky, které **omezují návrh, implementaci nebo provoz systému**. Mohou být _technická, organizační nebo legislativní_.

**Příklady:**

- Systém musí být vyvinut v jazyce Java.
- Databází musí být PostgreSQL.
- Aplikace musí být provozována na Linuxu.
- Systém musí splňovat požadavky GDPR.
- Projekt musí být dokončen do šesti měsíců.

---

# 5. Scénáře a případy užití

## 5.1 Scénáře

- Některou funkcionalitu je snadnější a srozumitelnější demonstrovat na konkrétním scénáři

> [!success]
> **Scénář** _demonstruje jeden konkrétní průchod systémem_ (konkrétní situaci použití). Slouží jako _vhodné doplnění_ (abstraktního) popisu požadavku.

- Scénář by měl obsahovat:
  1. Počáteční podmínky a stavy
  2. Popis normálního průběhu
  3. Chybové situace a jejich řešení
  4. Popis aktivit, které mohou probíhat souběžně
  5. Popis výsledného stavu systému

> [!info]
> _Příklad scénáře — Rezervace knihy_
>
> **Počáteční stav**: Uživatel je přihlášen
>
> **Normální průběh**:
>
> 1. Uživatel vyhledá knihu.
> 2. Vybere požadovanou knihu.
> 3. Klikne na „Rezervovat“.
> 4. Systém ověří dostupnost knihy.
> 5. Systém vytvoří rezervaci.
> 6. Uživatel obdrží potvrzení.
>
> **Chybové situace**:
>
> - Kniha neexistuje v našem systému — zobrazení chybové hlášky.
> - Kniha není dostupná — zobrazení chybové hlášky.
>
> **Konečný stav**: Kniha je rezervována pro daného uživatele.

## 5.2 Případy užití (Use cases)

> [!success]
> **Případ užití** je také _založen na scénářích_, ale je obecnější. Nepopisuje jeden konkrétní průchod krok po kroku, ale **jaké funkce systém poskytuje jednotlivým aktérům**. Využívá _základního diagramu_ z UML

- _Co všechno může uživatel dělat_?

- _Základní prvky_:
  - **Aktér = Subjekt komunikující se systémem**
    - Může to být uživatel, administrátor, externí systém…
    - Ve UML se kreslí jako _panáček_  
      ![](/api/files/019d9aac-b2b9-771f-89fc-016ca195507f/MacBook-2026-04-17-004557@2x.png)
  - **Případ užití = Funkcionalita systému**
    - Například: Přihlášení, vyhledání knihy, rezervace, …
    - Ve UML se kreslí jako _elipsa s názvem_![](/api/files/019d9aac-f8df-731a-b2af-0511f8c919c6/MacBook-2026-04-17-004558@2x.png)
  - **Vazba asociace = Základní vztah mezi aktérem a případem užití**
    - Vyjadřuje, že _aktér_ danou _funkcionalitu používá_.
    - Ve UML se kreslí jako propojení aktéra a případu užití
  - **Vazba «include» = Povinné vložení jiného případu užití**
    - Používá se pro funkcionalitu, která se opakuje na více místech
    - Například: Při rezervaci se vždy musí provést ověření uživatele.![](/api/files/019d9aad-a617-75d8-92ba-92525cee6c47/MacBook-2026-04-17-004560@2x.png)  
      
  - **Vazba «extend» = Volitelné rozšíření případu užití**
    - Používá se pro doplňkové nebo podmíněné chování.
    - Například: Použití slevového kupónu rozšiřuje objednávku. Objednávku lze vytvořit i bez kupónu.![](/api/files/019d9aad-d736-744b-98c6-9135fdf26964/MacBook-2026-04-17-004561@2x.png)
  - **Generalizace aktérů = Umožňuje vytvořit hierarchii aktérů**
    - Potomek dědí všechny vazby svého předka. Každý může mít navíc vlastní specializované funkcionality.
    - Například: Čtenář i knihovník jsou uživatelé systému.
  - **Hranice systému = Obdélník představující modelovaný systém**
    - Uvnitř se nacházejí případy užití.
    - Vně se nacházejí aktéři.
    - Jasně určuje, co je součástí systému a co patří do jeho okolí.![](/api/files/019d9aae-61f2-727e-a0ff-6ca96322c079/MacBook-2026-04-17-004563@2x.png)

> [!info]
> _Příklad — Blog_:
>
> ![](/api/files/019eeb69-1389-716d-8c97-171888c4d724/obrazek.png)

# 6. Kvalitativní parametry z pohledu uživatele a vývojáře

> [!success]
> **Kvalitativní parametry z pohledu uživatele** popisují _vlastnosti, které uživatel přímo vnímá při práci se systémem_, například použitelnost, spolehlivost, výkon, bezpečnost nebo dostupnost. **Z pohledu vývojáře** jsou důležité především _vlastnosti ovlivňující další vývoj a údržbu systému_, jako jsou udržovatelnost, rozšiřitelnost, testovatelnost, přenositelnost a kvalita zdrojového kódu.

## 6.1 Kvalitativní parametry z pohledu uživatele

- Jedná se o vlastnosti, které uživatel přímo vnímá při používání systému.

| Parametr | Co znamená | Příklad |
| --- | --- | --- |
| **Dostupnost** | Jaký podíl času je systém doopravdy použitelný. | Knihovní systém je dostupný 99,9 % času. |
| **Efektivita** | Vztah mezi výkonem systému a využitými prostředky.   Rychlost odezvy, propustnost systému. | Vyhledání knihy trvá maximálně 2 sekundy. |
| **Flexibilita** | Schopnost systému přizpůsobit se změnám. | Přidání nového typu uživatele (např. absolvent) nevyžaduje zásadní změny. |
| **Integrita** | Ochrana správnosti a konzistence dat. | Kniha nemůže být současně půjčena dvěma uživatelům. |
| **Kompatibilita** | Schopnost spolupracovat s jinými systémy nebo prostředími. | Systém komunikuje s univerzitním informačním systémem. |
| **Spolehlivost** | Jak dlouho funguje systém bez selhání. | Metrika MTBF (střední doba mezi poruchami) |
| **Odolnost (robustnost)** | Schopnost zvládat chyby a neočekávané situace. | Uživatel zadá neplatné datum a systém zobrazí chybovou hlášku místo pádu aplikace. |
| **Použitelnost** | Jak snadné je systém používat. | Nový uživatel dokáže rezervovat knihu bez návodu. |
| **Bezpečnost** | Ochrana dat a přístupu. | Cizí uživatel nesmí vidět moje výpůjčky. |

## 6.2 Kvalitativní parametry z pohledu vývojáře

- Popisují vlastnosti ovlivňující vývoj, údržbu a další rozšiřování systému.

| Parametr | Co znamená | Příklad |
| --- | --- | --- |
| **Udržovatelnost** | Jak snadno lze systém opravovat a upravovat. (čitelnost a kvalita kódu) | Změna délky výpůjčky nevyžaduje zásah do desítek souborů. |
| **Přenositelnost** | Přesun do jiného prostředí bez velké úpravy | Cross-platform aplikace |
| **Znovupoužitelnost** | Komponenty použitelné v jiných projektech | Modul autentizace lze použít v další aplikaci. |
| **Testovatelnost** | Jak snadno lze systém testovat. | Jednotlivé moduly lze testovat samostatně. |
| **Rozšiřitelnost** | Jak snadno lze přidávat nové funkce. | Lze jednoduše přidat rezervaci časopisů. |