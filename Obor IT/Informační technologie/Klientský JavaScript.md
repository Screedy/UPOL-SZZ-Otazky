- Programovací jazyk, který umožňuje skriptování na straně klienta 
- Kód (skript) je vykonáván webovým prohlížečem = **Klientský JavaScript**
- Klientský JS je základním nástrojem pro vytváření **interaktivních** webových stránek
- JavaScript je konkrétní implementací standardu **ECMAscript**
- Webové prohlížeče tento standard implementují
- Běžně se používá pro dynamické změny obsahu, interaktivitu, validaci formulářů, cookies,...
- Umí řídit vzhled a obsah webové stránky tím, že umožňuje manipulaci s HTML a CSS na stránce

## Začlenění JS do webové stránky
- Je vložen do HTML pomocí `<script>` tagu
- Většinou vložen do elementu `head`, může být i v elementu `body`
- Jeho pozice má vliv na vykonávání skriptu

```HTML
<!-- vložení externího souboru s příponou .js -->
<script src="script.js"></script>

<!-- vložení JavaScript kódu do HTML -->
<script>
	<!-- vypíše zprávu do konzole prohlížeče - používá se při testování -->
	console.log('Hello, world!');
</script>
```

## Manipulace s webovou stránkou (DOM)
- Webová stránka je dostupná přes object `document`, který je v prohlížeči reprezentován jako Document Object Model (DOM)
- DOM je programové rozhraní pro HTML
- Umožňuje programům změnit strukturu (HTML obsah), styl (CSS) a obsah dokumentů dynamicky
- JavaScript přistupuje k elementům pomocí metod jako `getElementById()`, `getElementsByClassName()`, `querySelector()`, a `querySelectorAll()`

```JS
// změní text elementu s ID 'demo' na "Toto je nový text!"
document.getElementById('demo').textContent = 'Toto je nový text!';
```

## Výběr elementů v DOM
- JavaScript poskytuje metody pro výběr a manipulaci s HTML elementy, což je základ pro interakci s uživatelským rozhraním

```JS
var myElement = document.querySelector('.myClass');
var allParagraphs = document.querySelectorAll('p');
```

- *`querySelector` vrátí první element odpovídající CSS selektoru*
- *`querySelectorAll` vrátí NodeList všech odpovídajících elementů*

```JS
// vytvoříme nový element li
var newElement = document.createElement("li");

// vytvoříme nový uzel DOM, který bude obsahovat text
var newTextNode = document.createTextNode("D");

// uzel obsahující text nastavíme jako potomka elementu
newElement.appendChild(newTextNode);
```
#### Vlastnosti elementů
- vlastnosti je možné číst a nastavovat
```JS
// nastavení vlastnosti color
newElement.style.color = "gold";

// přidání třídy k elementu
newElement.classList.add("list__item")
```

## Události
- JavaScript reaguje na uživatelské akce (kliky, pohyb myši, stisky kláves) pomocí event listeners
- Běžné události: `click`, `mouseover`, `keydown`, `load`

```JS
button.addEventListener('click', function() { 
	alert('Bylo kliknuto na tlačítko!'); 
});
```

## Časovače
- Umožňuje spustit kód po určitém intervalu 
- Jednou nebo opakovaně

```JS
// periodické opakování
var timer = setInterval(function(){console.log("čas vypršel");}, 3000);

// zastavení opakování
clearInterval(timer);

// jedno opakování
setTimeout(function(){console.log("čas vypršel");}, 3000);
```


> [!note] Frameworky a knihovny
>  - Při tvorbě stránek se běžně používají různé JavaScriptové knihovny
>  - Přinášejí výrazně jednodušší práci s DOM a také mnoho užitečné funkcionality
>  - jQuery, React, Angular, a Vue.js

##### Navigace
Předchozí:  [[Analýza kvality webové stránky]]
Následující: [[Systém - struktura, okolí, hranice, vstup a výstup, vlastnosti a klasifikace systémů]]
Celý okruh: [[2. Informační technologie]]