- Node.js je open-source, cross-platform JavaScript runtime environment, který umožňuje vývojářům psát serverovou stranu aplikací v JavaScriptu.

## Charakteristiky
1. **Asynchronní a událostmi řízené programování:** 
	- Node.js je navržen tak, aby byl **efektivní pro I/O**-vysoce **náročné aplikace**. 
	- Jeho asynchronní model **umožňuje obsluhovat mnoho požadavků současně**, což je důležité pro webové aplikace s vysokou odezvou.
2. **JavaScript na serveru:** 
	- Node.js umožňuje vývojářům psát serverovou stranu aplikací v JavaScriptu. 
	- To usnadňuje synchronizaci kódu mezi klientem a serverem.
3. **Modulární architektura:** 
	- Node.js podporuje moduly, což umožňuje vývojářům snadno rozšiřovat a znovupoužívat kód pomocí balíčků dostupných v Node.js balíčkovacím manažeru npm (Node Package Manager).
4. **Výkon:** 
	- Díky použití enginu V8 od společnosti Google je Node.js známý pro svůj vysoký výkon a rychlost.

## Použití
1. **Webové aplikace:** Node.js se často používá pro vytváření webových serverů a backendových aplikací, které mají asynchronní a vysoké požadavky na I/O.
2. **API server:** Node.js je ideální pro vytváření API serverů, které poskytují rozhraní pro komunikaci mezi klientem a serverem.
3. **Real-time aplikace:** Díky své schopnosti manipulovat s asynchronními událostmi je Node.js vhodný pro vytváření real-time aplikací, jako jsou chatovací aplikace, online hry a streamování dat.
4. **Nástroje pro vývojáře:** Node.js lze také použít pro vytváření nástrojů pro vývojáře, jako jsou build systémy, testovací nástroje a další.
5. **IoT (Internet of Things):** Node.js je vhodný pro vytváření aplikací pro IoT zařízení, protože umožňuje snadnou komunikaci s různými zařízeními pomocí protokolů jako MQTT nebo HTTP.

>[!Example] Příklad kódu Node.js serveru
>```javascript
>// Importování potřebných modulů
>const http = require('http');
>
>// Definování handleru, který zpracuje příchozí požadavky
>const requestHandler = (request, response) => {
>  console.log(`Přijatý požadavek z ${request.url}`);
>  
>  // Odpověď na různé URL adresy
>  if (request.url === '/') {
>    response.end('Hello, world!');
>  } else if (request.url === '/about') {
>    response.end('About page');
>  } else {
>    response.end('404 Not Found');
>  }
>};
>
>// Vytvoření serveru pomocí modulu http
>const server = http.createServer(requestHandler);
>
>// Server bude naslouchat na portu 3000
>const port = 3000;
>
>// Spuštění serveru a zpráva o spuštění
>server.listen(port, (err) => {
>  if (err) {
>    return console.log('Nastala chyba při spouštění serveru:', err);
>  }
>
>  console.log(`Server běží na http://localhost:${port}/`);
>});
>```

##### Navigace
Předchozí:  [[Možnosti tvorby nativních aplikací pomocí webových technologií]]
Následující:
Celý okruh: [[3. Programovací jazyky a programování]]