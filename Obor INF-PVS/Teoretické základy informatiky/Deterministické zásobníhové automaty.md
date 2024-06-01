- Řekneme, že PDA $M = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ je **deterministický**, jestliže jsou splněny tyto podmínky:
	1. Pro všechny $q \in Q, Z \in \Gamma$ platí: **kdykoliv $delta(q, \epsilon, Z) \neq \varnothing$, pak $\delta(q, a, Z) = \varnothing$** pro všechna $a \in \Sigma$
	2. Pro všechny $q \in Q, Z \in \Gamma$ a $a \in \Sigma \cup \set{\epsilon}$ **neobsahuje $delta(q, a, Z)$ více než jeden prvek**
- Podmínka 1 vylučuje možnost volby mezi krokem nezávislým na vstupním symbolu ($\epsilon$-krokem) a krokem, kdy se ze vstupu čte.
- Podmínka 2 říká, že je jak v případě čtecího kroku, tak i pro $\epsilon$-krok, neexistuje více než jedna varianta, jak dále pokračovat
- Řekneme, že $L$ je **deterministický bezkontextový jazyk** (DCFL), právě když existuje DPDA $M$ takový, že $L=L(M)$

## Normální forma (D)PDA
- Řekneme, že DPDA $M = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ je **v normální formě** jestliže platí:
	- Je-li $delta(q, a, X) = (p, \gamma)$, pak buď
		a. $\gamma = \epsilon$
		b. $\gamma = X$
		c. $\gamma = YX$ pro nějaké $Y \in \Gamma$.
- Identicky lze definovat normální formu i pro nedeterministický PDA. Uvedená normální forma tedy požaduje, aby jediné povolené operace nad zásobníkem byly 
	- **odstranění vrcholového symbolu** ze zásobníku podmínka (a) nebo 
	- **přidání jednoho symbolu na vrchol zásobníku**, podmínka (c),
	- podmínka (b) povoluje **změnit pouze vnitřní stav**, a to bez změny zásobníku.

##### Navigace
Předchozí:  [[Zásobníkové automaty]]
Následující: [[Deterministické bezkontextové jazyky]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]