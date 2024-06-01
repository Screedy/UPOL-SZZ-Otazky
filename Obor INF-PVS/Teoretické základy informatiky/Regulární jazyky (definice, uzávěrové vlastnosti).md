- Pojem regulární jazyk jsme používali jako pojem pro jazyk přijímaný konečným automatem a též pro pojem jazyk generovaný gramatikou typu $3$.

## Definice
>[!info] Definice regulárních jazyků
>- Třída regulárních jazyků nad abecedou $\Sigma$, označovaná jako $R(\Sigma)$, je definována induktivně takto:
>	1. $\varnothing, \set{\epsilon}$ a $\set{a}$ pro každé $a \in \Sigma$ je regulární jazyk nad $\Sigma$.
>	2. Jsou-li $L_{1}, L_{2}$ regulární jazyky nad $\Sigma$, jsou také $L_{1}.L_{2}, L_{1} \cup L_{2}$ a $L_{1}^{*}$ regulární jazyky nad $\Sigma$
>	3. Každý regulární jazyk vznikne po konečném počtu aplikací kroků $1$ a $2$.
>---
>- Jinými slovy, $R(\Sigma)$ je nejmenší třída jazyků nad $\Sigma$ splňující podmínky $1$ a $2$. 
>	- Jazyky uvedení $ad\ 1$ se nazývají elementární, 
>	- operace nad jazyky uvedení $ad\ 2$ se nazývají regulární
>- Je tedy vidět, že každý regulární jazyk lze popsat určením elementárních jazyků a předpisu, který určuje jak na tyto jazyky aplikovat regulární operace.

>[!Example] Příklad regulárního jazyku
>- $L_{R} = \set{w \in \set{0,1}^{*}| w \text{ nahlíženo jako binární číslo je dělitelné } 23}$
>	- $23$ stavů pojmenovaných $0, 1, ..., 22$ - odpovídají $23$ zbytkům po dělení $23$
>	- počáteční a jediný koncový stav je $0$

>[!example] Příklad neregulárního jazyku
>- $L_{NR} = \set{0^{n}1^{n}| n \geq 1}$
>- Množina řetězců sestávajících z $n$ nul následován $n$ jedničkami takový, že $n$ je alespoň jedna



## Uzávěrové vlastnosti regulárních jazyků
- Uzávěrová vlastnost je tvrzení, že daná operace na jazycích, pokud je aplikovaná na jazyky z nějaké třídy (v tomto případě regulární jazyky), dává jako výsledek jazyk z této stejné třídy

>[!Example] Příklad použití uzávěrových vlastností
>- Dá se snadno ukázat, že jazyk $L_{1} = \set{0^{n}1^{n}| n \geq 0}$ není regulární.
>- $L_{2} =$ množina všech řetězců se stejným počtem $0$ a $1$ také není regulární, to je ale tězší dokázat.
>- Regulární jazyky jsou však uzavřeny na $\cap$. Proto pokud by byl $L_{2}$ regulární, pak $L_{2} \cap L(0^{*}1^{*})=L_{1}$, tj. $L_{1}$ by byl též regulární, ten ale není, tedy ani $L_{2}$ být nemůže.

## Součinový DFA
- K dokázání uzávěrových vlastností regulárního jazyka, je možné využít tzv. Součinový DFA
- **Součinový DFA** simuluje běh více DFA zároveň
- Máme dva DFA $A_{1} = (Q_{1}, \Sigma, \delta_{1}, q_{0,1}, F_{1})$ a $A_{2}=(Q_{2}, \Sigma, \delta_{2}, q_{0,2}, F_{2})$ **vytvoříme DFA** jako $A_{1} \times A_{2} = (Q_{1} \times Q_{2}, \Sigma, \delta ', <q_{0,1}, q_{0,2}>, F')$ kde
	- množina stavů obsahuje všechny dvojice stavů $<q_{1}, q_{2}>$, kde $q_{1} \in Q_{1}$ a $q_{2} \in Q_{2}$
	- **abeceda zůstává stejná** (oba automaty musí mít stejnou abecedu)
	- $\delta'(<q_{1}, q_{2}>, a) = <\delta_{1}(q_{1},a), \delta_{2}(q_{2},a)>$ pro všechna $a \in \Sigma$
	- počáteční stav $<q_{0,1},q_{0,2}>$ je dvojice počátečních stavů z $A_{1}$ a $A_{2}$
	- množina koncových stavů $F'$ zvolíme podle účelu $A_{1} \times A_{2}$
---
- Nechť $L_{1} = L(A_{1})$ a $L_{2}(A_{2})$, pak pro ověření:
	- $L_{1} = L_{2}$ zvolím $F'= \set{<q_{1}, q_{2}>|\ (q_{1} \in F_{1} \land q_{2} \notin F_{2}) \lor (q_{1} \notin F_{1} \land q_{2} \in F_{2})}$ a pokud $L(A_{1} \times A_{2}) = \varnothing$, pak $L_{1} = L_{2}$
	- $L_{1} \subseteq L_{2}$ zvolím $F'=\set{<q_{1}, q_{2}>|\ (q_{1} \in F_{1} \land q_{2} \notin F_{2})}$ a pokud $L(A_{1} \times A_{2}) = \varnothing$, pak $L_{1} \subseteq L_{2}$
	- $L_{1} \cap L_{2}$ zvolím $F'=\set{<q_{1}, q_{2}> |\ (q_{1} \in F_{1} \land q_{2} \in F_{2})}$
	- $L_{1} \cup L_{2}$ zvolím $F'=\set{<q_{1}, q_{2}> |\ (q_{1} \in F_{1} \lor q_{2} \in F_{2})}$
	- $L_{1} - L_{2}$ zvolím $F'=\set{<q_{1}, q_{2}> |\ (q_{1} \in F_{1} \land q_{2} \notin F_{2})}$

### Uzavřenost na sjednocení
- Pokud jsou $L$ a $M$ regulurní jazyky, pak též $L \cup M$ je regulární jazyk
- Důkaz: Již podle definice regulárních jazyků, nebo mohu sestrojit součinový DFA

### Uzavřenost na konkatenaci
- Pokud jsou $L$ a $M$ regulární jazyky, pak též $L.M$ je regulární jazyk
>[!tip]- Důkaz
>- Již podle definice regulárních jazyků, nebo![[MacBook-2024-05-25-001334.png]]

### Uzavřenost na Kleeneho uzávěr
- Pokud je $L$ regulární jazyk, pak též $L^{*}$ je regulární jazyk
>[!tip]- Důkaz
>- Již podle definice regulárních jazyků, nebo![[MacBook-2024-05-25-001335.png]]![[MacBook-2024-05-25-001336.png]]

### Uzavřenost na průnik
- Pokud jsou $L$ a $M$ regulární jazyky, pak též $L \cap M$ je regulární jazyk
>[!tip]- Důkaz
>- Mohu sestrojit součinový DFA![[MacBook-2024-05-25-001337.png]]

### Uzavřenost na rozdíl
- Pokud jsou $L$ a $M$ regulární jazyky, pak též $L-M$ je regulární jazyk
>[!tip]- Důkaz
>- Mohu sestrojit součinový DFA![[MacBook-2024-05-25-001338.png]]

### Uzavřenost na komplement
- Pokud je $L$ regulární jazyk, pak též co-$L$ je regulární jazyk
>[!tip]- Důkaz
>- Lze uvést konstruktivní důkaz:
>	- Nechť $L$ je regulární jazyk nad abecedou $\Sigma$, rozpoznávaný deterministickým  konečným automatem $A=(Q, \Sigma, \delta, q, F)$. 
>	- Pak jazyk co-$L$ je rozpoznávaný konečným automatem co-$L=(Q, \Sigma, \delta, q, Q-F)$

### Uzavřenost na reverz
- Pokud je $L$ regulární jazyk, pak též $L^{R}$ je regulární jazyk
>[!tip]- Důkaz
>- Nechť $E$ je regulární výraz pro $L$, ukážeme, jak reverzovat $E$, čímž sestrojíme regulární výraz $E^{R}$ pro $L^{R}$
>	- Základ: Pokud je $E$ symbol $a, \epsilon,$ či $\varnothing$, pak $E^{R} = E$
>	- Indukce: Pokud je $E$
>		- $F+G$, pak $E^{R} = F^{R} + G^{R}$
>		- $FG$, pak $E^{R} = G^{R}F^{R}$
>		- $F^{*}$, pak $E^{R} = (F^{R})^{*}$

### Uzavřenost na homomorfismus
- Pokud je $L$ regulární jazyk a $h$ homomorfismus na jeho abecedě, pak $h(L) = \set{h(w) |\ w \text{ je v } L}$ je též regulární jazyk
- Důkaz u inverzního homomorfismu

### Uzavřenost na inverzní homomorfismus
- Třída regulárních jazyků je uzavřena vůči homomorfismu a inverznímu homomorfismu
- Nechť $h$ je homomorfismus a $L$ jazyk, jehož abeceda je výstupní jazyk $h$
- $h^{-1}(L) = \set{w |\ h(w) \text{ leží v } L}$
>[!tip]- Důkaz
>- ![[MacBook-2024-05-25-001339.png]]

##### Navigace
Předchozí:  [[Formální jazyky a jejich hierarchie]]
Následující: [[Konečné automaty deterministické a nedeterministické]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]