
## Polynomiální redukce
- Mějme $ANO/NE$ problémy $P_{1}, P_{2}$. Řekneme, že problém $P_{1}$ **je polynomiálně převeditelný na problém $P_{2}$**, $P_{1} \leq P_{2}$, jestliže **existuje** (převádějící) **polynomiální algoritmus $A$**, který pro libovolný vstup $w$ problému $P_{1}$ sestrojí vstup problému $P_{2}$, $A(w)$, přičemž platí, že odpověď na otázku problému $P_{1}$ pro vstup $w$ je $ANO$ právě tehdy, když odpověď na otázku problému $P_{2}$ pro vstup $A(w)$ je $ANO$.

## NP-úplný problém
- Problém $Q$ nazveme **NP-těžkým**, pokud každý problém ve tříde NP lze na problém $Q$ polynomiálně převést, tedy pokud platí $\forall P \in NPTIME:P \leq_{p} Q$.
- Problém $Q$ nazveme **NP-úplným**, pokud je NP-těžký a náleží do třídy NP

- Jestliže $P_{1} \leq_{p} P_{2}$ a $P_{1}$ je **NP-těžký**, pak $P_{2}$ **je rovněž NP-těžký**; když je navíc $P_{2}$ v NPTIME, je NP-úplný.

##### Navigace
Předchozí:  [[Třída P, třída NP, důvody jejich zavedení, jejich vzájemný vztah]]
Následující: [[Cook-Levinova věta]]
Celý okruh: [[1. Teoretické základy informatiky]]