

### Dědičnost

- klíčoví pojem
- pokud nastavíme elementu vlastnost na konkrétní hodnotu, přejímají to i potomci tohoto elementu
- např. nastavení barvy textu v nadřazeném elementem na zelenou tak i jeho potomci pokud neřeknou jinak budou mít barvu zelenou
- ne všechny vlastnosti se dědí
- pokud vlastnosti dáme hodnotu `inherit` = hodnotu rodiče
- pokud vlastnosti dáme hodnotu `initial` = defaultní hodnota prohlížeče
- vlastnost `all` řídí dědičnost všech vlastností a to i v potomku

### Kaskáda

- jak víme můžeme jednotlivé elementy mohou být vybrány různými selektory
```html
<article id="article">
	<h2 class="title"></h2>
</article> 
```
```css
h2 { color: red; }
article h2 { color: green; }
.title { color: blue; }
#article h2 { color: gold; }
```
- pokud v deklaracích budou vlastnosti stejné bude docházet ke kolizím CSS pravidel.
- tento problém řeší *princip kaskády*
	1. při kolizi se rozhoduje *specifičnost*, přesně řečeno hodnota uvedena v pravidle s více specifickým selektorem má přednost před méně specifickým
	2. při kolizi se shodnou specifičností rozhoduje *pořadí*, přesněji hodnota která byla uvedena později

#### Specifičnost

- specifičnost CSS selektoru vypovídá o jeho konkrétnosti.
- málo specifický vybírá více elementů než více specifický
- specifičnost reprezentovaná ve tvaru: `a b c`
	- `a` - počet id selektorů
	- `b` - počet class selektorů a pseudo-tříd v selektoru
	- `c` - počet elementů a pseudo-elementů
- `a` největší `c` nejmenší specifičnost
- v předchozím případě by byl `h2` modrý
- inline CSS má specifickou specifičnost `1 0 0 0`
- komplikace dědičnost - vždy nastavena hodnota má přednost před specifičností

#### Pořadí

- pokud CSS pravidla mají stejnou specifičnost, rozhoduje o nastavení vlastnosti pořadí pravidel ve kterém je tato vlastnost uvedena.
- rozhoduje i na úrovni deklaračního bloku

```css
.secound { 
	color: red;
	color: blue;
}
```

- tento kód nastaví modrou barvu html elementu pojmenovaný class secound

#### Důležitost

- pravidla kaskády jsou obejít pomocí *důležitosti*
- *důležitá* hodnota má přednost především
- uvádíme `!important`
- jakoby specifičnost byla `1 0 0 0 0`
- pokud více hodnot uvedeno `!important` -> pravidlo kaskády
```css
.title { 
	color: gold !important;
}
```
- nepoužívat!


### Celí proces

1. Pokud není hodnota nastavena, je použita výchozí hodnota definovaná webovým prohlížečem. 
2. Pokud je hodnota zděděna, přepisuje hodnotu nastavenou v bodu 1. 
3. Pokud je hodnota explicitně nastavena, přepisuje hodnotu nastavenou v bodech 1 a 2. 
4. Pokud dochází ke kolizi, rozhoduje kaskáda. 
5. Pokud je hodnota nastavena v inline CSS, přepisuje hodnotu nastavenou v bodech 1–4.  
6. Pokud je hodnotě nastavena důležitost, přepisuje hodnotu nastavenou v bodech 1–5. 
7. Pokud uživatel použije vlastní hodnotu (vlastní sadu stylů), přepisuje tato hodnota hodnotu nastavenou v bodech 1–6. 




##### Navigace
Předchozí:  [[Box model]]
Následující: [[Základy správného psaní CSS kódu - typické chyby a metodiky]]
Celý okruh: [[2. Informační technologie]]