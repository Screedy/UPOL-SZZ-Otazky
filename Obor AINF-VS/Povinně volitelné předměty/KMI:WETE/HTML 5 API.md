## 1. Co znamená „HTML 5 API“

Název **HTML 5 API** je trochu matoucí. Nejde jen o samotný značkovací jazyk HTML, ale obecně o **webová API dostupná v prohlížeči**, se kterými webová stránka pracuje hlavně pomocí JavaScriptu. Patří sem například kreslení do `<canvas>`, ukládání dat v prohlížeči, práce s polohou zařízení, multimédia, drag-and-drop, notifikace a další rozhraní.

Důležitá myšlenka: moderní webová stránka už nemusí být jen statický dokument. Díky webovým API může fungovat jako aplikace – kreslit grafiku, reagovat na vstup uživatele, ukládat stav, pracovat offline nebo využívat senzory a služby zařízení.

**Vztah technologií:**

- **HTML** definuje strukturu stránky a některé prvky, například `<canvas>` nebo `<iframe>`.
- **CSS** řeší vzhled a rozložení.
- **JavaScript** volá API prohlížeče a implementuje aplikační logiku.

---

## 2. Canvas API

### 2.1 Základní princip

**Canvas API** umožňuje kreslit grafiku pomocí JavaScriptu do HTML elementu `<canvas>`. Používá se například pro jednoduché hry, animace, grafy, vizualizace dat, úpravy obrázků nebo generování grafiky na straně klienta.

`<canvas>` je kreslicí plocha. Samotný HTML element pouze vytvoří prostor na stránce, ale kreslení se provádí přes JavaScriptový kontext, typicky přes **2D kontext**:

```js
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
```

Pojem **renderovací kontext** znamená objekt, přes který se kreslí. U 2D grafiky je to `CanvasRenderingContext2D`. Obsahuje metody jako `fillRect`, `lineTo`, `arc`, `drawImage`, `fillText` a vlastnosti jako `fillStyle`, `lineWidth` nebo `globalAlpha`.

### 2.2 Canvas není vektorová grafika

Canvas se často ovládá podobně jako vektorové kreslení – zadáváme souřadnice, čáry, oblouky a tvary. Výsledek je ale **bitmapa**. To znamená, že po vykreslení je obraz uložen jako mřížka pixelů. Prohlížeč si nepamatuje jednotlivé objekty typu „kruh“ nebo „čára“ jako samostatné editovatelné entity.

Důsledky:

- pokud chceme scénu změnit, obvykle ji smažeme a překreslíme,
- detekci kliknutí na objekty musíme řešit sami,
- při špatném škálování může obraz působit rozmazaně,
- pro objektovou nebo dokumentovou grafiku může být vhodnější **SVG**.

### 2.3 Základní kreslení

Nejjednodušší operace jsou obdélníky:

```js
ctx.fillStyle = '#00f';      // barva výplně
ctx.strokeStyle = '#f00';    // barva obrysu
ctx.lineWidth = 4;

ctx.fillRect(0, 0, 150, 50);     // vyplněný obdélník
ctx.strokeRect(0, 60, 150, 50);  // obdélník s obrysem
ctx.clearRect(30, 25, 90, 60);   // vyčištění části plátna
```

Důležité pojmy:

- **fill** znamená výplň tvaru,
- **stroke** znamená obrys tvaru,
- **clear** odstraní pixely v určité oblasti.

Souřadnice v canvasu se běžně počítají od levého horního rohu. Osa `x` roste doprava a osa `y` roste dolů.

### 2.4 Kreslení cest

Složitější tvary se kreslí pomocí **cesty**. Cesta je posloupnost kreslicích příkazů, například „přesuň se na bod“, „nakresli čáru“, „nakresli křivku“. Cesta se nezačne zobrazovat automaticky; musíme ji vykreslit pomocí `fill()` nebo `stroke()`.

```js
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(100, 10);
ctx.lineTo(10, 100);
ctx.closePath();

ctx.fill();
ctx.stroke();
```

Používané metody:

- `beginPath()` začne novou cestu,
- `moveTo(x, y)` přesune aktuální bod bez kreslení,
- `lineTo(x, y)` přidá úsečku,
- `closePath()` uzavře tvar,
- `fill()` vyplní oblast,
- `stroke()` vykreslí obrys.

### 2.5 Křivky, oblouky a barvy

Canvas umí kreslit i křivky a oblouky. **Bézierova křivka** je křivka určená počátečním bodem, koncovým bodem a kontrolními body, které ovlivňují její tvar. V praxi se používá pro hladké křivky.

```js
ctx.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y);
```

Oblouky a kružnice se kreslí pomocí `arc`:

```js
ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise);
```

Barvy lze zadávat například jako:

```js
ctx.fillStyle = '#0000ff';
ctx.strokeStyle = 'rgb(128, 128, 128)';
ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';
ctx.globalAlpha = 0.2;
```

**Alfa kanál** určuje průhlednost. Hodnota `1` znamená zcela neprůhledné a `0` zcela průhledné. Lze také nastavit vlastnosti čáry - například její tloušťku nebo zakončení.

### 2.6 Vkládání obrázků

Canvas umí vykreslovat obrázky pomocí `drawImage`. Obrázek může být vložen v původní velikosti, škálovaný nebo oříznutý.

```js
ctx.drawImage(img, dx, dy);
ctx.drawImage(img, dx, dy, dw, dh);
ctx.drawImage(img, sx, sy, sw, sh, dx, dy, dw, dh);
```

Význam parametrů:

- `dx`, `dy` určují cílovou pozici na canvasu,
- `dw`, `dh` určují cílovou velikost,
- `sx`, `sy`, `sw`, `sh` určují zdrojový výřez obrázku.

### 2.7 Manipulace s pixely

Canvas umožňuje přímý přístup k pixelům. K tomu slouží `ImageData`, typicky získané metodou `getImageData` nebo vytvořené přes `createImageData`.

```js
const imgData = ctx.getImageData(x, y, width, height);
const pixels = imgData.data;
```

`pixels` je pole hodnot, kde každý pixel zabírá čtyři položky:

1. červený kanál,
2. zelený kanál,
3. modrý kanál,
4. alfa kanál.

Hodnoty jsou obvykle v rozsahu `0–255`. Například jednoduchý negativ obrázku vznikne tak, že pro každý barevný kanál použijeme `255 - původní hodnota`.

Po úpravě dat se výsledek vrací do canvasu:

```js
ctx.putImageData(imgData, x, y);
```

### 2.8 Text, stíny a transformace

Canvas umí kreslit text:

```js
ctx.font = 'italic 30px sans-serif';
ctx.textBaseline = 'top';
ctx.fillText('Hello world!', 0, 0);
ctx.strokeText('Hello world!', 0, 50);
```

Dále umí stíny:

```js
ctx.shadowOffsetX = 5;
ctx.shadowOffsetY = 5;
ctx.shadowBlur = 4;
ctx.shadowColor = 'rgba(255, 0, 0, 0.5)';
```

A také transformace:

```js
ctx.save();
ctx.translate(x, y);
ctx.rotate(angle);
ctx.scale(sx, sy);
ctx.restore();
```

Pojmy:

- `translate` posune souřadnicový systém,
- `rotate` otočí souřadnicový systém,
- `scale` změní měřítko,
- `save` uloží aktuální stav kontextu,
- `restore` obnoví poslední uložený stav.

Transformace jsou důležité hlavně u animací, her a složitějších scén, protože je jednodušší posunout souřadnicový systém než přepočítávat všechny body ručně.

---

## 3. Události a interaktivita

Webová aplikace je interaktivní díky **událostem**. Událost je signál, že se něco stalo – uživatel klikl myší, pohnul kurzorem, dotkl se obrazovky, stiskl klávesu nebo se stránka načetla.

Události se registrují metodou `addEventListener`:

```js
canvas.addEventListener('mousedown', handleMouseDown, false);
window.addEventListener('keydown', handleKeyDown, false);
```

Příklady událostí:

- `mousedown`, `mouseup`, `mousemove` pro myš,
- `touchstart`, `touchmove`, `touchend` pro dotyková zařízení,
- `keydown` pro klávesnici,
- `load` pro načtení stránky.

U canvasu je potřeba zdůraznit, že canvas sám nezná objekty, které jsme do něj nakreslili. Pokud například nakreslíme kruh a chceme zjistit, zda na něj uživatel klikl, musíme si souřadnice kruhu uložit v JavaScriptu a sami spočítat, zda bod kliknutí leží uvnitř kruhu.

---

## 4. HTML5 hry

Canvas se často používá pro tvorbu jednoduchých her. Princip je takový, že herní objekty existují jako objekty v JavaScriptu a jejich aktuální stav se průběžně vykresluje do canvasu.

Typická struktura hry:

1. načtení zdrojů, například obrázků,
2. vytvoření herních objektů,
3. zpracování vstupu uživatele,
4. aktualizace stavu hry,
5. vykreslení scény,
6. opakování v herní smyčce.

Důležité pojmy:

- **herní smyčka** je opakovaný cyklus aktualizace a vykreslení,
- **kolize** znamená zjištění, zda se objekty dotkly nebo překryly,
- **scéna** je aktuální vizuální stav hry,
- **delegace událostí** znamená, že vstup uživatele je zpracován centrálně a následně předán odpovídajícím objektům.

Problémy u her:

- výkon procesoru a grafiky,
- rychlost překreslování,
- plynulost animací,
- správa většího množství objektů,
- fyzika a detekce kolizí.

Canvas je technicky poměrně jednoduchý, ale u větších her je pracné řešit vše ručně. Proto se často používají knihovny nebo frameworky.

---

## 5. Ukládání dat v prohlížeči

### 5.1 Proč ukládat data na klientovi

Starší představa byla, že JavaScript na straně klienta nemůže ukládat data. Moderní webové aplikace ale potřebují uchovávat například:

- uživatelská nastavení,
- stav aplikace,
- data pro offline režim,
- cache pro rychlejší načítání,
- rozpracované formuláře.

Historicky se k ukládání používaly hlavně **cookies**. Cookies jsou malé textové hodnoty, které se často posílají se síťovými požadavky na server. Hodí se například pro identifikaci relace, ale nejsou ideální pro větší klientská data.

---

## 6. Web Storage

**Web Storage API** nabízí jednodušší ukládání dvojic klíč–hodnota přímo v prohlížeči. Pracuje se dvěma hlavními objekty:

- `localStorage`,
- `sessionStorage`.

Obě úložiště ukládají pouze řetězce. Pokud chceme ukládat objekt, typicky ho převedeme pomocí `JSON.stringify` a při čtení zpět pomocí `JSON.parse`.

### 6.1 localStorage

`localStorage` ukládá data bez automatického vypršení. Data zůstávají dostupná i po zavření prohlížeče, dokud je uživatel nebo aplikace nesmaže.

```js
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme');
localStorage.removeItem('theme');
localStorage.clear();
```

Vhodné použití:

- nastavení motivu,
- jazyk aplikace,
- drobná cache,
- jednoduchý stav aplikace.

Nevhodné použití:

- citlivá data,
- hesla,
- přístupové tokeny s vysokým rizikem zneužití,
- velká strukturovaná data.

### 6.2 sessionStorage

`sessionStorage` je podobné `localStorage`, ale data jsou vázaná na konkrétní relaci stránky. Typicky se smažou po zavření karty nebo okna prohlížeče.

Použití:

- dočasný stav formuláře,
- kroky v průvodci,
- informace, které nemají přežít zavření karty.

### 6.3 Omezení Web Storage

Web Storage je jednoduché, ale má omezení:

- ukládá jen klíče a hodnoty jako řetězce,
- je synchronní, takže při větším objemu dat může blokovat hlavní vlákno,
- kapacita je omezená a závisí na prohlížeči,
- uživatel může data smazat,
- v privátním režimu se chování může lišit podle prohlížeče.

---

## 7. Web SQL a IndexedDB

### 7.1 Web SQL

**Web SQL Database** bylo API pro ukládání dat v klientské databázi ovládané pomocí SQL. Dnes je důležité hlavně historicky, protože specifikace už není aktivně udržovaná a Web SQL se nemá používat pro nové aplikace.

Důvod, proč je to důležité u státnic: Web SQL ukazuje, že ne každé „HTML5 API“ se dlouhodobě prosadilo. Moderní doporučenou alternativou je hlavně **IndexedDB**.

### 7.2 IndexedDB

**IndexedDB** je nízkoúrovňové API pro ukládání většího množství strukturovaných dat v prohlížeči. Na rozdíl od Web Storage se neomezuje jen na jednoduché řetězce. Umí ukládat objekty a používat indexy pro efektivnější vyhledávání.

Základní pojmy:

- **databáze** – úložiště pro jednu aplikaci/origin,
- **object store** – obdoba tabulky, ukládá záznamy,
- **key** – klíč záznamu,
- **index** – pomocná struktura pro rychlé vyhledávání,
- **transaction** – skupina operací, které se provedou v určitém režimu.

Vhodné použití:

- offline aplikace,
- větší klientská cache,
- ukládání strukturovaných dat,
- ukládání souborů nebo blobů,
- aplikace typu PWA.

Nevýhoda je složitější API. V praxi se proto často používají wrapper knihovny, například Dexie.js.

### 7.3 Web Storage vs. IndexedDB

| Vlastnost | Web Storage | IndexedDB |
| --- | --- | --- |
| Typ dat | řetězce | strukturovaná data, objekty, soubory/bloby |
| API | jednoduché | složitější |
| Operace | synchronní | asynchronní |
| Vhodné pro | malé hodnoty, nastavení | větší data, offline aplikace |
| Vyhledávání | podle klíče | podle klíčů a indexů |

---

## 8. Geolokace

**Geolocation API** umožňuje webové stránce získat polohu zařízení, typicky jako zeměpisnou šířku a délku. Používá se například pro mapy, navigaci, doporučení nejbližších poboček nebo lokální služby.

Základní použití:

```js
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(showPosition);
}

function showPosition(position) {
  console.log(position.coords.latitude);
  console.log(position.coords.longitude);
}
```

Důležité principy:

- uživatel musí přístup k poloze povolit,
- prohlížeč může přístup odmítnout nebo API nemusí být dostupné,
- poloha nemusí být dokonale přesná,
- práce s polohou je citlivá z hlediska soukromí,
- v moderních prohlížečích se geolokace běžně váže na bezpečný kontext, typicky HTTPS.

---

## 9. Mapy, YouTube a vložený externí obsah

### 9.1 Google Maps

Do webové stránky lze vložit mapu pomocí externího JavaScriptového API, například Google Maps API. Obvyklý postup je:

1. připravit HTML element, do kterého se mapa vloží,
2. načíst skript poskytovatele map,
3. inicializovat mapu v JavaScriptu,
4. nastavit střed mapy, přiblížení a typ mapy.

Typický příklad:

```html
<div id="map" style="width:400px;height:400px"></div>
<script>
function myMap() {
  const mapOptions = {
    center: new google.maps.LatLng(51.5, -0.12),
    zoom: 10,
    mapTypeId: google.maps.MapTypeId.HYBRID
  };
  const map = new google.maps.Map(document.getElementById('map'), mapOptions);
}
</script>
<script src="https://maps.googleapis.com/maps/api/js?callback=myMap"></script>
```

V praxi je pro produkční použití často potřeba API klíč a mohou platit kvóty nebo podmínky poskytovatele.

### 9.2 YouTube video

YouTube video lze jednoduše vložit pomocí `<iframe>`:

```html
<iframe
  width="420"
  height="345"
  src="https://www.youtube.com/embed/VIDEO_ID">
</iframe>
```

`<iframe>` vloží do stránky jiný dokument. V případě YouTube je tím dokumentem přehrávač videa. Pro pokročilejší práci, například ovládání přehrávání přes JavaScript, se používají specializovaná API nebo knihovny.

---

## 10. Další API a knihovny pro vizualizaci dat

Prezentace zmiňuje také **Trust Tokens**, dnes označované jako **Private State Token API**. Jde o experimentální technologii zaměřenou na přenos informace o důvěryhodnosti uživatele mezi kontexty bez přímého sdílení identity. Pro běžnou odpověď u státnic stačí vědět, že jde o modernější webové API řešící soukromí a boj proti zneužívání, nikoli o náhradu Canvas nebo Web Storage.

Pro vizualizaci dat se často používají knihovny:

- **D3.js** – velmi flexibilní knihovna pro datově řízené vizualizace,
- **Chart.js** – jednodušší knihovna pro běžné grafy,
- **amCharts** – komerčně zaměřená knihovna pro pokročilé grafy a dashboardy.

Důležité rozlišení: Canvas API je nízkoúrovňové kreslení. Knihovny pro vizualizaci dat nad tím staví vyšší abstrakci, takže vývojář místo ručního kreslení os, bodů a legend pracuje s daty a konfigurací grafu.

---

## 11. Krátké shrnutí

HTML 5 API je souhrnné označení pro rozhraní, která webovým aplikacím umožňují dělat věci dříve typické pro desktopové aplikace nebo pluginy. Canvas řeší programové kreslení, Web Storage a IndexedDB ukládání dat v prohlížeči, Geolocation API práci s polohou a další API umožňují integraci multimédií, map nebo bezpečnostních mechanismů. Klíčové je chápat, že HTML poskytuje strukturu, JavaScript volá API prohlížeče a CSS řeší vzhled. Díky tomu lze tvořit interaktivní, rychlé a částečně offline fungující webové aplikace.