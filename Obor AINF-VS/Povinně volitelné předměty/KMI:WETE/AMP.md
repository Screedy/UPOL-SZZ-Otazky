**AMP** je open-source webový framework zaměřený na tvorbu rychle načítaných webových stránek. Původně vznikl pod názvem **Accelerated Mobile Pages**, tedy „zrychlené mobilní stránky“, ale dnes se obvykle používá samostatné označení **AMP**, protože technologie není omezena jen na mobilní zařízení.

AMP bylo představeno v roce **2015** firmou Google jako reakce na dlouhodobý problém webu: mnoho stránek se na mobilních zařízeních načítalo příliš pomalu. Základní myšlenkou AMP je omezit některé techniky, které web zpomalují, a zároveň umožnit velmi rychlou distribuci obsahu přes cache a přednačítání.

Důležité je, že AMP není „magické zrychlení“ každého webu. Největší přínos má u obsahových a relativně statických stránek, například článků, blogů, dokumentace, produktových stránek nebo vybraných vstupních stránek e-shopu.

---

## Proč na rychlosti webu tolik záleží

Rychlost načítání stránky významně ovlivňuje uživatelský zážitek. Uživatel očekává, že web bude reagovat téměř okamžitě. Čím déle stránka čeká na první obsah, tím větší je riziko, že uživatel odejde.

Než prohlížeč vůbec stáhne první bajty HTML, musí se obvykle stát několik kroků:

- vyhledání domény přes **DNS**,
- navázání spojení se serverem,
- vytvoření zabezpečeného spojení přes **HTTPS/TLS**, (SSL je taky velká režie)
- odeslání požadavku na server,
- vygenerování odpovědi na serveru (největší brzda)
- stažení HTML a dalších zdrojů.

Velkou brzdou může být zejména serverové generování stránky a stahování mnoha externích zdrojů, například reklam, analytických skriptů, fontů nebo velkých obrázků. AMP se snaží zrychlit web hlavně tím, že stránka je více statická, dopředu validovatelná, dobře kešovatelná a její externí prvky jsou načítány kontrolovaně.

---

## Části AMP

1. AMP jako front-end framework
  - AMP HTML (k dispozici pouze speciální validní sada HTML)
  - AMP CSS (součástí HTML)
  - Předpřipravené komponenty (navigace, reklamy, karusel)
  - Statický layout - prohlížeč při načítání stránky ví, že tam bude obrázek nebo reklama, takže stránka pak po jeho reálném načtení “neposkočí”
  - Žádný vlastní JS (JS funguje, ale pouze předpřipravené věci)
  - Pouze validní kód
2. AMP jako specifická distribuce
  - AMP cache - kopie AMP stránky uložená na velmi rychlých serverech
  - AMP viewer - “obal” ve kterém se stránka může zobrazit
  - Přednačítání (např. uživatel je ve vyhledávači a Google načte stránku ještě před tím, než ji uživatel reálně otevře)
  - Umístění na speciálních serverech

---

## Jak funguje distribuce AMP stránky

Typický proces distribuce AMP vypadá takto:

1. Autor webu vytvoří běžnou stránku a k ní AMP verzi, případně vytvoří stránku přímo jako AMP.
2. V běžné stránce se uvede odkaz na AMP verzi pomocí `rel="amphtml"`.
3. V AMP stránce se uvede kanonická URL pomocí `rel="canonical"`, aby bylo jasné, jaká je hlavní verze obsahu.
4. Vyhledávač nebo jiný robot AMP stránku najde.
5. AMP Cache stránku stáhne, ověří její validitu, optimalizuje ji a uloží do mezipaměti.
6. Uživatel pak může dostat stránku z cache, často přes AMP Viewer.

Příklad vztahu mezi běžnou a AMP verzí:

```html
<!-- běžná stránka odkazuje na AMP verzi -->
<link rel="amphtml" href="https://example.com/clanek/amp">

<!-- AMP stránka odkazuje na kanonickou verzi -->
<link rel="canonical" href="https://example.com/clanek">
```

Jedna stránka tak může prakticky existovat na více místech:

- na **origin serveru**, tedy na původním webu,
- v **AMP Cache**,
- v **AMP Vieweru**, přes který ji zobrazuje konkrétní platforma.

---

## AMP Cache a optimalizace

**AMP Cache** je kešovací vrstva. Jejím úkolem je uložit validní AMP dokument, případně ho dále optimalizovat a rychle servírovat uživatelům.

AMP Cache může provádět například:

- validaci AMP dokumentu,
- čištění HTML,
- minifikaci kódu,
- optimalizaci obrázků,
- změnu formátu obrázků, například na modernější formáty (z JPEG na WEBP)
- přednačtení AMP komponent,
- optimalizaci odkazů na statický obsah (např. fonty) pro rychlejší načtení
- ochranu proti některým bezpečnostním problémům, například XSS.

Nejznámější je **Google AMP Cache**, ale cache nemusí provozovat pouze Google (můžou být i jiní poskytovatelé)

Kešování má ale i nevýhody. Největší problém je aktuálnost obsahu. Pokud se stránka na původním serveru změní, cache nemusí změnu zobrazit okamžitě. Aktualizaci cache lze obvykle vyžádat, ale stále je třeba počítat s tím, že mezi původním webem a kešovanou kopií může existovat krátké zpoždění.

---

## AMP Viewer

**AMP Viewer** je prostředí, ve kterém platforma zobrazuje AMP stránku uživateli. Vždy zobrazuje šedou lištu. Typicky jde o obal kolem stránky, který může pomáhat s rychlým zobrazením, navigací a integrací s platformou. Není to tedy samotná AMP stránka.

---

## Omezení AMP

AMP přináší rychlost za cenu omezení. Tato omezení nejsou náhodná - mají zabránit věcem, které typicky zpomalují web.

#### Omezení HTML

AMP stránka musí být validní AMP HTML. Některé běžné HTML prvky se používají jinak nebo jsou nahrazeny AMP komponentami.

Například:

- místo `<img>` se používá `<amp-img>`,
- pro video se používají AMP komponenty,
- pro iframe existuje kontrolovaná komponenta,
- formuláře se používají přes `amp-form`.

AMP komponenty často vyžadují atributy jako `width`, `height` a `layout`, aby bylo možné **předem vypočítat rozložení stránky.**

#### Omezení CSS

CSS se u AMP vkládá přímo do HTML, typicky do `<style amp-custom>`. Externí stylesheety nejsou běžně povoleny, s výjimkou některých pravidel pro fonty.

Důležitá omezení:

- velikost CSS je omezena přibližně na **75 kB**,
- není dovoleno používat některé problematické konstrukce,
- `!important` je zakázáno,
- zákaz stylování generovaného AMP kódu, ideálně nestylovat ani komponenty

#### Omezení JavaScriptu

AMP obecně neumožňuje vlastní libovolný JavaScript. JavaScript jako takový ale v AMP existuje – používá ho AMP runtime a jednotlivé komponenty.

Místo vlastního JS se používají připravené komponenty, například:

- `amp-carousel` pro karusel
- `amp-form` pro formuláře
- reklamní a analytické komponenty.

Toto omezení je zásadní. Díky němu AMP lépe kontroluje načítání zdrojů a zabraňuje tomu, aby stránka byla zpomalena autorskými nebo třetími skripty.

---

## Statický layout a lazy loading

Jedním z hlavních principů AMP je **statický layout**. Znamená to, že prohlížeč má dopředu vědět, jak velký prostor zaberou obrázky, reklamy, videa nebo jiné externí prvky.

Díky tomu se stránka při načítání méně „rozskakuje“ a uživatel může rychleji začít číst obsah. AMP také zavádí řízené načítání externích prvků, tedy **lazy loading**. Prvky, které nejsou hned potřeba, se nenačítají okamžitě, ale až ve chvíli, kdy se blíží do viditelné části stránky.

Tyto principy se postupně dostaly i do běžného webového vývoje. Dnes je například běžné používat atributy pro nativní lazy loading obrázků.

---

## Technická kostra AMP dokumentu

Zjednodušená AMP stránka může vypadat takto:

```html
<!doctype html>
<html amp lang="cs">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,minimum-scale=1">
  <script async src="https://cdn.ampproject.org/v0.js"></script>
  <style amp-custom>
    h1 { font-size: 2rem; }
  </style>
  <style amp-boilerplate>/* povinný AMP boilerplate */</style>
  <link rel="canonical" href="https://example.com/clanek">
  <title>Ukázková AMP stránka</title>
</head>
<body>
  <h1>Ahoj světe, tady AMP</h1>
  <amp-img src="obrazek.jpg" width="800" height="450" layout="responsive"></amp-img>
</body>
</html>
```

Základní znaky AMP dokumentu:

- značka `<html amp>` nebo varianta se symbolem blesku,
- načtení AMP runtime skriptu,
- vložené vlastní CSS přes `amp-custom`,
- povinný boilerplate styl,
- kanonický odkaz,
- použití AMP komponent místo některých běžných HTML prvků.

Validita je u AMP velmi důležitá. Nevalidní AMP stránka ztrácí hlavní výhody AMP distribuce, protože cache a platformy s ní nemohou bezpečně pracovat jako s AMP dokumentem.

---

## Proč nelze AMP zavést plošně na celý web

AMP nelze jednoduše aplikovat na celý internet z několika důvodů.

První problém je rozsah. Kešovat celý web by znamenalo obrovské množství duplicitního obsahu. Druhý problém je, že ne všechny weby jsou vhodné pro statický nebo výrazně omezený model. Moderní webové aplikace často potřebují komplexní JavaScript, personalizaci, stav aplikace, přihlášení a interaktivitu, což se s AMP slučuje obtížněji.

Další problém je vývojářská flexibilita. AMP omezuje HTML, CSS i JavaScript. To může být přijatelné u článku, ale problematické u komplexní aplikace.

Proto se AMP hodí hlavně tam, kde je důležitý rychlý první vstup na stránku a obsah je relativně stabilní.

---

## AMP a Google

AMP bylo od začátku silně spojeno s Googlem. Google technologii představil, provozuje významnou AMP Cache a integroval AMP do svého vyhledávání.

To přineslo dvě protichůdné interpretace:

- pozitivní: Google pomohl prosadit rychlejší a výkonnější web,
- kritická: Google získal větší vliv nad tím, jak se webový obsah publikuje a distribuuje.

Pozn. AMP není jen formát pro webové stránky. Postupně vznikly i další formy jako AMP Email (interaktivnější emaily - např. vyplnit v emailu formulář, podpora závisí na klientovi) nebo AMP Ads

---

## Možnosti nasazení AMP

AMP lze nasadit několika způsoby:

1. Dvě verze stránek - běžná HTML stránka a samostatná AMP verze
2. HTML s výjimkami pro AMP - základ je běžná HTML stránka, která se pro AMP upravuje (tento přístup se snaží minimalizovat rozdíly mezi verzemi)
3. A další

---

## Praktické využití AMP

AMP je nejvhodnější pro:

- zpravodajské články,
- blogy,
- dokumentační stránky,
- marketingové landing pages,
- vybrané produktové stránky,
- obsahové části e-shopu.

Méně vhodné je pro:

- komplexní webové aplikace,
- administrační rozhraní,
- vysoce personalizovaný obsah,
- aplikace silně závislé na JavaScriptu,
- weby, které potřebují netypickou interaktivitu.

V praxi se AMP často nasazuje jen na část webu – například na články nebo nejdůležitější vstupní stránky. Takové řešení je sice částečné, ale může dávat smysl, protože největší přínos AMP je u prvního rychlého načtení obsahu.