## Element `p`
- odstavec textu
- prakticky veškerý text
- text = alespoň věta

## Element `a`
- slouží jako odkaz
- atributy:
	- `href`: URL destinace
	- `rel`: specifikace vztahu odkazu k aktuálnímu dokumentu
	- `target`: kde má být odkaz otevřen (nedoporučuje se používat)
	- `title`: popisek
```HTML
<p><a href="zapocty.xls" title="Tabulka zápočtů"> Přehled zápočtů (.xls)</a> z předmětu KMI/WEB.</p>
```
- webové vyhledávače provádějí sémantickou analýzu
```HTML
<!-- možnost vykonávat různé základní operace -->
<a href="tel:123456789" rel="nofollow">Zavolejte nám</a>
```

## Element `img`
- slouží pro vložení obrázků
- atributy:
	- `src` : URL obrázku (relativní/absolutní)
	- `alt`: popisek obrázku
	- `height`: výška obrázku
	- `width`: šířka obrázku
- velikost obrázku může ovlivnit rychlost stránky
- moderní formáty: WebP, JPEG, AVIF

## Nadpisy
- elementy `h1`, ..., `h6`
```HTML
<h1>nadpis první úrovně</h1>
<h6>nadpis šesté úrovně</h6>
```
- postupně klesající důležitost
- výpis nadpisů **musí** být postupný

## Podnadpisy
- dva nadpisy za sebou $\neq$ podnadpis
- element `hgroup` služí pro vytvoření podnadpisu
```HTML
<hgroup>
	<h1>nadpis</h1>
	<p>podnadpis</p>
</hgroup>
```
- `p` může být více

## Struktura stránky
![[MacBook-2024-04-28-001094.png]]
- Stránka je rozdělená na strukturální elementy
	- `main`, `header`, `nav`, `article`, `section`, `aside`, `footer`

### Element `main`
- definice hlavního obsahu v rámci `body`
- na stránce musí být pouze jeden element `main`
	- teoreticky může být více, ale jen jeden aktivní
- slouží pro vymezení hlavního obsahu
```HTML
<body>
	<main>
	...
	</main>
</body>
```

### Element `header`
- určení hlavičky
- nesouvisí s `head`
- jako hlavička celé stránky nebo jako hlavička jednotlivých částí
- nesmí obsahovat `header` ani `footer`
```HTML
<body>
	<header>
		<h1> Obsah Stopařova průvodce Galaxií</h1>
	</header>
	
	<main>
	...
	</main>
</body>
```

### Element `nav`
- určení hlavní navigace (ne všechny navigace musí být v tomto elementu)
- *seznam odkazů*
```HTML
<nav> 
	<ul>
	    <li><a href="#">Stopařův průvodce Galaxií</a></li>
	    <li><a href="#">Restaurace na konci vesmíru</a></li>
	    <li><a href="#">Život, vesmír a vůbec</a></li>
	    <li><a href="#">Sbohem a díky za ryby</a></li>
	    <li><a href="#">Převážně neškodná</a></li>
	</ul> 
</nav>
```

### Element `aside`
- vymezuje obsah, který souvisí s předchozím uvedeným elementem
- většinou obsahuje doplňující informace, zdroje, vedlejší navigaci,... (typicky ***sidebar***)
##### Sidebar
obsah `aside` souvisí s obsahem `main`:
```HTML
... 
<main>
  <h1>Douglas Adams</h1>
  ...
</main>

<!-- sidebar -->
<aside> 
	...
</aside> 
...
```

obsah `aside` souvisí s obsahem `p`:
```HTML
<main>
  <h1>Douglas Adams</h1>
  <p>... proslulý především knihou Stopařův průvodce Galaxií ...</p>

  <!-- obsah související s obsahem předchozího elementu (p) -->
  <aside>
    <h2>Stopařův průvodce Galaxií</h2>
    <p>...</p>
  </aside>
</main>
```

### Element `footer`
- analogie elementu `header`
- určení patičky

### Element `article`
- úplný, samostatný a nezávislý obsah
- musí obsahovat [[HTML struktura webové stránky#Nadpisy |nadpis]]
- může obsahovat další elementy `article` a může obsahovat element [[HTML struktura webové stránky#Element `header`|header]] a `footer`
- elementy `article` jdou zanořit - předpokládá se, že souvisí s rodičovským elementem
```HTML
<article>
	<header>
    <h1>Kniha Stopařův průvodce Galaxií</h1>
    <img src="pruvodce.jpg" alt="Obálka průvodce" width="200">
	</header>

	<p>Stopařův průvodce Galaxií, nebo též Stopařův průvodce po Galaxii, jejímž autorem je Angličan <a href="https://cs.wikipedia.org/wiki/Douglas_Adams" rel="external" title="více o Douglas Adamsovi">Douglas Adams</a>, je prvním dílem stejnojmenné pentalogie označované jako <em>trilogie v pěti dílech</em>.</p>
</article>
```

### Element `section`
- slouží pro seskupení částí stránky, které spolu významově souvisí
- musí obsahovat společný [[HTML struktura webové stránky#Nadpisy |nadpis]]
- `section` je možné zanořit do elementu `article` a naopak
	- zaměňování těchto dvou elementů bývá častým zdrojem chyb
```HTML
... 
<main>
  <h1>Poslední novinky</h1>
  <section>
    <h2>Z domova</h2>
    <ul>...</ul>
  </section>

  <section>
    <h2>Ze světa</h2>
    <ul>...</ul>
  </section>
</main>
...
```
> [!warning] 
>  Pokud v tomto kódu zaměníme `section` za `article` bude výsledek **sémanticky nesprávný**, jelikož by obsah `article` byl závislý na obsahu mimo něj (na elementu `h1`).
****

### Strukturální elementy a outline webu
- Strukturální elementy restartují outline webové stránky (kromě `main`) 
- Následující kód je sémanticky správně(`section` restartoval outline):
```HTML
<h1></h1>
<h2></h2>
<article>
	<h3></h3>
	<section>
		<h2></h2>
	</section>
</article>
```

### Vylepšení přístupnosti
- Správné používání elementu zvyšuje přístupnost webových stránek
- Lze vylepšit použitím standardu [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/html-aria/)
## Nesémantické HTML elementy
- používají se pro účely vizualizace (pomocí CSS)
- jejich použití nepřiřadí obsahu žádný význam
### Element `div`
```HTML
<div class="box centered">Lorem ipsum</div>
```

### Element `span`
```HTML
<p>Stopařův <span class="text-bold">průvodce</span></p>
```



##### Navigace
Předchozí:  [[Syntaxe a sémantika HTML a CSS]]
Následující: [[Box model]]
Celý okruh: [[2. Informační technologie]]