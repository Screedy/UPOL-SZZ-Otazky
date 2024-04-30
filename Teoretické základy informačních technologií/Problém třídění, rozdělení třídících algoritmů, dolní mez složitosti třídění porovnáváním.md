### Problém třídění
- **Název:** Problém třídění
- **Vstup:** Posloupnost $n$ čísel $<a_{1}, ..., a_{n}>$
- **Výstup:** Permutace $<b_{1}, ..., b_{n}>$ vstupní posloupnosti taková, že $b_{1} \leq b_{2} \leq ... \leq b_{n}$

- Proč je problém třídění důležitý:
	- Vyskytuje se jako úloha při řešení mnoha úloh zpracování dat.
	- Algoritmy pro řešení složitějších problémů využívají algoritmy pro třídění.
	- Často potřebujeme setřídit pole složitějších datových položek než jsou čísla.
	- Algoritmy třídění používají řadu užitečných technik pro návrh algoritmů.

### Rozdělení třídících algoritmů
- Třídící algoritmy lze rozdělit podle několika kritérií, například:
1. Podle způsobu třídění:
	- **Porovnávací algoritmy:**
		- Tyto algoritmy porovnávají prvky, aby je mohli správně seřadit
		- Quicksort, Mergesort, Heapsort, ...
	- Některé třídící algoritmy, například Counting Sort nebo Radix Sort nepoužívají porovnání prvků, ale pracují s počtem výskytů nebo s číslicemi v číslech.
2. Podle časové složitosti:
	- **Algoritmy s časovou složitostí $O(n^{2})$**
		- Bubble Sort, Selection Sort, Insertion Sort.
	- **Algoritmy s časovou složitostí $O(n \log n)$**
		- QuickSort, MergeSort, HeapSort.
	- **Lineární algoritmy s časovou složitostí $O(n)$**
		- Counting Sort, Radix Sort.
3. Podle stability:
	- **Stabilní algoritmy**
		- Zachovávají pořadí stejných prvků v seznamu
		- MergeSort, Insertion Sort.
	- **Nestabilní algoritmy**
		- Mohou zaměnit pořadí stejných prvků
		- QuickSort, Selection Sort
4. Podle paměťové náročnosti:
	- **In-place algoritmy**
		- Provádějí třídění přímo v původním seznamu a nepotřebují žádnou další paměťovou alokaci.
		- QuickSort, Selection Sort.
	- **Out-of-place algoritmy**
		- Vytvářejí nový seznam pro seřazené prvky a mohou potřebovat více paměti.
		- MergeSort. Counting Sort

### Dolní mez složitosti třídění porovnáváním
- Věta: *Časová složitost v nejhorším případě libovolného algoritmu třídění porovnáváním je $\Omega (n \lg n)$*.
- Důkaz:![[MacBook-2024-03-11-000823@2x.png]]

##### Navigace
Předchozí:  [[Lineární datové struktury - seznam, zásobník, fronta]]
Následující: [[Základní metody třídění - insert sort, select sort, bubble sort]]
Celý okruh: [[1. Teoretické základy informačních technologií]]