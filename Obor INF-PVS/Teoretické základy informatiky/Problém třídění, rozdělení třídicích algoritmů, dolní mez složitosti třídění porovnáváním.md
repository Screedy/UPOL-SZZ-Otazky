## Problém třídění
- **Název:** Problém třídění
- **Vstup:** Posloupnost $n$ čísel $<a_{1}, ..., a_{n}>$
- **Výstup:** Permutace $<b_{1}, ..., b_{n}>$ vstupní posloupnosti taková, že $b_{1} \leq b_{2} \leq ... \leq b_{n}$

- Proč je problém třídění důležitý:
	1) Vyskytuje se jako úloha při řešení mnoha úloh zpracování dat.
	2)  Algoritmy pro řešení složitějších problémů využívají algoritmy pro třídění.
	3) Často potřebujeme setřídit pole složitějších datových položek než jsou čísla.
	4) Algoritmy třídění používají řadu užitečných technik pro návrh algoritmů.
### Rozdělení třídících algoritmů
- Třídící algoritmy lze rozdělit podle několika kritérií, například:
1. **Podle způsobu třídění**:
	- *Třídění vkládáním*:
		- Insertion sort
	- *Třídění výběrem*:
		- Selection sort
	- *Rozdělej a panuj*:
		- Quick sort, Merge sort
	- *Využití haldy (datová struktura):*
		- Heap sort
	- Nahoře zmíněné algoritmy využívají tzv. *třídění porovnáváním* (porovnají prvky ve struktuře, aby je mohli korektně seřadit)
	- Některé třídící algoritmy (Counting Sort nebo Radix Sort) nepoužívají porovnání prvků, ale pracují s počtem výskytů nebo s číslicemi v číslech.
2. **Podle časové složitosti**:
	- *Algoritmy s časovou složitostí $O(n^{2})$*
		- Bubble Sort, Selection Sort, Insertion Sort.
	- *Algoritmy s časovou složitostí $O(n \log n)$*
		- QuickSort, MergeSort, HeapSort.
	- *Lineární algoritmy s časovou složitostí $O(n)$*
		- Counting Sort, Radix Sort.
3. **Podle stability**:
	- *Stabilní algoritmy*
		- Zachovávají pořadí stejných prvků v seznamu
		- MergeSort, Insertion Sort.
	- *Nestabilní algoritmy*
		- Mohou zaměnit pořadí stejných prvků
		- QuickSort, Selection Sort
4. **Podle paměťové náročnosti**:
	- *In-place algoritmy*
		- Provádějí třídění přímo v původním seznamu a nepotřebují žádnou další paměťovou alokaci.
		- QuickSort, Selection Sort.
	- *Out-of-place algoritmy*
		- Vytvářejí nový seznam pro seřazené prvky a mohou potřebovat více paměti.
		- MergeSort, Counting Sort.

### Dolní mez složitosti třídění porovnáváním
>[!tip] Věta
>*Časová složitost v nejhorším případě libovolného algoritmu třídění porovnáváním je $\Omega (n \log n)$*.
- Čili nejsme schopni najít algoritmus, který by byl v časové složitosti lepši než již existující

>[!Example]- Důkaz věty
>
>![[MacBook-2024-03-11-000823.png]]
><iframe width="620" height="385" src="https://www.youtube.com/embed/WffUZk1pgXE?si=29P2ErxedVnQXbwz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>