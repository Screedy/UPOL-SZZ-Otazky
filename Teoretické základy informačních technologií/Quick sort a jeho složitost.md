- Algoritmus typu **"rozděl a panuj"** *(divide and conquer)*
	- Fáze "rozděl":
		- Zvolí se pivot $q$
		- Přemístí se prvky tak $A[p ... q - 1] \leq A[q]$ a $A[q + 1 ... r] \geq A[q]$
	- Fáze "panuj":
		- Setřídí se části $A[p ... q - 1]$ a $A[q + 1 ... r] \rightarrow$ **znovu zavolání** QuickSort
- Jedná se o tzv. **rekurzivní algoritmus**.
	- Při provádění algoritmu QuickSort (ve fázi "panuj") se *volá* sám QuickSort. 
	- To **nevede k zacyklení**, protože algoritmus je *volán* pro **stále kratší části** pole $A$. 
	- Při volání pro část tvaru **$A[p ... p]$** se provádění **okamžitě ukončí**. 
- Složitost algoritmu v průměrném případě: $\Theta (n \log n)$
- Složitost algoritmu v nejhorším případě: $\Theta (n^{2})$ 
	- prázdná pravá/levá část (pivot je vždy úplně na straně)
- **In-place** třídění
- **Nestabilní** třídící algoritmus
```C
Quick-Sort(A, p, r)
	if p<r
		then q <- Partition(A, p, r)
		     Quick-Sort(A, p, q-1)
		     Quick-Sort(A, q+1, r)
```
```C
Partition(A, p, r)
	x <- A[r]
	i <- p-1
	for j <- p to r-1
		do if A[j] <= x
			then i <- i+1
			     swap(A[i], A[j])
	swap(A[i+1], A[r])
	return i+1
```
Příklad:
<iframe width="690" height="385" src="https://www.youtube.com/embed/Hoixgm4-P4M?si=PSKtmEU9xNb69cmH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Odůvodnění složitosti QuickSort
<iframe width="690" height="385" src="https://www.youtube.com/embed/YQhfIoK8UDY?si=xfXlqXghJhufKSkE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

![[MacBook-2024-03-11-000843@2x.png]]

##### Navigace
Předchozí:  [[Základní metody třídění - insert sort, select sort, bubble sort]]
Následující: [[Merge sort a jeho složitost]]
Celý okruh: [[1. Teoretické základy informačních technologií]]