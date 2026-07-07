# 1. Úvod

- **Metodika vývoje software** určuje, jakým způsobem bude _probíhat celý proces vývoje_ od získání požadavků až po nasazení a údržbu systému.
- Každý software prochází základními aktivitami:
  1. **Specifikace** – definice požadavků
  2. **Vývoj** – návrh a implementace
  3. **Validace** – testování a ověření správnosti
  4. **Evoluce** – údržba a rozvoj systému

> [!danger]
> _Neexistuje univerzálně nejlepší metodika_. Výběr závisí na velikosti projektu, stabilitě požadavků, velikosti týmu, rizicích a zákazníkovi.

---

# 2. Model vodopád (Waterfall)

- Patří mezi **tradiční sekvenční modely**
- Jednotlivé fáze následují za sebou, další fáze začíná až po dokončení předchozí (fáze jsou formálně uzavírány — vzniká dokumentace)

## 2.1 Fáze vodopádu (typické pořadí)

1. **Specifikace požadavků** — proces zjištění a definování, jak má SW fungovat
2. **Návrh systému** — architektura, datový model, rozhraní modulů
3. **Implementace** — programování jednotlivých modulů
4. **Testování** — ověření, zda systém odpovídá specifikaci
5. **Nasazení** — předání zákazníkovi, instalace
6. **Údržba** — opravy chyb, drobné úpravy

![](/api/files/019eee7b-cf24-7149-819d-84f11bfc7405/obrazek.png)

## 2.2 Výhody vodopádu

- Jednoduchý, snadno pochopitelný i pro zákazníka (přehledný postup)
- Kvalitně dokumentovaný — každá fáze má jasné výstupy
- Snadno plánovatelný z pohledu zdrojů a harmonogramu (snadné sledování postupu)
- Vhodný pro **stabilní, dobře definované požadavky** (např. vojenské systémy, státní zakázky)

## 2.3 Nevýhody vodopádu

- **Nepružný** — špatně reaguje na změny požadavků (změna požadavků uprostřed projektu je velmi drahá)
- Zákazník vidí výsledek **až na konci** — velké riziko, že nedostane co očekával
- Testování přichází **pozdě** — chyby v analýze se odhalí až při testování, kdy je oprava nejdražší
- Předpokládá, že **požadavky jsou od začátku úplné a stabilní** — v praxi to tak téměř nikdy není

## 2.4 Kdy použít vodopád

- Požadavky jsou jasné a nezmění se (regulované prostředí)
- Tým je geograficky rozptýlený a potřebuje formální dokumentaci
- Projekt je menší nebo s dobře zmapovanou doménou

---

# 3. Iterativní modely

- Základ většiny agilních metod (snažily se zmírnit nedostatky vodopádu)
- Časté iterace celého SW procesu
- Konečná specifikace je hotová, až je hotova poslední iterace

- Několik druhů iterativního vývoje:
  - **Inkrementální vývoj**
    - Systém se dodává po částech = inkrementech
    - Zákazník vidí výsledky průběžně
    - Funkcionality jsou přidávány podle důležitosti (kritické části jsou dlouho testovány)
  - **Spirálový model**
    - Iterace ve spirále (každá otočka je 1 fáze SW procesu)
    - Spirála rozdělena na sektory:
      1. Určení záměrů dané fáze
      2. Vyhodnocení a snížení rizik
      3. Vývoj a validace
      4. Plánování
    - Jedna z mála metod, která explicitně řeší rizika

---

# 4. Agilní metody

- Agilní vývoj vznikl jako reakce na problémy vodopádového modelu.
- Ve vodopádu se předpokládá, že požadavky známe dopředu. V praxi ale zákazník často:
  - neví přesně, co chce,
  - požadavky mění,
  - objeví nové potřeby až při používání systému.

## 4.1 Hlavní principy

1. **Lidi a komunikace**
  - Úspěch projektu závisí hlavně na tom, jak dobře spolu lidé komunikují a spolupracují
2. **Funční software**
  - Nejdůležitější je dodávat fungující produkt
  - Dokumentace je důležitá, ale neměla by brzdit vývoj.
3. **Spolupráce se zákazníkem**
  - Zákazník není jen na začátku a na konci projektu.
  - Je součástí vývoje.
  - Průběžně kontroluje výsledky a poskytuje zpětnou vazbu.
4. **Reakce na změny**
  - Změna požadavků není problém.
  - Je přirozenou součástí vývoje.

## 4.2 Charakteristické znaky

- **Iterace**
  - Vývoj je rozdělen do krátkých cyklů.
  - Například 2 týdny.
- **Inkrementy**
  - Každá iterace přidává novou funkcionalitu.
- **Průběžné testování**
  - Testuje se neustále.
  - Nečeká se až na konec projektu.
- **Refactoring**
  - Průběžné zlepšování struktury kódu bez změny funkcionality.

## 4.3 Scrum

- **Scrum** je iterativní a inkrementální **způsob řízení vývoje softwaru** obvykle řazený mezi _agilní metodiky_

### Role

- **Product owner**
  - Zastupuje zákazníka
  - Určuje priority
  - Spravuje Product Backlog (= seznam všech požadavků na systém)
- **Scrum Master**
  - Je odpovědný za odstranění překážek týmu na dodání produktových cílů
- **Vývojový tým**
  - Je odpovědný za dodání potenciálně použitelných inkrementů

### Události

- Sprint planning
  - Plánování sprintu.
  - Tým si vybírá úkoly z _Product backlog_.
  - _Sprint Backlog_ = výběr úkolů pro aktuální sprint
- **Sprint**
  - Krátké období vývoje (jedna iterace)
  - Typicky 1–4 týdny
  - Na konci vzniká funkční inkrement produktu
- **Stand-up (Daily Scrum)**
  - Krátká denní schůzka (max. 15 minut)
  - Slouží ke koordinaci týmu
  - Typické otázky:
    1. Co jsem udělal od poslední schůzky?
    2. Co budu dělat dnes?
    3. Co mi brání v práci?
- **Sprint Review**
  - Prezentace výsledků zákazníkovi.
  - Získání zpětné vazby
- **Sprint Retrospective**
  - Hodnocení práce týmu.
  - Otázky:
    - Co fungovalo?
    - Co nefungovalo?
    - Co zlepšit?

![](/api/files/019eef2c-205b-72de-981b-cf3f46252f22/obrazek.png)

## 4.4 Kanban

- Druhá velmi známá agilní metoda
- Nejčastěji znázorňován jako tabule, která má několik sloupců (To Do → In Progress → Testing → Done). Úkoly se posouvají mezi sloupci.
- Je možné ho použít v jakémkoliv oboru, případně i denním životě
- Je horší na dlouhodobé plánování.
- Je méně strukturovaný než Scrum.

![](/api/files/019eef37-80fc-7528-b98b-f5f321044e16/obrazek.png)

## 4.5 Extrémní programování

- _Aplikování praktik agilního vývoje_ na **extrémní** úrovni (inkrementální dodávky, refactoring, …)
- Často používané techniky:
  - **Párové programování**
    - Jeden programuje. Druhý kontroluje. Role se střídají.
  - **Test-driven development**
    - Pro novou funkcionalitu se nejdříve napíšou testy a až poté se začne programovat funkcionalita
  - **Zrychlené dodávky**
    - Nové verze několikrát denně
- Vhodné pro menší týmy s vysokými nároky na kvalitu kódu

---

# 5. Srovnání: vodopád vs. agilní přístup

| Kritérium | Vodopád | Agilní |
| --- | --- | --- |
| Požadavky | Fixní na začátku | Mohou se měnit |
| Zákazník | Na začátku a konci | Průběžně zapojen |
| Dodávka | Jednorázová, na konci | Časté přírůstky |
| Dokumentace | Rozsáhlá, formální | Přiměřená, lehčí |
| Testování | Až po implementaci | Průběžně |
| Vhodnost | Stabilní domény | Dynamické prostředí |
| Riziko | Pozdní odhalení chyb | Brzy, ale i průběžně |