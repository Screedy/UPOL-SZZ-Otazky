## Testování SW
- dynamický proces (musíme mít spustitelný kód)
- pro každý požadavek (uživatelský i systémový) alespoň 1 test
- defect testing ... úspešný test = nález chyby
- nedává 100% záruku, záleží na kvalitě a četnosti testů
- test case ... vstupy a očekávané výstup
	- jednotlivá funkcionalita a kombinovaná může (ne)fungovat rozdílně
- testovací data
	- vhodná - krajní případy, né moc velké množství
	- často pevně daná pravidla jak volit
- zprávy o testování (vyvodí závěr)
##### Integrační testy (při vývoji)
- k dispozici zdrojové kódy (white box)
- snaha najít původce chyb (debbuging) může být složitá
- inkrementální přístup
- nová funkcionalita -> testovat i předešlé případy -> důkaz že jsme nic "nerozbili"
- automatizace
##### Funkční testy (před vydáním)
- release candidate (testování kandidáta na vydání) = ověřujeme celý systém
- není k dispozici zdroják (black box) => odhalení chyby jen předáme dál (neřešíme ho)
- snaha systém rozbít (SQL injection, dostat se tam kam nemůžu, stack overflow) nebo vyvolat chybovou hlášku
- testujeme posloupnost funcionalit
##### Testy výkonu
- testuje hotový systém 
- ověřujeme emergentní vlastnosti
- ověření že systém zvládne očekávanou zátěž
- **bottle neck** ... úzké hrdlo systému
- **stress test** ... plně vytížení systému
	- jak reaguje na zahlcení (aby nenastaly problémy s daty)
- **profiler** - ukazuje kde v systému trávíme nejvíc času a co využívá nejvíce zdrojů
	- 2 režimy - vzorkování a instrumentace

- code coverage ... kolik % kódu je pokryto testy
	- ani 100% nemusí znamenat bezchybnost
##### Testy komponent (unit)
- odhaluje chyby v samostatných komponentách
- fake data (i fake rozhraní)
- **code coverage** ... % řádků kódu pokrytá testy (100 % != bezchbyný kód)
##### Testy bezpečnosti
- co nás zajímá? bezpečnost dat, kdo má kam přístup, co se děje při přenosu dat
- penetrační testy (různé typy útoků, externí odborníci)
- **bug-bounty program** ... firmy platí nálezcům chyb
##### Alpha testy
- poslední krok před doručením
- nad reálnými daty
##### Beta testy
- testují už reální uživatelé
- pouze ladí drobnosti
#### Návrh testů
- každý požadavek by měl jít otestovat
- mezní případy podmínek
- path testing ... ověření všech podmínek (pokrytí všech větví diagramu aktivit)

> [!info]
> **Test driven developement**
 > - nejdříve testy, podle nich píšeme implementaci
> - refactoring - zjednodušení kódu po jeho napsání (a splnění daných testů)

#### Kategorie chyb
1) chyba dat - inicializace, magické konstanty, buffer overflow
2) chyba toku - správnost podmínek, cyklů
3) chyby ve vstupu/výstupu - využití vstupů, ošetření vstupů, správné přiřazení výstupů
4) chyby rozhraní - správnost typů, správný počet argumentů
- mnoho chyb lze odhalit strojově
- **statická analýza kódu** (nástroje kód prochází a hledají podezřelé části)
	- nedosažitelný kód
	- správnost typů
	- možnost `null` pointeru