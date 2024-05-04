### Counting Sort
- Algoritmus třídění, který využívá jinou informaci než porovnávání
- Lze použít pouze pro třídění celých čísel $0 ... k$
- Idea:
	- $A[0 ... n-1]$ - pole vstupní
	- $B[0 ... n-1]$ - pole výstupní
	- $C[0 ... k]$ - pole pomocné
- Složitost algoritmu v nejhorším případě: $\Theta (k+n)$
- **stabilní** algoritmus počítání
```C
Counting-Sort(A, B, k)
	for i <- 0 to k
		do C[i] <- 0
	for j <- 0 to n-1
		do C[A[j]] <- C[A[j]]+1  // C[i] obsahuje počet prvků v A rovných i
	for i <- 1 to k
		do C[i] <- C[i] + C[i-1] // C[i] obsahuje počet prvků v A <= i
	for j <- n-1 downto 0
		do B[C[A[j]]-1] <- A[j]
		   C[A[j]] <- C[A[j]]-1
```
#### Výpočet složitosti v nejhorším případě
- řádek $1-2: \Theta (k)$ instrukcí.
- řádek $3-4: \Theta (n)$ instrukcí.
- řádek $5-6: \Theta (k)$ instrukcí.
- řádek $7-9: \Theta (n)$ instrukcí.
- Tedy složitost Counting Sort je v nejhorším případě $\Theta (k + n)$.
- Je-li $k=O(n)$ (tedy $k \leq cn$ pro $c > 0$), je poté složitost v nejhorším případě $\Theta (n)$
>[!Example]- Příklad
><iframe width="620" height="385" src="https://www.youtube.com/embed/EItdcGhSLf4?si=RO0qIakGyg1kTm0k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Radix Sort
- Používali operátoři mechanických třídič děrných štítků
- Idea:
	- Třídíme $d$-místná čísla.
	- Třídění proběhne v $d$ průchodech.
		- V $1.$ průchodu se čísla setřídí podle jejich poslední číslice, 
		- v $2.$ podle předposlední, 
		- ...
- Lze jej využít i na třídění textových řetězců, data ve tvaru rok-měsíc-den, ...
- Složitost algoritmu v nejhorším případě: $\Theta (d(\text{složitost vnitřního algoritmu})$
```C
Radix-Sort(A, d)
	for i <- 1 to d
		do Stable-Sort(A, i)
```

>[!Example]- Příklad
>![[MacBook-2024-03-11-000850.png]]

#### Výpočet složitosti v nejhorším případě
- řádek $1$: $\Theta (d)$ instrukcí
- řádek $2:$ $\Theta (\text{Stable-Sort})$ instrukcí

### Bucket Sort
- Třídí čísla z intervalu $<0, 1)$
- Idea:
	- Projdeme prvky pole $A$ a každý z nich vložíme do příslučného intervalu *(do příslušného seznamu $B[i]$).*
	- Každý seznam setřídíme.
	- Prvky setříděných seznamů vložíme po řadě do výstupního pole
- Složitost algoritmu v nejhorším případě je: $\Theta (f(n))$
- Složitost v průměrném případě je $\Theta (n)$
```C
Bucket-Sort(A[0 ... n-1])
	for i <- 0 to n-1
		do vlož A[i] do seznamu B[floor(n*A[i])]
	for i <- 0 to n-1
		do Sort(B[i])
	vlož postupně prvky z B[0], ..., B[n-1] do pole A
```
>[!Example]- Příklad
><iframe width="690" height="385" src="https://www.youtube.com/embed/VuXbEb5ywrU?si=pyK3NrE4iY3oNip9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Výpočet složitosti v nejhorším případě
- To je případ, když všechny prvky z $A$ byly umístěny do jednoho seznamu $B[i]$
- Složitost bucket Sortu tedy je: $\Theta (n) + \Theta (f(n)) + \Theta (n) = \Theta (f(n))$


##### Navigace
Předchozí:  [[Heap sort a jeho složitost]]
Následující: [[Pořádkové statistiky]]
Celý okruh: [[1. Teoretické základy informačních technologií]]