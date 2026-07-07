# 1. Úvod

> [!success]
> **Prototyp** je _zjednodušená nebo neúplná verze budoucího softwarového systému_, která slouží k ověření nápadů, požadavků nebo technických řešení **dříve, než je vynaloženo maximum zdrojů na vývoj**.
>
> Jeho _cílem není vytvořit hotový produkt_, ale **získat zpětnou vazbu** a odhalit problémy co nejdříve.

# 2. Proč se prototypy používají?

- Lépe pochopit požadavky zákazníka (Zákazník/uživatel **neumí přesně specifikovat požadavky** v abstraktní podobě — ale dokáže reagovat na něco, co vidí.)
- Ověřit, zda navržené řešení dává smysl
- Odhalit nejasnosti a chyby v návrhu
- Získat zpětnou vazbu od uživatelů
- Snížit riziko drahých změn během vývoje (Umožňuje **odhalit problémy a nedorozumění** v rané fázi, kdy je jejich oprava nejlevnější.)

### 2.1 Výhody prototypů

- **Snížení rizika** — chyby v pochopení požadavků se odhalí brzy.
- **Lepší komunikace** — zákazník vidí konkrétní věc, ne abstraktní dokumenty.
- **Vyšší spokojenost zákazníka** — je zapojen do procesu, výsledek odpovídá jeho představám.
- **Lepší kvalita výsledného produktu** — požadavky jsou přesnější.
- Umožňuje **testování použitelnosti** (usability) v rané fázi.

> [!info]
> #### Příklad
>
> Zákazník chce e-shop.
>
> Po vytvoření klikatelného prototypu zjistí, že by chtěl:
>
> - košík vpravo nahoře,
> - jiný způsob filtrování,
> - jednodušší objednávku.
>
> Tyto změny stojí jen několik minut místo týdnů přepisování hotového systému.

### 2.2 Nevýhody prototypů

- **Zákazník si splete prototyp s hotovým produktem** — zákazník může mít pocit, že je systém téměř hotový a chce ho hned nasadit
- Vytvoření prototypu **stojí čas i peníze**,
- Prototypování může **prodloužit projekt**, pokud se iterace opakují donekonečna bez jasného cíle.
- Pokud se začne používat nekvalitní prototyp jako finální systém, může vzniknout špatně navržený software.

---

# 3. Způsob vytvoření prototypů

| Druh prototypu | Popis | Výhody / Charakteristika |
| --- | --- | --- |
| **Papírový prototyp (Paper Prototype)** | Nejjednodušší varianta. Rozhraní je nakreslené na papíře nebo tabuli. | Extrémně levný, rychlý na vytvoření, snadno upravitelný |
| **Wireframe** | Jednoduchý návrh rozložení obrazovky. Obsahuje tlačítka, menu, formuláře a rozmístění prvků. Neobsahuje grafický design. | Slouží k návrhu struktury uživatelského rozhraní bez grafických detailů. |
| **Klikatelný (interaktivní) prototyp** | Vypadá jako skutečná aplikace. Lze mezi obrazovkami přecházet klikáním, ale neobsahuje skutečnou logiku. | Umožňuje simulovat práci s aplikací a získat zpětnou vazbu od uživatelů. |
| **Funkční prototyp** | Obsahuje část skutečné funkcionality, například přihlášení, vyhledávání nebo ukládání dat. | Slouží k ověření technického řešení a implementace. |

---

# 4. Typy prototypů

## 4.1 Throwaway prototyp (prototyp na vyhození)

- Rychle se vytvoří, ukáže zákazníkovi, získá zpětná vazba — a pak se **zahodí**.
- Kód/design není určen pro produkci, je záměrně „špinavý".
- Cílem je **objasnit požadavky**, ne vytvořit základ produktu.
- **Výhoda:** Rychlost, žádný tlak na kvalitu kódu.
- **Nevýhoda:** Zákazník může naléhat, aby se prototyp rovnou nasadil do produkce — to je nebezpečné, protože kód nebyl navržen pro trvalé použití.

## 4.2 Evolutionary prototyp (evoluční prototyp)

- Prototyp se postupně **zdokonaluje a rozrůstá** až do výsledného produktu.
- Každá iterace přidává funkce na základě zpětné vazby.
- Cílem je od začátku psát **kvalitní, udržitelný kód**.
- **Výhoda:** Žádné vyhazování práce, systém vzniká organicky.
- **Nevýhoda:** Složitější plánování, může vzniknout architektonický dluh, pokud raná rozhodnutí nejsou revidována.

---

## Prototyp v kontextu metodiky vývoje

- V **modelu vodopád** se prototyp používá především ve fázi analýzy požadavků — jednorázově, throwaway přístup.
- V **agilním přístupu** je evoluční prototypování přirozenou součástí — každý sprint přináší funkční inkrement, který zákazník vidí a komentuje.