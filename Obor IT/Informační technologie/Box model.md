# CSS box model
- popisuje vizualizaci každého HTML elementu.
- ten se skládá z:
![[MacBook-2024-05-06-11-07-35.png|250]]
	1. venkovní hrany
	2. venkovního okraje (`margin`)
	3. rámečku (`border`)
	4. vnitřního okraje (`padding`)
	5. vnitřní hrany
	6. obsahu
## Rámeček - `border`
- úprava vizualizace rámečku: **border-\***
```CSS
 /* styl čáry, pokud není nastaven, rámeček se nezobrazí */
 border-style: solid;
 border-color: gray; /* barva čáry */
 border-width: 1px; /* tloušťka čáry */

 /* zkrácený zápis (preferovaný způsob zápisu),
 na pořadí nezáleží */ border: 1px solid gray;

 /* každou stranu rámečku lze nastavit zvlášť */
 border-top: 1px solid red;
 border-bottom: 2px dotted green;
 border-right: 3px dashed blue;
 border-left: 4px double gray;
 border-top-style: dotted;
 border-right-width: 2px;
```

> [!info] 
>  Existuje i rámeček *`outline`*, ten se ale používá pouze při **ladění / vývoji**, jelikož jeho velikost může upravovat každý prohlížeč jinak
## Okraje
### Vnější - `margin`
- vizualizace vnějších okrajů: **margin-\***
```CSS
/* vnejší okraj, nastavení všech */
margin: 15px;
/* sdružený zápis, postupně: top, right, botttom, left */
margin: 20px 15px 20px 15px;
/* sdružený zápis, top a bottom, left a right */
margin: 20px 15px;
/* nastavení jednotlivých okrajů */
margin-top: 20px;
margin-right: 15px;
margin-bottom: 20px;
margin-left: 15px;
```

> [!tip] 
>  Lze použít hodnotu **auto** pro automatické nastavení levého a pravého vnějšího okraje pro horizontální zarovnání na střed
>  ```CSS
>  .box--center {margin: auto;}
>  ```
### Vnitřní - `padding`
- vizualizace vnitřních okrajů: **padding-\*
```CSS
/* vnitřní okraj, nastavení všech */
padding: 15px;
/* sdružený zápis, postupně: top, right, botttom, left */
padding: 20px 15px 20px 15px;
/* sdružený zápis, top a bottom, left a right */
padding: 20px 15px;
/* nastavení jednotlivých okrajů */
padding-top: 20px;
padding-right: 15px;
padding-bottom: 20px;
padding-left: 15px;
```

## Zobrazení elementu
- zobrazení elementu pomocí vlastnosti `display`
- tři základní zobrazení:
	1. **Blokové zobrazení** (`block`) - zalomí řádky před a za elementem
	2. **Řádkové zobrazení** (`inline`) - nedochází k zalomení řádků, *ignorují se vlastnosti elementu: margin-top, margin-bottom, width a height*
	3. **Řádkově-blokové zobrazení** (`inline-block`) - uvnitř se chová jako blokový z venku jako řádkový
```CSS
.box--block {display: block;}
.box--inline {display: inline;}
.box--inline-block {display: inline-block;}
```

> [!tip] 
>  Vlastnost `display` má i hodnotu `none`, která způsobí, že se element (ani jeho potomci) nevykreslí
> ```CSS
>  .box--hidden {display:none;}
> ```

## Rozměry elementu
- vlastnosti `width` a `height` jdou použít pouze u blokového zobrazení: `display: block;` nebo `display: inline-block;`
- možnost omezit velikost elementu: `min-width` a `min-height`, `max-width` a `max-height`

> [!warning] Výchozí stav
> Ve výchozím stavu se šířka (analogicky i výška) vypočítá vztahem:
> - `width`(`height`) + `padding` + `border` = **skutečná šířka(výška) elementu**
> 
> Pokud chceme aby vlastnost `width`(`height`) skutečně odpovídala nastavené hodnotě použijeme `box-sizing: border-box;`
> 

> [!example] Bez `border-box`
> Skutečná šířka elementu: **134 px**
> ```CSS
> .menu--item {
> 	 width: 100px;
> 	 border: 1px solid gold;
> 	 padding: 16px;
>  }
>  ```

> [!example]  S vlastností `border-box`
> Skutečná šířka elementu: **100 px**
> - *Do rozměrů je započítávána šířka(výška) vnitřního okraje (2 \* padding) i šířka(výška) vnitřního okraje a rámečku (2 \* border)*
>  ```CSS
> .menu--item {
> 	 width: 100px;
> 	 border: 1px solid gold;
> 	 padding: 16px;
> 	 box-sizing: border-box;
>  }
>  ```

> [!info] 
> - Pokud upravujeme velikosti elementů, může se stát že obsah elementu **přeteče** (*obsah je větší než velikost rodičovského elementu*)
> - Chování přetečení upravíme vlastností `overflow`


##### Navigace
Předchozí:  [[HTML struktura webové stránky]]
Následující: [[Dědičnost a kaskáda]]
Celý okruh: [[2. Informační technologie]]