- React je knihovna pro tvorbu uživatelských rozhraní vyvinutá společností Facebook. 
- Jeho hlavním účelem je **usnadnění vývoje webových aplikací**, zejména těch, které **vyžadují** časté **aktualizace dat** a **interakci s uživatelem**. 

## Charakteristika
1. **Komponenty**: React je založen na konceptu komponent, což jsou samostatné, znovupoužitelné části uživatelského rozhraní. Každá komponenta může mít vlastní stav a metody.
2. **Virtuální DOM**: React používá virtuální DOM k optimalizaci výkonu. 
	- Namísto toho, aby přímo manipuloval s reálným DOM (Document Object Model), React pracuje **s jeho virtuální reprezentací** (**Shadow DOM**), což umožňuje **efektivnější aktualizace** a minimalizaci re-rendering.
3. **Jednosměrný tok dat**: Data v React aplikacích obvykle cirkulují jedním směrem - od nadřazených komponent k dceřiným komponentám. To zlepšuje předvídatelnost a spravovatelnost aplikace.
4. **Declarative syntax**: Syntaxe Reactu je deklarativní, což znamená, že se zaměřuje na popis toho, jak by měl vypadat výsledný stav aplikace, namísto toho, jak ho dosáhnout.
5. **Životní cyklus komponent**: Každá komponenta v Reactu prochází určitými fázemi životního cyklu, jako je inicializace, aktualizace a odstranění. Toto umožňuje programátorům připojit k těmto událostem vlastní logiku.
6. **JSX**: JSX je syntaxe pro psaní HTML podobných struktur přímo v JavaScriptu. Tato kombinace HTML a JavaScriptu umožňuje vytvářet komponenty s přehlednějším kódem.

## Použití
- React je často využíván pro vývoj moderních webových aplikací a jednostránkových aplikací (Single Page Applications - SPA). 
- Je populární pro tvorbu uživatelsky přívětivých, interaktivních a rychlých webových rozhraní. 
- Jeho ekosystém zahrnuje také mnoho doplňků a knihoven, které zjednodušují práci s ním, jako například React Router pro routování, Redux pro správu stavu aplikace nebo Styled Components pro stylování komponent pomocí CSS v JavaScriptu.

>[!Example]- JSX vs nízkoúrovňový přístup
>**nízkoúrovňový přístup**
>```JavaScript
>import React, { useState } from 'react';
>
>function createElement(type, props, ...children) {
>  return {
>    type,
>    props: {
>      ...props,
>      children: children.map(child =>
>        typeof child === "object" ? child : createTextElement(child)
>      ),
>    },
>  };
>}
>
>function createTextElement(text) {
>  return {
>    type: "TEXT_ELEMENT",
>    props: {
>      nodeValue: text,
>      children: [],
>    },
>  };
>}
>
>function render(element, container) {
>  const dom =
>    element.type === "TEXT_ELEMENT"
>      ? document.createTextNode("")
>      : document.createElement(element.type);
>
>  const isListener = name => name.startsWith("on");
>  Object.keys(element.props)
>    .filter(isListener)
>    .forEach(name => {
>      const eventType = name.toLowerCase().substring(2);
>      dom.addEventListener(eventType, element.props[name]);
>    });
>
>  const isAttribute = name => !isListener(name) && name !== "children";
>  Object.keys(element.props)
>    .filter(isAttribute)
>    .forEach(name => {
>      dom[name] = element.props[name];
>    });
>
>  element.props.children.forEach(child => render(child, dom));
>  container.appendChild(dom);
>}
>
>function App() {
>  const [items, setItems] = useState([]);
>  const [text, setText] = useState('');
>
>  const addItem = () => {
>    setItems([...items, text]);
>    setText('');
>  };
>
>  return createElement('div', null,
>    createElement('h1', null, 'Seznam položek'),
>    createElement('ul', null,
>      items.map((item, index) => (
>        createElement('li', { key: index }, item)
>      ))
>    ),
>    createElement('input', {
>      type: 'text',
>      value: text,
>      onChange: (e) => setText(e.target.value),
>      placeholder: 'Nová položka'
>    }),
>    createElement('button', { onClick: addItem }, 'Přidat')
>  );
>}
>
>export default App;
>```
>
>**JSX**
>```JavaScript
>import React, { useState } from 'react';
>
>function App() {
>  // Stav pro uchování seznamu položek
>  const [items, setItems] = useState([]);
>  // Stav pro uchování aktuální hodnoty formuláře
>  const [text, setText] = useState('');
>
>  // Funkce pro přidání nové položky do seznamu
>  const addItem = () => {
>    setItems([...items, text]);
>    setText(''); // Vymazání textového pole po přidání
>  };
>
>  return (
>    <div>
>      <h1>Seznam položek</h1>
>      <ul>
>        {/* Mapování seznamu položek na <li> elementy */}
>        {items.map((item, index) => (
>          <li key={index}>{item}</li>
>        ))}
>      </ul>
>      {/* Formulář pro přidání nové položky */}
>      <input
>        type="text"
>        value={text}
>        onChange={(e) => setText(e.target.value)}
>        placeholder="Nová položka"
>      />
>      <button onClick={addItem}>Přidat</button>
>    </div>
>  );
>}
>
>export default App;
>```

## React Hooky
- Doposud měli možnost mít stav pouze objektové komponenty. 
- React hooks byly představeny v zatím poslední verzi knihovny React a umožňují vytvářet funkční komponenty s vnitřním stavem. 
- Tímto objektové komponenty ztrácejí smysl (ve skutečnosti jsou v knihovně postupně utlačovány, jejich odstranění se ale zatím neplánuje).

### useState
>[!Example] Hook `useState`
>```JavaScript
>// načtení hooku
>import React, { useState } from 'react';
>// funkční komponenta
>function Example() { 
>	const [count, setCount] = useState(0);
>	
>	return (
>		<div>
>			<p>You clicked {count} times</p>
>			<button onClick={() => setCount(count+1)}>Click me</button>
>		</div>
>	);
>	}
>	export default Example;
>```

### useEffect
>[!Example] Hook `useEffect`
>- umožňuje provádět vedlejší efekt (například načtení dat, výpis do konzole, změna DOM a další).
>- useEffect je spuštěn při každém renderování (tedy i při prvním).
>```JavaScript
>// načtení hooku
>import React, { useState, useEffect } from 'react';
>// funkční komponenta
>function Example() { 
>	const [count, setCount] = useState(0);
>
>	useEffect(() => { console.log (`You clicked ${count} times`); });  >//rozšíření předchozího
>	
>	return (
>		<div>
>			<p>You clicked {count} times</p>
>			<button onClick={() => setCount(count+1)}>Click me</button>
>		</div>
>	);
>	}
>	export default Example;
>```
>- Pomocí tohoto hooku lze i získávat data:
>```JavaScript
>export function GitUser({login}) {
>// destukturalizace props
>const [data, setData] = useState();
>useEffect(() => {
>	if(!login) return;
>	fetch(`https://api.github.com/users/${login}`)
>		.then(r => r.json())
>		.then(setData)
>		.catch(console.error);
>	 }, [login]); // [] je dependeci array (kdy má být hook spušten), pokud je >[] tak jen na začátku
>	 
>	 if(!data) return loading...;
>	 
>	 if(data) { return {JSON.stringify(data, null, 2)}
>	 }
>} // poznámka: vyzkoušet lze například
>```


### useContext

>[!Example] hook `useContext`
>- Dalším užitečným hookem je useContext, který umožňuje vytvářet globální stav. To je poněkud nepřesné označení, jelikož React komponenty jsou uspořádány ve stromu a jednotlivé vlastnosti mohou být přejímány od rodičů v tomto stromu (pokud je uvedeno). 
>-  useContext umožňuje vytvářet props, které jsou sdíleny v daném podstromu.
>```JavaScript
>import React, { useState, useEffect, useContext } from 'react';
>
>const themes = { 
>light: { foreground: "#000000", background: "#eeeeee" }, 
>dark: { foreground: "#ffffff", background: "#222222" } };
>
>const ThemeContext = React.createContext(themes.light);
>```
>
>```JavaScript
>function Example() { 
>return (
>	<ThemeContext.Provider value={themes.dark}>
>	<Toolbar />
>	</ThemeContext.Provider>
>); 
>} 
>
>function Toolbar(props) {
>	return (
>		<div>
>		<ThemedButton />
>		</div>
>	); 
>} 
>
>function ThemedButton() {
>	const theme = useContext(ThemeContext);
>	return (
>		<button style={{ background: theme.background, color: theme.foreground >}}>
>		Text tlacitka
>		</button>
>	);
>} 
>
>export default Example;
>```

### Další hooky

- Za zmínku ještě stojí `useReducer` hook, který z aktuálního stavu vytváří stav nový. Například přepínání `true` a `false`, které je ukázáno níže.
`const [checked, toggle] = useReducer(checked => !checked, false);`

- Užitečný hook je také `useMemo`, který umožňuje zapamatovat při renderování vypočítané hodnoty. Ty následně nemusí být opět přepočítávány (pouze pokud dojde ke změně hodnot, ze který byly vypočítány). Tento hook slouží **pro optimalizaci výkonu**.
- Hooky je možné volat pouze na top-level úrovni. Nesmí být v cyklech a podmínkách (můžou je ale obsahovat). Hook by měl být volán pouze uvnitř komponenty. ESlint v create-react-app tato pravidla hlídá.
- Kromě vestavěných hooks je možné vytvářet vlastní.

##### Navigace
Předchozí:  [[Technologie AJAX a její použití]]
Následující: [[Možnosti tvorby nativních aplikací pomocí webových technologií]]
Celý okruh: [[3. Programovací jazyky a programování]]