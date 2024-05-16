- layout webové stránky určuje, jak jsou různé prvky na stránce uspořádány

## Grid
- zavádí **dvoudimenzionální mřížku** (grid), do které je možné rozmisťovat prvky

>[!Example] Základní pojmy
>![[grid-pojmy.png|500]]
>- **grid kontejner** - základní element obsahující mřížku
>- **čáry** - vymezují *buňky* a *oblasti* (seskupení buněk)
>- **řádky** a **sloupce** - speciální oblasti, řádek/sloupec buněk
>- **hlavní osa** - osa x
>- **příčná osa** - osa y
>---
 >- osy určují jakým způsobem budou prvky v mřížce zarovnány
 >- čáry *nejsou zobrazeny* pouze vymezují oblasti do kterých jdou umístit elementy
 >- **Vytvoření mřížky(gridu)**: elementu nastavíme `display: grid` (případně `display: inline-grid`), to vytvoří mřížku a do ní následně rozmístíme elementy

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
	display: grid; /* lze i inline grid */
	/*nastavení třech řádků*/
	grid-template-rows: 100px 300px 100px; 
	/*nastavení tžech sloupců*/
	grid-template-columns: 200px 400px 200px;
}
```
**Obrázek mřížky pro předchozí kód**
![[grid-prvni.png]]
 - *index čáry* - pří vytvoření mřížky
#### Index čáry
![[index-cary.png]]
 - čáry jsou indexované vzestupně zleva doprava na hlavní ose a na příčné z hora dolů
 - současně zprava doleva od $-1$ do $-n$ a na příčné zdola nahoru
 - indexy odpovídají i indexům **sloupce** a **řádku**
 - možnost čáry pojmenovat
```CSS
.grid { 
	grid-template-rows: [header-start] 100px [content-start] 300px [footer-start] 100px; 
	grid-template-columns: 200px 400px 200px [col-3-end]; 
}
```
- možnost přidání více jmen do hranatých závorek pro jednu čáru
#### Jednotka fraction - `fr`
- **náhrada pixelů**
- **přizpůsobuje se** různým zobrazovacím zařízením
- určuje poměrnou část nespecifikovaného místa
>[!Example] Příklady `fr`
>```CSS
>/* prostřední sloupec bude pružný */ 
>grid-template-columns: 200px 1fr 200px; 
>/* všechny sloupce budou pružné, prostřední zabírá 2x více místa než první a poslední sloupec */ 
>grid-template-columns: 1fr 2fr 1fr;
>```

#### Automatické generování mřížky
- možné generovat automaticky pomocí funkce `repeat()`
- pouze jeden `repeat()` v deklaraci

**Příklady**
```CSS
/* 12 sloupců, první a poslední je 2x vetší*/
grid-template-columns: 2fr repeat(10, 1fr) 2fr;

/* 12 sloupců, opakuje se vzor 1fr 2fr, 8 tedy 1fr 2fr 1fr 2fr ... */
grid-template-columns: repeat(6, 1fr 2fr);
```

- pří automatickém generování můžeme nechat prohlížeč rozhodnout kolikrát má daný vzor opakovat, 
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

> [!note] Zkrácený zápis
> existuje ještě zkrácený zápis pro `grid-template` a pro `grid` (dobré pro jednoduché mřížky)
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

- vymezení oblasti čarami
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
	- `gap`
- zarovnání v mřížce
	- `justify-items` - zarovnání všech buněk na hlavní ose
	- `align-items` - zarovnání všech buněk na příčné ose
	- `justify-content` - zarovnání sloupců na hlavní ose
	- `align-content` - zarovnání řádků na příčné ose
## Flexbox
- automatické rozmístit elementy do řádků nebo sloupců

![[flexbox.png]]
- **flex kontejner** - obsahuje **flex** položky
- **hlavní osa** - osa x (u řádku, u sloupce naopak)
- **příčná osa** - osa y (u řádku, u sloupce naopak)

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
- `flex-direction` - **změna směru hlavní osy**
![[flex-direction.png]]

- `flex-wrap` - **zalomení elementů** ve flex kontejneru
![[flex-wrap.png]]
#### Umístění elementů
- `justify-content`- umístění položek flexboxu na **hlavní ose**
![[justify-content.png]]
- `align-content` - umístění položek na **příčné ose**
![[align-content.png]]
- `align-items` - **zarovnání** položek na **vedlejší ose**
![[align-items.png]]

#### Položky kontejneru
- `flex-grow` - řídí zvětšení položek kontejneru na hlavní ose
	- `flex-grow: 2;` se označuje jako **relativní flex**. element má 2x více místa
- `flex-shrink` - protiklad
	- udává, jak mají být zmenšeny, pokud se nevejdou do kontejneru
- výchozí hodnota je 1
![[flex-grow.png]]

- `align-self` - možnost zarovnat každou položku samostatně
- `flex-basis` - možné určit výchozí rozměr položky (hodnota `auto` -> z flex modelu)

- možnost zapsání všech předchozích položek zkráceně
```CSS
.flex__iteam {
/*flex-grow flex-shrink flex-basis*/
 flex: 1 0 auto; 
}
```

- **absolutní flex** - `flex-basis: 0`  se spojením `flex-grow` lze docílit chování kdy rozdělení probíhá na základě `flex-grow.
```CSS
.flex__item {flex: 1;} 

.flex__item--changed {flex: 2;}
/*položky .flex__item--changed jsou 2x větší než .flex__items*/
```

## Pozicování elementů
- změna jeho umístění oproti normal flow na stránce. K tomu účelu slouží vlastnost `position`.
- **Hodnoty position**
	 - `static` - výchozí hodnota, pozice určena normal flow 
		 - <img src="https://media.geeksforgeeks.org/wp-content/uploads/20211029154457/20211029154026.gif" alt="static pozicovani" height="200px">
	 - `relative` - relativní pozice k jeho normal flow, místo které zabírá je ponecháno prázdné
		- <img src="https://media.geeksforgeeks.org/wp-content/uploads/20211029155726/20211029155406.gif" alt="relative pozicovani" height="200px">
	 - `absolute` - absolutní pozicování umístí prvek relativně k jeho nejbližšímu předkovi s `position: relative;`.
		 - <img src="https://media.geeksforgeeks.org/wp-content/uploads/20211029152705/20211029152518.gif" alt="absolute pozicovani" height="200px">
	 - `fixed` - pevná pozice vzhledem k viewportu
		 - <img src="https://media.geeksforgeeks.org/wp-content/uploads/20211029142813/20211029142357.gif" alt="fixed pozicovani" height="200px">
	 - `sticky` - kombinace relativního a fixního pozicování (relativní dokud není odrolován, pak fixní)
- pokud je element `relative, fixed, absolute nebo sticky`
	- možnost nastavit `top, right, bottom, left`
	- určuje pozici elementu vzhledem k počátečním souřadnicím (liší se podle typu pozicování)

#### Relativní pozicování
- počátek souřadnicového systému je dán normal flow a je umístěn v **levém horní rohu elementu** pro `top` a `left`, pro `bottom` a `right` pravý dolní roh
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
- hodnota je celé číslo (i záporné)
- větší číslo překryje menší
<br>

>[!summary] Grid a Flexbox
>##### Grid
> - základem je **grid kontejner**, obsahující **mřížku** pro rozmístění prvků
> - v CSS musíme nastavit `display: grid` nebo `display: inline-grid`
> - určen čárami, které vymezují buňky a oblasti (řádky a sloupce)
> - jednotlivé oblasti lze pojmenovat
> - osy určují jakým způsobem budou prvky v mřížce zarovnány
> - osy nejsou zobrazeny pouze vymezují prostor pro jednotlivé elementy
> - vždy hlavní + vedlejší osa
> ##### Flexbox
> - základem je **flex container**, který obsahuje **flex položky**
> - v CSS musíme nastavit `display: flex`
> - sloupec a řádek - vždy hlavní + vedlejší osa
> 
> Pomůcka pro vlastnosti Gridu a Flexboxu:
> - zarovnání obsahu kontejneru na hlavní ose provádí vlastnosti justify-\* a zarovnání na příčné ose se provádí vlastnosti align-\*
> - zarovnání všech položek určují vlastnosti \*-items, distribuci volného místa (mezery) mezi položkami určuje vlastnost \*-content a zarovnání samostatné položky určuje \*-&nbsp;self
> ![[grid-flexbox.png|350]]
> 

> [!summary] Pozicování
> je změna umístění elementu (oproti normal flow) na stránce
> 
> vlastnost `position`: 
> - `static` - výchozí pozice určená normal flow
> - `relative` - relativní vzhled k flow, místo, které element zabíral je prázdné
> - `absolute` - absolutní pozice vzhledem k oknu prohlížeče nebo prvnímu absolutně, relativně či fixně pozicovanému rodičovskému elementu, místo je použité pro jiné elementy
> - `fixed` - pevná pozice vzhledem k viewportu prohlížeče
> - `sticky` - kombinace relativní a fixní pozice (dokud není odrolováno)


##### Navigace
Předchozí:  [[Základy správného psaní CSS kódu - typické chyby a metodiky]]
Následující: [[Responzivní design]]
Celý okruh: [[2. Informační technologie]]