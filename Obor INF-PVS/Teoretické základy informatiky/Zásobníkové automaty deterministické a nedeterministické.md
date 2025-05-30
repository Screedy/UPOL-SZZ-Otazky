## Zásobníkový automat (PDA)
- *Push down automata*
- Lze si je představit jako konečný automat s tím, že navíc obsahuje (pomocnou) paměť, která pracuje jako zásobník a jejíž velikost není shora omezená
- Přijímají (jako CFG) bezkontextové jazyky

>[!info] Definice nedeterministického zásobníkového automatu
>- **Nedeterministický zásobníkový automat** (PDA) je sedmice $M = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$, kde:
>	- $Q$ je konečná množina, jejíž prvky nazýváme stavy
>	- $\Sigma$ je konečná množina, tzv. vstupní abeceda
>	- $\Gamma$ je konečná množina, tzv. zásobníková abeceda
>	- $\delta : Q \times (\Sigma \cup \set{\epsilon}) \times \Gamma \rightarrow 2^{Q \times \Gamma}$ je přechodová funkce
>		- Stavu, vstupnímu symbolu a symbolu na vrcholu zásobníku přiřadí množinu dvojic skládajících se ze stavu a řetězce zásobníkových symbolů
>	- $q_{0} \in Q$ je počáteční stav
>	- $Z_{0} \in \Gamma$ je počáteční symbol v zásobníku
>	- $F \subseteq Q$ je množina koncových stavů

#### Konfigurace
- Nechť $M = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ je PDA.
- **Vnitřní konfigurací** $M$ nazveme libovolný prvek $(q, \gamma) \in Q \times \Gamma^{*}$, kde $q$ je **momentální stav** PDA $M$ a $\gamma$ je **celý obsah zásobníku** s vrcholem psaným vlevo.
- **Konfigurací** nazveme trojici $(p, w, a)$ z $Q \times \Sigma^{*} \times \Gamma^{*}$, udávající mimo vnitřní konfigurace navíc i $w$ - **dosud nepřečtenou část vstupního řetězu**.

- Na množině všech konfigurací automatu $M$ definujeme binární relaci $\vdash_{M}$, **krok výpočtu** takto: $$(p, aw, Za) \vdash_{M} (q, w, \gamma a) \Leftrightarrow^{def} \exists(q,\gamma) \in \delta(p, a, Z) \text{ pro } a \in \Sigma \cup \set{\epsilon}$$ Reflexivní a tranzitivní uzávěr relace kroku výpočtu značíme $\vdash_{M}^{*}$

- **Jazyk akceptovaný PDA $M$ koncovým stavem** definujeme jako $$L(M)=\set{w \in \Sigma^{*} |\ (q_{0}, w, Z_{0} \vdash^{*} (q_{f}, \epsilon, a), \text{ kde } q_{f} \in F, a \in \Gamma^{*})}$$
- **Jazyk akceptovaný PDA $M$ prázdným zásobníkem** definujeme jako $$L_{e}(M)=\set{w \in \Sigma^{*} |\ (q_{0}, w, Z_{0}) \vdash^{*} (q, \epsilon, \epsilon), \text{ kde } q \in Q}$$
- Jazyk $L=L_{e}(M)$ pro nějaký PDA $M \Leftrightarrow L=L(N)$ pro nějaký PDA $N$
#### Deterministický PDA
- Řekneme, že PDA $M = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ je **deterministický**, jestliže jsou splněny tyto podmínky:
	1. Pro všechny $q \in Q, Z \in \Gamma$ platí: **kdykoliv $\delta(q, \epsilon, Z) \neq \varnothing$, pak $\delta(q, a, Z) = \varnothing$** pro všechna $a \in \Sigma$
	2. Pro všechny $q \in Q, Z \in \Gamma$ a $a \in \Sigma \cup \set{\epsilon}$ **neobsahuje $\delta(q, a, Z)$ více než jeden prvek**
- Podmínka 1 vylučuje možnost volby mezi krokem nezávislým na vstupním symbolu ($\epsilon$-krokem) a krokem, kdy se ze vstupu čte.
- Podmínka 2 říká, že je jak v případě čtecího kroku, tak i pro $\epsilon$-krok, neexistuje více než jedna varianta, jak dále pokračovat
- Řekneme, že $L$ je **deterministický bezkontextový jazyk** (DCFL), právě když existuje DPDA $M$ takový, že $L=L(M)$
## Normální forma (D)PDA
- Řekneme, že DPDA $M = (Q, \Sigma, \Gamma, \delta, q_{0}, Z_{0}, F)$ je **v normální formě** jestliže platí:
	- Je-li $\delta(q, a, X) = (p, \gamma)$, pak buď
		a. $\gamma = \epsilon$
		b. $\gamma = X$
		c. $\gamma = YX$ pro nějaké $Y \in \Gamma$.
- Identicky lze definovat normální formu i pro nedeterministický PDA. Uvedená normální forma tedy požaduje, aby jediné povolené operace nad zásobníkem byly 
	- **odstranění vrcholového symbolu** ze zásobníku podmínka (a) nebo 
	- **přidání jednoho symbolu na vrchol zásobníku**, podmínka (c),
	- podmínka (b) povoluje **změnit pouze vnitřní stav**, a to bez změny zásobníku.

##### Navigace
Předchozí:  [[Bezkontextové jazyky a jejich vlastnosti (uzávěrové vlastnosti, jednoznačnost)]]
Následující: [[Turingův stroj (TS), nedeterministický TS]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]