## Proces
- **proces** určuje stav výpočtu v danou chvíli
	- je buď přímo vykonávám nebo reprezentován jako *pokračování*
	- v OS charakterizován pomocí: kód programu, paměťový prostor, data, zásobník, registry
- **context switch** ... přepínání procesů
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
#### Algoritmy pro plánování
1) First comed first served
	- první proces získá procesor, zbytek čeká ve frontě
2) Shortes job first
	- vybírá proces, který spotřebuje nejméně času
	- dobrá průchodnost, ale je nutno odhadnout potřebný čas
3) Shortest remaining time next
	- pokud následující potřebuje méně času, tak je přepnut
4) Round robin
	- každý proces má časové kvantum (> než je nutné)
	- zbytek řazen ve frontě
	- je spravedlivý
5) Prioritní fronta
	- každý proces má danou prioritu (dána staticky či dynamicky, po I/O vyšší)
	- pro každou prioritu zvlášť fronta
	- procesy s nízkou prioritou mohou vyhladovět
6) Shortes process next
	- odhad podle předchozí aktivity procesu
	- vhodný pro interaktivní OS
7) Guaranteed scheduling
	- každý proces dostane stejně času -> postupně se určuje poměr kolik času měl vs kolik potřeboval
	- volí se ten co má poměr nejmenší
8) Lottery scheduling
	- náhodně volení losů (možnsot výměny losů mezi procesy)
9) Fair share scheduling
	- podle skupin procesů
## Multitasking
- zjednodušeně - jeden procesor, více procesů
- procesor střídavě vykonává jednotlivé procesy
#### 1. Kooperativní multitasking
- proces se musí dobrovolně zříci procesoru
- např. starší OS, JavaScript
#### 2. Preemptivní multitasking (pro nás hlavní)
- systém rozhoduje o odebrání procesoru procesu
- např. současné OS

- **atomická operace** ... během vykonání je NELZE přerušit
- **historie** ... posloupnost atomických operací
## Slabá férovost
- historie je *slabě férová* pokud v každém stavu platí: "jestliže se proces chystá vykonat operaci, musí se dále v historii objevit"
- plánovač je *slabě férový* pokud jsou slabě férová všechny jeho historie
