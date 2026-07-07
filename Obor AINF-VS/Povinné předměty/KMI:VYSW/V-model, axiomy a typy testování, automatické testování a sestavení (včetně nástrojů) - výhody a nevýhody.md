# 1. V-model

> [!success]
> **V-model** je _vývojový model_ vycházející z **vodopádového modelu**, který zdůrazňuje _propojení jednotlivých fází vývoje s odpovídajícími fázemi testování_.
>
> **Každá fáze návrhu má svůj odpovídající test**.

![](/api/files/019f0e32-c040-74ff-83b0-e67793b0d647/obrazek.png)

> [!warning]
> Graficky má tvar písmene **V**
>
> - Levá strana = **verifikace**
>   - _Děláme produkt správně?_
>   - Kontrolujeme dokumentaci, návrhy a implementaci, zda byly vytvořeny správně podle požadavků.
> - Pravá strana = **validace**
>   - _Děláme správný produkt?_
>   - Testujeme hotový software, zda skutečně řeší potřeby zákazníka a splňuje jeho požadavky.

## 1.1 Levá strana — Verifikace

- Probíhá ještě před samotným programováním.

### 1.1.1 Analýza požadavků

- Definují se požadavky zákazníka
- Vzniká dokumentace požadavků
- Připravují se akceptační testy

> [!info]
> **Požadavek:** „Registrovaný uživatel může vytvořit objednávku.“
>
> **Akceptační test:** Přihlásím se jako registrovaný uživatel, vložím produkt do košíku, dokončím objednávku a ověřím, že se zobrazí potvrzení a objednávka je uložena v systému.

### 1.1.2 Specifikace systému

- Podrobně popisuje, jak má systém fungovat z funkčního hlediska
  - Návrh funkcionality
  - Datový slovník (Popisuje všechna data používaná v systému. U každé položky definuje její název, datový typ, význam a případná omezení)
- Příprava systémových (funkčních) testů

> [!info]
> **Funkcionalita:** „Uživatel může přidat produkt do nákupního košíku.“
>
> **Systémový test:** Přihlásím se do aplikace, otevřu stránku produktu, kliknu na tlačítko **Přidat do košíku** a ověřím, že se produkt zobrazí v košíku se správným množstvím i cenou.

### 1.1.3 Architektura systému

- Definuje se strukturu podsystémů a jejich komunikace
  - Návrh HW a SW architektury
  - Návrh komunikace modulů
- Příprava integračních testů

> [!info]
> Ověřím, že po dokončení objednávky modul **Objednávky** správně komunikuje s modulem **Sklad** a sníží počet kusů na skladě.

### 1.1.4 Návrh modulů

- Detailní návrh jednotlivých částí
- Pseudokód
- Příprava unit testů

> [!info]
> Otestuji metodu `calculateTotalPrice()`. Pro položky za 500 Kč a 300 Kč musí metoda vrátit celkovou cenu 800 Kč.

## 1.2 Pravá strana — Validace

- Ověřuje se již vytvořený software.

### 1.2.1 Unit testy **(testování jednotek)**

- Test _jednotlivých funkcí / metod_ **izolovaně**
- Většinou provádí sami programátoři → _white-box testování_
- Zkouší se všechny možné vstupy (platné **i neplatné**)

### 1.2.2 Integrační testy

- Spojí se jednotlivé moduly a testuje se, zda spolu **správně komunikují** (správné formáty dat, API volání…)
- Většinou _black-box testování_ — zajímá nás komunikace mezi moduly, ne jak fungují uvnitř.

### 1.2.3 Systémové testy

- Funkční testování celého systému podle specifikace (chová se systém přesně tak, jak bylo dokumentováno)

### 1.2.4 Akceptační testy

- Provádí **zákazník**, nikoli vývojový tým
- Ověřuje, že systém splňuje jeho požadavky

## 1.3 Výhody

- Jednoduchý a přehledný
- Testování se plánuje již od začátku projektu
- Dobrá dokumentace
- Vhodný pro projekty s pevnými požadavky

## 1.4 Nevýhody

- Malá flexibilita (špatně reaguje na změny požadavků)
- Pozdní vznik funkčního produktu
- Vyšší administrativní náročnost

---

# 2. Axiomy testování

> [!success]
> **Axiomy** představují _obecně uznávané zásady testování softwaru_.

1. **Software nelze otestovat úplně**
  - Nelze vyzkoušet _všechny možné vstupy a situace_.
  - **Příklad**: Kalkulačka přijímá miliardy různých čísel.
2. **Testování je vždy rizikové**
  - Testují se _především nejdůležitější části systému_ (nemáme dost času ani prostředků otestovat úplně všechno, proto se nejvíce testují funkce, u kterých by případná chyba způsobila největší škody)
  - **Příklad:** Bankovní převod má vyšší prioritu než změna barvy tlačítka.
3. **Testování neprokáže nepřítomnost chyb**
  - Úspěšné testy _říkají jen „testy prošly"_, ne „software je bezchybný".
4. **Shlukování chyb (Defect clustering)**
  - Pokud někde nacházíme _hodně chyb, pravděpodobně jich tam bude ještě více._
5. **Paradox pesticidů**
  - _Stejné testy_ časem _přestanou nacházet nové chyby_.
  - Řešení:
    - pravidelně vytvářet nové testy
    - upravovat testovací scénáře
6. **Ne všechny chyby se opravují**
  - Některé jsou _příliš drahé nebo málo významné_.
  - **Příklad**: Kosmetická chyba v písmu zápatí je lepší ignorovat (stojí méně) než opravit.
7. **Někdy je těžké chybu reprodukovat**
  - Vznikají jen _za specifických podmínek_.
  - **Latentní chyby**: Závisí na specifickém stavu systému, pořadí operací, časování (race conditions).
8. **Specifikace není nikdy konečná**
  - _Požadavky se během vývoje mění_ (testy musí být průběžně aktualizovány)
9. **Tester není příliš oblíbený**
  - Tester _upozorňuje na problémy_, které vývojáři musí opravovat. To _vytváří sociální napětí v týmu_.
10. **Softwarový tester je důležitá a samostatná technická profese**
  - Vyžaduje znalosti _testovacích metod, analytické myšlení a systematičnost_.

---

# 3. Typy testování

> [!danger]
> Základní typy testování jsou uvedeny v 1.2 Pravá strana — Validace

## 3.1 Podle znalosti vnitřní struktury

- **White box testování**
  - Tester **zná kód a vnitřní logiku**.
  - Může navrhovat _testy pro konkrétní větve podmínek, smyčky_ atd. Používá se při unit testování.
- **Black box testování**
  - Tester **nezná vnitřní strukturu**.
  - Testuje se _chování systému na základě vstupů a výstupů_. Používá se při integračních a akceptačních testech.

## 3.2 Speciální typy testů

- **Regresní testování**
  - Po změně systému se ověřuje, že se _nerozbila starší funkcionalita_.
- **Repeat test**
  - **Opakované** _spuštění téže operace_.
  - Odhalí úniky paměti nebo degradaci výkonu v čase.
- **Stress test**
  - Provoz systému **s minimálními zdroji** (málo RAM, pomalý disk).
  - Zjistíme, jak se _systém chová pod tlakem_.
- **Load test**
  - Systém je **zatížen maximálním** _množstvím dat_ nebo _uživatelů_
  - Cílem je _najít bod selhání_.
    - Nástroj: **HP LoadRunner**.
- **Testování konfigurací**
  - Systém se testuje **na různých HW/SW konfiguracích** (různé prohlížeče, OS, rozlišení obrazovky).
- **Testování jazykových verzí (Localization testing)**
  - Správné _používání Unicode_.
  - Testování _lokálních nastavení_ (desetinná čárka vs. tečka, formát data).
  - Testování _překladu_ — správnost i délka textů (přeložený text může být delší a „vypadnout" z UI).
  - _Pravopis_

---

# 4. Automatické testování

- Automatické testování znamená, že _testy provádí program bez zásahu člověka_. Typicky se spouští **při každé změně zdrojového kódu**.

### 4.1 Výhody

- **Rychlost** — automatický test proběhne mnohonásobně rychleji než ruční.
- **Efektivita** — lze spouštět tisíce testů bez lidské práce.
- **Přesnost** — žádné chyby z nepozornosti, test provede přesně to, co je naprogramováno.
- **Redukce lidských zdrojů** — méně potřeba manuálních testerů pro opakované testy.
- **Simulace hardwaru a prostředí** — lze emulovat různé HW konfigurace nebo síťové podmínky bez fyzického vybavení.
- **Vhodné pro regresní testy**

### 4.2 Nevýhody

- **Paradox pesticidů** — stejné skripty spouštěné stále dokola přestávají nacházet nové chyby. Nutná pravidelná aktualizace testů.
- **Změna specifikace = nutná změna testů**
- **Příprava skriptů je časově náročná** — počáteční investice do psaní testů může být vysoká
- **Nelze automatizovat vše** — některé chyby stejně musí ověřit člověk (UX, estetika, použitelnost)

## 4.3 Nástroje pro automatické testování

- **Jednotkové testování** — Slouží k testování jednotlivých funkcí, metod nebo tříd izolovaně od zbytku systému.
  - _Příklady_:
    - **JUnit** – jednotkové testy v Javě.
    - **NUnit** – jednotkové testy v .NET/C#.
    - **pytest** – jednotkové testy v Pythonu.
    - **Vitest / Jest** – jednotkové testy v JavaScriptu a TypeScriptu.
- **Automatizace testování webových aplikací** — Simulují práci skutečného uživatele (klikání na tlačítka, vyplňování formulářů nebo navigaci mezi stránkami)
  - _Příklady_:
    - **Selenium** – univerzální nástroj podporující mnoho jazyků i prohlížečů.
    - **Cypress** – moderní framework zaměřený na testování webových aplikací.
    - **Playwright** – rychlé end-to-end testování více prohlížečů od Microsoftu.
- **Výkonnostní a zátěžové testování** — Ověřují, jak se systém chová při větším počtu uživatelů nebo vysokém zatížení.
  - _Příklady_**:**
    - **Apache JMeter** – simulace stovek až tisíců uživatelů.
    - **HP LoadRunner** – profesionální nástroj pro výkonnostní testy.
- **Síťové monitorovací nástroje** **(Sniffer)** — Zachytávají síťovou komunikaci mezi aplikacemi a umožňují kontrolovat přenášená data.
  - _Příklady_**:**
    - **Wireshark**
    - **Fiddler**
    - **Charles Proxy**
- **Stubs** **(zástupné komponenty)** — Nahrazují části systému, které ještě nejsou hotové nebo nejsou dostupné.
- **Monkey testing (náhodné testování)** — Nástroj provádí náhodné akce nebo generuje náhodná data a sleduje, zda aplikace nespadne.
  - _Rozlišujeme_:
    - **hloupá opice** — kliká zcela náhodně,
    - **částečně inteligentní opice** — zapisuje provedené kroky,
    - **inteligentní opice** — rozpozná ovládací prvky aplikace a vybírá smysluplné akce.
- **Šumový generátor** **(Noise generator)** — Posílá systému neplatná nebo poškozená data a ověřuje jeho odolnost.

---

# 5. Automatické sestavení (Build Automation)

- Automatické sestavení znamená, že po změně zdrojového kódu se automaticky:
  - stáhnou závislosti,
  - projekt zkompiluje,
  - spustí testy,
  - vytvoří artefakt (např. JAR, EXE, Docker image).

## 5.1 Continuous Integration (CI)

- CI znamená _průběžnou integraci změn_ do společného repozitáře.
- Po každém commitu se typicky:
  - **sestaví** aplikace,
  - spustí **unit testy**,
  - případně **integrační testy**,
  - změří **pokrytí kódu**,
  - _vývojář dostane informaci_ o výsledku.

## 5.2 Continuous Delivery (CD)

- Automatické _doručení SW koncovým uživatelům_.
- Zahrnuje správu konfigurací, přístupových údajů
- **Delivery** je **pouze doručení** nikoliv nasazení na produkci

## 5.3 Continuous Deployment

- Automatické _nasazení aktuální verze_
- **Vhodné** pro automatické nasazování **do testovacího prostředí**
- Samotné nasazení na produkci je dobré _mít automatizované “na jedno kliknutí”_ (Zákazník odsouhlasí novou verzi)

## 5.4 Výhody

- Rychlé odhalení chyb
- Stejné prostředí pro všechny vývojáře
- Méně manuální práce
- Rychlejší vydávání verzí
- Vyšší kvalita softwaru

## 5.5 Nevýhody

- Složitější počáteční nastavení
- Potřeba údržby pipeline
- Náklady na infrastrukturu
- Chybně nastavená automatizace může blokovat celý vývoj

## 5.6 Nástroje

- **Build nástroje** — Jejich úkolem je **automaticky sestavit aplikaci**. Je součástí CI.
  - _Příklady_:
    - **Maven** — Nejpoužívanější build nástroj pro Javu.
    - **Gradle** — Modernější alternativa Mavenu.
    - **Ant** — Starší build nástroj pro Javu.
    - **npm** — Build nástroj (resp. správce balíčků se skripty) pro JavaScript.
    - **Make** — Používá se hlavně v Linuxu a C/C++.
- **CI/CD nástroje** — **Řídí celý proces**.
  - _Příklady_:
    - **Jenkins**
    - **GitHub Actions**
    - **GitLab CI/CD**
    - **Azure DevOps**
    - **TeamCity**