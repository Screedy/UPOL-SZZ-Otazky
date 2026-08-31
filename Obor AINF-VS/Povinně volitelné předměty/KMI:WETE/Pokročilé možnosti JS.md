## 1. Kontext: proč Web API existují

Moderní webové aplikace se postupně přibližují nativním aplikacím: mají pracovat offline, zpracovávat soubory, komunikovat v reálném čase, používat kameru nebo mikrofon, reagovat na vstupy uživatele a zvládat náročnější výpočty. Samotný jazyk JavaScript k tomu nestačí, proto prohlížeč nabízí **Web API** – rozhraní, která JavaScriptu zpřístupňují funkce prohlížeče, zařízení a síťové komunikace. MDN Web Docs Web API popisuje jako rozhraní používaná při vývoji webových aplikací a webů. ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API?utm_source=chatgpt.com "Web APIs - MDN Web Docs - Mozilla"))

Důležité je rozlišovat:

- **JavaScript** je programovací jazyk.
- **Web API** jsou rozhraní poskytovaná prostředím, typicky prohlížečem.
- **Browser API** umožňují pracovat například s historií, soubory, okny, událostmi, pracovními vlákny nebo síťovou komunikací.

Cílem těchto API je rozšířit možnosti webové aplikace tak, aby nemusela být jen statickou stránkou, ale mohla se chovat jako komplexní aplikace.

---

## 2. History API – historie prohlížeče

### Základní problém

U klasického webu odpovídá každá URL konkrétní stránce. Když uživatel klikne na odkaz, prohlížeč načte novou stránku a přidá ji do historie. Tlačítka **Zpět** a **Vpřed** pak přirozeně fungují.

U moderních aplikací, hlavně u **single-page aplikací** a AJAXových aplikací, se ale často mění pouze obsah stránky bez plného reloadu. To může způsobit, že URL zůstane stejná a historie prohlížeče neodpovídá tomu, co uživatel v aplikaci vidí.

### Starší řešení: `location.hash`

Jednodušší způsob reprezentace stavu stránky je použití fragmentu URL, například:

```js
location.hash = "#detail-produktu";
```

Na změnu lze reagovat pomocí:

```js
window.onhashchange = () => {
  console.log(location.hash);
};
```

Výhodou je jednoduchost. Nevýhodou je, že hash část URL je omezená a působí spíše jako nouzové řešení.

### Modernější řešení: `history.pushState()` a `history.replaceState()`

**History API** poskytuje přístup k historii relace prohlížeče a umožňuje manipulovat se zásobníkem historie.

Metoda `pushState()` přidá nový záznam do historie prohlížeče, zatímco `replaceState()` upraví aktuální záznam historie.

History API je důležité hlavně pro single-page aplikace. Umožňuje, aby URL, historie prohlížeče a aktuální stav aplikace dávaly smysl i bez klasického načítání nové stránky.

---

## 3. Cross-Origin Messaging – komunikace mezi okny

### Same-origin policy

Hlavní myšlenka - webové stránky jsou kvůli bezpečnosti izolované. Běžně platí pravidlo **same-origin policy**, podle kterého spolu mohou volně komunikovat jen dokumenty ze stejného původu, tedy stejného protokolu, domény a portu.

To je bezpečné, ale v praxi někdy potřebujeme komunikaci mezi:

- hlavní stránkou a vloženým `<iframe>`,
- stránkou a popup oknem…

### `window.postMessage()`

Metoda `window.postMessage()` umožňuje bezpečnou komunikaci mezi objekty `Window`, například mezi stránkou a iframe nebo popup oknem.

---

## 4. Server-Sent Events, SSE

### Základní myšlenka

U běžného HTTP modelu klient pošle požadavek a server odpoví. Pokud chce klient nová data, musí se znovu ptát. Tomu se říká **polling**.

**Server-Sent Events** umožňují, aby server posílal nová data klientovi sám (automatický update bez dotazu na server)

### `EventSource`

Na klientovi se používá rozhraní `EventSource`. Instance `EventSource` otevře trvalé spojení na HTTP server, který posílá události ve formátu `text/event-stream`.

```js
const source = new EventSource("/events");

source.onmessage = (event) => {
  console.log(event.data);
};
```

Na serveru musí odpověď používat MIME typ:

```http
Content-Type: text/event-stream
```

### Vlastnosti SSE

SSE je **jednosměrná komunikace**: data tečou ze serveru ke klientovi. Klient sice může dál posílat běžné HTTP požadavky, ale samotné SSE spojení není obousměrné jako WebSocket.

Typické použití:

- notifikace,
- živé logy,
- aktualizace dashboardu…

SSE se hodí tam, kde server potřebuje průběžně posílat aktualizace klientovi, ale klient nemusí ve stejném spojení posílat data zpět. Je jednodušší než WebSocket, ale méně univerzální.

---

## 5. Web Workers

### Problém: JavaScript a hlavní vlákno

JavaScript v prohlížeči tradičně běží na hlavním vlákně, kde se zároveň obsluhuje uživatelské rozhraní. Pokud spustíme výpočetně náročnou operaci, může se UI zaseknout.

Příklad problému:

```js
while (true) {
  // blokuje hlavní vlákno
}
```

Prohlížeč potom nemůže plynule překreslovat stránku ani reagovat na vstupy uživatele.

### Co je Web Worker

**Web Worker** umožňuje spustit JavaScript v samostatném vlákně na pozadí. Hlavní výhoda je, že náročný výpočet neblokuje uživatelské rozhraní.

### Omezení Workeru

Worker neběží ve stejném prostředí jako hlavní stránka. Nemá přístup k objektům `window` a `document`, takže nemůže přímo manipulovat s DOM. Komunikuje s hlavním vláknem pomocí zpráv.

### Příklad

Hlavní vlákno:

```js
const worker = new Worker("./worker.js");

worker.onmessage = (event) => {
  console.log("Výsledek:", event.data);
};

worker.postMessage([1, 2, 3, 4, 5]);
```

Worker:

```js
onmessage = (event) => {
  const sum = event.data.reduce((a, b) => a + b, 0);
  postMessage(sum);
};
```

### Shared Worker

**SharedWorker** je varianta workeru, kterou může sdílet více skriptů, například více oken stejné aplikace. Oproti běžnému workeru se komunikuje přes port.

---

## 6. Service Workers

### Co je Service Worker

**Service Worker** je speciální typ workeru, který funguje jako mezivrstva mezi webovou aplikací, prohlížečem a sítí. Na rozdíl od běžného Web Workeru není určen hlavně pro výpočty, ale pro řízení síťových požadavků a offline chování aplikace.

### K čemu se používá

Service Worker umožňuje:

- zachytávat síťové požadavky,
- ukládat odpovědi do cache,
- poskytovat offline režim,
- aktualizovat statické soubory aplikace,
- používat push notifikace,
- budovat Progressive Web Apps.

### HTTPS

Service Workers se z bezpečnostních důvodů používají v zabezpečeném kontextu, typicky přes HTTPS. Výjimkou bývá lokální vývoj na `localhost`.

### Životní cyklus

Zjednodušený cyklus:

1. **Registrace** – stránka zaregistruje service worker.
2. **Stažení** – prohlížeč stáhne skript service workeru.
3. **Instalace** – obvykle se připraví cache.
4. **Aktivace** – service worker začne řídit stránky.
5. **Aktualizace** – při změně souboru se instaluje nová verze.

### Příklad registrace

```js
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("/sw.js");
}
```

### Shrnutí k Service Workers

Service Worker je klíčová technologie pro PWA. Umožňuje, aby se webová aplikace chovala podobně jako nativní aplikace: fungovala offline, rychle se načítala a zvládala notifikace.

---

## 7. WebSocket

### Problém běžného HTTP

HTTP je založené na modelu request-response. Klient se ptá, server odpovídá. Pro real-time aplikace je to omezující, protože by klient musel server neustále dotazovat.

**WebSocket API** umožňuje otevřít obousměrnou interaktivní komunikační relaci mezi prohlížečem a serverem. Díky tomu může klient posílat zprávy serveru a server může posílat zprávy klientovi bez opakovaného pollingu

### Příklad

```js
const socket = new WebSocket("wss://example.com/socket");

socket.onopen = () => {
  socket.send("Ahoj servere");
};

socket.onmessage = (event) => {
  console.log("Zpráva ze serveru:", event.data);
};

socket.onclose = () => {
  console.log("Spojení ukončeno");
};

socket.onerror = (error) => {
  console.error("Chyba WebSocketu:", error);
};
```

### Kdy použít WebSocket

WebSocket se hodí pro:

- chat,
- multiplayer hry,
- real-time dashboardy,
- kolaborativní editory,
- burzovní nebo sportovní živá data.

---

## 8. WebRTC

### Co je WebRTC

**WebRTC** znamená Web Real-Time Communication. Umožňuje webovým aplikacím zachytávat a přenášet audio nebo video a také vyměňovat libovolná data mezi prohlížeči bez nutnosti instalovat pluginy.

Používá se například pro:

- videohovory,
- hlasovou komunikaci,
- sdílení obrazovky,
- peer-to-peer přenos dat,
- některé real-time aplikace.
- Např. Messenger, Whatsapp a další

### Proč je WebRTC složité

Tohle řešení je poměrně složité. V praxi nestačí jen spojit dva prohlížeče. Je potřeba vyřešit:

- signalizaci,
- oprávnění ke kameře a mikrofonu,
- šifrovaný přenos…

### Shrnutí k WebRTC

WebRTC je silná technologie pro real-time komunikaci mezi uživateli. Je ale složitější než WebSocket nebo SSE, protože řeší přímou komunikaci mezi zařízeními, média, síťové překážky a bezpečnost.

---

## 9. HTML File API

### Co řeší File API

**File API** umožňuje webovým aplikacím přistupovat k souborům, které uživatel aplikaci výslovně poskytne. Typicky přes `<input type="file">` nebo drag-and-drop.

Důležité je, že webová stránka nemá libovolný přístup k disku uživatele. Pracuje jen se soubory, které uživatel vybral nebo přetáhl do aplikace.

### Typické použití

File API se používá pro:

- náhled obrázku před uploadem,
- AJAX upload bez reloadu stránky,
- validaci souboru před odesláním,
- čtení textových nebo binárních souborů,
- drag-and-drop upload.

File API posouvá webové aplikace směrem k nativním aplikacím, protože umožňuje pracovat se soubory přímo v prohlížeči. Přístup je ale bezpečnostně omezený na soubory vybrané uživatelem.

---

## 10. Pointer Lock API

### Co je Pointer Lock

**Pointer Lock API** umožňuje zamknout kurzor myši k určitému prvku a pracovat s relativním pohybem myši místo absolutní pozice kurzoru (nejsme limitování prohlížečem nebo obrazovkou).

### Proč je to užitečné

Bez Pointer Lock API se kurzor zastaví na okraji okna nebo obrazovky. To je problém například u 3D hry z pohledu první osoby, kde uživatel potřebuje plynule otáčet kamerou libovolně dlouho jedním směrem.Typické použití

Pointer Lock API se používá hlavně pro:

- 3D hry,
- first-person ovládání,
- 3D modelovací nástroje,
- aplikace vyžadující neomezený pohyb myši.