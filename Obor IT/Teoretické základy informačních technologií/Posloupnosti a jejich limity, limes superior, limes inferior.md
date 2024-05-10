## Posloupnost
- Každé zobrazení $\mathbb{N}$ do $\mathbb{R}$ nazýváme **číselná posloupnost**.
- Zapisujeme $(a_{n})^{\infty}_{x=1}$ nebo jen $(a_{n})$

### Způsoby zadání posloupnosti
- Číselná posloupnost bývá zadána:
	1. **Několika prvními členy** $$\frac{1}{1 \cdot 4}, \frac{3}{4 \cdot 7}, \frac{5}{7 \cdot 10}, \frac{7}{10 \cdot 13}, ...$$
	2. **n-tým členem** $$\left(\frac{n}{n+1}\right), \left( (-1)^{n}n \right), \left( \left(1 + \frac{1}{n}\right)^{n} \right)$$
	3. **rekurentně**
		- Obsahuje zpravidla $1.$ člen a pravidlo, jak vytvořit další člen ze členů předcházejících $$a_{1} = 1,\ \ a_{n+1}=\frac{1}{2} \left( a_{n} + \frac{10}{a_{n}} \right)$$

### Podposloupnost
- Posloupnost $(b_{n})$ se nazývá **podposloupnost** $(a_{n})$, právě když existuje posloupnost přirozených čísel $k_{1} < k_{2} < k_{3} < ...$ tak, že $\forall{n \in N}$ je $b_{n} = a_{kn}$.