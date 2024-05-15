Rekurze a rekurzivní datové struktury jsou klíčovými koncepty v počítačové vědě a programování. Rekurze je technika, která umožňuje funkci volat sama sebe. Rekurzivní datové struktury jsou takové struktury, které obsahují odkazy na stejný typ struktury.

## Rekurze

Rekurze je základní technikou v programování, kde funkce volá sama sebe s menšími částmi vstupu, dokud není dosaženo určitého podmíněného ukončení. Tato technika se obvykle používá k řešení problémů, které lze snadno rozdělit na menší části stejného typu. Příkladem může být faktoriál čísla, Fibonacciho posloupnost, procházení stromů atd.

Příklad rekurzivní funkce pro výpočet faktoriálu:

```Python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

## Rekurzivní datové struktury

Rekurzivní datové struktury jsou struktury, které obsahují odkazy na objekty stejného typu. Toto umožňuje vytvářet složitější struktury, jako jsou spojové seznamy, stromy, grafy atd.

#### Spojový seznam

Spojový seznam je rekurzivní datová struktura, která se skládá z uzlů, kde každý uzel obsahuje data a odkaz na následující uzel v seznamu.

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

Spojové seznamy můžou obsahovat i odkaz na předchozí prvek.
#### Strom

Strom je hierarchická datová struktura skládající se z uzlů, kde každý uzel má určitý počet podřízených uzlů, nazývaných potomci.

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

Rekurze je využívána k procházení a manipulaci s rekurzivními datovými strukturami jako jsou stromy a spojové seznamy. Pomocí rekurze můžeme snadno implementovat algoritmy pro procházení, vyhledávání, vkládání, mazání a mnoho dalších operací na těchto strukturách.

### Procházení spojového seznamu

Spojový seznam můžeme procházet pomocí rekurze nebo iterativního způsobu.

#### Rekurzivní procházení spojového seznamu

```Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Funkce pro rekurzivní procházení spojového seznamu
def recursive_traversal(node):
    if node is None:
        return
    print(node.data)  # Provádí operaci s daty uzlu
    recursive_traversal(node.next)

# Vytvoření spojového seznamu
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# Spuštění rekurzivního procházení
recursive_traversal(node1)
```

### Procházení stromu

Procházení stromu můžeme provést pomocí různých strategií, jako je inorder, preorder a postorder.

#### Preorder procházení stromu (kořen - levý podstrom - pravý podstrom)

```Python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

# Funkce pro preorder procházení stromu
def preorder_traversal(node):
    if node is None:
        return
    print(node.data)  # Provádí operaci s daty uzlu
    for child in node.children:
        preorder_traversal(child)

# Vytvoření stromu
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")

root.children.append(child1)
root.children.append(child2)
child2.children.append(child3)

# Spuštění preorder procházení
preorder_traversal(root)
```

##### Navigace
Předchozí:  [[Funkce vyšších řádů - mapování, filtrování, redukce a anonymní funkce]]
Následující: [[Iterátory a generátory]]
Celý okruh: [[3. Programovací jazyky a programování]]