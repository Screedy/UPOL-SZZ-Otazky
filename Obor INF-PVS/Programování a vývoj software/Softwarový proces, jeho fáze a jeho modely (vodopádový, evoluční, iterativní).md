## Softwarový proces
- aktivity nutné k dokončení softwarového produktu
1) specifikace - jak to má vypadat?
	- zjistit - definovat - shodnout se na řešení
	- omezení vývoje (peníze, aktuální podmínky atd.)
	- **nejdůležitější část** (když to zkazím hned tady, tak se to potáhne všude dál)
	- nutné znát i problematiku zakázky
	- výstupem je formální definice = **dokument specifikace požadavků** (DSP)
	- studie proveditelnosti ->  zjištění a analýza požadavků -> soupis požadavků -> kontrola co jsme udělali
2) návrh + vývoj - ta technická část
3) validace - ověření, toho co se udělalo
4) evoluce - úpravy při tom, co SW už běží

## Vodopádový model
- fáze procesu jako samostatné jednotky (fáze je po dokončení "ukončena")
	- v modelu se nepřekrývají, v praxi ano
- během implementace je možné provádět jemné změny v hotových částech nebo část *zmrazit* a chyby v ní se odloží na později 
- **výhody**: jednoduchá měřitelnost pokroku a řádná dokumentace k ukončeným fázím
- **nevýhody**: možná špatná struktura, první verze až po ukončení 1. vodopádu (trvá dlouho)
![[Pasted image 20250221121739.png]]

> [!tip]
> - **kloc** ... thousand lines of code
> - Jednotka používaná pro měření rozsahu projektu.
## Evoluční model
- rychle se vyvine prvotní verze (můžeme ukázat zákazníkovi) => upřesňování požadavků => vývoj verze finální
- extrémně důležitá zpětná vazba
- vhodný pro menší projekty (do 500 kloc)
1) průzkumný vývoj
	- zákazník je aktivní v procesu vývoje
	- vývoj jde od částí, kde zákazník ví co chce a následně je přidána další funkcionalita
2) postupný (throwaway) vývoj
	- pro lepší pochopení potřeb zákazníka
	- prototyp se zaměří na nejasné části => obvykle se následně zahodí (po analýze) => výsledný produkt vznikne reimplementací na základě požadavků
![[SCR-20250221-likd.png]]
## Iterativní model
- hybridní model
- častá iterace celého vývojového procesu
- nadmnožina 2 typů
#### Inkrementální vývoj
 - přírůstkový model
 - postupné dodávání malých přírůstků od jádra
 - tento postup se opakuje
 - systém je v provozu od ranných začátků (kritické části jsou v provozu nejdéle => nejlépe otestovány)
 - nutné správně určit jádro systému na začátku
![[Pasted image 20250221124431.png]]
#### Spirálový vývoj
- 1 otočka spirály = 1 fáze SW procesu
- spirála je rozdělena na jednotlivé sektory
	1) určení záměrů (alternativní možnosti, analýza, definice rizik)
	2) vyhodnocení a snížení rizik (prototypy, simulace, dotazníky)
	3) vývoj a validace (zpracování a ověření dané fáze)
	4) plánování (revize předchozí části, plánování další, info zákazníkovi)
- jediná metoda explicitně řešící rizika
![[Pasted image 20250221125144.png]]