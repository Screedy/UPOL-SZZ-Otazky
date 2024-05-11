- při psaní CSS pravidel je dobré co nejvíce využívat dědičnost, kaskádu a znuvupoužitelnost
### Typické chyby

#### Nízká specifičnost
- používání selektorů, které obsahují jména HTML elementů
- to je nevýhodné pokud se elementy opakovaně objevují na různých místech ve více podobách
- pokud by jsme chtěli další elementy s jinou barvou dostaneme se do slepé uličky
- vytvoříme nepřehledné řešení

```CSS
/* špatně - použití selektoru, který obsahuje jméno HTML elementu */
em { color: gray; }

...
/* výjimka pro jiné em elementy */
.text-color-secondary { color: gold; }
```

- pokud je takových úprav více psaní CSS musíme opakovaně měnit již nastavené hodnoty -> **redundantní CSS**.
- řešení pojmenováním elementů pomocí atributu **class**

```CSS
.text-color-primary { color: gray; }
.text-color-secondary { color: gold; }
```

- jediná výjimka je úprava výchozího(globální) chování elementů
```CSS
body { color: white; }
```

#### Vysoká specifičnost

- používání selektorů s příliš velkou specifičností.

```HTML
<nav>
	<ul id="navigation">
		<li class="item">lol1</li>
		<li class="item active">lol2</li>
	</ul>
</nav>
```

```CSS
/* nastavíme barvu všech položek na černou */ 
#navigation .item {color: black;}
/* nastavíme barvu aktivní položky, class="active" */ 
.active {color: gold;} 
/* nastavíme barvu první položky na zelenou */
#navigation .item:first-child {color: green;}
```

- ukázkový kód ale **nefunguje**
- kaskáda způsobí, že pravidlo `.active { color: gold; }` se neaplikuje
- jelikož má menší specifičnost
- pokusíme se opravit:
```CSS
/* funguje, ale zvýšili jsme specifičnost */ 
#navigation .active {color: gold;}
```

- zkomplikuje situaci
- použitý selektor má vyšší specifičnost kvůli vysoké specifičnosti ostatních selektorů
- navíc stále jsou tam chyby $\rightarrow$ pokud by aktivní položkou byl první element `li` bude zobrazen zeleně
- už jen dvě možnosti řešení (ani jedno dobré)
	1. `!important`
	2. změna `class` na `id`
- oba případy zase zvednou specifičnost
- **proč je problematická:**
	- selektory s velkou specifičností **omezují dědičnost**
	- **redundantní** kód
	- se **špatnou organizací** -> velké problémy 
- **řešení:**
	- vyhnout se selektoru atributu `id`
	- vyhnout se psaní `!important`

#### Pojmenování
- pojmenovávání elementů dle jejich vzhledu -> po čase může problematické když chceme změnit design a už to neodpovídá názvu
```CSS
/* špatně */
.button-color-gold {color: gold;}
/* později chceme změnit barvu */
.button-color-gold {color: gray;} /* matoucí */
```
- lepší pojmenovávat dle **použití**
- případná změna hodnot nebude matoucí
```CSS
/* správně */
.button-color-primary {color: gold;}
```
 - pojmenování dle umístění (`.button-main-page`) taky není vhodné -> element může být použit na jiných místech -> název v jiném místě bude nelogický

### CSS metodiky
- pomohou nám vyhnout se chybám
- popisují **základní konvence** psaní CSS
#### OOCSS (Object Oriented CSS)
- **doporučuje**:
	- používat selektory s **nízkou specifičností** 
	- vyhnout se pojmenování na základě vizuální podoby a místa použití
	- nepromítat kontext elementu do CSS selektorů

>[!fail] Příklad
>```CSS
>/* chybné dle OOCSS */ 
>.article .title { 
>	color: gold; 
>	border-left: 1em solid gold; 
>	padding: 1em; 
>}
>```
>```HTML
><!-- pro následujcí kód-->
><h2 class="title">Lorem Ipsum</h2>
>
><article class="article">
>	<h2 class="title">dolor sit amet</h2>
></article>
>```
>

- zabraňuje snadnému znovupoužití na jiném místě
- chceme element `h2` (*Lorem Ipsum*) vizualizovat stejně jako `h2`(*dolor sit amet*) ale jinou barvou
- existující pravidlo nám tomu brání a musíme přidat redundantní pravidlo

>[!fail] Příklad
>```CSS
>/* chybné dle OOCSS */ 
>.article .title { 
>	color: gold; 
>	border-left: 1em solid gold; 
>	padding: 1em; 
>} 
>/* přidané redundantní pravidlo */ 
>.title { 
>	color: gray; 
>	border-left: 1em solid gray; 
>	padding: 1em; 
>}
>```

- **řešení dle OOCSS** - přejmenování a odstranění kontextu v selektorech

>[!success] Správné řešení
>```HTML
><h2 class="title">Lorem Ipsum</h2>
><article>
>	<h2 class="title title-article">dolor sit amet</h2>
></article>
>```
>```CSS
>/* vlastnosti pro všechny nadpisy */ 
>.title { 
>	color: gray; 
>	border-left: 1em solid gray; 
>	padding: 1em; 
>} 
>/* specifické vlastnosti pro nadpis v elementu article */ 
>.title-article { 
>	color: gold; 
>	border-color: gold; 
>}
>```

**Základní principy:**
- vyčlenění **společných vlastností** do jedné třídy, úprava pro specifické části jsou určený dalšími CSS pravidly které upravují jen určité atributy
- nahrazení kontextové závislosti **vhodným pojmenováním**
- další upravující/rozšiřující pravidla pomocí rozšíření názvu

#### BEM (Block Element Modificator)
- implementuje OOCSS
- zajímavá metodika většinou se používá část o pojmenování elementů
- **struktura -** blok, element a modifikátor
	- **blok -** samostatná nezávislá část stránky
	- **element -** představuje součást bloku
	- **modifikátor -** představuje variantu bloku či elementu
```CSS
/* blok */
jmeno-bloku

/* modifikátor bloku */ 
jmeno-bloku--jmeno-modifikatoru-bloku 

/* element bloku */ 
jmeno-bloku__jmeno-elementu

/* modifikátor elementu bloku */
jmeno-bloku__jmeno-elementu--jmeno-modifikatoru-elementu
```

>[!Example] Příklad
>```HTML
><!-- Představ me si že tento kód je sekundární navigace na stránce-->
><ul class="nav nav--secodary" role="navigation"> 
>	<li class="nav__item">
>		<a href="#">A</a>
>	</li>
>	<li class="nav__item nav__item--active">
>		<a href="#">B</a>
>	</li>
></ul>
>```
>
>```CSS
>/* společné pro všechny navigace */ 
>.nav {...} 
>/* specifika pro sekundární navigaci */ 
>.nav--secondary {...} 
>/* položka navigace */ 
>.nav__item {...} 
>/* specifika pro aktivní položku navigace */ 
>.nav__item--active {...}
>```

- vhodné rozdělení tříd **minimalizuje redundanci** výsledného CSS.
- díky struktuře názvu je vždy blok zapouzdřený (neovlivňuje zbylé části stránky)

#### SUIT CSS
```CSS
/* komponenta (blok v terminologii BEM) */ 
JmenoKomponenty 

/* modifikátor komponenty */ 
JmenoKomponenty--jmenoModifikatoruKomponenty 

/* část komponenty (element v terminologii BEM) */ 
JmenoKomponenty-jmenoCastiKomponenty 

/* modifikátor části komponenty */ 
JmenoKomponenty-jmenoCastiKomponenty--jmenoModifikatoruCastiKomponenty
```
- **utility třídy** - jsou CSS pravidla obsahující pouze jednu deklaraci (pouze jeden účel)
	- kód z utility tříd se označuje jako **atomické CSS**
	- lze pomocí nich vytvořit celou web stránku
	- náročný ale populární
	 $\rightarrow$ na atomickém CSS je založený Tailwind CSS

>[!Example] Příklad utility tříd
>```CSS
>.text-color-primary { color: gray; }
>.text-color-secondary { color: gold; }
>.margin-1 { margin: 1rem; }
>```

### Organizace souboru

 - zabývá se jak pravidla CSS organizovat v souborech

#### ITCSS (Inverted Triangle CSS)

1. od pravidel s největším dosahem (největší vizuální změna) po pravidla s nejmenším dosahem
2. od pravidel s největší specifičností po pravidla s nejnižší specifičností;
3. od pravidel s největší konkrétností po pravidla s nejmenší konkrétností

![[itcss.png|350]]
#### Kde začít?
#### Předloha atomický design 
- je vhodné implementovat elementární části stránky, kterým se v terminologii říkají ***atomy***
- Následně **skládáním atomů** -> **komponenty** -> **design**
- umožňuje spolupráci více vývojářů (každý pracuje na atomu)

![[design1.png]]
###  Předloha méně atomických prvků
- vhodné vytvořit **základní vizualizaci** a tu následně **vylepšovat**
- nejprve hrubý layout stránky a následně komponenty
- pokud se komponenty opakují v různých variantách -> vytvořit **obecnou podobu** následně **upravovat** specifické **části**
![[design2.png]]



##### Navigace
Předchozí:  [[Dědičnost a kaskáda]]
Následující: [[Layout webové stránky - grid, flexbox, pozicování]]
Celý okruh: [[2. Informační technologie]]