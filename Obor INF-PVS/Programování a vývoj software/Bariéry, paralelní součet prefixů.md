## Bariéra
- místo v programu, kde se čeká až k němu dojdou všechny procesy (laicky řešeno)
- jde o synchronizační mechanismus
- zajistí, že všechny procesy dojdou do daného bodu, než se bude pokračovat dál
- řešíme pomocí sdíleného počítadla, kterého hodnotu zvýšíme vždy když daný proces dojde do místa bariéry; čekáme dokud hodnota počítadlo nebude rovna počtu procesů a poté můžeme pokračovat
	- $n$ ... počet procesů
	- $count$ ... počet procesů, které dorazili k bariéře
	- $passsed[i]$ ... proces $i$ prošel bariérou
	- ![[Pasted image 20250315151900.png]]
	- **problém:** takto implementovanou bariéru můžeme použít pouze jednou
>[!info]
>**Fetch and add**
> Složená atomická operace `FA(var, num)`. `var` je proměnná a `num` číslo. Atomicky provede následující kroky: zjistí hodnotu `val` proměnné `var`, zvýší hodnotu `var` o `num` a vrátí hodnotu `val`.
```python
# Implementace bariéry
FA(count, 1)
await count == n
```
#### Znovupoužitelná bariéry
- Máme 2 počítadla a "prohodíme" jejich roli
- ![[Pasted image 20250315152426.png]]
## (Paralelní) součet prefixů
- Vstupem je pole čísel
- Výstupem je taktéž pole čísel, kde v každém políčku je následující prvkem součtem předchozích políček
$$\begin{gather}
y_0​=x_0 \\​​
y_i=y_i−1+x_i \\
Pro \; i = 1, 2, ..., n -1
\end{gather}
$$
- Triviálním přístupem získáme lineární časovou složitost ($n$)
	- ![[Pasted image 20250315153716.png]]
- Paralelním přístupem sčítám postupně v krocích prvky v poli, tím se mi postupně budují nová pole a zvětšuji vzdálenost sčítaných prvků ($0, 1, ...$)
	- Postupně dostavám korektní výsledky od začátku pole až nakonec
- Tím se mi časová složitost zlepší na $log_2(n)$
- 
 

