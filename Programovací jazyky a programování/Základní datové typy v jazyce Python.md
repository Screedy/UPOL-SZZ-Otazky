Python je dynamicky typovaný jazyk, což znamená, že interpret (nebo kompilátor) je schopen automaticky určit datový typ proměnné na základě přiřazené hodnoty. V Pythonu se datové typy automaticky přizpůsobují hodnotám, které jsou jim přiřazeny, a umožňují dynamickou manipulaci s daty.

## Základní datové typy:

1. **Integer (celé číslo):** Reprezentuje celé číselné hodnoty, například `5` nebo `-10`.

2. **Float (desetinné číslo):** Reprezentuje desetinné hodnoty, například `3.14` nebo `-0.001`.

3. **Boolean (logická hodnota):** Reprezentuje pravdivostní hodnoty `True` a `False`.

4. **String (řetězec znaků):** Reprezentuje textové hodnoty, například `"hello world"` nebo `'Python je skvělý'`.

5. **List (seznam):** Ukládá posloupnost prvků, může obsahovat různé datové typy, například `[1, 2, 3]` nebo `['jablko', 'hruška', 'banán']`.

6. **Tuple (n-tice):** Podobný seznamu, ale je neměnný (immutable), například `(1, 2, 3)`.

7. **Dictionary (slovník):** Ukládá páry klíč-hodnota, klíč musí být unikátní, například `{'jmeno': 'Jan', 'vek': 30}`.

8. **Set (množina):** Ukládá unikátní prvky, nepodporuje duplikáty, například `{1, 2, 3}`.

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