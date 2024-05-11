- Schopnost přizpůsobit se různým velikostem displeje
- Responzivní design je zásadní pro vytvoření webových stránek, které efektivně fungují na širokém spektru zařízení od desktopů po mobilní telefony

## Plně fluidní layout 
- Flexibilní layout, který se umí přizpůsobit většině všech zařízení
- Pouze jednoduché stránky mohou být plně fluidní
- Vyhnutí se používání position: absolute -> pevně daná velikost je na různých zařízení vnímána jinak
- Ideální je používat:
	- Pro písma: `em`, `rem`,  (relativní velikost vzhledem k velikost fontu) 
	- Pro mezery: `vw`, `vh` (nedoporučuje se kvůli iOS)
	- Případně: `%`
## Media Queries
- Media Queries jsou mocným nástrojem pro modifikaci layoutu stránek podle specifikací zařízení, na kterých jsou zobrazeny
- Umožňují aplikovat různé styly pro různé charakteristiky zařízení, jako je šířka, výška, orientace obrazovky nebo typ zařízení
- Media queries mohou cílit na konkrétní zařízení nebo široké kategorie, což umožňuje designérům přizpůsobit zobrazení obsahu k potřebám uživatelů

```CSS
/* Základní syntaxe media query */
@media (min-width: 600px) {
  .container {
    width: 80%;
    margin: auto;
  }
}

/* Použití více podmínek */
@media (min-width: 600px) and (orientation: landscape) {
  body {
    color: navy;
  }
}

```

>[!note] Container queries
> Umožňuje stylování elementů na základě vlastností jejich rodičovského kontejneru, nikoli na základě viewportu, jako je to v případě tradičních media queries.
> Tato funkce je poměrně nová -> [limitovaná podpora prohlížečů](https://caniuse.com/?search=Container%20queries).
## Flexibilní obrázky
- Flexibilní obrázky a média jsou klíčové pro zajištění, že obsah stránky se správně zobrazuje na všech zařízeních
- Obrázky se automaticky přizpůsobují velikosti a orientaci zařízení, aby byly vždy dobře viditelné
- Tato nastavení zajistí, že obrázky se nikdy neroztáhnou mimo svůj kontejner a udržují své původní proporce

```CSS
img {
  max-width: 100%;
  height: auto;
}
```

## Využití Flexboxu a Gridu pro responzivní layouty
- Flexbox a Grid jsou dvě moderní CSS technologie, které usnadňují tvorbu responzivních layoutů 
- Flexbox je ideální pro jednorozměrné layouty a umožňuje snadné zarovnání prvků ve flex kontejneru
- Grid je vhodnější pro složitější dvourozměrné rozvržení
- Flexbox poskytuje snadnou kontrolu nad zarovnáním a distribucí prostoru mezi prvky v kontejneru, zatímco Grid umožňuje přesnější kontrolu nad rozvržením prvků ve dvourozměrném prostoru
```CSS
.container {
  display: flex;
  flex-wrap: wrap;
}

.item {
  flex: 1 1 150px;
}
```

## Breakpoints
- Breakpoints jsou specifické body, kde se obsah webu (vizualizace) mění prostřednictvím media queries (*např. z desktopu na mobil*)
- Tyto body jsou obvykle založeny na běžných velikostech obrazovek a pomáhají zajistit, že layouty jsou optimalizované pro různé zařízení
- Správné nastavení breakpoints je klíčové pro účinný responzivní design, aby byly stránky přístupné a uživatelsky přívětivé na jakémkoli zařízení

```CSS
/* Mobilní zařízení */
@media (max-width: 480px) {
  .sidebar {
    display: none;
  }
}

/* Tablety */
@media (min-width: 481px) and (max-width: 768px) {
  .sidebar {
    width: 50%;
  }
}
```


##### Navigace
Předchozí:  [[Layout webové stránky - grid, flexbox, pozicování]]
Následující: [[Základní HTML elementy a jejich vizualizace]]
Celý okruh: [[2. Informační technologie]]