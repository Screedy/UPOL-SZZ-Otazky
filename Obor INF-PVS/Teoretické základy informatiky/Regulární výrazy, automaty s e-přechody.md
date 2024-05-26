
## Regulární výrazy
>[!info] Definice
>- Množina regulárních výrazů (regular expressions) nad abecedou $\Sigma$, označovaná $RE(\Sigma)$, je definována induktivně takto:
>	1. $\epsilon , \varnothing$ a $a$ pro každé $a \in \Sigma$ je **regulární výraz nad $\Sigma$** (tzv. základní regulární výrazy)
>	2. Jsou-li $E$. $F$ regulární výrazy nad $\Sigma$, jsou také $(E.F), (E+F)$ a $(E)^{*}$ **regulární výrazy nad $\Sigma$**
>	3. Každý regulární výraz vznikne po **konečním počtu** aplikací kroků $1$ a $2$

- Základní regulární výrazy se podobají symbolům, se kterými jsme se bězně setkávali. Tučně jsou zapsány proto, že je třeba je chápat jako symboly zcela nové; tyto "dvojníky" jsme zavedli proto, abychom mohli vždy snadno rozlišit mezi syntaxí a sémantikou regulárních výrazů.
- V regulárních výrazech se mohou vyskytovat také kulaté závorky jako metasymboly, které pomáhají vymezit rozsah operátorů. Abychom jejich použití omezili na minimum, přijmeme konvenci týkající se **priority operátorů:** Největší prioritu má "$*$", pak "$.$" a nakonec "$+$", přičemž "nadbytečné" závorky lze vypouštět.

- **Každý regulární výraz $E$ nad abecedou $\Sigma$ popisuje** (jednoznačně určuje) **jazyk $L(E)$ nad abecedou $\Sigma$** (jazyk $L(E)$ je *sémantikou regulárního výrazu $E$*) podle těchto pravidel:
	- $L(a) = \set{a}$ pro každé $a \in \Sigma$
	- $L(\epsilon) = \set{\epsilon}$
	- $L(\varnothing) = \varnothing$
	- $L(E_{1}+E_{2}) = L(E_{1}) \cup L(E_{2})$
	- $L(E_{1}.E_{2}) = L(E_{1}).L(E_{2})$
	- $L(E^{*}) = (L(E))^{*}$

>[!Example] Příklady
>$$L((a+b)^{*}(ab+bb)(a+b)^{*}) = \set{w \in (a,b)^{*} |\ w \text{ obsahuje podslovo } ab \text{ nebo } bb}$$
>$$L((aa+ab+ba+bb)^{*}) = \set{w \in \set{a,b}^{*} |\ w \text{ má sudou délku}}$$
>$$L((0^{*}1^{*}2^{*})^{*}) = \set{0,1,2}^{*}$$
>- Z výše řečeného se okamžitě nahlédne fakt, že jazyk je regulární nad $\Sigma$ právě když je popsatelný nějakým regulárním výrazem nad $\Sigma$.

- Nechť $E$ je regulární výraz. Pak existuje konečný automat rozpoznávající $L(E)$
- Nechť $L$ je akceptovaný nějakým (libovolným) DFA, pak $L$ je popsatelný nějakým regulárním výrazem.
>[!Example] Struktura převeditelnosti
>![[MacBook-2024-05-26-001346.png]]


## Nedeterministický konečný automat s $\epsilon$-přechody
- Model nedeterministického konečného automatu je možné dála rozšířit o tzv. $\epsilon$-kroky. Automat pak může svůj stav za určitých okolností změnit samovolně. Tato schopnost je formálně popsána pomocí $\epsilon$-kroků, které si lze na přechodových grafech představit jako hrany, jejichž návěštím je prázdné slovo. Přes tyto hrany může automat během výpočtu na slově $w$ měnit svůj stav bez toho, aby ze vstupu cokoliv přečetl - mezi přečtením dvou po sobě jdoucích symbolů z $w$ může provést libovolné konečné množství $\epsilon$-přechodů
>[!Example] Příklad
>- Následující automat s $\epsilon$-kroky rozpoznává právě ta slova $w \in \set{0, 1}^{*}$, která jsou tvaru $01^{k_{1}}01^{k_{2}}...01^{k_{n}}$, kde $n \geq 1$ a $k_{i} \geq 1$ pro každé $1 \leq i \leq n$:![[MacBook-2024-05-26-001347.png]]

>[!info] Definice
>- **Nedeterministický konečný automat s $\epsilon$-přechody $M$** je **uspořádaná pětice $M = (Q, \Sigma, \delta, q_{0}, F)$**
>	- $Q$ je neprázdná konečná množina stavů
>	- $\Sigma$ je konečná množina vstupních symbolů, nazývaná také vstupní abeceda
>	- $\delta$ je přechodová funkce ve tvaru $\delta : Q \times (\Sigma \cup \set{\epsilon}) \rightarrow 2^{Q}$
>	- $q_{0} \in Q$ je počáteční stav
>	- $F \subseteq Q$ je množina koncových/akceptujících stavů

- Rozšířenou přechodovou funkci $\hat{\delta}$ ovšem musíme definovat odlišným způsobem. Nejprve **zavedeme funkci** $D_{\epsilon}:Q \rightarrow 2^{Q}$, která pro daný stav $p$ vrací množinu stavů, kterých může $M$ dosáhnout z $p$ bez toho, aby četl vstup.
- Pro dané $p \in Q$ je $D_{epsilon}(p)$ nejmenší množina $X \subseteq Q$ taková, že platí:
	- $p \in X$
	- Pokud $q \in X$ a $r \in \delta(q, \epsilon)$, pak také $r \in X$.
- Funkci $D_{\epsilon}$ je možné přirozeně rozšířit na množiny stavů: je-li $Y \subseteq Q$, položíme $$D_{\epsilon}(Y) = \cup_{q \in Y} D_{\epsilon}(q)$$
- Nyní již můžeme definovat **rozšířenou přechodovou funkci** $\hat{\delta}: Q \times \Sigma^{*} \rightarrow 2^{Q}$ takto:
	- $\hat{\delta}(q, \epsilon) = D_{\epsilon}(q)$
	- $\hat{\delta}(q, wa) = \cup_{p \in \hat{\delta}(q,w)} D_{\epsilon}(\delta(p,a))$

- Jazyk přijímaný $M$ s $\epsilon$-přechody je definován takto: $$L(M) = \set{w \in \Sigma^{*} |\ \hat{\delta}(q_{0}, w) \cap F \neq 0}$$
- Ke každému NFA s $\epsilon$-přechody existuje ekvivalentní NFA (bez $\epsilon$-přechodů)

##### Navigace
Předchozí:  [[Konečné automaty deterministické a nedeterministické]]
Následující: [[Minimalizace konečného deterministického automatu]]
Celý okruh: [[1. Teoretické základy informatiky]]