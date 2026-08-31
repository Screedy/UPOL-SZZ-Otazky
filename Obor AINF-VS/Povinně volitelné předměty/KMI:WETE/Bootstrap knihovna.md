## 1. Základní charakteristika

**Bootstrap** je volně dostupná front-endová UI knihovna / framework pro tvorbu webového uživatelského rozhraní. Poskytuje **předpřipravené CSS styly**, **layoutový systém, komponenty a volitelné JavaScriptové pluginy**. Cílem Bootstrapu je zrychlit tvorbu konzistentního, responzivního a použitelně vypadajícího webového rozhraní. Hodí se zejména pokud si nevěříme s HTML a CSS nebo nemáme cit na grafiku (ale i pokud umíme a chceme ušetřit čas).

Bootstrap se používá hlavně tam, kde je důležitá rychlá tvorba funkčního rozhraní a konzistence prvků, například u administrací, interních systémů nebo prototypů. Naopak u běžných prezentačních webů nebo webů s výrazně specifickým vizuálním stylem může být jeho použití problematické, protože Bootstrap přináší **vlastní designový systém** (web potom vypadá "bootstrapově")

### Hlavní části Bootstrapu

Bootstrap se skládá především z těchto částí:

1. **Layout systém**  
  Slouží k rozvržení stránky. Typicky pracuje s kontejnery, řádky a sloupci.
2. **Komponenty**  
  Předpřipravené prvky rozhraní, například tlačítka, formuláře, navigace, modální okna, alerts, dropdowny, karty nebo carousel.
3. **Utility třídy**  
  Pomocné CSS třídy pro rychlé nastavení okrajů, odsazení, barev, zarovnání, viditelnosti, flexboxu a dalších vlastností.
4. **JavaScriptové pluginy**  
  Přidávají interaktivitu některým komponentám, například modálním oknům, dropdownům, tooltipům nebo collapse prvkům.

---

## 2. Bootstrap a responzivní web

Jedním z nejznámějších prvků Bootstrapu je jeho mřížkový systém. Často se proto zjednodušeně říká, že „Bootstrap = mřížka“. To je ale omezený pohled. Mřížka je důležitá, ale Bootstrap zahrnuje mnohem více.

### Responzivní design

**Responzivní design** znamená, že se vzhled webu přizpůsobuje velikosti obrazovky nebo okna prohlížeče. Jeden HTML dokument se tedy zobrazuje jinak na mobilu, tabletu a desktopu.

Bootstrap používá tzv. **mobile-first** přístup. To znamená, že základní styly jsou navržené pro malé obrazovky a pro větší obrazovky se postupně přidávají další pravidla pomocí breakpointů.

### Breakpoint

**Breakpoint** je hranice šířky viewportu, od které se změní rozložení nebo vzhled stránky. Například na mobilu mohou být prvky pod sebou, zatímco na desktopu vedle sebe.

Bootstrap má předdefinované breakpointy, které umožňují psát třídy jako například:

```html
<div class="col-12 col-md-6 col-lg-4">
```

Tento příklad znamená:

- na nejmenších obrazovkách prvek zabere celou šířku,
- od střední velikosti polovinu šířky,
- od velké velikosti třetinu šířky.

---

## 3. Mřížkový systém Bootstrapu

Bootstrapový grid používá kombinaci kontejnerů, řádků a sloupců.

### Container

**Container** je obal stránky nebo její části. Určuje maximální šířku obsahu a zarovnává jej na stránce.

Bootstrap rozlišuje například:

```html
<div class="container">...</div>
```

a

```html
<div class="container-fluid">...</div>
```

`container` má omezenou maximální šířku podle breakpointu. `container-fluid` zabírá celou dostupnou šířku.

### Row

**Row** představuje řádek v mřížce. Slouží jako obal pro sloupce.

```html
<div class="row">
  ...
</div>
```

### Column

**Column** představuje sloupec. Bootstrap tradičně pracuje s rozdělením řádku na 12 částí.

```html
<div class="row">
  <div class="col-6">Levý sloupec</div>
  <div class="col-6">Pravý sloupec</div>
</div>
```

V tomto příkladu mají oba sloupce polovinu šířky.

### Flexbox

Mřížkový systém Bootstrapu je postavený na CSS Flexboxu. Flexbox je CSS model pro rozmisťování prvků v jednom směru, tedy typicky v řádku nebo ve sloupci. Umožňuje například snadné zarovnání prvků, změnu jejich pořadí nebo práci s volným místem.

Důležité je, že Bootstrap ve výchozí konfiguraci nestaví svůj hlavní grid na CSS Gridu, ale na Flexboxu. CSS Grid je moderní CSS nástroj pro dvourozměrné rozvržení, ale Bootstrapový grid historicky i prakticky vychází hlavně z Flexboxu.

---

## 4. Komponenty Bootstrapu

**Komponenta** je znovupoužitelný prvek uživatelského rozhraní. Bootstrap nabízí komponenty, které mají předem definovanou HTML strukturu, CSS třídy a někdy i JavaScriptové chování.

Mezi typické komponenty patří:

- tlačítka,
- formuláře,
- navigace,
- karty,
- alerts,
- badges,
- modální okna,
- dropdown menu,
- accordion,
- carousel.

### Příklad tlačítka

```html
<button class="btn btn-primary">Uložit</button>
```

Třída `btn` říká, že jde o bootstrapové tlačítko. Třída `btn-primary` určuje jeho význam a vzhled podle primární barvy systému.

### Příklad alertu

```html
<div class="alert alert-success">
  Změny byly úspěšně uloženy.
</div>
```

Třída `alert` definuje obecný vzhled oznámení. Třída `alert-success` říká, že jde o pozitivní nebo úspěšnou zprávu.

---

## 5. Utility třídy

**Utility třídy** jsou malé pomocné třídy, které nastavují jednu konkrétní vlastnost nebo malou skupinu vlastností. Díky nim lze rychle upravovat vzhled bez psaní vlastního CSS.

Například:

```html
<div class="mt-3 p-4 text-center">
  Obsah
</div>
```

Tento zápis znamená:

- `mt-3` nastaví horní vnější okraj,
- `p-4` nastaví vnitřní odsazení,
- `text-center` zarovná text na střed.

Utility třídy šetří čas, ale jejich nadužívání může vést k méně přehlednému HTML. Je proto dobré je používat rozumně.

---

## 6. Bootstrap a JavaScript

Bootstrap obsahuje také volitelné JavaScriptové pluginy. Ty se používají u komponent, které nejsou jen statické, ale mají interaktivní chování. Typickým příkladem je modální okno, dropdown menu, tooltip nebo collapse.

Významnou změnou v Bootstrapu 5 bylo odstranění závislosti na jQuery. Starší verze Bootstrapu jQuery používaly, ale Bootstrap 5 používá vlastní JavaScript založený na moderních možnostech prohlížečů. To zlepšuje použitelnost Bootstrapu v moderních projektech a usnadňuje kombinaci například s Reactem, Vue nebo dalšími frameworky.

---

## 7. Designový systém Bootstrapu

Bootstrap není jen sada jednotlivých CSS tříd. Přináší také vlastní designový systém. Ten zahrnuje například:

- typografii,
- barvy,
- velikosti prvků,
- rozestupy,
- chování komponent,
- zaoblení rohů,
- stavy prvků, například hover, active nebo disabled.

Problém nastává ve chvíli, kdy chceme vytvořit web, který se od tohoto systému výrazně liší. Pak vývojář často začne přepisovat velké množství výchozích stylů. To je obvykle špatný přístup, protože se tím ztrácí hlavní výhoda Bootstrapu: rychlá tvorba konzistentního rozhraní.

Lepší je Bootstrap přizpůsobovat systematicky, například pomocí Sass proměnných, než proti němu bojovat náhodným přepisováním CSS.

---

## 8. Typické problémy při použití Bootstrapu

### 1. Web vypadá „bootstrapově“

Protože Bootstrap obsahuje výchozí vzhled komponent, mnoho webů může působit podobně. To nemusí vadit u administrací nebo interních aplikací, ale může to být problém u značkových webů, kde je důležitá originalita.

### 2. Nepochopení designového systému

Pokud vývojář nevnímá, že Bootstrap má vlastní systém, může jednotlivé komponenty používat nekonzistentně. Výsledkem je rozhraní, které kombinuje výchozí Bootstrap s náhodnými úpravami.

### 3. Přepisování výchozích stylů

Častou chybou je ruční přepisování velkého množství CSS. Například vývojář použije bootstrapové tlačítko a potom kompletně přepíše jeho barvu, velikost, okraje i chování. V takovém případě je otázka, zda Bootstrap vůbec pomáhá.

### 4. Nevhodné použití na silně individuální design

Pokud má projekt přesně navržený vizuální styl, Bootstrap může být spíše omezením. V takové situaci může být vhodnější psát vlastní CSS nebo použít jiný nástroj.

---

## 9. Přizpůsobení Bootstrapu

Bootstrap je možné přizpůsobit. Důležité je dělat to správně.

### Sass

**Sass** je preprocesor CSS. Umožňuje používat proměnné, funkce, mixiny a další konstrukce, které se následně přeloží do běžného CSS.

Bootstrap používá Sass, takže jeho vzhled lze měnit pomocí Sass proměnných. Například lze upravit barvy, rozestupy, zaoblení nebo typografii.

### Proměnné

**Proměnná** je pojmenovaná hodnota, kterou lze používat na více místech. Například primární barva může být definována jednou a potom použita u tlačítek, odkazů nebo aktivních stavů.

Zjednodušený příklad:

```scss
$primary: #0d6efd;
$border-radius: .375rem;
```

Pokud se proměnná změní před sestavením Bootstrapu, projeví se změna systematicky v celé knihovně.

### CSS proměnné

Bootstrap 5 používá také CSS proměnné, tedy custom properties. Ty existují přímo ve výsledném CSS a mohou se měnit i za běhu v prohlížeči.

Příklad:

```css
:root {
  --bs-primary: #0d6efd;
}
```

CSS proměnné jsou užitečné například pro témata, tmavý režim nebo rychlé prototypování.

---

## 10. Bootstrap vs. Tailwind CSS

Bootstrap a Tailwind CSS mají odlišnou filozofii.

### Bootstrap

Bootstrap poskytuje hotové komponenty a výchozí vzhled. Vývojář může rychle vytvořit celé rozhraní, protože velká část vizuálního rozhodování je už předpřipravená.

Bootstrap se hodí, když:

- potřebujeme rychle vytvořit funkční UI,
- nevadí nám výchozí designový systém,
- tvoříme administraci, dashboard nebo interní aplikaci,
- chceme používat hotové komponenty.

### Tailwind CSS

Tailwind CSS je utility-first framework. Neposkytuje primárně hotové komponenty se vzhledem, ale velké množství malých utility tříd. Vývojář skládá design přímo z těchto tříd.

Tailwind se hodí, když:

- chceme větší kontrolu nad vizuálním stylem,
- máme vlastní design,
- nechceme být tolik svázáni výchozími komponentami,
- jsme ochotni psát více tříd v HTML.

---

## 11. Bootstrap jako framework a šablony

Bootstrap lze používat nejen jako knihovnu komponent, ale také jako základ celého vizuálního frameworku aplikace. Existuje mnoho hotových šablon založených na Bootstrapu, hlavně pro administrace a dashboardy.

Výhody šablon:

- rychlý start projektu,
- hotové stránky a komponenty,
- jednotný vzhled,
- úspora času.

Nevýhody šablon:

- často jsou placené,
- mohou obsahovat zbytečně mnoho kódu,
- mohou být obtížně přizpůsobitelné,
- mohou ještě více posilovat „bootstrapový“ vzhled,
- projekt se může stát závislým na konkrétní šabloně.

Šablony tedy mohou být praktické, ale je potřeba hlídat jejich kvalitu, udržovatelnost a vhodnost pro konkrétní projekt.