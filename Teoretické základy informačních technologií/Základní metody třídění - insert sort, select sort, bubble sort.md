### Insertion Sort
- Třídění vkládáním
- Idea algoritmu je založena na třídění $n$ rozdaných karet
- Složitost algoritmu v nejlepším případě: $\Theta (n)$ (vstupní pole už je setříděné)
- Složitost algoritmu v nejhorším případě: $\Theta (n^{2})$ (vstupní pole je setříděné naopak)
![[MacBook-2024-03-11-000831@2x.png | 400]]

- Příklad:
	- Tříděné pole:![[MacBook-2024-03-11-000832@2x.png | 150]]
	- ![[MacBook-2024-03-11-000833@2x.png]]

### Selection Sort
- Idea *"Najdi nejmenší prvek v poli a vyměň ho"*
	- min z $A[0 ... n-1] \rightarrow A[0]$
	- min z $A[1 ... n-1] \rightarrow A[1]$
	- $...$
	- min z $A[n-2 ... n-1] \rightarrow A[n-2]$
- Složitost algoritmu v nejhorším i v nejlepším případě je $\Theta (n^{2})$
![[MacBook-2024-03-11-000834@2x.png | 500]]
- Příklad:
	- Tříděné pole: ![[MacBook-2024-03-11-000835@2x.png | 200]]
	- ![[MacBook-2024-03-11-000836@2x.png]]

### Bubble Sort
- Bublinkové třídění
- Nejmenší prvek *"probublá"* vlevo, pak *"probublá"* druhý nejmenší prvek ...
- Další varianty Bubble Sort:
	- Optimalizace vynecháním některých průchodů
	- Cocktail Sort
- Složitost algoritmu v nejhorším případě: $\Theta (n^{2})$
![[MacBook-2024-03-11-000837@2x.png]]
- Příklad:
	- Tříděné pole![[MacBook-2024-03-11-000835@2x.png | 200]]
	- ![[MacBook-2024-03-11-000838@2x.png | 500]]![[MacBook-2024-03-11-000839@2x 1.png| 500]]
