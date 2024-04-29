### Datové struktury
- = **Způsob uložení entit**, které se vyskytují v programu, **do paměti**
	- **entita** = jakákoliv přesně definovaná množina dat

### Lineární datové struktury
- Prvky jsou **seřazeny do posloupnosti** (má smysl uvažovat o pořadí prvků)
- U každého prvku **známe předka a následníka** (pokud existují)

#### Zásobník (Stack)
- Pracuje na principu **LIFO** (Last In First Out)
- Operace
	- `Push(S, x)` $\rightarrow$ nahrazuje **insert**
	- `Pop(S)`         $\rightarrow$ **odstraní** naposled přidaný prvek a **vrátí** jej
- ![|300](https://lh7-us.googleusercontent.com/docsz/AD_4nXccWc9MdnLUX2GI6dUOi6Zas5g6rrTf4rbxug2BMzEGNFolCfcpODZLsM2Cs6WARDxOvM0MJrWj1F91nnl_Mf8A0bViPOD5fUdw1-Mev1m27eYbKVpPeGBMp7JmCgtUMrE_nBC0EHlzGgdJ_b7G9w?key=1oMgW2MUuii1DDrztmo2_Q)

#### Fronta (Queue)
- Pracuje na principu **FIFO** (First In First Out)
- Operace
	- `Enqueue(Q, x)` $\rightarrow$ nahrazuje **insert**
	- `Dequeue(Q)`       $\rightarrow$ **odstraní** nejdříve přidaný prvek a **vrátí** jej
- ![| 300](https://lh7-us.googleusercontent.com/docsz/AD_4nXcsS8mu7D3TC8mmAKeGZLnc9nQWCKkmRIK4baOcZ3vvVOmcrx4nmpMcYE5XDoyIiDhj5ZVJnJnW5CvZW1ZOOXBCAm0HAAtiEiQP4LYRK8Z2G0G2GYKZ71993iMnRsMZCOAbwcbyNqSbohJADWA8eUE?key=1oMgW2MUuii1DDrztmo2_Q)

#### Spojový seznam (cyklický, se zarážkou)
- Prvky jsou lineárně za sebou, nelze přistupovat pomocí indexu, zapojení je zajištěno pomocí pointerů
- Nemusí být v paměti za sebou
- **Jednosměrný** = u prvků známe následovníka
- **Obousměrný** = u prvků známe následovníka i předchůdce
- ![[MacBook-2024-03-11-000822@2x.png | 500]]

##### Navigace
Předchozí:  [[O-notace a růst funkcí, definice, vlastnosti, příklady použití]]
Následující: [[Problém třídění, rozdělení třídících algoritmů, dolní mez složitosti třídění porovnáváním]]
Celý okruh: [[1. Teoretické základy informačních technologií]]