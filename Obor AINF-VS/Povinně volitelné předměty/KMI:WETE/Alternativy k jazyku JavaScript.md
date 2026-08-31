JavaScript je jedna ze základních technologií webu vedle HTML a CSS. V prohlížeči má výjimečné postavení, protože je dlouhodobě standardním jazykem pro skriptování webových stránek na straně klienta. Proto se často říká, že JavaScript na webu prakticky nemá plnohodnotnou přímou alternativu.

Důležité je rozlišit dvě věci:

1. **Alternativa syntaxe nebo vývojového jazyka**  
  Programátor píše v jiném jazyce, ale výsledek se přeloží do JavaScriptu. Typickým příkladem je TypeScript.
2. **Alternativa běhového formátu**  
  Programátor píše například v C, C++ nebo Rustu a výsledek se přeloží do jiného formátu, který prohlížeč umí spustit. Typickým příkladem je WebAssembly.

Ve většině případů tedy nejde o úplné „nahrazení“ JavaScriptu, ale spíše o technologie, které JavaScript doplňují nebo nad ním staví.

---

## 2. Transpilace

**Transpilace** je překlad zdrojového kódu z jednoho programovacího jazyka do jiného jazyka na podobné úrovni abstrakce. Vývojář tedy může psát například v TypeScriptu, ale výsledná aplikace se v prohlížeči spouští jako JavaScript.

Typické důvody pro transpilaci:

- pohodlnější syntaxe,
- typová kontrola,
- lepší čitelnost a udržovatelnost,
- možnost používat vlastnosti, které nejsou přímo dostupné ve všech cílových prostředích.

---

## 3. TypeScript

### 3.1 Základní charakteristika

**TypeScript** je silně typovaný jazyk postavený nad JavaScriptem. Přidává do JavaScriptu především typové anotace a lepší podporu pro vývoj větších aplikací (pro to je populární). Orientuje se především na čitelnost a přehlednost kódu.

TypeScript se nepouští v prohlížeči přímo. Nejprve se přeloží do JavaScriptu a teprve výsledný JavaScript běží v prohlížeči nebo například v prostředí Node.js.

Hlavní přínosy TypeScriptu:

- umožňuje zachytit část chyb už při vývoji,
- zpřehledňuje datové struktury a rozhraní,
- zlepšuje našeptávání a kontrolu v editoru,
- hodí se pro větší projekty s více vývojáři.

TypeScript není úplně jiný ekosystém než JavaScript. Spíše je to rozšíření JavaScriptu o typový systém.

### 3.2 Základní datové typy

V JavaScriptu se typy proměnných běžně nepíší explicitně. V TypeScriptu je možné typ uvést.

```ts
let cislo: number = 42;
let retezec: string = "Joey";
let logickaHodnota: boolean = true;
```

Základní typy:

- `number` – čísla,
- `string` – textové řetězce,
- `boolean` – logické hodnoty `true` a `false`.

Typové anotace pomáhají kompilátoru i vývojáři pochopit, jaká hodnota se v proměnné očekává.

### 3.3 Složené datové typy

TypeScript umí popsat i složitější datové struktury.

```ts
let list: Array<number> = [1, 2, 3];
enum Color { Red, Green, Blue }
```

Důležité pojmy:

- **Pole** – kolekce hodnot stejného nebo podobného typu.
- **Enum** – výčet pojmenovaných hodnot.
- **Any** – typ, který vypíná přísnou typovou kontrolu pro danou hodnotu. Je užitečný při práci s neznámými daty, ale měl by se používat opatrně.

### 3.4 Funkce a návratové typy

TypeScript umožňuje určit i návratový typ funkce.

```ts
function f(): void {
  console.log("blah");
}
```

Typ `void` znamená, že funkce nevrací žádnou užitečnou hodnotu. Používá se například u funkcí, které pouze něco vypisují, mění stav nebo volají jinou akci.

### 3.5 Interface

**Interface** popisuje tvar objektu. Neříká, jak přesně má být objekt implementován, ale určuje, jaké vlastnosti a metody musí mít.

```ts
interface InterfacePoint {
  x: number;
  y: number;
  print(): void;
}
```

Tento interface říká, že objekt typu `InterfacePoint` musí mít:

- číselnou vlastnost `x`,
- číselnou vlastnost `y`,
- metodu `print`, která nic nevrací.

### 3.6 Třídy, dědičnost a dekorátory

TypeScript podporuje objektově orientované programování. Třída může implementovat interface:

```ts
class Point implements InterfacePoint {
  // implementace vlastností a metod
}
```

Důležité pojmy:

- **Třída** – šablona pro vytváření objektů.
- **Implements** – třída slibuje, že splní strukturu daného rozhraní.
- **Extends** – klíčové slovo pro dědičnost, tedy odvození nové třídy od existující.

---

## 4. Python jako alternativa k JavaScriptu

Další skupinou nástrojů jsou knihovny, které umožňují psát webovou logiku v Pythonu nebo spouštět Python v prostředí webového prohlížeče.

Příklady:

- Brython,
- Transcrypt,
- Pyodide,
- Skulpt.

Tyto nástroje se liší tím, jak fungují. Některé překládají Python do JavaScriptu, jiné umožňují spustit Python pomocí WebAssembly.

### 4.1 Kdy to dává smysl

Python v prohlížeči může být užitečný například:

- ve výuce programování,
- v interaktivních demonstračních aplikacích,
- tam, kde má cílová skupina zkušenost s Pythonem, ale ne s JavaScriptem.

### 4.2 Omezení

Pythonové alternativy nejsou běžnou náhradou JavaScriptu pro klasický frontendový vývoj.

Typická omezení:

- menší ekosystém pro běžné webové UI,
- horší integrace s existujícími JavaScriptovými frameworky,
- větší objem načítaného kódu,
- možné výkonnostní nebo kompatibilitní limity.

Je proto vhodnější chápat je jako specializované nástroje, ne jako univerzální náhradu JavaScriptu.

---

## 5. Dart

### 5.1 Základní charakteristika

**Dart** je programovací jazyk vyvíjený společností Google. Je navržený pro tvorbu aplikací napříč platformami (nesplněný sen Googlu o dominaci webu).

Dart se používá hlavně ve spojení s frameworkem **Flutter**, který slouží k tvorbě uživatelských rozhraní pro mobilní, webové i desktopové aplikace.

### 5.2 Význam

Dart je zajímavý hlavně tam, kde chceme sdílet jednu kódovou základnu pro více platforem. Pro klasické webové stránky se používá méně často než JavaScript nebo TypeScript. Častější použití je pro vývoj mobilních aplikací (jeden kód, ze kterého “zbuildíme” aplikaci pro iOS i Android)

---

## 6. WebAssembly

### 6.1 Co je WebAssembly

**WebAssembly**, zkráceně **WASM** je po HTML, CSS a JS, dalším nativně podporovaným jazykem, který mohou spouštět moderní webové prohlížeče.

Na rozdíl od TypeScriptu nejde o jazyk, který by se běžně psal ručně. Vývojář obvykle píše v jazyce jako C, C++, Rust nebo Go a tento kód se přeloží do WebAssembly.

WebAssembly je navrženo tak, aby běželo rychle a efektivně (je v mnoha případech rychlejší než JS). Hodí se hlavně pro výpočetně náročné části aplikací.

### 6.2 Postavení mezi webovými technologiemi

WebAssembly není plnohodnotná náhrada JavaScriptu. V běžných webových aplikacích často potřebuje JavaScript jako propojení s DOM, tedy se strukturou HTML stránky.

### 6.3 Typický postup použití

Zjednodušený postup:

1. Programátor napíše výpočetně náročnou část například v C, C++ nebo Rustu.
2. Kód se přeloží do souboru `.wasm`.
3. JavaScript tento soubor načte.
4. JavaScript zavolá funkce exportované z WebAssembly modulu.
5. Výsledek se použije ve webové aplikaci.

Příklad z prezentace je funkce pro druhou mocninu čísla:

```c
int square(int n) {
  return n * n;
}
```

Po překladu do WebAssembly lze tuto funkci volat z JavaScriptu.

```js
fetch("test.wasm")
  .then(bytes => bytes.arrayBuffer())
  .then(mod => WebAssembly.compile(mod))
  .then(module => {
    let instance = new WebAssembly.Instance(module);
    console.log(instance.exports.square(15));
  });
```

Tento příklad ukazuje důležitou myšlenku: WebAssembly vykoná výpočet, ale JavaScript se stará o načtení modulu a komunikaci s okolím webové stránky.

### 6.4 Kdy se WebAssembly hodí

WebAssembly se hodí hlavně pro:

- zpracování velkých dat,
- grafické a multimediální aplikace,
- hry,
- kompresi a dekompresi,
- kryptografii,
- simulace,
- portování existujících knihoven napsaných v C, C++ nebo Rustu na web.

Výhodou je, že lze využít existující kód a spustit ho v prohlížeči s výkonem blízkým nativnímu běhu.

---

## 7. Krátké shrnutí

Alternativy k JavaScriptu na webu většinou nejsou přímé náhrady. Nejčastější přístup je psát v jiném jazyce a výsledek převést do JavaScriptu nebo WebAssembly. TypeScript je dnes nejpraktičtější a nejrozšířenější nadstavba JavaScriptu pro větší projekty. Pythonové nástroje jsou vhodné spíše pro výuku, data a experimenty. Dart je významný hlavně díky Flutteru a multiplatformnímu vývoji. WebAssembly je důležité pro výkonné části aplikací a pro přenos existujícího kódu z jazyků jako C, C++ nebo Rust na web.