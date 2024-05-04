### Co a k čemu jsou grafy
- Grafy představují místa a spojení mezi nimi
- Grafy mají řadu různorodých aplikací

- Teorie grafů se zabývá situacemi spojenými s grafy (**Jaký vlak si vybrat, abych byla na místě co nejrychleji?** Jak se nejrychleji dostat do školy? **Která cesta je nejkratší?**)

- **Objekty** se nazývají *vrcholy*, **spojení** pak *hrany*
- Graf je dán množinou vrcholů a množinou hran mezi nimi

- Nezáleží-li na orientaci hran, nazývá se **graf neorientovaný**, v opačném případě se nazývá **orientovaný**

### Neorientované a orientované grafy - základní pojmy
#### Neorientovaný graf
![[MacBook-2024-03-05-000788.png| 300]]
- Na obrázku je **neorientovaný graf** který má vrcholy $u, v, w, x$ a $y$
- *Vrcholy* jsou znázorněny *kroužky*. Úsečky znázorňují *hrany*.
- Protože v neorientovaném grafu **nemají hrany orientaci**, můžeme hranu mezi vrcholy reprezentovat **neuspořádanou dvojicí, tedy dvouprvkovou množinou** napr. $\{u, w\}$
#### Orientovaný graf
![[MacBook-2024-03-05-000789.png| 300]]
- Na obrázku je *orientovaný graf* který má opět vrcholy $u, v, w, x$ a $y$
- Hrany **jsou orientované** a jsou znázorněny *šipkami*. Reprezentujeme je tedy **uspořádanou dvojicí** např. $<w, u>$
---
- **Neorientovaný graf** je dvojice **$G = <V,E>$**, kde $V$ je neprázná množina vrcholů a $E \subseteq \{\{u, v\} \mid u, v \in V, u \neq v \}$ je množina dvouprvkových množin vrcholů, tzv. *neorientovaných hran*
- **Orientovaný graf** je dvojice $G = <V,E>$, kde $V$ je neprázdná množina vrcholů a $E \subseteq V \times V$ je množina uspořádaných dvojic vrcholů, tzv. *orientovaných hran*

- u $\{u, v \}$ říkáme, že hrana spojuje $u$ a $v$
- u $<u, v>$ říkáme, že hrana vede z $u$ do $v$
- u obou případů $(\{u, v \}, <u, v>)$ se nazývají vrcholy $u, v$ koncové

- **Graf $G = <V,E>$**, $V$ a $E$ se nazývají množina vrcholů a množina hran grafu $G$ a značí se $V(G)$ a $E(G)$
- Graf můžeme zadat **přímo obrázkem**, což může být přehlednější než jeho popis jakožto struktury $G = <V, E>$

- K orientovanému grafu je třeba někdy uvažovat graf, který vznikne zanedbáním orientace stran. Říká se mu **symetrizace orientovaného grafu**
- **Symetrizace orientovaného grafu** $G = <V, E>$ je **neorientovaný graf** $G' = <V, E'>$, kde
	- $\{u,v \} \in E'$ právě když $<u, v> \in E$ nebo $<v, u> \in E$

![[MacBook-2024-03-05-000790.png]]
- Graf vlevo je symetrizací grafu vpravo

### Izomorfismus
- Obrázek daného grafu není určen jednoznačně. Dva různé obrázky přitom mohou popisovat v zásadě stejné grafy, byť to na první pohled není patrné. 
- V případě, že graf je dán obrázkem, mohou se obrázky dvou v zásadě stejných grafů lišit rozmístěním vrcholů, zakreslením hran, popř. také označením vrcholů. 
- Grafy, které mají stejnou strukturu, se nazývají **izomorfní**.

- Nechť **$G_{1} = <V_{1}, E_{1}>$ a $G_{2} = <V_{2}, E_{2}>$** jsou <u>neorientované</u> grafy. **Bijekce $h: V_{1} \rightarrow V_{2}$** se nazývá *izomorfismus* $G_{1}$ do $G_{2}$, pokud pro každé vrcholy $u, v \in V_{1}$ je
	- **$\{u, v \} \in E_{1}$ právě když $\{h(u), h(v)\} \in E_{2}$**

- Nechť **$G_{1} = <V_{1}, E_{1}>$ a $G_{2} = <V_{2}, E_{2}>$** jsou <u>orientované</u> grafy. **Bijekce $h: V_{1} \rightarrow V_{2}$** se nazývá *izomorfismus* $G_{1}$ do $G_{2}$, pokud pro každé vrcholy $u, v \in V_{1}$ je
	- **$<u, v > \in E_{1}$ právě když $<h(u), h(v)> \in E_{2}$**
![[MacBook-2024-03-05-000791.png]]

### Podgrafy
- Části grafů se nazývají podgrafy
- (Orientovaný nebo neorientovaný) **graf $<V_{1}, E_{1}>$** je podgrafem grafu $<V_{2}, E_{2}>$, právě když **$V_{1} \subseteq V_{2}$ a $E_{1} \subseteq E_{2}$**. Podgraf $<V_{1}, E_{1}>$ grafu $<V_{2}, E_{2}>$ se nazývá **indukovaný**, právě když **$E_{1}$ obsahuje každou hranu z $E_{2}$**, jejíž oba **koncové vrcholy patří do $V_{1}$**
- ![[MacBook-2024-03-07-000798.png]]
- Graf uprostřed společně s grafem vpravo jsou podgrafy grafu vlevo, přitom graf uprostřed není indukovaný protože mu chybí hrana $\{u, w\}$, graf vpravo je.

### Cestování v grafech
- **Sled** v grafu $G = <V,E>$ je posloupnost $v_{0}, e_{0}, v_{1}, e_{1},  ..., v_{n}, e_{n}$ kde $v_{i} \in V$ jsou vrcholy, $e_{i} \in E$ jsou hrany a platí, že
	- $e_{i} = \{v_{i-1, v_{i}}\}$ pro $i = 1, ..., n$, je-li graf neorientovaný
	- $e_{i} = <v_{i-1, v_{i}}>$ pro $i = 1, ..., n$, je-li graf orientovaný
- Číslo $n$ se nazývá **délka sledu**

- Sled $v_{0}, e_{0}, v_{1}, e_{1},  ..., v_{n}, e_{n}$ se nazývá:
	- **uzavřený**, je-li $v_{0} = v_{n}$
	- **tah**, neopakuje-li se v něm žádná hrana
	- **cesta**, neopakuje-li se v něm žádný vrchol
	- **kružnice**, je-li tahem, $v_{0} = v_{n}$ a s výjimkou vrcholů $v_{0}$ a $v_{n}$ jsou každé dva vrcholy různé

- **vzdálenost z vrcholu $u$ do vrcholu $v$** je **délka cesty z $u$ do $v$**, které má ze všech cest z $u$ do $v$ **délku nejmenší**

##### Navigace
Předchozí:  [[Inducke a rekurze, matematická indukce a její varianty]]
Následující: [[Hledání nejkratší cesty, Dijkstrův algoritmus]]
Celý okruh: [[1. Teoretické základy informačních technologií]]