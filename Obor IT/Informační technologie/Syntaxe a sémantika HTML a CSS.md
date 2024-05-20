## HTML (HyperText Markup Language)
- značkovací jazyk
- slouží pro definici **významu** (**sémantiky**) **obsahu** webové stránky
- nejzákladnější webová technologie

### Syntaxe HTML
- HTML používá značky (tags), které jsou uzavřeny ve špičatých závorkách `< >`
#### Elementy
- HTML element se skládá z **otevírací** značky, **obsahu** a **zavírací** značky. 
- Elementy mohou **obsahovat další elementy** (dětské elementy), **text** nebo mohou být **prázdné**.
	```HTML
	<p id="prvniOdstavec" class="text">Toto je odstavec textu.</p>
	```
- **Typy HTML Elementů**:
	1. **Párové elementy**: Tyto elementy mají **otevírací a zavírací značk**u. Většina HTML elementů je párových, například `<div>`, `<h1>`, `<table>`, `<a>` atd.
	2. **Samozavírací elementy**: Některé HTML elementy nevyžadují zavírací značku a jsou "samozavírací". Tyto elementy často vkládají média nebo vytvářejí vstupy do formulářů. Příklady zahrnují `<img>`, `<input>`, `<br>`, a `<hr>`.

#### Atributy
- skládají se z názvu a hodnoty, které jsou spojeny rovnítkem
- hodnota atributu by měla být vždy **obalena uvozovkami**
	```HTML
	<a href="https://www.example.com">Navštivte naši stránku</a>
	```
- `<a>` je HTML element (odkaz) a `href` je atribut, který definuje cíl odkazu, v tomto případě URL [https://www.example.com](https://www.example.com/)
- běžné atributy: `id`, `class`, `style`, `title`, `src`, `alt`, `href`

#### Komentáře
```HTML
<!-- příklad komentáře -->

<h2> Má smysl žít? </h2>

<!--
příklad komentáře
přes
více řádků
-->
```

#### Zanořování elementů
- vytváří **vztah potomek-rodič**
- značky musí být uzavírány **v pořadí LIFO**
```HTML
<p> ... <em>trilogie v pěti dílech</em> ... </p>
```
- elementy vytvářejí hierarchickou strukturu potomek-rodič
  ![[MacBook-2024-04-28-001093.png| 300]]

## Význam (sémantika) HTML
- sémantické HTML používá **sémantické značky**, které poskytují **smysluplnou strukturu** obsahu
- používání sémantických elementů umožňuje **vývojářům, prohlížečům a vyhledávačům** lépe pochopit, **jaké informace stránka obsahuje** a jak jsou tyto informace organizovány
>[!Example] Příklad sémantiky
>```HTML
>	<h1>Stopařův průvodce Galaxií</h1>
>	<p>Kniha Stopařův průvodce Galaxií je ...</p>
>```
>>[!missing] Příklad **bez** sémantiky
>>```HTML
>>	<span>Stopařův průvodce Galaxií</span>
>>	<span>Kniha Stopařův průvodce Galaxií je ...</span>
>>```
- ověřit sémantickou správnost **není možné**
- **syntaktická správnost** (validita) ale **jde**:
	- ověřuje se **vůči standardu**
	- automatické nástroje - **validátory**
	- HTML kód by **měl být vždy validní**

## CSS (Cascading Style Sheets)
- HTML elementy mají výchozí vizualizaci, CSS umožňuje změnu této vizualizace
- je to obecný princip oddělení obsahu od prezentace
- CSS pravidla jsou tvořena selektory a deklaracemi

### Syntaxe CSS
-   Příklad pravidla:
	```CSS
	selektor {
	    vlastnost: hodnota;
	    vlastnost2: hodnota2;
	}
	```
- **Selektor** určuje HTML elementy, na které se dané styly aplikují.
- **Vlastnost** je specifický styl, který chceme upravit, například barva písma nebo pozadí.
- **Hodnota** definuje nastavení dané vlastnosti.
- Konkrétní příklad:
	```CSS
	p {
	    color: red;
	    font-size: 16px;
	}
	```

#### Základní selektory
- Název elementu:
	```CSS
	h1 {color: gold;}
	```

- Pojmenování elementů:
	```CSS
	/* elementy které mají class="title" */
	.title {color: gold;}
	
	/* elementy em které mají class="title" */
	em.title {color: gold;}
	```

- v případě `id` bychom použili `#` namísto `.`:
	```CSS
	#title {color: gold;}
	```

- musí být přímý potomek:
	```CSS
	article > p {color: gold;}
	```
- `<p> ... </p>` musí být přímý potomek `<article>`

#### Pseudo-element a preudo-třída
- **pseudo-element** = část stránky, která není určena žádným elementem, ale chová se k ní jako k elementu:
	```CSS
	/* pseudo-element, výběr prvního řádku elementu p */
	p::first-line {color: red;}
	```
- **pseudo-třída** = elementy identifikované na základě jejich pozice v HTML nebo vlastnosti:
	```CSS
	/* pseudo-třída, výběr prvního potomka elementu p */
	p::first-child {color: red;}
	```

#### Výběr dle stavu
```css
a:link {...}
a:visited {...}
a:focus {...}
a:hover {...}
a:active {...}
```
- některé lze použít i na jiné elementy než a
- pořadí důležité $\rightarrow$ kombinace stavů

## Propojení HTML a CSS
1. externí CSS soubor s příponou .css:
	```HTML
	<head>
		<link rel="stylesheet" href="main.css">
	</head>
	```
2. vnořené CSS, element style:
	```HTML
	<style>
		h1 {color: gold;}
	</style>
	```
3. inline CSS:
	```HTML
	<h1 style="color: gold;">
	```




##### Navigace
Předchozí:  [[Architektura webové stránky]]
Následující: [[HTML struktura webové stránky]]
Celý okruh: [[2. Informační technologie]]