## Proces
- **proces** určuje stav výpočtu v danou chvíli
	- je buď přímo vykonávám nebo reprezentován jako *pokračování*
	- v OS charakterizován pomocí: kód programu, paměťový prostor, data, zásobník, registry
- proces se může nacházet v několika *stavech*
	1) **běžící** - procesor vykonává instrukce procesu
	2) **připravený** - proces může být vykonán
	3) **blokovaný** - nemůže být vykonán, může ho odblokovat bežící proces
	- ![[Pasted image 20250310130820.png]]
#### Sdílené vazby
- umožní komunikaci mezi procesy
- nový proces sdílí s procesem, který jej vytvořil všechny vazby definované **v době vzniku**
## Plánovač
- uloží běžící proces a následně obnoví **náhodně** vybraný proces
- spouštíme po
	- náhodně zvoleném čase (čas jako počet kroků zásobníkového stroje)
	- nebo při vyprázdnění programového zásobníku

- **paralelní program** ... určuje více procesů, které spolupracují na splnění úkolu
	- např. UI, OS, paralelní algoritmy, databázové systémy
## Multitasking
- zjednodušeně - jeden procesor, více procesů
- procesor střídavě vykonává jednotlivé procesy
#### Kooperativní multitasking
- proces se musí dobrovolně zříci procesoru
- např. starší OS, JavaScript
#### Preemptivní multitasking (pro nás hlavní)
- systém rozhoduje o odebrání procesoru procesu
- např. současné OS

- **atomická operace** ... během vykonání je NELZE přerušit
- **historie** ... posloupnost atomických operací
## Slabá férovost
- historie je *slabě férová* pokud v každém stavu platí: "jestliže se proces chystá vykonat operaci, musí se dále v historii objevit"
- plánovač je slabě férový pokud jsou slabě férová všechny jeho historie
