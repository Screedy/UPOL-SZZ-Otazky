

- možnosti jak lze měnit umístění elementů na stránce

### Grid

- zavádí dvoudimenzionální mřížku (grid), do které je možné rozmisťovat prvky.

**Obrázek ukazující základní pojmy**
![[grid-pojmy.png]]

- *grid kontejner* - element obsahující mřížku
- *čáry* - vymezují *buňky* a *oblasti* (seskupení buněk)
- *řádky* a *sloupce* - řádek/sloupec buněk
- *hlavní osa* - osa x
- *příčná osa* - osa y

 - osy určují jakým způsobem budou prvky v mřížce zarovnány.
 - čáry nejsou zobrazeny pouze vymezují oblasti do kterých jdou umístit elementy
 - při inicializaci gridu je první potřeba nastavit `display: grid` následně vytvořit mřížku následně rozmístit elementy

**HTML pro příklady**
```HTML
<div class="grid">
	<div clas="grid__item">A</div>
	<div clas="grid__item">B</div>
	<div clas="grid__item">C</div>
	<div clas="grid__item">D</div>
</div>
```
#### Vytvoření mřížky

**Ukázka vytvoření gridu**
```CSS
.grid {
	display: grid; 
	/*nastavení třech řádků*/
	grid-template-rows: 100px 300px 100px; 
	/*nastavení tžech sloupců*/
	grid-template-columns: 200px 400px 200px;
}
```
**Obrázek mřížky pro přechozí kód**
![[grid-prvni.png]]
 - *index čáry* - pří vytvoření mřížky
#### Index čáry

![[index-cary.png]]

 - čáry jsou indexované vzestupně zleva doprava na hlavní ose a na příčné z hora dolů
 - současně zprava doleva od -1 do -n a na příčné zdola nahoru
 - možnost čáry pojmenovat
```CSS
.grid { 
	grid-template-rows: [header-start] 100px [content-start] 300px [footer-start] 100px; 
	grid-template-columns: 200px 400px 200px [col-3-end]; 
}
```
- možnost přidání více jmen do hranatých závorek pro jednu čáru

#### Index sloupce a řádku

- stejně jako indexovány čáry

#### Jednotka *fr*

- náhrada pixelů
- přizpůsobuje se různým zobrazovacím zařízením
- určuje poměrnou část nespecifikovaného místa
**Příklady**
```CSS
/* prostřední sloupec bude pružný */ 
grid-template-columns: 200px 1fr 200px; 

/* všechny sloupce budou pružné a zabírat stejné místo */
grid-template-columns: 1fr 1fr 1fr; 

/* všechny sloupce budou pružné, 
	prostřední zabírá 2x více místa než první a poslední 
		sloupec */ 
grid-template-columns: 1fr 2fr 1fr;
```

#### Automatické generování mřížky

- možné generovat automaticky pomocí funkce `repeat()`
**Příklady**
```CSS
/* 12 stejných sloupců */ 
grid-template-columns: repeat(12, 1fr);

/* 12 sloupců, první a poslední je 2x vetší*/
grid-template-columns: 2fr repeat(10, 1fr) 2fr;

/* 12 sloupců, opakuje se vzor 1fr 2fr, 8 tedy 1fr 2fr 1fr 2fr ... */
grid-template-columns: repeat(6, 1fr 2fr);

/* 12 stejných sloupců, každý se bude jmenovat column */ 
grid-template-columns: repeat(12, [column] 1fr);
```

- pří automatickém generování můžeme nechat prohlížeč rozhodnout. kolikrát má daný vzor opakovat, 
	- nelze použít s jednotkou `fr, min-content, max-content`
	- možné použít funkci `minmax()`

##### Auto-fill

- je vzor zopakovaný tolikrát, kolikrát to umožní daný prostor, přičemž je preferováno vložení nové buňky před zvětšením
```CSS
.grid { 
	display: grid; 
	width: 800px; 
	grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); 
}
```
![[auto-fill.png]]
##### Auto-fit

- je vzor zopakovaný tolikrát, kolikrát to umožní daný prostor, přičemž je preferováno zvětšení buňky před vložením nové
```CSS
.grid { 
	display: grid;
	width: 800px; 
	grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); 
}
```
![[auto-fit.png]]

#### Pojmenovávání oblastí

- pomocí `grid-template-areas`
```CSS
.grid { 
	grid-template-rows: 100px 300px 100px; 
	grid-template-columns: 200px 400px 200px; 
	grid-template-areas: 
		"header header header" 
		"left main right" 
		"footer footer footer"; 
	}
```
![[pojmenovávání__oblastí.png]]

#### Umístění elementů do mřížky

- po vytvoření můžeme umisťovat jednotlivé elementy

**Rozšíření HTML**
```HTML
<div class="grid">
	<div clas="grid__item grid__item--A">A</div>
	<div clas="grid__item grid__item--B">B</div>
	<div clas="grid__item grid__item--C">C</div>
	<div clas="grid__item grid__item--D">D</div>
</div>
```


- elementy umístíme tak že určíme čáry, které vymezují oblast do které chceme element umístit
	- `grid-row-start, grid-row-end, grid-column-start a grid-column-end`
	- zkrácená `grid-row, grid-column`
```CSS
/* zkrácená forma */ 
grid-column: x / y; 

/* nezkrácená forma */ 
grid-column-start: x; 
grid-column-end: y;
```
- možnost umístit do konkrétního řádku nebo sloupce
	- `grid-row, grid-column`
```CSS
/* umístění do sloupce x */
grid-column: x;
```

**Příklad**
```CSS
.grid__item--A { 
	grid-row-start: header-start; 
	grid-row-end: 2; 
	grid-column-start: 1; 
	grid-column-end: -1; /* lze i 4 */ 
} 
/* zkrácený zápis, pojmenování */ 
.grid__item--B { 
	grid-row: content-start / 3; 
	grid-column: 2 / 3; 
} 
/* zkrácený zápis, indexy sloupců a řádků */ 
.grid__item--C { 
	grid-row: 2; 
	grid-column: 3 
} 
/* zkrácený zápis, reverzní indexování */ 
.grid__item--D { 
	grid-row: 3 / -1; 
	grid-column: 1 / -1; 
}
```
*Výsledek:*
![[příklad__umistění--grid.png]]

- možnost také umístit do pojmenované oblasti (grid-template-area) pokud ji máme pojmenovanou
	- `grid-area`
```CSS
.grid__item--A {
	grid-area: header;
} 
.grid__item--B {
	grid-area: main;
}
...
```
- `grid-area` - možnost také použít na indexy čar
```CSS
/* row-star / column-start / row-end / column-end */ 
.grid__item--A {grid-area: 1 / 1 / 2 / -1;} 
.grid__item--B {grid-area: 2 / 2 / 3 / 3;}
...
```
- možnost určit jen začínající čáru a počet buněk
	- pomocí `span`
```CSS
/* usnadnění pomocí span = kolik má zabírat řádků/sloupců */ 
.grid__item--A { 
	grid-row-start: 1; 
	grid-row-end: span 1; 
	grid-column-start: 1; /* lze i span 3 */ 
	/* pokud je předchozí span 3, pak -1 */ 
	grid-column-end: span 3; 
} 
	
.grid__item--B { 
	grid-row: 2 / span 1; 
	grid-column: 2 / span 1; 
}

.grid__item--C { 
	grid-area: 2 / 3 / span 1 / span 1; 
}
...
```

#### Implicitní mřížka

- je generovaná, pokud umístíme element mimo explicitní mřížku
- `grid-auto-rows (columns)`

```CSS
.grid { 
	display: grid; 
	/* explicitní mřížka */ 
	grid-template-rows: 100px 300px 100px;
	 grid-template-columns: 200px 400px 200px; 
	 /* implicitní mřížka */ 
	 grid-auto-rows: 1fr; 
	 grid-auto-columns: 1fr; 
 } 
/* umístíme prvek mimo explicitní mřížku */ 
.grid__item--C { 
	grid-row: 2 / span 1; 
	grid-column: 4 / 5; 
 }
```

#### Zarovnávání

- mezery mezi řádky a sloupci
	- `column-gap`
	- `row-gap`
	- `gap
- zarovnání v mřížce
	- `justify-items` - zarovnání všech buněk na hlavní ose
	- `align-items` - zarovnání všech buněk na příčné ose
	- `justify-content` - zarovnání sloupců na hlavní ose
	- `align-content` - zarovnání řádků na příčné ose
### Flexbox

- automatické rozmístit elementy do řádků nebo sloupců

![[flexbox.png]]
- *flex kontejner* - obsahuje *flex položky*
- *hlavní osa* - osa x
- *příčná osa* - osa y 

**HTML pro příklady**
```HTML
<div class="flex">
	<div class="flex__item">1</div>
	<div class="flex__item">2</div>
	<div class="flex__item">3</div>
	<div class="flex__item">4</div>
	<div class="flex__item">5</div>
</div>
```

- pro to aby se kontejner choval jako flex
	- `display: flex`
- elementy se zarovnávají dle hlavní osy

- `flex-direction` - může změnit směr hlavní osy)
![[flex-direction.png]]

- `flex-wrap` - zalomení elementů ve flex kontejneru
![[flex-wrap.png]]

#### Umístění elementů

- `justify-content`- umístění položek flexboxu na hlavní ose
![[justify-content.png]]
- `align-content` - umístění položek na příčné ose
![[align-content.png]]
- `align-items` - zarovnání položek na vedlejší ose
![[align-items.png]]

#### Položky kontejneru

- `flex-grow` - řídí zvětšení položek kontejneru na hlavní ose
	- `flex-grow: 2;` se označuje jako *relativní flex*. element má 2x více místa
- `flex-shrink` - protiklad
	- udává, jak mají být zmenšeny, pokud se nevejdou do kontejneru
- výchozí hodnota je 1
![[flex-grow.png]]

- `align-self` - možnost zarovnat každou položku samostatně
- `flex-basis` -možné určit výchozí rozměr položky (hodnota `auto` -> z flex modelu)

- možnost zapsání všech přechozích položek zkráceně
```CSS
.flex__iteam {
/*flex-grow flex-shrink flex-basis*/
 flex: 1 0 auto; 
}
```

- *aboslutní flex* - `flex-basis: 0`  se spojením `flex-grow` lze docílit chování kdy rozdělení probíhá na základě `flex-grow.
```CSS
.flex__item {flex: 1;} 

.flex__item--changed {flex: 2;}
/*položky .flex__item--changed jsou 2x větší než .flex__items*/
```

### Pozicování elementů

- změna jeho umístění oproti normál flow na stránce. K tomu účelu slouží vlastnost `position`.
- **Hodnoty position**
	 - `static` - výchozí hodnota, pozice určena flow 
	 - `relative` - relativní pozice k jeho normal flow, místo které zabírá je ponecháno prázdné
	 - `absolute` - absolutní vzhledem k oknu nebo prvnímu  absolutně, relativně či fixně pozicováními rodičovskému elementu, původní místo použito ostatníma elementy, jeho aktuální pozice neovlivňuje ostatní elementy
	 - `fixed` - pevná pozice vzhledem k viewportu
	 - `sticky` - kombinace relativního a fixního pozicování (relativní pokuĎ není odrolován, pak fixní)
- pokud je element `relative, fixed, absolute nebo sticky`
	- možnost nastavit `top, right, bottom, left`
	- určuje pozici elementu vzhledem k počátečním souřadnicím (liší se podle typu pozicování)

#### Relativní pozicování

- počátek souřadnicového systému je dán normal flow a je umístěn v levém horní rohu elementu pro `top` a `left`, pro `bottom` a `right` pravý dolní roh

#### Absolutní pozicování

- `top`, `left` - leví horní roh webové stránky nebo rodičovského elementu s nastavenou vlastnosti `position`
- `bottom`, `right` - stejné jen praví dolní roh

#### Fixní pozicování

- pozicování dle prohlížeče. (levý horní roh a pravý dolní roh)
#### Sticky pozicování

- chová se jako relativně pozicováný ale pokud je odrolován mimo okno začne se chovat fixně
#### Překrytí elementů

- překrytí řídí normál flow
- Změnit pořadí překrytí je možné pomocí `z-index`
- hodnota je celé číslo nezáporné
- větší číslo překryje menší


##### Navigace
Předchozí:  [[Základy správného psaní CSS kódu - typické chyby a metodiky]]
Následující: [[Responzivní design]]
Celý okruh: [[2. Informační technologie]]