- Rekurze je technika v programování, kdy funkce volá sama sebe.
- Rekurze je velmi užitečná při práci s datovými strukturami, které mají rekurzivní povahu, jako jsou spojové seznamy a stromy.
- Tyto datové struktury se skládají z podobných menších struktur, což je činí vhodnými pro řešení pomocí rekurze.

## Rekurze
- Rekurzivní funkce musí splňovat podmínky:
	1. **Základní případ** - podmínka, která ukončí rekurzi
	2. **Rekurzivní případ** - část, kde funkce volá sama sebe
- Např. faktoriál čísla, Fibonacciho posloupnost, procházení stromů, ...

>[!Example] Příklad faktoriál
>```Python
>def factorial(n):
> 	if n == 0:
> 		return 1
> 	else:
> 		return n * factorial(n - 1)
>```

## Rekurzivní datové struktury
- Rekurzivní datové struktury jsou struktury, které obsahují odkazy na objekty stejného typu. Toto umožňuje vytvářet složitější struktury, jako jsou spojové seznamy, stromy, grafy atd.

#### Spojový seznam
- Spojový seznam je rekurzivní datová struktura, která se skládá z uzlů, kde každý uzel obsahuje data a odkaz na následující uzel v seznamu.
- Spojové seznamy můžou obsahovat i odkaz na předchozí prvek.

```Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Příklad vytvoření spojového seznamu
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# výsledný seznam
1 -> 2 -> 3
```

#### Strom
- Stromy jsou hierarchické datové struktury, kde každý uzel může mít nulové nebo více poduzlů.
- Binární strom je speciální druh stromu, kde každý uzel má nejvýše dva potomky.

```Python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

# Příklad vytvoření stromu
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")

root.children.append(child1)
root.children.append(child2)
child2.children.append(child3)

# Výsledná strom
    A
   / \
  B   C
      |
      D

```

## Procházení rekurzivních struktur
- Rekurze je využívána k procházení a manipulaci s rekurzivními datovými strukturami jako jsou stromy a spojové seznamy. 
- Pomocí rekurze můžeme snadno implementovat algoritmy pro procházení, vyhledávání, vkládání, mazání a mnoho dalších operací na těchto strukturách.

### Procházení spojového seznamu
- Spojový seznam můžeme procházet pomocí rekurze nebo iterativního způsobu.

>[!Example] Rekurzivní procházení spojového seznamu
>```Python
># Funkce pro rekurzivní procházení spojového seznamu
>def recursive_traversal(node):
> 	if node is None:
> 		return
> 	print(node.data)  # Provádí operaci s daty uzlu
> 	recursive_traversal(node.next)
>```

### Procházení stromu

- Procházení stromu můžeme provést pomocí různých strategií, jako je inorder, preorder a postorder.

#### Preorder procházení stromu (kořen - levý podstrom - pravý podstrom)

>[!Example] preorder procházení stromu
>```Python
># Funkce pro preorder procházení stromu
>def preorder_traversal(node):
> 	if node is None:
> 		return
> 	print(node.data)  # Provádí operaci s daty uzlu
> 	for child in node.children:
> 		preorder_traversal(child)
>```

##### Navigace
Předchozí:  [[Funkce vyšších řádů - mapování, filtrování, redukce a anonymní funkce]]
Následující: [[Iterátory a generátory]]
Celý okruh: [[3. Programovací jazyky a programování]]