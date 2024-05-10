## Souborové systémy
- umožňují uchovávání většího množství dat
- data jsou perzistentní (přežijí proces)
- k datům je umožněn souběžný přístup
- **řešení**: ukládání dat na vnější paměť (např. disk), data jsou ukládána do souborů tvořící souborový systém
---
- OS nabízí základní sadu funkcí pro operace se soubory:
	- `create`: vytvoření souboru
	- `write/append`: přepis nebo zápis na konec souboru
	- `read`: čtení ze souboru
	- `seek`: změna pozice
	- `erase`: odstranění souboru
	- `truncate`: zkrátí daný soubor na požadovanou velikost

## Oddíly
- každý fyzický disk se obvykle skládá z jedné nebo více logické části (partition)
- v každém oddílu může existovat souborový systém (svazek)
- v Unix každý svazek připojen jako adresář
- ve Windows jednotlivé svazky označeny (`a:`, `b:`, `c:`,...)
---
- **VFS : Virtual File System**:
	- využití abstrakce: umožňuje kombinovat různé FS do jednoho VFS
	- možnost připojit běžný soubor jako svazek
	- kompatibilita síťových disků

>[!Example]- Příklad VFS
>![[MacBook-2024-05-03-001166.png]]

### LVM (Logical Volume Management)
- = metoda správy diskového prostoru
- poskytuje větší variabilitu než konvenční způsob dělení disků na diskové oddíly
- umožňuje spojovat více pevných disků nebo oddílů do logických celků
- možnost emulovat RAID
- možnost vložit vrstvu starající se o snapshoty, provádět šifrování
>[!Example] LVM
>![[MacBook-2024-05-03-001168.png]]

### RAID (Redundant Array of Independent Disks)
- kombinuje několik fyzických diskových jednotek do jednoho logického úložiště
- cílem je zvýšit spolehlivost, rychlost a kapacitu diskového úložiště
- **RAID 0** (stripping) - Data jsou rozdělena na bloky a distribuována rovnoměrně mezi disky bez redundantních dat.
- **RAID 1** (mirroring) - Data jsou zrcadlena
- **RAID 5** (stripping with parity) - 
	- Data a paritní informace jsou rozloženy mezi tři nebo více disků.
	- Parita umožňuje obnovu dat z ostatních disků v případě selhání jednoho disku.
- **RAID 6** (stripping with double parity) - 
	- jako 5, ale podporuje strátu dvou disků
- a různé kombinace... například **RAID 10**, **RAID 60**, ...

## Struktura souboru
- často je soubor chápán jako proud bytů 
	- občas jiná struktura, jako třeba multimediální soubor (více proudů)
- macOS: každý soubor má dva proudy (data, prostředky)
- NT: umožňuje k proudu přidat libovolný počet proudů
- s daty jsou k souboru připojena metadata (vlastník, přístupová práva, velikost souboru, čas vytvoření, čas posledního přístupu, ...)

## Zajištění konzistence dat
### Žurnálování
- data se zapisují v transakcích
- často se žurnálují jen metadata
- Algoritmus:
	1. nejdříve se změna zapíše do žurnálu
	2. po zapsání do žurnálu je záznam označen speciální značkou
	3. data se zapíší na cílové místo na disku
	4. po zapsání na disk je záznam z žurnálu smazán
- při připojení FS se kontroluje stav žurnálu
	- zápis záznamu do žurnálu nebyl dokončen (chybí značka) $\rightarrow$ transakce se neprovede
	- jinak: transakce se zopakuje podle instrukcí v žurnálu
- žurnál je cyklický (při zaplnění maže začátek)
- potřeba atomický zápis na disk

### Copy-on-Write
>[!Example] Copy-on-Write
>![[MacBook-2024-05-03-001169.png]]


## Příklady souborových systémů
- **FAT**
	- FS původně pro MS-DOS
	- jednoduchý design
	- soubory a adresáře ve tvaru $8+3$
	- nemá ochranu proti poškození dat
	- varianty: FAT12, FAT16, FAT32, VirtualFAT, exFAT
- **UFS: Unix File System**
	- reálně používané varianty UFS obvykle obsahují navzájem nekompatibilní rozšíření
	- využívá strukturu i-node
		- $15$ ukazatelů na bloky na disku:
		- $0-11$ ukazují na bloky na disku
		- $12$ nepřímý blok $1.$ úrovně
		- $13$ nepřímý blok $2.$ úrovně
		- $14$ nepřímý blok $3$. úrovně
		- nepřímé bloky odkazují do datové části

>[!Example] struktura i-node 
>![[MacBook-2024-05-03-001167.png]]

- **NTFS**
	- hlavní souborový systém Windows NT
	- oproti FAT ochrana před poškozením, práva žurnálování a transakce
- **ZFS**
	- kombinuje prvky LVM a RAID
	- disky spojeny do poolu, FS dělá automaticky stripping
	- deduplikace dat
	- podpora komprese
	- RAID-Z: podobný RAID-5, ale má různě velké bloky
	- u dat kontrolní součty
	- konzistence založan na CoW (Copy on Write)

##### Navigace
Předchozí: [[Práce se vstupně výstupními zařízeními, ovladače]]
Následující: [[Tabulky v SQL a jejich vztah k relacím]]
Celý okruh: [[2. Informační technologie]]