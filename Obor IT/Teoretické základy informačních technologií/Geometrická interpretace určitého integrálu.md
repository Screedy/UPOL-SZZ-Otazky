## Určitý integrál
- Existuje několik definic určitého integrálu:
	- Cauchyův
	- Newtonův,
	- **Riemannův** (nejčastější) - zobecnění Cachyuova integrálu,
	- Lebesgueův...
- Definice se liší množinou funkcí, pro které platí
- Na rozdíl od neurčitého integrálu, kde výsledkem je množina primitivních funkcí, je výsledkem určitého integrálu **číslo**, které můžeme interpretovat jako obsah plochy pod křivkou grafu funkce $f$ na intervalu $\langle a, b \rangle$ 
	- určitý integrál uvažujeme na uzavřeném intervalu, na níž je funkce $f$ omezena
	- říkáme **určitý integrál $f$ od $a$ do $b$**
- Využití pro výpočet:
	- obsahu plochy pod křivkou grafu (rovinného útvaru),
	- délky křivek,
	- objemy rotačních těles, pláště těles,...
	- jiné aplikace ve fyzice, chemii

>[!Tip] Poznámka
> **Idea výpočtu** obsahu plochy pro vymezený úsek grafu:
> -  Úsek grafu rozdělíme na $n$ podintervalů stejné délky
> 	- (obecně stejné délky mít nemusí)
> -  Pro každý interval můžeme uvažovat obdélník, jehož základna je dána dělením a výška je dána některou funkční hodnotou na daném podintervalu
> 	- např. lokální maximum/minimum
> - Odhad (aproximace) obsahu celé plochy spočítáme jako součet obsahů ploch jednotlivých obdélníků
> - Je přitom zřejmé že, pokud vezmeme jako výšky jednotlivých obdélníků lokální maxima/minima, je tento odhad nepřesný
> 	- Přesnější odhad získáme jemnějším rozdělením na více podintervalů (užších obdélníků)


## Obsah rovinného útvaru
- Uvažme funkci $f$, která je spojitá a kladná na intervalu $\langle a,b \rangle$. Potom určitý integrál funkce $f$ $$\int_{a}^{b} f(x) dx$$ udává obsah $S(U)$ rovinného útvaru $U$ ohraničeného grafem funkce $f$, osou $x$ a přímkami $x=a$ a $x=b$
- Jestliže funkce $f$ nabývá na intervalu $\langle a,b \rangle$ **záporných hodnot**, pak je obsah vypočítán jako $$S(U)=|\int_{a}^{b} f(x) dx|=-\int_{a}^{b} f(x) dx$$![[Pasted image 20240708132736.png]]

- Jestliže funkce $f$ nabývá na intervalu $\langle a,b \rangle$ **kladných i záporných hodnot**, pak stačí tento interval rozdělit na dílčí intervaly, ve kterých nabývá funkce pouze kladných (resp. záporných) hodnot
  - spočítáme obsahy jednotlivých dílčích intervalů dle výše uvedených úvah a sečteme

 ![[Pasted image 20240708132700.png]]

- Je-li rovinný útvar $U$ omezený spojitými funkcemi $f$ shora a funkcí $g$ zdola (platí $g(x)<f(x)$ pro $\forall x \in \langle a,b \rangle$), pak pro obsah $S(U)$ platí: $$S(U)=\int_{a}^{b}f(x)-g(x)dx$$
  - tento vztah platí i případě, že funkce v některých částech nabývají záporných hodnot

  - pokud se navíc funkce $f(x)$ a $g(x)$ neprotínají stačí si výpočet zjednodušit na $S(H)=\int_{a}^{b}|f(x)-g(x)dx|=\int_{a}^{b}|g(x)-f(x)dx|$

![[Pasted image 20240708132929.png]]


- Příklad výpočtu:

![[Pasted image 20240708124404.png]]

- Obsah plochy A + B omezené funkcemi $f$ a $g$ z výše uvedeného obrázku bychom spočítali následovně:
  1. Vyhledáme průsečíky funkcí na daném intervalu: $[-5, 0], [0, 0]$ a $[4,0]$
  2. Ze znalosti vzájemné velikost $f(x)$ a $g(x)$ spočítáme $$S=A+B=\int_{-5}^{0}f(x)-g(x)dx\ + \int_{0}^{4}g(x)-f(x)dx$$
  3. Pokud bychom uspořádání $f(x)$ a $g(x)$ na určeném intervalu neznali, stačí: $$ S=A+B=|\int_{-5}^{0}f(x)-g(x)|\ + |\int_{0}^{4}f(x)-g(x)|$$

## Délka rovinné křivky
- Nechť funkce $f$ je na intervalu $\langle a,b \rangle$ spojitá a má definovanou derivaci, pak pro délku jejího grafu platí: $$l=\int_{a}^{b} \sqrt{1+(f^{'}(x))^{2}}\ dx$$
## Objem rotačního tělesa
- Vezmeme-li rovinný útvar a necháme ho rotovat kolem osy $x$, vznikne nám rotační těleso, jehož objem můžeme spočítat pomocí určitého integrálu
- Nechť rotační těleso vznikne rotací křivky funkce $y=f(x)$ kolem osy $x$ na intervalu $\langle a,b \rangle$, pak pro jeho objem platí: $$V=\pi \int_a^{b} (f(x))^{2} dx$$
- Pokud bychom chtěli spočítat objem rotačního tělesa ohraničený dvěma funkcemi $f(x)$ a $g(x)$, pak pro jeho objem platí: $$V=\pi \int_{a}^{b}|(f(x))^{2}-(g(x))^{2}|dx$$
## Obsah rotační plochy
- Pomocí určitého integrálu spočítáme i obsah pláště rotačního tělesa: $$S=2\pi \int_{a}^{b}|f(x)|*(1+(f^{'}(x))^{2})dx$$

##### Navigace

Předchozí: [[Riemannův určitý integrál - definice, základní věta integrálního počtu, metody výpočtu]]
Následující: [[Algoritmus, problém, časová složitost algoritmu v nejhorším a průměrném případě]]
Celý okruh: [[1. Teoretické základy informačních technologií]]
