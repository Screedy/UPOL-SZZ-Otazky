## Specifikace požadavků a proces zjišťování
- zákazník musí přesně specifikovat cíle a vlastnosti celého systému
1) **Abstraktní popis funkčních požadavků**
	- základní funkce na abstraktní úrovni
	- např. telefon umožní uskutečnit hovor a poslat SMS
2) **Definice vlastností systému**
	- nefunkcionální emergnetní vlastnosti
	- jak má být bezpečný a spolehlivý
	- v každém subsytému
	- např. telefon vydrží 100 hodin v pohotovostním režimu
3) **Jak se systém nemá chovat**
	- občas nůže být vhodnější říct, co NEMÁ dělat
- jaká jsou fáze?
	1) rozdělení požadavků do skupin
	2) identifikace subsystémů
	3) přiřezení požadavek - subsytém
	4) specifikace funkcionality subsystémů
	5) definice rozhraní mezi subsystémy
	- fáze se ovlivňují navzájem (i zpětně) => možný i spirálový vývoj
#### Modelování systémlů
- abstraktní záležitost (v různé míře)
- **blokový diagram komponent**
	![[Pasted image 20231216113244.png]]
	- může být další i pro každý subsystém
- vhodné doplnit tabulkou
	![[Pasted image 20231218163346.png]]
#### Studie providitelnosti
- levná, krátká
- výstupem je zpráva, která nám odpoví jestli se do toho vůbec máme pustit, případně co změnit aby to šlo
- zdroje: manažeři uživatelů, SW inženýři, technologičtí experti, koncoví uživatelé
- co má systém řešit? co by se dělalo pokud by nebyl implementován? můžeme použít info odjinud? musíme nasadit novou technologii?
#### Zjišťování požadavků
- zjistit požadavky a analyzovat je
- co nejvíce informací k fomrulaci uživatelských a systémových požadavků
- mnoho zúčastněných => problémy v porozumění
	- neví co chtějí
	- nejsou realistické
	- možné spory
	- různé pojmy
4) **objevování požadavků** - interakce s účastníky (nesmíme na nikoho zapomenout)
5) **klasifikace a organizace** - setřídení nasbíraných informací
6) **prioritizace a vyjednávání** - řešení sporů, co má přednost
7) **dokumentace** - bude sloužit jako podklad pro další fázi
- fáze možno opakovat, kvůli zpětné vazbě
- rozhovory
	- uzavřené vs otevřené otázky
	- získání vhledu do problematiky
	- pozor na moc nápadů
	- občas těžko porovant papír vs realita
	- vhodné demonstrovat na prototypu
	- použití konkrétních scénářů (pozor i na to co se může pokazit)
#### Validace požadavků
- běheme procesu
- oprávněnost, konzistence, úplnost, realizovatelnost, ověřitelnost
- revize od týmu nebo externího uživatele, prototyp produktu, testovací případy
#### Správa požadavků
- požadavky se v průběhu budou měnit
- koncepční vs konkrétní
- nutné udržovat historii verzí požadavků
- nutné je mít navzájem provázané
- verzovací systémy + jak evidovat změny
#### Proces změny požadavků
- změna by neměla proběhnout jen tak
- co je za problém, zda je validní, jak konkrétně změnit
- co jde ruku v ruce se změnou (cena, implementace, časová náročnost)
- rozchod DSP a reality při urgentní změna (může vést k lavinovému efektu)