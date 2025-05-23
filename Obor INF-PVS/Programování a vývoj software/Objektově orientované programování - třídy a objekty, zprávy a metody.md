## Princip OOP
- konstruktor, selektor a mutátor (pojmy z obecných datových struktur)
- v OOP tyto funkce chápeme jako její součást => tím pádem jsou samostatné a nezávislé
- OOP tedy přináší nový problém *Jak rozdělit činnosti programu mezi objekty?*
## Objekty
- v OOP je program složen ze samostatných nezávislých jednotek zvaných **objekty**
- objekt koná na základě pokynů jež mu jsou zasílány formou **zpráv**
- dva hlavní principy objektů jsou nezávislost a samostatnost
>[!info]
>**samostatnost** - stačí říct, co mají dělat (není nutné specifikovat *jak*)
>**nezávislost** - vlastnost se odvíjí od nutnosti zajištění vnějších podmínek, lepší nezávislost umožňuje lepší znovupoužitelnost
#### Vlastnické vztahy mezi objekty
- jiný typ hierarchie (vztah *prvek - kontejner*)
- méně formální než *předek - potomek*
- využíván k předání zodpovědnosti na vlastníka
- přímý vlastník objektu je **delegát**
## Zprávy
- jsou identifikovány jménem
- stejně jako funkce mohou obsahovat argumenty a "výsledkem" může být vrácená hodnota
- objekt na přijetí zprávy reaguje tak, že spustí a vykoná kód zvaný **metoda** (proces nazývaný obsluha zprávy)
#### Události
- odlišné od obecných zpráv
1) objekt ji posílá svému majiteli (delegátovi)
2) úkolem je informovat
3) objekt na tuto zprávu nemá očekávat reakci
## Metody
- zvláštní druh funkce
- má jméno a parametry
- objekt může mít více metod
- metody a zasílané zprávy mají **stejný název**
- máme různé typy metod
	- **public** - veřejná, přístupná odkudkoliv i z venčí
	- **protected** - chráněná, přístup pouze ze třídy a jejich potomků (Python `_method()`)
	- **private** - soukromá, může volat jen ona třída přímo (Python `__method()`)
	- v ostatních jazycích se obvykle značí klíčovými slovy

> [!info]
>**vnitřní stav objektu** - souhrn dat, která objekt obsahuje

>[!info]
>- čtení vlastnosti - *getter* - `property()`
>- nastavení vlastnosti - *setter* - `set-property()`
## Atributy / sloty
- data v objektu 
- nejsou uživateli (navenek) známé

>[!warning]
>**Bariéra mezi vnitřním stavem a rozhraním**
>- je nutné rozlišovat mezi autorem objektu a uživatelem (v realitě to pořád může být tentýž programátor)
>- uživatel nemá znát informace o implementaci objektu a ani je používat
##  Třídy
- základní typ objektů v OOP
- aby 2 objekty patřily stejné třídě musí splňovat
	1) stejná sada slotů
	2) stejné metody
- = popis objektu
- objekt patřící třídě nazýváme **instancí**
```lisp
; třída point se sloty x a y
(defclass point ()
	(x y))
```
