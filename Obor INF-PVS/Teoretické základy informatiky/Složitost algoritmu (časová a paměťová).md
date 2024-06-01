1. **Asymptotická horní mez ($f$ roste nejvýše tak rychle jako $g$)**
	- Pro libovolné funkce $f,g: \mathbb{N} \rightarrow \mathbb{N}$ znamená zápis $f \in O(g)$ toto: $$(\exists k \in \mathbb{N})(\exists n_{0} \in \mathbb{N})(\forall n \geq n_{0}): f(n) \leq k * g(n)$$
2. **Asymptotická oboustranná mez ($f$ roste stejně rychle jako $g$)**
	- Pro libovolné funkce $f,g: \mathbb{N} \rightarrow \mathbb{N}$ zápis $f \in \Theta(g)$ znamená, že $f \in O(g)$ a $g \in O(f)$
	- Zápis $$(\exists k_{1} \in \mathbb{N})(\exists k_{2} \in \mathbb{N})(\exists n_{0} \in \mathbb{N})(\forall n \geq n_{0}): k_{1} * g(n) \leq f(n) \leq k_{2} * g(n)$$
3. **Asymptotická ostrá horní mez ($f roste pomaleji než $g$)**
	- Pro libovolné funkce $f, g : \mathbb{N} \rightarrow \mathbb{N}$ zápis $f \in o(g)$ znamená, že $$(\forall k \in \mathbb{N})(\exists n_{0} \in \mathbb{N})(\forall n \geq n_{0}): k * f(n) < g(n)$$

>[!info] Definice časové složitosti
>- **Velikost vstupu TS** rozumíme počet buněk (vstupní pásky), které daný vstup zabírá.
>- **Délka výpočtu TS $M$**  pro konkrétní vstup se definuje jako počet provedení instrukcí, které $M$ pro daný vstup vykoná, než se zastaví.
>- **Časovou složitostí TS $M$** rozumíme **funkci $T_{M} : \mathbb{N} \rightarrow \mathbb{N}$**, kde $T_{M}(n)$ znamená délku výpočtu $M$ nad vstupem velikosti $n$ v **nejhorším případě**; tedy $T_{M}(n) = \max{\set{k |\ k \text{ je délka výpočtu } M \text{ nad (nějakým) vstupem velikosti } n}}$

>[!info] Definice paměťové složitosti
>- **Velikostí paměti** TS $M$ potřebné při výpočtu pro konkrétní vstup rozumíme číslo $p+1$, kde $p$ je maximum z adres buněk, jež jsou během výpočtu (nad daným vstupem) navštíveny.
>- **Paměťovou složisostí** TS $M$ rozumíme funkci $S_{M}: \mathbb{N} \rightarrow \mathbb{N}$, kde $S_{M}(n)$ znamená velikost potřebné paměti při výpočtu $M$ nad vstupem velikosti $n$ v **nejhorším případě**; tedy $S_{M}(n) = \max{\set{k |\ k \text{ je velikost paměti potřebné při výpočtu } M \text{ nad vstupem velikosti } n}}$

- **Savitchova věta**
	- Je-li problém $P$ rozhodován **nedeterministickým** TS s prostorovou složitostí $O(n^{k})$, pak je také rozhodován **deterministickým** TS s prostorovou složitostí $O(n^{2k})$

##### Navigace
Předchozí:  [[Riceova věta]]
Následující: [[Třída P, třída NP, důvody jejich zavedení, jejich vzájemný vztah]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]