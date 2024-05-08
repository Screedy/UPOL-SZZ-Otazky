## Dědičnost
- klíčoví pojem
- pokud nastavíme elementu vlastnost na konkrétní hodnotu, přejímají to i potomci tohoto elementu
- např. nastavení barvy textu v nadřazeném elementem na zelenou tak i jeho potomci pokud neřeknou jinak budou mít barvu zelenou
- ne všechny vlastnosti se dědí
- pokud vlastnosti dáme hodnotu `inherit` = hodnotu rodiče
- pokud vlastnosti dáme hodnotu `initial` = defaultní hodnota prohlížeče
- vlastnost `all` řídí dědičnost všech vlastností a to i v potomku

> [!example] Vlastnost `all`
> - analogicky je možné použít klíčové slovo `initial` místo `inherit`
> 
>  ```HTML
>  <p>Stopařův průvodce Galaxií, jehož autorem je Angličan Douglas Adams, je prvním dílem stejnojmenné pentalogie označované jako <em>trilogie v pěti dílech</em>.</p>
>  ```
> 
>  ```CSS
> /* vlastnost display není děděna */
> p {  
>     display: block; 
>     color: gold;
> }
> 
> /* em zdědí všechny vlastnosti (a jejich nastavení) od svého rodiče */
> em {all: inherit;}
> ```

## Kaskáda
- jak víme můžeme jednotlivé elementy mohou být vybrány různými selektory

HTML:
```html
<article id="article">
	<h2 class="title"></h2>
</article> 
```

CSS:
```css
h2 { color: red; }
article h2 { color: green; }
.title { color: blue; }
#article h2 { color: gold; }
```
- pokud v deklaracích budou vlastnosti stejné bude docházet ke kolizím CSS pravidel
- řeší pravidlo(princip) kaskády
##### Pravidlo kaskády má 2 části:
1. při kolizi rozhoduje **specifičnost**, přesně řečeno hodnota uvedena v pravidle s více specifickým selektorem má přednost před méně specifickým
2. při kolizi se shodnou specifičností rozhoduje **pořadí**, přesněji hodnota která byla uvedena **později**

> [!tip] Pravidlo kaskády je nejdůležitější koncept CSS
### Specifičnost
- specifičnost CSS selektoru vypovídá o jeho konkrétnosti
- málo specifický vybírá více elementů než více specifický
- specifičnost reprezentovaná ve tvaru: `a b c`
	- `a` - počet id selektorů
	- `b` - počet class selektorů a pseudo-tříd v selektoru
	- `c` - počet elementů a pseudo-elementů
- `a` největší `c` nejmenší specifičnost
- inline CSS má specifickou specifičnost `1 0 0 0`
- **komplikace dědičnosti** - vždy nastavená hodnota má přednost před hodnotou získanou dědičností (bez ohledu na specifičnost)

> [!example] Nastaví se vlastnost `color` na **blue**
> -  0 1 0 < 1 0 1
> ```CSS
>  /* specifičnost: 1 0 1 */
>  #article h2 {color: blue;}
>  /* specifičnost: 0 1 0 */
>  .title {color: red;}
>  ```

>[!note]
>Kombinační operátory **+**, **>** a **~** nemají na výpočet specifičnosti vliv
>
### Pořadí
- pokud CSS pravidla mají stejnou specifičnost, rozhoduje o nastavení vlastnosti pořadí pravidel ve kterém je tato vlastnost uvedena -> aplikují se **později uvedené**

> [!example] Nastaví se vlastnost `color` na **red**
> ```HTML
> <div class="second first"></div>
>  ```
>  
> ```CSS
> .first {color: blue;}
> .second {color: red;}
>  ```

- rozhoduje i na úrovni **deklaračního bloku**

```css
.second { 
	color: red;
	color: blue;
}
```

- tento kód nastaví modrou barvu html elementu pojmenovaný class second
### Důležitost
- pravidla kaskády jdou obejít pomocí **důležitosti**
- **důležitá** hodnota má přednost především
- uvádíme `!important`
- jakoby specifičnost byla `1 0 a b c`
- pokud více hodnot používá `!important` -> pravidlo kaskády
```css
.title { 
	color: gold !important;
}
```
- **nepoužívat!** (výjimka: lze použít **pouze** při práci s externími knihovnami)
## Celý proces
1. Pokud není hodnota nastavena, je použita **výchozí** hodnota definovaná webovým prohlížečem. 
2. Pokud je hodnota **zděděna**, přepisuje hodnotu nastavenou v bodu 1. 
3. Pokud je hodnota **explicitně** nastavena, **přepisuje** hodnotu nastavenou v bodech 1 a 2. 
4. Pokud dochází ke **kolizi**, rozhoduje **kaskáda**. 
5. Pokud je hodnota nastavena v **inline CSS**, přepisuje hodnotu nastavenou v bodech 1–4.  
6. Pokud je hodnotě nastavena **důležitost**, přepisuje hodnotu nastavenou v bodech 1–5. 
7. Pokud uživatel použije vlastní hodnotu (vlastní sadu stylů), přepisuje tato hodnota hodnotu nastavenou v bodech 1–6. 




##### Navigace
Předchozí:  [[Box model]]
Následující: [[Základy správného psaní CSS kódu - typické chyby a metodiky]]
Celý okruh: [[2. Informační technologie]]