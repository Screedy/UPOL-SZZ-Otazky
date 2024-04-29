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
![[MacBook-2024-04-28-001094@2x.png]]
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
```HTML

```