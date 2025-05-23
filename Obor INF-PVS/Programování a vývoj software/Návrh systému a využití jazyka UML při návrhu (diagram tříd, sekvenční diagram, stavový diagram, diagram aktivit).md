## Jazyk UML
- **UML** (*unified modeling language*) je standardizovaný pro vizuální modelování SW systémů
- Zjednoduší vhled do problematiky velkých systémů
- Používá se i v dokumentaci
- Je velmi intuitivní

- Modelování může mít různou preciznost a jsou různé modely
#### Strukturální prvky v UML
- Podstatná jména jazyka (pro koncepty nebo fyzické věci)
1) Třídy - formální popis objektů mající stejné vlastnosti
2) Aktivní třídy - třídy obsahující více procesů či vláken
3) Rozhraní - kolekce operací popisující poskytovanou službu
4) Spolupráce - popisuje interakci mezi elementy
5) Případ užití - popis sekvence akcí s výstupem, které by měl systém umožnit
6) Komponenty - modulární součásti systému (skrývají implementaci za rozhraní)
7) Artefakty - části systému s fyzickou informací (soubory, knihovny, ...)
![[Pasted image 20231221145625.png]]
#### Chování v UML
- Dynamické části jazyka (slovesa popisující chování)
- Propojují strukturální prvky jazyka
1) Interkace - soubor zpráv, které si objekty vyměnují
2) Stavový stroj - sekvence stavu objektu, ve kterých se během života vysktyuje
3) Aktivita - sekvence akcí, které objekt provádí
![[uml.png]]
#### Seskupování objektů
- Pro přehlednost se organizují do skupin
1) Balíčky - pouze k organizaci návrhu (ve vývoji zanikme)
2) Poznámky - textová specifikace
![[Pasted image 20250423182009.png]]
#### Vztahy v UML
1) **závislosti** - sémantické vztahy
2) **asociace** - strukturální vztahy, popis vazby (1:N)
3) **agregace** - "has a"
4) **generalizace** - popis dědičnosti
5) **generalizace** - jeden vyžaduje, druhý zaručuje (funkcionalitu)
- n-ární vztahy (mezi vícero objekty)
![[Pasted image 20231221150316.png]]
#### Diagramy v UML
- vizualizace z různých úhlů pohledu
	- jasné definice = **13 diagramů**
	- každý jiná část problematiky
	- při dodržení pravidel možno "vytvářet nové"
1) **class diagram**
2) **component diagram** - zapouzdřené třídy + jejich rozhraní
3) **object diagram** - objekty ze tříd v konkrétním čase (před/po interakci)
4) **artefact diagram** - vnitřní fyzická stránka systému (knihovny, soubory)
5) **diagram nasazení** - fyzická implementace, custom objekty (server, počítače, ...)
6) **diagram případů užití** - aktéři + co používají
7) **sekvenční diagram** - spolupráce objektů v čase
8) **komunikační diagram** - struktura objektů při zasílání zpráv (není časová osa => číslování)
9) **stavový diagram**  - změna stavu objektu při událostech
10) **diagram aktivit** - složitější případy užití (větvení atd.)
##  Diagram tříd
- Zobrazuje: třídy, rozhraní
- Jde často generovat z OOP kódu (nebo opačně)
- Pouze statická hierarchie
- Umožňuje modelovat vztahy mezi třídami
- Znaménka u atributů i metod mají význam (veřejné, privátní, protected)
- ![[Pasted image 20250423182438.png]]
## Sekvenční diagram
- Zobrazuje spolupráci objektů v času (formou zasílání zpráv obvykle)
- Obvykle se znázorňuje v rámci 1 případu užití
- Čas roste shora dolů
- ![[Pasted image 20250424084321.png|500]]
## Stavový diagram
- Zobrazuje stavový stroj daného objektu
- Dynamický pohled na systém (přechody, události, aktivity)
- Změna stavu objektu při konkrétní události
- Má konečný počet stavů (podobné konečným automatům z KMI/FJ)
- Obvykle řízen vnějším vstupem
- ![[Pasted image 20250424084512.png]]
## Diagram aktivit
- Složitější dynamické případy užití
- Zobrazuje podmínky a konkrétní hodnoty při vstupu/výstupu do/z akce
- Zobrazuje tok dat (řídící tok)
- ![[Pasted image 20250424084805.png]]