- Algoritmus typu **"rozděl a panuj"** *(divide and conquer)*
	- Fáze "rozděl":
		- Zvolí se pivot $q$
		- Přemístí se prvky tak $A[p ... q - 1] \leq A[q]$ a $A[q + 1 ... r] \geq A[q]$
	- Fáze "panuj":
		- Setřídí se části $A[p ... q - 1]$ a $A[q + 1 ... r] \rightarrow$ znovu zavolání QuickSort
- Jedná se o tzv. **rekurzivní algoritmus**. Totiž, při provádění algoritmu QuickSort (ve fázi "panuj") se "volá" sám QuickSort. To však **nevede k zacyklení**, protože algoritmus je "volán" pro stále kratší části pole $A$, a při volání pro část tvaru **$A[p ... p]$** se provádění **okamžitě ukončí**. ($A[p ... p]$ je totiž setřízena - jeden prvek).
- Složitost algoritmu v průměrném případě: $\Theta (n \log n)$
- Složitost algoritmu v nejhorším případě: $\Theta (n^{2})$ (prázdná pravá/levá část, pivot je vždy úplně na straně).
![[MacBook-2024-03-11-000840@2x.png | 500]]
- Příklad:
	- Tříděné pole: ![[MacBook-2024-03-11-000841@2x.png | 200]]
	- ![[MacBook-2024-03-11-000842@2x.png]]

### Odůvodnění složitosti QuickSort
[https://www.youtube.com/watch?v=YQhfIoK8UDY](https://www.youtube.com/watch?v=YQhfIoK8UDY)
![[MacBook-2024-03-11-000843@2x.png]]