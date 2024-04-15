
### 1. Syntax Errors (Chyby syntaxe):

Syntax errors se vyskytují, když Python narazí na neplatnou syntaxi ve vašem kódu. Tyto chyby jsou detekovány již při parsování kódu, protože neodpovídá syntaxi jazyka Python.

```Python
>>> print("Hello, world!"
SyntaxError: unexpected EOF while parsing
```

### 2. Runtime Errors (Běhové chyby):

Runtime errors (také nazývané výjimky) se vyskytují, když je kód syntakticky správný, ale obsahuje logickou chybu, která brání jeho vykonání. Tyto chyby se objevují až při běhu programu.

```Python
>>> x = 10
>>> y = 0
>>> result = x / y
ZeroDivisionError: division by zero
```

### 3. Logické chyby:

Logické chyby jsou obtížnější na identifikaci, protože program s nimi stále funguje, ale ne tak, jak je zamýšleno. Tyto chyby se vyskytují, když je algoritmus nesprávně navržen nebo implementován.

```Python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Správný výstup: 120
print(factorial(-1))  # Logická chyba: Factorial of negative number
```

### 4. IndexError:

IndexError nastává, když se pokoušíte přistupovat k prvkům v seznamu, n-tici nebo řetězci pomocí indexu, který je mimo rozsah.

```Python
>>> my_list = [1, 2, 3]
>>> print(my_list[3])
IndexError: list index out of range
```

### 5. KeyError:

KeyError se objeví, když se pokusíte přistoupit k prvkům slovníku pomocí klíče, který ve slovníku neexistuje.

```Python
>>> my_dict = {'a': 1, 'b': 2}
>>> print(my_dict['c'])
KeyError: 'c'
```

### 6. AttributeError:

AttributeError nastává, když se pokusíte přistoupit k atributu objektu, který tento objekt neobsahuje.

```Python
>>> my_list = [1, 2, 3]
>>> print(my_list.append)
AttributeError: 'list' object has no attribute 'append'
```

### 7. NameError:

NameError se objeví, když se používá nedefinovaná proměnná.

```Python
>>> print(my_variable)
NameError: name 'my_variable' is not defined
```

### 8. TypeErrors:

TypeError nastává, když operace je provedena na objektu nepodporujícím danou operaci.

```Python
>>> x = "5"
>>> y = 2
>>> print(x + y)
TypeError: can only concatenate str (not "int") to str
```

### 9. KeyboardInterrupt:

KeyboardInterrupt se vyskytuje, když uživatel přeruší běh programu stiskem klávesy, obvykle Ctrl + C.

```Python
>>> while True:
...     pass
... 
KeyboardInterrupt
```

## Hledání chyb:

- **Použití traceback:** Python poskytuje traceback, který identifikuje umístění chyby a zásobník volání, což může pomoci při hledání chyb.

- **Debugging:** Použití debuggeru jako pdb nebo využití vývojových prostředí s funkcemi pro ladění může usnadnit hledání chyb.

- **Logování:** Přidání výstupů nebo logovacích zpráv do kódu může pomoci identifikovat místa, kde program nefunguje správně. (Jak někdo řekl u Janoštíka: Prostě to "vyprintíme".)