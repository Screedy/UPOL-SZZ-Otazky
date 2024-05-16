- Python je dynamicky typovaný jazyk, což znamená, že interpret je schopen automaticky určit datový typ proměnné na základě přiřazené hodnoty. 
- V Pythonu se datové typy automaticky přizpůsobují hodnotám, které jsou jim přiřazeny, a umožňují dynamickou manipulaci s daty.

## Základní datové typy:

1. **Integer (celé číslo):** 
	- celá čísla
	- např. `5` ,`-10`
2. **Float (desetinné číslo):** 
	- Reálná čísla s plovoucí desetinnou čárkou
	- např. `3.14`, `-0.001`
3. **Boolean (logická hodnota):** 
	- Reprezentuje pravdivostní hodnoty 
	- např. `True` a `False`.
4. **String (řetězec znaků):** 
	- Sekvence znaků
	- Imutabilní (neměnné)
	- např. `"hello world"` nebo `'Python je skvělý'`.
5. **List (seznam):**
	- Uspořádaná, změnitelná (mutabilní) sekvence prvků.
	- Může obsahovat různé typy dat.
	- např. `[1, 2, 3]` nebo `['jablko', 'hruška', 'banán']`.
6. **Tuple (n-tice):**
	- Podobný seznamu, ale je neměnný (immutable).
	- Může obsahovat různé typy dat.
	- např. `(1, 2, 3)`.
7. **Range**:
	- Reprezentuje sekvenci čísel generovanou na základě počáteční, koncové hodnoty a kroku.
	- Používá se často v cyklech `for`.
8. **Dictionary (slovník):** 
	- Neuspořádaná kolekce párů klíč-hodnota.
	- např. `{'jmeno': 'Jan', 'vek': 30}`.
9. **Set (množina):** 
	- Neuspořádaná kolekce unikátních prvků.
	- např. `{1, 2, 3}`.
10. **NoneType**:
	- Speciální typ reprezentující absenci hodnoty.
	- Má jedinou hodnotu `None`

## Vlastnosti datových typů v Pythonu:

1. **Dynamické přiřazení typů:** Python automaticky určuje datový typ proměnných na základě hodnoty, která je do nich přiřazena. Například:

```Python
x = 5       # x je nyní typu int
x = "hello" # x je nyní typu str
```

2. **Silná typová kontrola:** Python provádí silnou typovou kontrolu, což znamená, že nelze provádět operace s datovými typy, které nejsou kompatibilní. Například nelze sčítat číslo a řetězec, pokud není provedena konverze.

4. **Dynamické rozšiřování:** Python umožňuje dynamicky rozšiřovat datové struktury, jako jsou seznamy a slovníky, přidáváním nových prvků nebo klíčů. Například:

```Python
list = [1, 2, 3] list.append(4) # Přidává prvek 4 na konec seznamu
```

4. **Metody a operátory:** Každý datový typ v Pythonu má své vlastní metody a operátory pro manipulaci s daty. Například metoda `append()` pro seznamy, nebo operátor `+` pro spojování řetězců.

5. **Dynamická alokace paměti:** Python spravuje paměť dynamicky, což znamená, že se stará o alokaci a dealokaci paměti pro proměnné a datové struktury.


##### Navigace
Předchozí:  [[Výrazy a jejich vyhodnocování v jazyce Python]]
Následující: [[Základy systému výjimek v jazyce Python]]
Celý okruh: [[3. Programovací jazyky a programování]]