- Většina webových aplikací se skládá ze tří částí: uživatelského rozhraní, logiky aplikace a datového rozhraní. 
- Význam uživatelského rozhraní je jasný. 
- Logika aplikace reprezentuje implementovanou funkcionalitu. 
- Datové rozhraní představuje rozhraní pro připojení k databázi, kde jsou uložena data, se kterými aplikace pracuje.

## Monolitická architektura
- Celá aplikace je vyvíjena a nasazována jako **jeden celek**.
- **Výhody**:
	1. **Srozumitelnost a jednoduchost**: Noví vývojáři mohou snáze pochopit, jak aplikace funguje, protože vše je součástí jedné kódbáze.
	2. **Jednoduché testování**: Testování může být jednodušší, protože neexistují závislosti na externích službách nebo síťových voláních, které by mohly komplikovat testovací proces.
	3. **Snadné nasazení**: Jelikož je aplikace sestavena do jednoho balíčku, může být nasazení rychlé a jednoduché.
- **Nevýhody:**
	1. **Škálovatelnost**: Monolitické aplikace mohou být obtížně škálovatelné, zejména v distribuovaných prostředích nebo v cloudových službách, kde je potřeba flexibilně škálovat jednotlivé komponenty.
	2. **Obtížná údržba**: S rostoucí velikostí kódbáze se může stát, že údržba a implementace nových funkcí bude složitější a nákladnější.
	3. **Nedostatek flexibility**: Jakékoli změny, i malé, mohou vyžadovat znovusestavení a nasazení celé aplikace, což může být časově náročné a riskantní vzhledem k možnosti zavlečení chyb.
	4. **Odolnost vůči chybám**: Chyba v jedné části aplikace může způsobit selhání celého systému.

## MVC architektura
- Rozděluje aplikaci na **3 základní celky**:
	- **Model** - Odpovídá za práci s daty a přístup k databázi. Také určuje formát dat.
	- **View** - Vytváří vizualizaci (UI). Typicky taková šablona jak bude vypadat webová stránka při poskytnutí určitých dat.
	- **Controller** - Implementuje části funkcionality aplikace. Většinou metody, kterým lze předávat parametry.

| ![[MacBook-2024-05-18-001272.png\|440]] | ![[MacBook-2024-05-18-001271.png\|450]] |
| ------------------------------------ | -------------- |

### Charakteristika MVC architektury
- **Oddělení zájmů**: MVC **odděluje** datovou logiku (Model) od zobrazení (View) a ovládací logiky (Controller), což umožňuje lepší správu a údržbu kódu.
- **Znovupoužitelnost**: Každá část (Model, View, Controller) může být znovupoužita v jiných částech aplikace nebo dokonce v jiných aplikacích.
- **Testovatelnost**: Díky oddělení logiky je každá část snadněji testovatelná, což usnadňuje vytváření unit testů a zvyšuje stabilitu aplikace.
- **Flexibilita**: MVC umožňuje snadnou změnu uživatelského rozhraní nebo aplikační logiky, aniž by to mělo vliv na ostatní části aplikace.
- **Škálovatelnost**: Díky oddělení zájmů je aplikace obecně snáze škálovatelná, protože lze jednotlivé komponenty rozvíjet nezávisle na sobě.
## Architektura mikroslužeb
- spočívá v rozdělení aplikace na malé, nezávislé služby, které spolu komunikují přes definované rozhraní nebo API
- každá mikroslužba je samostatný proces, který provádí velmi specifickou funkci aplikace a je nezávislý na ostatních částech systému

### Charakteristiky architektury mikroslužeb
1. **Dekompozice**: Aplikace je rozdělena na menší komponenty, které jsou často organizovány kolem obchodních schopností nebo funkcí.
2. **Nezávislost**: Mikroslužby jsou nezávislé na sobě, což znamená, že vývoj, nasazení a škálování každé mikroslužby může probíhat nezávisle na ostatních službách.
3. **Decentralizace**: Řízení a databáze jsou decentralizovány. Každá mikroslužba typicky spravuje svou vlastní databázi.
4. **Jednoduchost**: Každá mikroslužba je relativně malá a jednoduchá, což usnadňuje její pochopení, vývoj a údržbu.
5. **Heterogenita**: Různé mikroslužby mohou být napsány různými programovacími jazyky a používat různé technologie ukládání dat podle toho, co je pro danou službu nejvhodnější.

![[Microservices vs Monolit.png]]
### Nevýhody architektury mikroslužeb
1. **Složitost**: Správa mnoha malých služeb může být komplikovanější než správa monolitické aplikace, zejména pokud jde o testování, sledování a zajištění bezpečnosti.
2. **Komunikace**: Vzájemná komunikace mezi službami přes síť může představovat výkonnostní a spolehlivostní výzvy.
3. **Datová konzistence**: Každá mikroslužba spravuje svá vlastní data, což může ztížit udržení konzistence dat napříč systémem.

##### Navigace
Předchozí:  [[Webové aplikace a přehled technologií používaných při jejich tvorbě]]
Následující: [[Zpracování HTTP požadavků - předávání dat mezi webovým a aplikačním serverem, překlady realizace]]
Celý okruh: [[3. Programovací jazyky a programování]]