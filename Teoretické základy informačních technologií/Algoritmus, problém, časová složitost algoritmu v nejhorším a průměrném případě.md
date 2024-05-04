### Algoritmus
- **Algoritmus** je posloupnosti instrukcí pro řešení problému
	- $\Rightarrow$ vede k dalším otázkám
	- **Instrukce** je jednoznačný srozumitelný pokyn
	- **Řešení problému algoritmem** = vykonáváním instrukcí podle algoritmu se od vstupu $I$ po konečném počtu kroků dobereme k výstupu $O$

> [!tip]
>Pojem **algoritmus** je podobně jako pojem množina **základním pojmem**, který **není** definován pomocí jednodušších pojmů, je jen objasňován svými vlastnostmi na konkrétních příkladech.

### Problém
- Definice **problém**:
	- Problém **je určen trojicí $(IN, OUT, p)$**, kde **$IN$** je množina (přípustných) vstupů, **$OUT$** je množina výstupů a **$p:IN \rightarrow OUT$** je funkce přiřazující každému vstupu odpovídající výstup

>[!Example] Příklad problému
>**Název**: *Dosažitelnost vrcholů v grafu*
>**Vstup**: *Neorientovaný/Orientovaný graf $G=(V,E)$ a vrchol $s \in V$*
>**Výstup**: Jsou všechny vrcholy $v \in V$ dosažitelné z $s$?

### Časová složitost algoritmu v nejhorším případě a v průměrném případě
- Vyjadřuje závislost trvání výpočtu daného algoritmu na velikosti vstupních dat
- **Funkce**, která **velikosti vstupních dat přiřadí trvání výpočtu**
  $$
  \begin{matrix}
  n \\ \vdots \\ \text{velikost vstupu}
  \end{matrix}
  \rightarrow
  \begin{matrix}
  T(n) \\ \vdots \\ \text{trvání výpočtu}
  \end{matrix}
  $$
- **$T(n)$** lze chápat dvěma základními možnostmi:
	1. **Časová složitost v nejhorším případě**
		- $T(n)$ znamená *délku výpočtu algoritmu $A$* nad vstupem velikosti $n$ v <u>nejhorším případě</u>;
		- **$T(n) = \text{max} \{k \mid k \text{ je délka výpočtu } A \text{ nad vstupem velikost } n \}$**
	2. **Časová složitost v průměrném případě**
		- $T(n)$ znamená *délku výpočtu algoritmu $A$ nad vstupem velikosti $n$* <u>v průměrném případě</u>;
		- $T(n) = \frac{t_{A}(i_{1})+...+t_{A}(i_{m})}{m}$
		- $t_{A}(i)$ je počet elementárních výpočetních kroků vykonaných od zahájení do skončení výpočtu algortmem $A$ pro vstup $i$

##### Navigace
Předchozí:  [[Geometrická interpretace určitého integrálu]]
Následující: [[O-notace a růst funkcí, definice, vlastnosti, příklady použití]]
Celý okruh: [[1. Teoretické základy informačních technologií]]