- Z venku se tváří jako běžná datová struktura, ale hodnoty počítá až v momentě kdy je o ně zažádáno
- Pro zrychlení můžeme jednou spočítané hodnoty kešovat
- Ukázka jako seznamu, který poskytuje svůj průměr a mediám
## Příslib
- Dosud nevypočítaná hodnota, se kterou můžeme jako s hodnotou nakládat
	-  Čili můžeme ji ukládat, používat jako argument atd.
- Příklad je posloupnost, kde $n$-tý člen počítáme až když ho chceme zjistit
```lisp
;; konstruktor
(defmacro delay (expr)
	`(lambda () ,expr))

;; vynucuje vyhodnocení
(defun force (promise)
	(funcall promise))
```
- Nevýhodou je že se pokaždé počítá hodnota znovu (chceme kešovat opět)
- Uděláme z příslibu datovou strukturu, která si bude hodnotu pamatovat
>[!warning] Bezpečnost datových struktur
>Do datových struktur nezasahujeme jinak než pomocí dokumentovaných operací. Mohlo by dojít k uvedení do nekonzistentního stavu.
## Proudy
- Takové *líné seznamy* (jejich `cdr` se vypočítá až když je potřeba)
>[!info] Proud
>- symbol `nil`, tzv. *prázdný proud* nebo
>- pár, jehož *cdr* je příslib proudu, tj. hodnoty vyhovující opět této definici.
- Mohou být nekonečné
- Práce je dost podobná jako se seznamy
##  Řetězení funkcí na lineárních datových strukturách
- Seznamy chápeme jako celistvé hodnoty (funkcionální styl)
	- Můžou být vstupem i výstupem funkce
- Volání funkcí na jeden seznam za sebou ... **řetězení**
- ![[Pasted image 20250422090525.png]]
- Máme několik základních operací na seznamech
#### Mapování
- Převod seznamu na jiný, stejně dlouhý seznam, jehož prvky vznikly aplikací dané funkce na prvky výchozího seznamu.
#### Filtrace
- Vypuštění prvků seznamu, které splňují (nesplňují) danou podmínku, případně jsou (nejsou) nějakým způsobem totožné se zadanou hodnotou.
#### Redukce
- Výpočet hodnoty ze seznamu postupnou aplikací zadané funkce dvou argumentů vždy na předchozí výsledek a další prvek seznamu.
- Mapování i filtraci lze napsat pomocí redukce
#### Třídění
- Uspořádání prvků seznamu podle zadaného kritéria (funkce dvou argumentů).
#### Hledání
- Zjištění prvku seznamu, který splňuje (nesplňuje) zadanou podmínku nebo je (není) nějakým způsobem totožný se zadanou hodnotou. Hledání lze chápat jako speciální typ redukce, ovšem s tím omezením, že při redukci nelze přerušit prohledávání seznamu, když je hledaný prvek nalezen.
## Generátory
- Abstraktní datová struktura se složkou, jejíž hodnota se při každém přístupu změní
- Alternativní název *itetáror* (např. v Pythonu)
- Používají vedlejší efekt (nepatří do funkcionálního programování)