## Konfigurace
- **Konfigurace** Turingova stroje je dána
	- stavem řídící jednotky
	- obsahem pásky
	- pozicí hlavy
- **Konkrétní konfiguraci** stroje $M = (Q, \Sigma, \Gamma, \delta, q_{0}, F)$ popíšeme trojicí
	- $(u, q, v)$, či zkráceně $uqv$, kde $u,v \in \Gamma^{*}$ a $q \in Q$
- **Počáteční konfigurace** stroje $M$ pro vstup $w \in $\Sigma^{*}$ je konfigurace $q_{0}w$
- **Akceptující konfigurace** stroje $M$ pro vstup $w \in \Sigma^{*}$ je např. $wq_{Accept}$
- **Zamítající konfigurace** stroje $M$ pro vstup $w \in \Sigma^{*}$ je např. $wq_{Reject}$

## Výpočet
- **Výpočet Turingova stroje** $M = (Q, \Sigma, Gamma, \delta, q_{0}, F)$ na vstupním slově $w \in \Sigma^{*}$ chápeme jako **posloupnost konfigurací** $C_{0}, C_{1}, C_{2}, ...$ kde $C_{0}$ je iniciální konfigurace $q_{0}w$ a pro $i = 0,1,2,...$ máme $C_{i} \vdash_{M} C_{i+1}$ (tedy $C_{i+1}$ dostaneme z $C_{i}$ jedním krokem, aplikací přechodové funkce $\delta$). Výpočet může skončit v **koncové konfiguraci**, nebo být **nekonečný**.
- Stroj $M$ **akceptuje vstupní řetězec $w \in \Sigma^{*}$** právě když výpočet $M$ na $w$ je **konečný** a poslední konfigurace je **akceptující**.
- Stroj $M$ **zamítá vstupní řetězec $w \in \Sigma^{*}$** právě když výpočet $M$ na $w$ je **konečný** a poslední konfigurace je **zamítající**.
- Množinu všech slov $w \in \Sigma^{*}$, které **TS $T$ přijímá = akceptuje**, značíme $L(T)$.
- Jazyk $L(T)$ nazýváme **jazyk částečně rekurzivní = akceptovaný** TS $T$.
- Pokud navíc platí, že TS $T$ **zamítá** každé slovo, které **nepatří** do $L(T)$, nazýváme jazyk $L(T)$ **jazyk rekurzivní = rozhodovaný** TS $T$.

##### Navigace
Předchozí:  [[Turingův stroj, nedeterministický TS]]
Následující: [[Church-Turngova teze, varianty TS]]
Celý okruh: [[1. Teoretické základy informatiky]]