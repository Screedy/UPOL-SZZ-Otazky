*Níže uvedené informace jsou čerpány z Paradigmat Programování a mohou být specifické pro implementaci v Lispu.*
## Prototypové OO jazyky
- pracují s objekty bez zavedení pojmu *třída*
- objekty tedy nejsou instance třídy nýbrž odvozeny z prototypů (přebírají jejich funkčnost)
- nejznámější je *JavaScript*
- jednodušší než přístup s třídami
## Principy
1) neexistují třídy
2) objekty mají ve slotech uloženy data i metody
3) dědičnost na úrovni objektů (objekt má slot(y) obsahující předka(y))
- princip dědičnosti pro hledání hodnoty slotu funguje stějně jako v OOP (pomocí stromu dědičnosti)
- **klonování** - vytvoření nového objektu, který obsahuje pouze slot určující jeho předka
#### Zasílání zprávy
- funkce `send` a lambda seznam
```lisp
(object message &rest args )

object:  objekt
message: zpráva (symbol)
args:    argumenty zprávy v seznamu
```
- názvem zprávy sdělíme objektu s jakým slotem chceme pracovat
- výsledkem je nějaký další objekt (může být i vedlejší efekt)
## Metody
- funkce s 1 a více parametry
- první argument obvykle `self` (obsahuje příjemce zprávy)
1) standardní metody
2) primitiva - psané v Lispu né prototypovém jazyce
## Objekt
- skládá se z pojmenovaných slotů (ve slotu opět uložen objekt)
- i prostředí je reprezentováno jako objekt
- dědičnost se implementuje také ve slotu (slot `super`)
- nový objekt vytvoříme klonováním
- **inline objekt** - jeho popis je zapsán přímo ve zdrojovém kódu
- **primitivní inline objekt** = literál - např. číslo, textový řetězec, ...