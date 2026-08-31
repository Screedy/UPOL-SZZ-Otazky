CSS je jazyk pro popis vzhledu webových dokumentů. V základní podobě je syntakticky jednoduchý: vybíráme prvky pomocí selektorů a k nim zapisujeme deklarace vlastností a hodnot.

Problém nastává ve chvíli, kdy projekt roste. CSS soubory mohou být dlouhé, opakující se a hůře udržovatelné. Typickým příkladem je změna barvy značky, mezery, velikosti písma nebo názvosloví tříd na mnoha místech projektu. Právě tento praktický problém motivoval vznik CSS preprocesorů.

Hlavní myšlenka: nepsat veškeré výsledné CSS ručně, ale psát pohodlnější zdrojový kód, ze kterého nástroj vygeneruje běžné CSS pro prohlížeč.

---

## Meze samotného CSS

Dříve CSS postrádalo některé konstrukce známé z programovacích jazyků, například:

- proměnné,
- funkce,
- vnořování pravidel,
- výpočty,
- podmínky a cykly,
- pohodlné rozdělení kódu do modulů.

To vedlo k tomu, že větší CSS bylo často „upovídané“ a nepřehledné.

Dnes už je situace lepší. Moderní CSS umí například vlastní vlastnosti, tedy CSS proměnné, funkci `calc()` a nativní CSS nesting. Přesto CSS stále není obecný programovací jazyk a některé věci, například generování většího množství tříd nebo pokročilejší logiku při sestavení stylů, se řeší lépe pomocí nástrojů.

---

## CSS preprocesor

**CSS preprocesor** je nástroj, který generuje standardní CSS. Tento proces se často označuje jako **transpilace** (převod kódu z jednoho jazyka nebo syntaxe do jiného jazyka podobné úrovně).

Existuje jich řada, ale v praxi je dnes nejdůležitější SASS (konkrétně syntaxe SCSS).

### SASS vs. SCSS

**SASS** je název technologie i původní syntaxe. Původní SASS syntaxe používá odsazování a nepoužívá složené závorky ani středníky.

**SCSS** je novější a běžnější syntaxe SASSU. Je kompatibilnější s běžným CSS: používá složené závorky, středníky a běžný zápis CSS. To znamená, že platný CSS soubor je většinou zároveň platný SCSS soubor.

### Implementace Sassu

Důležitá je implementace, tedy konkrétní program, který Sass/SCSS převádí na CSS.

- **Dart Sass** je současná oficiálně podporovaná implementace.
- **LibSass** dosáhl konce životnosti a pro nové projekty se nepoužívá.
- **Ruby Sass** je historická implementace, jejíž vývoj byl ukončen.

---

## Proměnné

Proměnná umožňuje pojmenovat hodnotu a používat ji na více místech.

```scss
$color-main: #58508d;
$color-contrast: #ffa600;

.box {
  background-color: $color-main;
  color: $color-contrast;
}
```

Výsledné CSS už proměnné Sassu neobsahuje:

```css
.box {
  background-color: #58508d;
  color: #ffa600;
}
```

Výhoda je údržba. Když se změní hlavní barva projektu, změní se na jednom místě.

### SASS proměnné vs. CSS proměnné

SASS proměnná existuje při sestavení kódu. Do prohlížeče se nedostane.

CSS proměnná (**custom property**), existuje až v prohlížeči, účastní se kaskády a může se měnit podle kontextu, například podle třídy, media query nebo JavaScriptu.

```css
:root {
  --color-main: #58508d;
}

.box {
  background-color: var(--color-main);
}
```

Zjednodušeně:

- Sass proměnné jsou vhodné pro hodnoty známé při buildu.
- CSS proměnné jsou vhodné pro hodnoty, které mají reagovat na kaskádu, téma nebo runtime změny.

---

## Komentáře

SCSS rozlišuje dva typy komentářů.

```scss
// komentář pouze pro preprocesor

/* komentář pro CSS */
```

Jednořádkový komentář `//` je určen jen pro zdrojový SCSS kód a do výsledného CSS se nevygeneruje. Blokový komentář `/* ... */` je součástí vygenerovaného CSS.

---

## Interpolace

**Interpolace** znamená vložení hodnoty proměnné do místa, kde SASS očekává část názvu, selektoru nebo vlastnosti.

```scss
$where: top;

.box {
  #{$where}: 1em;
}
```

Výsledek:

```css
.box {
  top: 1em;
}
```

Interpolace se hodí při generování názvů tříd, vlastností nebo cest k souborům. Je ale potřeba ji používat opatrně, protože příliš dynamické názvy mohou zhoršit čitelnost kódu.

---

## Nesting: vnořování pravidel

**Nesting** umožňuje psát CSS pravidla do sebe podle struktury komponenty.

```scss
.nav {
  height: 3em;

  ul {
    margin: 0;
    padding: 0;
  }
}
```

Výsledek:

```css
.nav {
  height: 3em;
}

.nav ul {
  margin: 0;
  padding: 0;
}
```

Výhoda je kratší a přehlednější zápis. Nevýhoda je riziko příliš dlouhých selektorů. Hluboké vnořování často vede k příliš specifickému CSS, které se později špatně přepisuje.

Praktické pravidlo: vnořovat jen tam, kde to opravdu zlepšuje čitelnost, a vyhýbat se hlubokým řetězcům typu `.page .content .article .header a`.

---

## Rodičovský selektor `&`

Symbol `&` označuje aktuální rodičovský selektor.

```scss
a {
  text-decoration: underline;

  &:hover {
    text-decoration: none;
  }
}
```

Výsledek:

```css
a {
  text-decoration: underline;
}

a:hover {
  text-decoration: none;
}
```

`&` je důležitý hlavně pro pseudo-třídy, modifikátory a práci s metodikami pojmenování tříd.

---

## SCSS a BEM

**BEM** je metodika pojmenování CSS tříd. Název znamená:

- **Block** – samostatná komponenta, například `.nav`,
- **Element** – část komponenty, například `.nav__item`,
- **Modifier** – varianta komponenty nebo elementu, například `.nav--secondary` nebo `.nav__item--active`.

SCSS umožňuje s BEM zápisem pracovat pomocí `&`.

```scss
.nav {
  &--secondary {
    /* sekundární navigace */
  }

  &__item {
    /* položka navigace */

    &--active {
      /* aktivní položka */
    }
  }
}
```

Výsledek:

```css
.nav--secondary {}
.nav__item {}
.nav__item--active {}
```

Výhoda je menší opakování názvu bloku. Kritika spočívá v tom, že výsledné názvy tříd nejsou ve zdrojovém kódu vždy vidět celé, což může snižovat čitelnost.

---

## Dědičnost: `@extend`

V SASSU se pojem dědičnost používá trochu zavádějícím způsobem. Nejde o dědičnost jako v objektově orientovaném programování, ale spíše o rozšíření selektoru.

```scss
.box {
  border: 1px solid black;
}

.box--emphasize {
  @extend .box;
  border-color: red;
}
```

Výsledek může být:

```css
.box, .box--emphasize {
  border: 1px solid black;
}

.box--emphasize {
  border-color: red;
}
```

`@extend` říká, že jeden selektor má sdílet pravidla s jiným selektorem. Výhodou je menší výsledné CSS. Nevýhodou je, že může vytvářet složité kombinace selektorů a skryté vazby mezi částmi kódu.

---

## Skryté třídy: placeholder selektory

**Placeholder selektor** začíná znakem `%`. Sám o sobě se do výsledného CSS nevygeneruje. Použije se až ve chvíli, kdy ho někdo rozšíří pomocí `@extend`.

```scss
%box {
  border-width: 1px;
  border-style: solid;
}

.box--normal {
  @extend %box;
  border-color: black;
}
```

Výhoda je, že ve výsledném CSS nevznikne zbytečná třída `%box`. Placeholder je vhodný pro sdílený základ, který nemá existovat jako samostatná třída v HTML.

---

## Mixiny

**Mixina** je znovupoužitelný blok stylů. Vkládá se pomocí `@include`.

```scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.box {
  @include flex-center;
}
```

Výsledek:

```css
.box {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

Mixiny se hodí, když chceme opakovaně vložit stejný nebo podobný blok deklarací.

### Parametrizované mixiny

Mixina může přijímat parametry.

```scss
@mixin flex-center($flex-direction: row) {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: $flex-direction;
}

.box--column {
  @include flex-center(column);
}
```

Parametry mohou mít výchozí hodnoty. Při volání lze používat poziční argumenty nebo pojmenované argumenty.

### Mixiny vs. `@extend`

- Mixina vloží kopii deklarací tam, kde je použita.
- `@extend` propojí selektory a sdílí deklarace přes společné pravidlo.

Mixiny jsou obvykle čitelnější a bezpečnější. `@extend` se používá, když je žádoucí explicitně určit závislosti mezi částmi kódu.

---

## Funkce

**Funkce** v SASSU vrací hodnotu. Používá se tam, kde potřebujeme něco spočítat nebo odvodit.

```scss
$base: 1em;

@function add-m($x: 1em) {
  @return $base + $x;
}

.box {
  margin: add-m(2em);
}
```

Výsledek:

```css
.box {
  margin: 3em;
}
```

Funkce by měla vracet hodnotu, zatímco mixina typicky generuje deklarace nebo celé bloky CSS.

Sass také podporuje `@warn` a `@error`, tedy varování a chyby během sestavení. To se hodí například při kontrole neplatných argumentů.

---

## Větvení programu - podmínky

SASS podporuje větvení pomocí `@if`, `@else if` a `@else`.

```scss
@mixin theme-colors($light-theme: true) {
  @if $light-theme {
    background-color: white;
    color: black;
  } @else {
    background-color: black;
    color: white;
  }
}
```

Podmínky umožňují generovat různé CSS podle hodnot proměnných nebo parametrů.

SASS má také funkci `if()`, která se podobá ternárnímu operátoru.

```scss
$show-border: false;

.box {
  padding: 1em;
  border: if($show-border, 1px solid black, null);
}
```

Pokud je hodnota vlastnosti `null`, SASS ji do výsledného CSS nevypíše.

---

## Větvení programu - cykly

Cykly umožňují generovat opakující se pravidla.

### `@each`

```scss
@each $icon in $icons {
  .icon--#{$icon} {
    background: url("#{$icon}.png");
    width: 2em;
    height: 2em;
  }
}
```

Tento kód vygeneruje třídy `.icon--up`, `.icon--right`, `.icon--bottom` a `.icon--left`. Tyto třídy budou mít nastaveny vlastnosti width, height a background (název obrázku je také doplněn podle up/right/bottom/left).

### `@for`

```scss
@for $i from 1 through 3 {
  .size-#{$i} {
    width: 20ch * $i;
  }
}
```

Cykly jsou silné, ale neměly by se zneužívat. Jsou vhodné pro utility třídy, sady ikon nebo opakující se varianty komponent.

---

## Vestavěné moduly

SASS obsahuje vestavěné moduly s funkcemi. Načítají se pomocí `@use`.

```scss
@use "sass:math";

@debug math.ceil(4.2);
```

Modulový systém pomáhá udržet kód přehledný, protože funkce a proměnné jsou jmenně oddělené. To snižuje riziko konfliktů v názvech.

---

## Organizace kódu

Větší projekt se obvykle nedrží v jednom souboru. Sass umožňuje rozdělit kód na menší části.

Historicky se používalo hlavně `@import`. Dnes se preferují:

- `@use` – načte modul a zpřístupní jeho proměnné, mixiny a funkce přes namespace,
- `@forward` – předává obsah modulu dál, typicky při tvorbě knihovny nebo veřejného API stylů.

---

## Temná strana preprocesorů

Preprocesory byly pro webový vývoj zásadní, ale mají i nevýhody.

Hlavní problémy:

- příliš složité abstrakce mohou zakrýt výsledné CSS,
- hluboký nesting vede ke složitým selektorům,
- nadměrné používání mixinů může nafouknout výsledný CSS soubor,
- `@extend` může vytvářet nečekané vazby mezi selektory,
- část schopností preprocesorů postupně přebírá moderní CSS.

Důležité je chápat preprocesor jako nástroj pro lepší pracovní postup, ne jako náhradu za znalost CSS.

---

## CSS postprocesor

**CSS postprocesor** zpracovává CSS po jeho napsání nebo vygenerování. Zatímco preprocesor typicky převádí rozšířený jazyk na CSS, postprocesor bere CSS jako vstup a upravuje ho.

Typické úkoly postprocesoru:

- převod moderních CSS vlastností pro starší prohlížeče,
- optimalizace a minifikace CSS,
- kontrola kvality kódu,
- práce s CSS moduly nebo dalšími pluginy.

Nejdůležitější nástroj v této oblasti je **PostCSS**.

---

## PostCSS

**PostCSS** je nástroj pro transformaci CSS pomocí JavaScriptu. Je založený na pluginech. Samotný PostCSS je tedy spíše platforma než jeden konkrétní preprocesor nebo postprocesor.

Příklad principu:

1. PostCSS načte CSS.
2. Převede ho na strukturu, se kterou mohou pracovat pluginy.
3. Pluginy CSS upraví.
4. PostCSS vygeneruje výsledné CSS.

---

## Preprocesor vs. postprocesor

| Vlastnost | Preprocesor | Postprocesor |
| --- | --- | --- |
| Typický vstup | SCSS, SASS, Less, Stylus | CSS |
| Typický výstup | CSS | upravené CSS |
| Hlavní účel | pohodlnější zápis a generování CSS | transformace, kompatibilita, optimalizace |
| Příklad | SASS | PostCSS |
| Typická funkce | proměnné, mixiny, nesting, funkce | autoprefixing, minifikace, fallbacky |

V praxi se často používají oba přístupy. Například vývojář napíše SCSS, Sass ho převede na CSS a PostCSS pak výsledné CSS ještě upraví.