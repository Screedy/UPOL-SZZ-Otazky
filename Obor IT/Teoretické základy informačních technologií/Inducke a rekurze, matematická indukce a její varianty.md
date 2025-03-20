## Co to je indukce a rekurze
- **Inducke a rekurze** jsou důležité a navzájem provázané jevy
- Zatímco pro **indukci** je charakteristický **postup od menšího k většímu**, tedy přístup *zdola nahoru*, pro **rekurzi** je to naopak, tedy přístup *shora dolů*.
```C
f(n)
	if n = 1 then return 1
	else return n * f(n-1)
```
- Protože se v těle této procedury pro výpočet `f(n)` využívá `f` (na řádku $2$), řádek $1$ obsahuje tzv. **ukončující podmínku**. Bez ní by se procedura nezastavila (zacyklila by se).
- Proceduru lze popsat jinak následovně: 
$$
f(n)=
\begin{cases}
1 & \text{pokud } n = 1, \\
n\ \cdot f(n-1) & \text{pokud } n > 1.
\end{cases}
$$
- Na uvedenou proceduru se lze dívat jako na proceduru, která vychází z **induktivní definice:**
	- faktoriál definujeme nejprve pro základní prvky (pro $n = 1$),
	- pro složitější prvky ($n > 1$) definujeme faktoriál pomocí toho, co jsme definovali pro jednodušší prvky ($f(n-1)$).
- Uvažujme nyní následující proceduru pro výpočet faktoriálu:
```C
f(n)
	if n > 1 then return n * f(n-1)
	else return 1
```
- Od první uvedení procedury *definice se liší jen v pořadí podmínek*. Zatímco **první procedura má induktivní charakter** (zdola nahoru), právě uvedená **procedura popisuje** faktoriál **přístupem shora dolů**.

## Matematická indukce
- Umožňuje dokazovat tvrzení tvaru
	- "pro každé přirození číslo $n$ platí $V(n)$, kde $V(n)$ je nějaké tvrzení, které závisí na $n$".
- Základem dokazování matematickou indukcí je následující tvrzení (**princip indukce**):
	- Nechť je pro každé $n \in \mathbb{N}$ dáno tvrzení $V(n)$.
	- Předpokládejme, že platí
		1. $V(1)$ (indukční předpoklad)
		2. pro každé $n \in \mathbb{N}$: z $V(n)$ plyne $V(n+1)$ (indukční krok).
		Pak $V(n)$ platí pro každé $n \in \mathbb{N}$.

### Definice matematickou indukcí
- Vraťme se k definici faktoriálu:
	1. `pro n = 1 je f(n) = 1`
	2. `pro n > 1 je f(n) = n * f(n - 1)`
- Intuitivně je jasné, že tímto způsobem je jednoznačně definována jistá funkce. 
- Z čeho ale plyne že funkce splňující podmínky $1$ a $2$ z uvedené definice existuje a je určena jednoznačně?
	- **Věta:** Nechť je dána množina $V$, prvek $a \in V$ a funkce $G: \mathbb{N} \times V \rightarrow V$. Pak existuje právě jedna funkce $F: \mathbb{N} \rightarrow V$, pro kterou platí
		1. $F(1) = a,$
		2. pro každé $n \in \mathbb{N}$: $F(n+1)=G(n,F(n))$

## Strukturální indukce
- Strukturální indukce je **zobecněním matematické indukce**. Místo množiny $\mathbb{N}$, se kterou pracuje matematická indukce, pracuje strukturální indukce s množinou $T$ **jistých objektů**.
- Základní myšlenky strukturální indukce jsou následující:
	- $T$ je zpravidla množina řetězců utvořených podle induktivních pravidel.
		- Například **formule**:
			- (atomické) $p \in T$ pro každý výrokový symbol $p$;
			- (složené) pokud $\phi, \psi \in T$, pak: 
			  $$ 
				\begin{aligned}
				\neg\phi \in T, \\
				(\phi \land\psi) \in T, \\
				(\phi \lor \psi) \in T, \\
				(\phi \rightarrow \psi) \in T, \\
				(\phi \leftrightarrow \psi) \in T.
				\end{aligned}
			    $$

### Definice strukturální indukcí
- Definice strukturální indukcí je zobecněním definice matematickou indukcí
- Chceme definovat nějaký objekt pro každý prvek z množiny $T$. To uděláme následovně:
	- definujeme pro atomické prvky $T$,
	- definujeme pro složené prvky $T$.
##### Navigace
Předchozí:  [[Pravděpodobnost, Laplaceova definice, pravděpodobnostní prostor, náhodná veličina, střední hodnota, vlastnosti pravděpodobnosti]]
Následující: [[Orientované a neorientované grafy, základní pojmy]]
Celý okruh: [[1. Teoretické základy informačních technologií]]