## Turingův stroj (TS)
- Podobný konečným automatům
- Rozdíly jsou v nekonečné pásce, možnosti pohybu hlavy na obě strany, hlava i zapisuje, znaky se mohou přepisovat
>[!info] Definice Turingova stroje
>- Turingův stroj je definován jako **šestice $M = (Q, \Sigma, \Gamma, \delta, q_{0}, F)$**, kde
>	- $Q$ je konečná neprázdná množina stavů,
>	- $\Sigma$ je konečná neprázdná množina vstupních symbolů,
>	- $\Gamma$ je neprázdná množina páskových symbolů, kde $\Sigma \subseteq \Gamma$ a v $\Gamma - \Sigma$ je (přinejmenším) speciální znak $\square$ (prázdný znak \[blank\])
>	- $q_{0} \in Q$ je počáteční stav
>	- $F \subseteq Q$ je množina koncových stavů
>	- $\delta : (Q-F) \times \Gamma \rightarrow Q \times \Gamma \times \set{-1,0,+1}$ je přechodová funkce

- Význam instrukce $(q, a) \rightarrow (q', a', m)$ je tento:
	- Tato instrukce je aplikovatelná v konfiguraci, kdy řídící jednotka je ve stavu $q$ a hlava čte na pásce symbol $a$
	- Vykonání instrukce znamená následující:
		- řídící jednotka přejde do stavu $q'$,
		- hlava zapíše do aktuálně čtené buňky symbol $a'$,
		- je-li
			- $m=+1$, hlava se posune na sousední buňku pásky doprava,
			- $m=-1$, hlava se posune na sousední buňku pásky doleva,
			- $m=0$, hlava se nikam neposune
- Turingův stroj svůj výpočet **po dosažení koncového stavu končí**

- **Konfigurace** TS je dána
	1) Stavem řídící jednotky
	2) Obsahem pásky
	3) Pozicí hlavy
#### Nedeterministický TS
>[!info] Definice NTS
>- **Nedeterministický Turingův stroj (NTS)** je dán stejnými složkami jako deterministický Turingův stroj (TS) až na přechodovou funkci.
>	- Jiná definice přechodové funkce $\delta : Q \times \Gamma \rightarrow 2^{Q \times \Gamma \times \set{-1,0,+1}}$
- Nedeterministický algoritmus $A$ rozhoduje ANO/NE problémy $P$, jestliže:
	1) Pro vstup problému $P$, na nějž je odpověď ANO, **alespoň jeden výpočet** nedeterministického algoritmu $A$ vydá ANO.
	2) Pro vstup problému $P$, na nějž je odpověď NE, **každý výpočet** nedeterministického algoritmu $A$ vydá NE.
- Výpočet NTS tvoří **strom výpočtů**![[MacBook-2024-05-29-001401.png]]
- Činnost nedeterministického TS je možné snadno simulovat pomocí deterministického algoritmu tak, že deterministický algoritmus systematicky simuluje činnost všech jednotlivých větví výpočtu (prochází strom výpočtu do hloubky)

##### Navigace
Předchozí:  [[Zásobníkové automaty deterministické a nedeterministické]]
Následující: [[Jazyk přijímaný TS, jazyk rozhodovaný TS]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]