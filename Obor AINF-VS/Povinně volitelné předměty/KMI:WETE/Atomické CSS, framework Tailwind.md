# Atomické CSS

Atomické CSS je způsob psaní CSS, ve kterém se výsledný vzhled skládá z malých jednoúčelových tříd. Abychom pochopili, proč vzniklo, je potřeba začít u problémů běžného CSS: kaskáda, dědičnost, specifičnost, přepisování pravidel a obtížná údržba větších projektů.

### 1. Co je CSS a proč je potřeba ho organizovat

- **CSS** (_Cascading Style Sheets_) je jazyk pro vizualizaci webových stránek. Je založen na souboru pravidel, která definují vzhled HTML elementů na stránce.
- **Struktura pravidel** je přesně daná. Obsahuje selektor pro výběr elementů a deklarační blok, v němž určujeme, jaké vlastnosti a hodnoty chceme takto zvoleným elementům přiřadit.

```css
.box {
  padding: 1rem;
}
```

- Při psaní pravidel je klíčové mít na paměti **pravidlo kaskády**. To určuje, že v případě konfliktu mezi pravidly, má prioritu to, které je specifičtější nebo je v CSS kódu uvedeno později.
- CSS pravidla můžeme psát jako:
  - **Externí CSS** - do samostatného souboru s příponou `.css`
  - **Vnořené CSS** - v HTML souboru v rámci elementu `style`
  - **Inline CSS** - do atributu `style` konkrétního elementu se zapisují jednotlivé vlastnosti
- CSS soubory často obsahují **stovky řádků kódu**, proto je důležité v nich udržovat pořádek. Je důležité využívat koncepty CSS, které to pomáhají řešit - pravidlo kaskády a **dědičnost**. Ta umožňuje, aby nastavené vlastnosti elementu byly automaticky nastaveny také jeho potomkům. Tyto koncepty ale jsou často nedostačující.
- Na malém webu může stačit několik jednoduchých tříd. U větší aplikace ale začne být problémem:
  - globální rozsah CSS tříd,
  - nechtěné přepisování stylů,
  - rostoucí specifičnost selektorů,
  - duplicita kódu,
  - obtížná údržba a spolupráce více lidí.
- Proto vznikají **_CSS metodiky_**. Jejich cílem není změnit samotný jazyk CSS, ale zavést pravidla, jak třídy pojmenovávat, jak rozdělovat styly a jak udržet CSS předvídatelné.

---

### 2. CSS metodiky

**_CSS metodika_** je sada doporučení pro psaní, pojmenování a organizaci stylů. Jako příklad můžeme uvést **BEM** nebo **SUIT CSS** (ale je jich mnoho).

### BEM

- **_BEM_** ze slov **_Block, Element, Modifier_**. To napovídá, že BEM zavádí strukturu blok, element a modifikátor a řeší jejich pojmenování.
  - **Blok** - samostatná komponenta, která má vlastní význam. Může to být například navigace, karta, formulář nebo tlačítko. V názvu používáme pomlčky pro oddělení slov
  - **Element** - část bloku, která bez daného bloku nedává samostatný smysl. V BEM se zapisuje pomocí **dvojitého podtržítka**. Například položka navigace.
  - **Modifikátor** - vyjadřuje variantu nebo stav bloku či elementu. Zapisuje se pomocí **dvojité pomlčky.**
- Třídy mají jasný název, ze kterého je vidět, ke které komponentě patří. Díky tomu se snižuje riziko, že jeden styl nechtěně ovlivní jinou část stránky.
- Typicky se styluje přes jednu třídu, například `.nav__item`, místo složitých selektorů typu `ul.nav li a`. Nízká specifičnost usnadňuje pozdější úpravy, protože není nutné pravidla „přebíjet“ stále silnějšími selektory.

```css
/* nová konvence */
jmeno-bloku
jmeno-bloku--jmeno-modifikatoru
jmeno-bloku__jmeno-elementu--jmeno-modifikatoru
```

```css
.nav {...} /* společné pro všechny navigace */
.nav--secondary {...} /* specifika pro sekundární navigaci */
.nav__item {...} /* položka navigace */
.nav__item--active {...} /* specifika pro aktivní položku navigace */
```

---

### 3. Organizace CSS souborů

Při vývoji je často pohodlnější mít CSS rozdělené do více menších souborů, protože se v nich lépe orientuje. V produkci se historicky často preferoval jeden výsledný soubor, protože menší počet HTTP požadavků znamenal rychlejší načítání. Prezentace ale upozorňuje, že při použití HTTP/2 může být použití více souborů přijatelnější.

Obecně neexistuje jedno správné řešení. Organizace CSS závisí na velikosti projektu, týmu, nástrojích a způsobu nasazení.

Častý kompromis je mít při vývoji více souborů a při buildu je spojit nebo optimalizovat.  
Styly se mohou organizovat například podle:

- layoutu,
- komponent,
- typografie,
- barev,
- utilit,
- témat.

### ITCSS

**ITCSS** znamená **Inverted Triangle CSS**. Jde o architekturu pro organizaci CSS, která se snaží držet kód škálovatelný, předvídatelný a udržitelný. ITCSS je způsob organizace CSS, ne konkrétní knihovna.

Hlavní myšlenka je řadit CSS od obecných pravidel ke konkrétním a od pravidel s nízkou specifičností k pravidlům s vyšší specifičností. Proto se používá obraz „obráceného trojúhelníku“.

ITCSS je důležitý hlavně u větších projektů, protože pomáhá předcházet chaotickému růstu CSS. Místo náhodného přidávání pravidel se styly ukládají do vrstev podle toho, jak jsou obecné nebo konkrétní.

---

### 4. Utility třídy

**_Utility třída_** je jednoúčelová CSS třída. Typicky obsahuje jednu deklaraci.

Příklad:

```css
.text-primary {
  color: gold;
}

.text-secondary {
  color: gray;
}
```

Utility třídy nepopisují komponentu jako celek, ale jednu konkrétní vizuální vlastnost. Místo toho, aby se vytvořila třída `.card-title`, můžeme použít kombinaci utility tříd přímo v HTML.

```html
<h2 class="text-center mt-4">
  Nadpis
</h2>
```

#### Výhody a nevýhody

- + Rychlé prototypování
- + Menší riziko kolizí mezi komponentami
- + Malé a znovupoužitelné stavební bloky
- - HTML je delší a méně přehledné
- - Bez design systému může vzniknout chaos

---

### 5. Atomické CSS

**_Atomické CSS_** je přístup, ve kterém je CSS postavené na jednoúčelových utility třídách.  
Název „atomické“ vychází z představy, že výsledný vzhled se skládá z velmi malých jednotek – „atomů“. Každá třída řeší malou část výsledného vzhledu. Tento přístup je nízkoúrovňový, s velmi malým CSS, ale je důležité mít design systému a dokumentaci.

Pro atomické CSS existuje řada frameworků, které poskytují hotovou sadu utility tříd. Vývojář tedy nemusí psát všechny jednoúčelové třídy ručně, ale používá předem připravený systém.

Obecný princip:

```html
<div class="mt-4 p-4 text-center">
  Obsah
</div>
```

---

# Tailwindcss

- Jedním z těchto frameworků je **_tailwindcss_**. Tento framework poskytuje zdokumentované předem připravené utility třídy, které píšeme přímo do HTML souboru. Tyto třídy navíc dodržují metodiku pojmenování, jejich použití je tedy poměrně intuitivní.
- Výsledný CSS soubor je pak sestaven **automaticky**. To vede k **minimální velikosti** výsledného CSS souboru. **JIT (Just-in-Time) Engine.**
- Tailwind CSS klade mimo jiné důraz na responzivní design, což usnadňuje přizpůsobení stránek pro různé velikosti obrazovek.
- **V tailwind.config.js** můžeš definovat vlastní barvy, rozšiřovat základní téma a třeba si vytvořit vlastní breakpointy pro lepší responzivitu než tu jejich základní **(sm, md, lg, xl, 2xl)**
- **Arbitrary values:** Pokud chceš hodnotu která v Tailwindu není v základu stačí k tomu použít hranaté závorky - **top-[117px]**
- **Tailwind UI:** Oficiální knihovna vytvořených UI komponent
- **Pretier plugin:** v tolika utilitních třídách může nastat zmatek. Proto byl vytvořen plugin Pretier, který seřadí jednotlivé třídy podle **důležitosti.**