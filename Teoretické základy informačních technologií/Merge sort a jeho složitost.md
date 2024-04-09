- Třídění sléváním (slučováním)
- Algoritmus "rozděl a panuj"
	- Setřiď levou polovinu pole, setřiď pravou polovinu pole, "slij" obě poloviny
- Složitost algoritmu v nejhorším případě: $\Theta (n \log n)$
![[MacBook-2024-03-11-000844@2x.png | 500]]

### Odůvodnění složitosti MergeSort
- $T(n) = c$ pro $n = 1$
- $T(n) = 2T(\frac{n}{2}) + cn$ pro $n > 1$
- $T(n) = cn \log n + cn = \Theta (n \log n)$
- ![[MacBook-2024-03-11-000845@2x.png | 500]]

- Příklad:![[MacBook-2024-03-11-000846@2x.png]]

