- Třídění haldou (hromadou)
- Využívá datovou strukturu zvanou **halda**
	- **(Binární) halda =** pole, ve kterém uložení prvků simuluje jejich přirozené uložení v binárním stromu
- Složitost algoritmu v nejhorším případě: $\Theta (n \log n)$
- Pole $A[0 ... n-1]$ se nazývá **max-halda**, pokud pro každý $i = 1, ..., n-1$ platí, že $A[i] \leq A[\text{Parent}(i)]$
- Pole $A[0 ... n-1]$ se nazývá **min-halda**, pokud pro každý $i = 1, ..., n-1$ platí, že $A[i] \geq A[\text{Parent}(i)]$

![[MacBook-2024-03-11-000847@2x.png | 700]]

### Odůvodnění složitosti Heap Sort
**[https://www.youtube.com/watch?v=6WTL8Vkn90U](https://www.youtube.com/watch?v=6WTL8Vkn90U)**
