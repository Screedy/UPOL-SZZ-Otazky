
### Základní pojmy pro porovnání růstu funkcí
- $O(g)$ ... **Asymptotická horní mez**
	- používána se pro popis **horního limitu** růstu funkce
	- $O(g(n)) = \{ f(n) \mid (\exists c \in \mathbb{N}) (\exists n_{0} \in \mathbb{N})(\forall n \geq n_{0}): 0 \leq f(n) \leq c \cdot g(n)\}$ 
	- **Asymptotická horní mez funkce $g(n)$** je množina funkcí $f(n)$, takových, že **existuje** přirozené číslo $c > 0$ a existuje přirozené číslo $n_{0}$ tak, že **pro každé** $n \geq n_{0}$ platí $0 \leq f(n) \leq c \cdot g(n)$
	- ![[MacBook-2024-05-13-001247@2x.png | 250]]

- $\Omega(g)$ ... Asymptotická dolní mez
	- $\Omega (g(n)) = \{ f(n) \mid (\exists c \in \mathbb{N})(\exists n_{0} \in \mathbb{N})(\forall n \geq n_{0}): 0 \leq c \cdot g(n) \leq f(n) \}$
	- **Asymptotická dolní mez funkce $g(n)$** je množina funkcí $f(n)$, takových že **existuje** přirození číslo $c > 0$ a **existuje** přirozené číslo $n_{0}$ tak, že **pro každé** $n \geq n_{0}$ platí: $0 \leq c \cdot g(n) \leq f(n)$
	- ![[MacBook-2024-05-13-001245@2x.png | 250]]

- $\theta (g)$ ... **Asymptotická oboustranná mez**
	- popisuje těsnější popis chování funkce
	- $\theta (g(n)) = \{f(n) \mid (\exists c_{1} \in \mathbb{N})(\exists c_{2} \in \mathbb{N})(\exists n_{0} \in \mathbb{N})(\forall n \geq n_{0}): 0 \leq c_{1} \cdot g(n) \leq f(n) \leq c_{2} \cdot g(n)\}$
	- **Asymptotická oboustranná mez funkce $g(n)$** je množina funkcí $f(n$, takových, že **existují** přirozená čísla $c_{1} > 0$ a $c_{2} > 0$ a **existuje** přirozené číslo $n_{0}$ takové, že **pro každé** $n \geq n_{0}$ platí: $0 \leq c_{1} \cdot g(n) \leq f(n) \leq c_{2} \cdot g(n)$
	- Věta: $f(n) \in \theta (g(n))$ právě když $f(n) \in O(g(n))$ a $f(n) \in \Omega (g(n))$
	- ![[MacBook-2024-05-13-001246@2x.png | 250]]

- $o(g)$ ... **Asymptotická ostrá horní mez**
	- $o(g(n)) = \{ f(n) \mid (\forall c \in \mathbb{N})(\exists n_{0} \in \mathbb{N})(\forall n \geq n_{0}): 0 <f(n) < c \cdot g(n) \}$
	- **Asymptotická ostrá horní mez funkce $g(n)$** je množina funkcí $f(n)$, takových, že **pro každé** přirozené číslo $c > 0$ **existuje** přirozené číslo $n_{0}$ tak, že **pro každé** $n \geq n_{0}$ platí: $0 <  f(n) < c \cdot g(n)$

- $\omega (g)$ ... Asymptotická ostrá dolní mez
	- $\omega (g(n)) = \{ f(n) \mid (\forall c \in \mathbb{N})(\exists n_{0} \in \mathbb{N})(\forall n \geq n_{0}): 0 < c \cdot g(n) < f(n) \}$
	- **Asymptotická ostrá dolní mez funkce $g(n)$** je množina funkcí $f(n)$, takových, že **pro každé** přirozené číslo $c > 0$ **existuje** přirozené číslo $n_{0}$ tak, že **pro každé** $n \geq n_{0}$ platí: $0 < c \cdot g(n) < f(n)$

### Základní pravidla (vlastnosti)
#### Věta o tranzitivitě odhadů
- Pokud $f = O(g)$ a $g = O(h)$, pak $f = O(h)$.
- Pokud $f = \Omega (g)$ a $g = \Omega (h)$, pak $f = \Omega (h)$.
- Pokud $f = \Theta (g)$ a $g = \Theta (h)$, pak $f = \Theta (h)$.
- Pokud $f = o(g)$ a $g = o(h)$, pak $f = o(h)$.
- Pokud $f = \omega (g)$ a $g = \omega (h)$, pak $f = \omega (h)$.

#### Věta o reflexivitě odhadů
- $f = O(f)$.
- $f = \Omega (f)$.
- $f = \Theta (f)$.

#### Věta o symetrii odhadů
- $f = \Theta (g)$ právě když $g = \Theta (f)$.

#### Věta o symetrii horních a dolních odhadů
- $f = O(g)$ právě když $g = \Omega (f)$.
- $f = o(g)$ právě když $g = \omega (f)$.

## Big-O Complexity chart
![[MacBook-2024-04-29-001106.png]]

<iframe width="690" height="385" src="https://www.youtube.com/embed/__vX2sjlpXU?si=E-RiU8rWlfMJvZvC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### Navigace
Předchozí:  [[Algoritmus, problém, časová složitost algoritmu v nejhorším a průměrném případě]]
Následující: [[Lineární datové struktury - seznam, zásobník, fronta]]
Celý okruh: [[1. Teoretické základy informačních technologií]]