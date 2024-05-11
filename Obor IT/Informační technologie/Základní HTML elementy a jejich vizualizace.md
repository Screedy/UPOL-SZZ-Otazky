- Základní HTML elementy jsou stavebními bloky webových stránek. 
- Každý element má své specifické vizuální reprezentace, které definují, jak se bude obsah zobrazovat v prohlížeči
## Práce s textem

```HTML
<h1> - <h6> <!-- Nadpisy od největšího po nejmenší -->
<p> <!-- Odstavec textu -->
<strong> <!-- Tučný text -->
<em> <!-- Kurzíva -->
<br> <!-- Zalomení řádku -->
```
#### element `time`
- určení času nebo doby trvání se používá element time, který disponuje atributem `datetime`
- `datetime`: 
	- strojově čitelný formát data (YYYY-MM-DDThh:mm:ss)
	- délka trvání (PThhHmmMssS)

```HTML
<p>Raketa odstartuje <time datetime="2022-09-29T16:00:00">29. září 2022 v 16 hodin</time>.</p>

<p>Maraton uběhl přibližně za <time datetime="PT3H54M23S">3 hodiny a 54 minut</time>.</p>
```
#### element `abbr`
- označení zkratek v textu
- vysvětlena v atributu title

```HTML
<p><abbr title="Domain Name System">DNS</abbr> je hierarchický systém doménových jmen.</p>
```
## Formátování textu

```HTML
<b> <!-- Tučné písmo -->
<i> <!-- Italika -->
<u> <!-- Podtržený text -->
<small> <!-- Menší písmo -->
<mark> <!-- Zvýraznění textu -->
```

## Vlastnosti písma
- pomocí CSS pak můžeme upravit vizuální prezentaci textu, typ písma, velikost, výšku řádku, barvy

```CSS
font-family: 'Arial', sans-serif; /* Typ písma */
font-size: 16px; /* Velikost písma */
line-height: 1.5; /* Výška řádku */
color: #333; /* Barva textu */
```

## Obrázky a média
- HTML podporuje vkládání obrázků a dalších mediálních typů

```HTML
<img src="url_obrazku.jpg" alt="Popis obrázku">
<video src="url_videa.mp4" controls></video>
<audio src="url_zvuku.mp3" controls></audio>
```

## Odkazy
- Jsou fundamentální pro propojení obsahu na internetu. 
- HTML poskytuje element `<a>` pro vytvoření hypertextových odkazů

```HTML
<a href="url_stranky.html">Název odkazu</a>
```

## Seznamy
- Umožňují organizovat informace do bodů nebo kroků a jsou nezbytné pro přehledné strukturování obsahu

```HTML
<ul> <!-- Neuspořádaný seznam -->
  <li>Položka 1</li>
  <li>Položka 2</li>
</ul>
<ol> <!-- Uspořádaný seznam -->
  <li>Krok 1</li>
  <li>Krok 2</li>
</ol>
```
## Tabulky
- Užitečné pro organizaci a prezentaci dat ve strukturované formě

```HTML
<table>
  <tr> <!-- Řádek tabulky -->
    <th>Header 1</th> <!-- Hlavička tabulky -->
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Data 1</td> <!-- Buňka tabulky -->
    <td>Data 2</td>
  </tr>
</table>
```

## Formuláře
- Jsou klíčové pro interakci uživatele s webovou stránkou, umožňují sběr dat od uživatelů
- `input` má atribut `type` který určuje konkrétní typ formulářového prvku

```HTML
<form action="submit_form.php" method="post">
  <label for="name">Jméno:</label>
  <input type="text" id="name" name="user_name">
  <input type="submit" value="Odeslat">
</form>
```


##### Navigace
Předchozí:  [[Responzivní design]]
Následující: [[Analýza kvality webové stránky]]
Celý okruh: [[2. Informační technologie]]