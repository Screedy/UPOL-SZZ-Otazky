### Insertion Sort
- **Třídění vkládáním**
- Idea algoritmu je založena na **třídění $n$ rozdaných karet**
- Složitost algoritmu v nejlepším případě: $\Theta (n)$ (vstupní pole už je setříděné)
- Složitost algoritmu v nejhorším případě: $\Theta (n^{2})$ (vstupní pole je setříděné naopak)
- **In-place** třídění (prostorová složitost $\Theta(1)$)
- **Stabilní** třídící algoritmus
```C
Insertion-Sort(A[0 ... n-1])
	for j <- 1 to n-1
		do t <- A[j]
		   i <- j-1
		   while i >= 0 and A[i] > t
			   do A[i+1] <- A[i]
			      i <- i-1
		   A[i+1] <- t
```

>[!Example]- Příklad
><iframe width="660" height="385" src="https://www.youtube.com/embed/JU767SDMDvA?si=Fa9zf5Szl6VcFWMY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Selection Sort
- Idea *"Najdi nejmenší prvek v poli a vyměň ho"*
	- min z $A[0 ... n-1] \rightarrow A[0]$
	- min z $A[1 ... n-1] \rightarrow A[1]$
	- $...$
	- min z $A[n-2 ... n-1] \rightarrow A[n-2]$
- Složitost algoritmu v nejhorším i v nejlepším případě je $\Theta (n^{2})$
- **In-place** třídění (prostorová složitost $\Theta(1)$)
- **Nestabilní** třídící algoritmus
```C
Selection-Sort(A[0 ... n-1])
	for j <- 0 to n-2
		do iMin <- j
		   for i <- j+1 to n-1
				do if A[i] < A[iMin] then iMin <- i
		   t <- A[j]; A[j] <- A[iMin]; A[iMin] <- t
```

>[!Example]- Příklad
><iframe width="660" height="385" src="https://www.youtube.com/embed/g-PGLbMth_g?si=vfjcGbP2lhtcWpIX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Bubble Sort
- Bublinkové třídění
- Nejmenší prvek *"**probublá**"* vlevo, pak *"**probublá**"* druhý nejmenší prvek ...
- Další varianty Bubble Sort:
	- **Optimalizace vynecháním některých průchodů**
	- **Cocktail Sort**
- Složitost algoritmu v nejhorším případě: $\Theta (n^{2})$
- **In-place** třídění (prostorová složitost $\Theta(1)$)
- **Stabilní** třídící algoritmus
```C
Bubble-Sort(A[0 ... n-1])
	for j <- 0 to n-2
		do for i <- n-1 downto j+1
			do if A[i] < A[i-1]
			   then temp <- A[i]; A[i] <- A[i-1]; A[i-1] <- temp
```

>[!Example]- Příklad
><iframe width="660" height="385" src="https://www.youtube.com/embed/xli_FI7CuzA?si=lSIQxg8Uo_cko_-i" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


##### Navigace
Předchozí:  [[Problém třídění, rozdělení třídících algoritmů, dolní mez složitosti třídění porovnáváním]]
Následující: [[Quick sort a jeho složitost]]
Celý okruh: [[1. Teoretické základy informačních technologií]]