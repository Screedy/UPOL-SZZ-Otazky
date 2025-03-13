## Definice
- parametrizován přirozeným číslen $t ≤ 2$
1) počet klíčů v uzlech - v každém uzlu maximálně $2t-1$ klíčů a minimálně $t-1$ klíčů (výjimkou je kořen)
2) počet potomků - uzel má $n$ klíčů, pak buď $0$ potomků (kořen) nebo $n+1$ potomků
3) hloubka listových uzlů - všechny listy jsou ve stejné hloubce
4) podmínka uspořádání - klíče jsou uspořádány vzestupně a uloženy v poli
![[b-strom.jpeg]]
## Implementace
```C
struct {
	keys,      // pole klicu o velikosti 2t-1
	children,  // pole potomku o velikosti 2t
	parent,    // pointer na rodice
	n,         // pocet klicu v uzlu
	leafs,     // zda je uzel listem
	data       // pointer na satelitni data
}
```
>[!info]
>B-strom s paramterem $t≥2$ obsahující $n≥1$ klíčů má výšku nejvýše $log_t(n+1/2)$
#### Vyhledávání
- rozhodování do kterého stromu se půjde záleží na porovnání s polem klíčů
```python
search(x, k)
	i = 0
	while i < x.n and k > x.keys[i]
		i = i + 1

	if i < x.n and k == x.keys[i]
		return x, i
	else if x.leaf
		return false
	else
		return search(x.children[i], k)
```