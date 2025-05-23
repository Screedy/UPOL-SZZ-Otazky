## Pravidlo *is-a*
- vychází ze stromu dědičnosti
- vztah podmnožina a nadmnožina

>[!info]
>**Pravidlo is-a**
>Je-li třída D potomkem třídy C, pak každé D je C.

- příklad z reality *každý automobil je vozidlo, každý pes je savec* (podle reality se snažíme program modelovat)
- ![[strom-dedicnost.png]]
- z obrázku platí: *point is a shape, polygon is a compound-shape*
- **ne**platí: *circle is a compound-shape*

>[!info]
>**Princip substituce**
>Pokud kdekoliv v programu nahradíme instanci třídy instancí jejího potomka, musíme dostat stejné výsledky.

## Kontraktové programování
- pochází z jazyka *Eiffel*
- založeno na principu *"Než začneme programovat třídu, stanovíme podmínky , které musí splňovat (kontrakty).*
- máme 3 typy kontraktů
	1) **invariant třídy** - podmínky, jenž instance třídy musí neustále splňovat (tzn. pokud instance nesplňuje je v nekonzistentním stavu), např: poloměr kruhu je kladné číslo
	2) **prekondice třídy** - podmínky na stav instance a hodnoty parametrů metody při jejím volání, např: hodnoty parametrů metody `set-radius` třídy `circle` musí být kladná čísla
	3) **postkondice třídy** - podmínky na stav instance po vykonání metody (= stanovují efekt metody, hlavní i vedlejší), např: pro metodu `set-color` třídy `shape` se musí hodnota vlastnosti `color` po provedení metody rovnat parametru této metody
- invariant stanovujeme při definici třídy, pre/post-kondice při definici metody
#### Vztah kontraktů vůči vztahu předek-potomek
1) pro potomka platí všechny invarianty předky (další může libovolně přidat)
2) prekondice potomka musí být slabší než prekondice předka (potomek může odebírat)
3) postkondice potomka musí být silnější než postkondice předka
## Princip Barbary Liskovové

>[!info]
>**Princip B. Liskovové (formální znění)**
>
>Pokud s instancemi třídy pracujeme se znalostmi o této třídě, máme jistotu, že dojdeme ke správným výsledkům, ikdyž instance není přímou instancí třídy.
