- Obecně můžeme na doménách atributů zavádět operace
	- Např. na celých číslech operace sčítání $+$
- Taktéž na doménách můžeme zavádět relace
	- Např. uspořádání na celých číslech $≤$
#### Skalární výraz
- Skalární výraz $\theta$ na $R$ je výraz, který obsahuje atributy z $R$, hodnoty z domén a aplikuje operace na hodnot požadovaných typů
	- Např. `age + 1` je skalární výraz na `{age}` (doména atributu `age` jsou celá čísla)
- $\theta(r)$ je **hodnota skalárního výrazu** $\theta$
- Hodnotu v n-tici zjistíme tak, že vypočítáme hodnotu výrazu $\theta$, kde za každý atribut $y$ dosadíme hodnotu $r(y)$ 
	- Např. hodnota výrazu `age + 1` v n-tici `{<age, 32>}` je 33 (32 + 1 = 33)
##  Definice rozšíření
- Relace $D$ na $R$, atribut $y \notin R$ a skalární výraz $\theta$ na $R$ potom rozšíření $D$ o $y$ podle $\theta$ definujeme takto:
 ![[Pasted image 20250502172832.png]]
- Rozšíří relaci o nový atribut
	- Ten se pro každou n-tici dopočítá z původní n-tice pomocí výrazu
```sql
SELECT *, 2022 - born AS age FROM ( TABLE actors ) t1;
```
- **Kardinalita** ... počet řádků
- **Arita** ... počet atributů
- **Singleton** ... relace, kde arita i kardinalita je 1 (lze ho považovat za skalární výraz)