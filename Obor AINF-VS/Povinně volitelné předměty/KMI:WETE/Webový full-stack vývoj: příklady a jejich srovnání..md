## 1. Co znamená full-stack vývoj

**Full-stack vývoj** znamená, že vývojář řeší jak **front-end**, tak **back-end** webové aplikace.

- **Front-end** je část aplikace běžící v prohlížeči uživatele. Řeší uživatelské rozhraní, interakce, formuláře, vizualizaci dat a komunikaci s back-endem. FE-orientovaný vývojář dobře ovládá JavaScript/TypeScript a front-end frameworky, ale back-end řeší jednodušším API, serverless funkcemi nebo hotovým backendovým řešením.
- **Back-end** je serverová část aplikace. Řeší obchodní logiku, autentizaci, práci s databází, zpracování požadavků a poskytování API. BE-orientovaný vývojář dobře ovládá serverovou technologii, databáze a API, ale front-end řeší jednodušeji – například šablonami, formuláři nebo základním JavaScriptem.
- **Databáze** slouží k trvalému uložení dat. Nemusí být vždy součástí stejného hostingu ani stejného serveru jako aplikace.

Dnes je „plnohodnotný“ full-stack vývoj obtížný, protože oblast webového vývoje je velmi rozsáhlá. V praxi se vývojáři často specializují více na jednu stranu. Důležité je rozumět alespoň jedné back-end technologii, protože každá netriviální webová aplikace nakonec potřebuje řešit serverovou logiku, bezpečnost a práci s daty.

---

## 2. Základní části webového full-stacku

Typická webová aplikace se skládá z několika vrstev:

### 2.1 Klientská část

Klientská část běží v prohlížeči. Základ tvoří:

- **HTML** – struktura stránky.
- **CSS** – vzhled a rozvržení.
- **JavaScript** – interaktivita, práce s daty, komunikace se serverem.

Moderní front-end často používá framework nebo knihovnu, například React, Vue nebo Angular. Ty pomáhají rozdělit uživatelské rozhraní na menší komponenty a lépe spravovat stav aplikace.

### 2.2 Serverová část

Serverová část přijímá HTTP požadavky, provádí aplikační logiku a vrací odpovědi. Může vracet:

- hotové HTML stránky,
- JSON data pro front-end,
- soubory,
- chybové odpovědi,
- přesměrování.

Na back-endu se používají různé technologie: PHP, Node.js, Python, Java, .NET, Ruby a další.

### 2.3 Datová vrstva

Datová vrstva řeší ukládání a načítání dat. Nejčastější varianty jsou:

- **relační databáze** – například MySQL, MariaDB, PostgreSQL,
- **dokumentové databáze** – například MongoDB,
- jednoduché ukládání do souborů – JSON, XML nebo CSV, pokud jde o malý nebo jednoduchý projekt (například potřebujeme ukládat data ve formátu klíč-hodnota)

Volba databáze má být odvozena od tvaru dat a potřeb aplikace, ne pouze od popularity technologie. Pokud mají data jasné vztahy, tabulky a integritní omezení, bývá vhodnější relační databáze. Pokud se ukládají dokumenty s proměnlivou strukturou, může dávat smysl dokumentová databáze.

---

## 3. PHP stack

### 3.1 Charakteristika PHP

**PHP** je jazyk historicky navržený primárně pro tvorbu webů. Od verze PHP 8 už je to konečně dospělý programovací jazyk (verze 4,5 a 7 nikoho nezajímaly).

Typický PHP stack je tvořen PHP + MySQL/MariaDB + HTML/CSS/JavaScript.

### 3.2 Výhody PHP

- **Dostupný hosting** – PHP podporuje velké množství hostingů.
- **Ověřená technologie** – používá se dlouho a existuje mnoho návodů, knihoven i hotových řešení.
- **Nízká vstupní bariéra** – jednoduchou aplikaci lze napsat poměrně rychle.
- **Velká standardní knihovna** – PHP obsahuje mnoho funkcí pro práci se soubory, textem, formuláři, databázemi a webovým prostředím.

### 3.3 Nevýhody PHP

- **Primárně back-endová technologie** – pro moderní interaktivní front-end je stejně potřeba JavaScript.
- **Škálování závisí na architektuře a serverovém prostředí** – tradiční PHP aplikace běží typicky v modelu request-response, kde se při každém požadavku spustí zpracování a vytvoří odpověď.
- **Není enterprise** – neznamená to, že PHP nelze použít ve velkých projektech, ale v korporátním prostředí často dominují jiné platformy.

### 3.4 Šablony

Čisté PHP se dnes už běžně nevidí. Využívá se v kombinaci se **šablonovacími systémy,** které oddělují aplikační logiku od HTML výstupu. Místo toho, aby se HTML skládalo ručně v PHP kódu, vytvoří se šablona, do které se doplní data.

Příklady šablonovacích systémů:

- Smarty,
- Plates,
- Mustache,
- Latte,
- Twig.

### 3.5 ORM

**ORM** znamená _Object-Relational Mapping_. Jde o vrstvu, která mapuje objekty v programu na tabulky v relační databázi. V PHP je mírně zaostalé, ale jsou k dispozici externí služby.

Bez ORM vývojář píše přímo SQL dotazy. S ORM pracuje více s objekty, například `User`, `Article`, `Order`.

Výhody ORM:

- méně ručně psaného SQL,
- jednotný způsob práce s databází,
- lepší udržovatelnost u větších aplikací.

Nevýhody ORM:

- může skrývat složitost SQL,
- někdy generuje neefektivní dotazy,
- vývojář stejně musí rozumět databázím.

### 3.6 PHP frameworky

**Framework** je sada nástrojů a pravidel, která usnadňuje vývoj aplikace. PHP framework typicky obsahuje:

- routování,
- šablony,
- ORM nebo integraci s ORM,

Frameworky typicky vynucují MVC architekturu.

Příklady PHP frameworků:

- **Laravel** – velmi populární, široký ekosystém, důraz na vývojářskou produktivitu.
- **Nette** – český framework, známý mimo jiné šablonovacím systémem Latte.

---

## 4. JavaScript full-stack

### 4.1 Charakteristika JavaScript stacku

JavaScript se původně používal hlavně v prohlížeči. Díky runtime prostředím jako **Node.js** nebo **Deno** lze JavaScript nebo TypeScript používat i na serveru.

Typický JavaScript stack: Node.js nebo Deno + databáze + front-end framework (a těch je hodně)

### 4.2 Výhody JavaScript stacku

- **Jeden jazyk na front-endu i back-endu** – tým může sdílet znalosti, typy, validační logiku nebo části kódu.
- **Velký ekosystém balíčků** – zejména kolem Node.js a npm.
- **Velká škálovatelnost**
- **Přesah mimo web** – JavaScript ekosystém se používá i pro PWA, desktopové aplikace pomocí Electronu nebo mobilní aplikace přes React Native.

### 4.3 Nevýhody JavaScript stacku

- **Rychlý vývoj ekosystému** – technologie, nástroje a doporučené postupy se často mění.
- **Vyšší nároky na znalosti** – vývojář musí rozumět asynchronnímu programování, práci se stavem, build nástrojům a často i TypeScriptu.
- **Komplexita moderního front-endu** – u větších aplikací je potřeba řešit routing, stav, validace, data fetching, SSR nebo caching.
- **Riziko přílišné závislosti na balíčcích** – velký ekosystém je výhoda, ale zároveň může vést k nadměrnému počtu závislostí.

### 4.4 Node.js

**Node.js** je runtime pro spouštění JavaScriptu mimo prohlížeč. Je zaběhnutý a má rozsáhlý ekosystém.

Důležitý pojem je **event loop**. Node.js běžně používá jeden hlavní JavaScriptový thread, ale neblokující I/O umožňuje obsluhovat mnoho požadavků efektivně. Operace jako síť nebo disk se delegují mimo hlavní běh programu a výsledek se zpracuje později.

Node.js se hodí pro:

- REST API,
- real-time aplikace,
- aplikace s mnoha I/O operacemi,
- back-end pro moderní front-end aplikace.

---

## 5. JavaScript front-end frameworky

Front-end framework nebo knihovna pomáhá stavět uživatelské rozhraní z komponent.

### 5.1 React

**React** je knihovna pro tvorbu uživatelských rozhraní. Staví UI z komponent, které lze skládat do větších celků.

Charakteristika:

- velmi rozšířený ekosystém,
- komponentový model,
- velká komunita,

React sám o sobě není plný framework. Řeší hlavně UI, zatímco routing, data fetching, SSR nebo stavová správa se řeší dalšími knihovnami nebo frameworkem nad Reactem.

### 5.2 Vue

**Vue** je progresivní JavaScript framework pro tvorbu webových rozhraní.

Charakteristika:

- dobře čitelná syntaxe,
- nižší vstupní bariéra než u některých konkurentů,
- komponentový přístup,
- ekosystém zahrnuje například Nuxt pro full-stack a serverově renderované aplikace.

Vue je často vnímáno jako pragmatická volba pro týmy, které chtějí moderní framework, ale nechtějí příliš komplikovanou architekturu.

### 5.3 Angular

**Angular** je plnohodnotný framework pro tvorbu webových aplikací.

Charakteristika:

- používá TypeScript,
- obsahuje mnoho věcí přímo v základu,
- hodí se pro větší týmy a rozsáhlejší aplikace,
- má silnější architektonická pravidla než React nebo Vue.

Angular se často používá v enterprise prostředí, kde je výhodou jednotná struktura aplikace.

Důležité je nevnímat množství frameworků jako nutnost naučit se všechny. Pro praxi je rozumné vybrat jeden hlavní ekosystém a tomu rozumět do hloubky (existuje jich ještě mnoho dalších).

---

## 6. Problém moderního JavaScript full-stacku: přesun práce na klienta

Moderní web často přesouvá část práce z back-endu na front-end. Server může poskytovat jen API a většina logiky zobrazení běží v prohlížeči.

Výhoda:

- server může být jednodušší,
- front-end je interaktivnější,
- část výpočtů a vykreslování se přesune ke klientovi.

Nevýhoda:

- aplikace může být pomalejší při prvním načtení,
- prohlížeč musí stáhnout a zpracovat více JavaScriptu,
- může se zhoršit SEO,
- aplikace je složitější na optimalizaci.

Řešením je **pre-rendering**.

---

## 7. Pre-rendering

**Pre-rendering** znamená, že HTML stránky se vytvoří dříve, než se plně spustí JavaScript v prohlížeči. Cílem je rychlejší první zobrazení stránky, lepší SEO a menší zátěž klienta. Možnosti jsou například server-side nebo static-site rendering.

### 7.1 Server-side rendering

**Server-side rendering** neboli **SSR** znamená, že HTML se generuje na serveru při požadavku.

Postup:

```text
uživatel pošle požadavek → server vygeneruje HTML → prohlížeč zobrazí stránku → JavaScript doplní interaktivitu
```

Výhody:

- rychlejší první zobrazení,
- lepší SEO,
- vhodné pro dynamický obsah.

Nevýhody:

- větší zátěž serveru,
- složitější infrastruktura než čistě statický web.

### 7.2 Frameworky pro pre-rendering

V React ekosystému se používá zejména:

- **Next.js** – SSR, SSG, ISR, routing, API routes a další full-stack funkce.
- **Remix** – důraz na webové standardy, serverové načítání dat a formuláře.
- **Gatsby** – zaměření na statické weby a obsah.

---

## 8. JavaScript back-end: frameworky a ORM

### 8.1 Express

**Express** je minimalistický webový framework pro Node.js. Používá se hlavně pro routing a tvorbu API.

Příklad použití:

- REST API,
- jednoduchý back-end,
- server pro single-page aplikaci,
- prototyp nebo menší služba.

Express je flexibilní, ale mnoho architektonických rozhodnutí nechává na vývojáři.

### 8.2 Šablonovací systémy v Node.js

Podobně jako PHP může i Node.js generovat HTML pomocí šablon.

Příklady:

- Pug,
- EJS,
- doT,
- Nunjucks.

Tento přístup je vhodný pro serverově renderované weby, kde není potřeba plně oddělený front-end.

### 8.3 ORM v JavaScript ekosystému

Příklady ORM a databázových nástrojů:

**Prisma** je často používané řešení v TypeScript projektech, protože klade důraz na typovou bezpečnost a generovaný klientský kód pro práci s databází.

---

## 9. „Newebová“ cesta: jiné serverové technologie

Webový back-end nemusí být napsaný v technologii, která vznikla primárně pro web. Prakticky každý obecný programovací jazyk lze použít na serveru, pokud má knihovny pro HTTP, práci s databází a šablony nebo API.

### 9.1 .NET a ASP.NET Core

**.NET** je platforma od Microsoftu. Pro webový vývoj se používá hlavně **ASP.NET Core**.

Vlastnosti:

- častá volba v enterprise prostředí,
- silná typová kontrola díky C#,
- dobrá integrace s nástroji Microsoftu,
- podpora moderních webových aplikací.

### 9.2 Python

Python se na webu používá hlavně přes frameworky:

- **Flask** – minimalistický framework.
- **Django** – plnohodnotný framework.
- **FastAPI** – moderní framework často používaný pro API.

Flask je vhodný pro menší aplikace nebo služby, kde chce vývojář větší volnost. Django nabízí hotovou strukturu, ORM, administraci a mnoho bezpečnostních mechanismů. FastAPI se hodí pro moderní API, zejména pokud se využívá typování a automatická dokumentace rozhraní.