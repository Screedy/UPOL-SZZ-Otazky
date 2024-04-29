- **$i$-tá pořádková statistika** množiny s $n$ prvky je $i$-tým **nejmenším prvek dané množiny**. 
	- ($i$-tý prvek **po setřídění** posloupnosti)
- **Nejmenší** prvek (minimum) je **$1.$** **pořádková statistika**
- **Největší** prvek (maximum) je $n.$ **pořádková statistika**
- "Prostřední prvek" (**medián**)
	- **$n$ je liché:** **Medián** = $\frac{n+1}{2}.$ pořádková statistika
	- **$n$ je sudé:** (Pokud neřekneme jinak, bude medián znamenat dolní medián):
		- **Dolní medián** = $\lfloor \frac{n+1}{2} \rfloor$. pořádková statistika
		- Horní medián = $\lceil \frac{n+1}{2} \rceil$

## Problém týkající se pořádkové statistiky
- **Název:** "Výběr $i$-té pořádkové statistiky"
- **Vstup:** $A[0 ... n-1]$ a číslo $i \ (1 \leq i \leq n)$
- **Výstup:** $i.$pořádková statistika  prvku z $A$

- Příklad:
	- vstup $A = <2, 1, 4, 6, 2, 8, 1>, i = 1, \text{výstup} = 1$
	- vstup $A = <2, 1, 4, 6, 2, 8, 1>, i = 2, \text{výstup} = 1$
	- vstup $A = <2, 1, 4, 6, 2, 8, 1>, i = 3, \text{výstup} = 2$
	- vstup $A = <2, 1, 4, 6, 2, 8, 1>, i = 7, \text{výstup} = 8$

### Možné řešení problému
#### Naive-Select
- Časová složitost v nejhorším případě algoritmu Naive-Select je **rovna** časové složitosti v **nejhorším případě algoritmu** **Sort**
```C
Naive-Select(A[0 ... n-1], i)
	Sort(A)
	return A[i]
```

#### Randomized-Select
- Použijeme **Partition** z algoritmu QuickSort s **náhodným** výběrem pivota *(Rozdíl oproti QuickSort je, že po provedení Partition se zabýváme vždy **jen jednou částí**, levou nebo pravou)*
- Složitost algoritmu v průměrném případě: $\Theta (n)$
- Složitost algoritmu v nejhorším případě: $\Theta (n^{2})$
- Poznámka: Pokud hledáme $i$-tý prvek v poli, kde indexujeme od 0, musíme na vstup zadat $i-1$
```C
Randomized-Select(A, p, r, i)
	if p=r
		then return A[p]
	q <- Randomized-Partition(A, p, r)
	k <- q-p+1
	if i=k
		then return A[q]
	else if i<k
		then return Randomized-Select(A, p, q-1, i)
	else return Randomized-Select(A, q+1, r, i-q+p-1)
```
```C
Randomized-Partition(A, p, r)
	k <- Random(p, r)
	swap(A[k], A[r])
	return Partition(A, p, r)
```
Příklad:
<iframe width="690" height="385" src="https://www.youtube.com/embed/AHaaFVmAsvA?si=Xw3qDMfgqfKATgHH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### Navigace
Předchozí:  [[Další metody třídění - counting sort, radix sort, bucket sort]]
Následující: [[Vyhledávání v lineárních datových strukturách]]
Celý okruh: [[1. Teoretické základy informačních technologií]]