# 1. Úvod

- **Testování softwaru** je proces _ověřování, zda program funguje správně,_ _splňuje zadané požadavky_ a _chová se tak, jak uživatel očekává_.
- V rámci procesu vývoje softwaru se testování _typicky zařazuje_ mezi **implementaci** a **nasazení** — tedy po vytvoření programu, ale před jeho předáním uživatelům nebo zákazníkovi. (Jinak to může být například při test-driven development)
- Testování zároveň pomáhá ověřit _nejen technickou správnost programu_, ale i to, zda software **odpovídá skutečným potřebám uživatelů**.

---

# 2. Základní typy chyb

- Při vývoji softwaru mohou _vznikat různé druhy chyb_. Je důležité si uvědomit, že chyba nemusí být _způsobena pouze programátorem_. Proto rozlišujeme několik základních typů chyb.

## 2.1 Programátorské chyby

- Vznikají **při implementaci programu**.
- Programátor může udělat _překlep_, _špatně vyhodnotit logický výraz_, zvolit _nevhodný algoritmus_ nebo neznat všechny vlastnosti použité knihovny či vývojového prostředí.

> [!info]
> Podmínka je napsána jako `vek > 18` místo `vek >= 18`.

## 2.2 Nedostatky v zadání

- Aplikace může být vytvořena zcela bez chyb, ale přesto _nemusí řešit problém_, **kvůli kterému vznikla**.
- Příčinou bývají _neúplné nebo špatně formulované požadavky_, chyba analytika nebo _nedostatečná komunikace se zákazníkem_.

> [!info]
> Zákazník potřebuje evidenci směn zaměstnanců, ale v zadání se tato potřeba neobjevila.

## 2.3 Technologické nedostatky

- Tyto chyby souvisejí s _použitou technologií_ nebo **technickými omezeními systému**.
- Může jít například _o nízký výkon aplikace_ nebo _problémy při vyšší zátěži_.

> [!info]
> Webová aplikace funguje správně pro desítky uživatelů, ale při stovkách současně připojených uživatelů přestane odpovídat.

## 2.4 Ostatní chyby

- Do této skupiny patří chyby vzniklé **především kvůli lidskému faktoru**, například _nedorozumění nebo špatná komunikace mezi účastníky_ projektu.

> [!info]
> Dva programátoři vyvíjejí propojené moduly. Jeden očekává datum ve formátu `DD.MM.RRRR`, druhý ve formátu `MM/DD/YYYY`, takže komunikace mezi moduly nefunguje.

---

# 3. Softwarová chyba

- **Softwarová chyba** (bug) je stav, kdy _se software nechová podle požadavků, specifikace nebo očekávání uživatele_.

> [!note]
> Základní typy chyb popisují, **odkud chyba vznikla**, zatímco pojem **softwarová chyba** popisuje, **jak se tato chyba projeví v samotném programu**

- Za **softwarovou chybu** lze _považovat situaci_, kdy:
  1. **software _nedělá něco, co by měl dělat podle specifikace_**_,_
    - _Například_: Po kliknutí na „Uložit“ se dokument neuloží.
  2. **software** **_dělá něco, co by podle specifikace dělat neměl_**,
    - _Například_: Po kliknutí na „Tisk“ se aplikace zavře.
  3. **software _dělá něco, co není uvedeno ve specifikaci_** (navíc)
    - _Například_: Aplikace po spuštění automaticky odešle statistiky na server, přestože to nebylo požadováno
  4. **software _nedělá něco, co není ve specifikaci, ale mělo by_**,
    - _Například_: Formulář nekontroluje, zda je zadaný e-mail ve správném formátu.
  5. **software je _obtížně použitelný, pomalý nebo nesrozumitelný_**,
    - _Například_: Na otevření jednoduchého okna musí uživatel čekat 30 sekund.

- Chyba _prochází definovanými stavy_:

1. **Nalezena** — tester identifikuje problém
2. **Otevřena** — záznam je vytvořen v bug tracking nástroji
3. **Vyřešena** — vývojář problém opravil
4. **Uzavřena** — tester ověřil opravu a uzavřel záznam

## 3.1 Klasifikace chyb

### A) Vážnost (Severity)

- **Stupeň 1**
  - **Nejzávažnější problémy:**
    - Pád systému, ztráta dat, poškození dat, prolomení bezpečnosti.
    - Příklad: Aplikace crashuje při každém druhém přihlášení.
- **Stupeň 2**
  - Chyby vedoucí k _nesprávným výsledkům operací_ nebo _ke ztrátě důležité funkcionality systému_.
  - Příklad: Výpočet slevy vrátí špatné číslo.
- **Stupeň 3**
  - **Kosmetické a drobné problémy**
  - Pravopis, kosmetické chyby v GUI.
  - Příklad: Špatně zarovnaný tlačítko v dialogu.

### B) Priorita (Priority)

- **Okamžitá oprava**
  - Blokuje další testování nebo je viditelná zákazníkovi.
- **Před nasazením**
  - Musí se opravit před uvedením software do provozu.
- **Pokud dovolí čas**
  - Mělo by se opravit, ale není kritické.

> [!warning]
> Vážnost a priorita **nejsou to samé!** Chyba s nízkou vážností (překlep na titulní stránce) může mít **vysokou prioritu** (zákazník to hned uvidí).

## 3.2. Cena softwarových chyb

> [!danger]
> Platí jednoduchá zásada: **čím dříve chybu najdete, tím levnější je její oprava.**

- Chyba nalezená ve fázi **specifikace** — prakticky nulové náklady na opravu.
- Chyba nalezená při **kódování** — malé náklady.
- Chyba nalezená při **testování** — středně velké náklady.
- Chyba nalezená až **u zákazníka po nasazení** — velmi vysoké náklady (podpora, záplaty, reputační škoda).

---

# 4. Vlastnost systému

- **Vlastnost** (feature) je _zamýšlené chování nebo funkce systému_, která byla navržena a **odpovídá požadavkům či specifikaci**.
- Vlastnost _nemusí být vždy uživateli příjemná_ nebo vyhovující, ale pokud _odpovídá zadání, nejedná se o chybu_.

> [!info]
> _Příklady vlastností_:
>
> - Automatické odhlášení uživatele po 15 minutách nečinnosti.
> - Povinnost zadat heslo o minimálně 8 znacích.
> - Omezení velikosti nahrávaného souboru na 10 MB.

> [!danger]
> **Klíčová poučka:** Chyba vs. vlastnost se vždy řeší odkazem na schválenou specifikaci. Proto je kvalita specifikace zásadní — _špatná specifikace = špatně definované chyby_.