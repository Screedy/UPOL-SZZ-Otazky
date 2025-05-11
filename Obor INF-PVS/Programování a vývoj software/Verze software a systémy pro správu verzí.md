## Verzování SW
- přidělíme jednoznačné ID pro aktuální stav projektu
- běžné dvojí značení
	1) marketingový název
	2) interní číslování
- mělo by dávat smysl (nikoliv náhodný řetězec)
- mělo by jít snadno zapamatovat
- hned určit co je starší a co novější
- občas se přidává i kódové jméno
- opět máme ustálené schéma
- obvykle zveřejněno i s **roadmap**
#### Sémantikcé verzování
- `major.minor.patch`
- pomáhá s problémy typu dependency hell
- deklarace veřejného API
- bez leading zeroes
- pokud `major` == 0, tak není stabilní
- patch se zvyšuje při opravách chyb
- minor při přidání nové funkcionality se zpětnou kompatabilitou
- major při nekompatabilních změnách ve veřejném API
- při zvýšením se vždy nižší verze nulují
- rozšíření pomocí pomlčky `1.0.0-aplha`
- pomocí + přidáme metadata `1.0.0-beta+exp.sha.511`
#### Verze odvozená od data
- vhodnější pro produkty měnící se často
- kombinace s sémantickým verzováním
- ihned poznáme stáří produktu
#### Další
- obyčejné číslo
- sudá-lichá vezre (sudá ... stabilní, lichá ... vývojová)
- zeroVer - major je pořád 0

- naše schéma by mělo být zveřejněno
- každé vydání musí obsahovat changelog
- zveřejnit roadmap
- včas ohlásit vydání nové major
- změna schématu (občas je nevyhnutelná, může přinést komplikace)
	- Java 1.8.0 -> Java 8
## Verzovací systémy
- nutné u projektů, kde pracuje více lidí
	- je nutné mít k dispozici i starší verzi
	- možnost synchronizovat přidané funkcionality od více lidí najednou
#### Git
- distribuovaný verzovací systém
- Linus Torvalds
- dnes nejpopiulárnější
##### Repozitář
- databáze obsahující všechny informace nutné ke správě verzí a sledování změn
- `.git`
- object store ... vše potřebné pro obnovení verze (logy, autoři, úložiště origo souborů)
- index ... dočasný binární soubor trackující změny
	- po commitu jsou zaznamenány natrvalo
- commit ... záznam o změně v repozitáři
	- ukládá pouze změněné soubory
	- vždy má předka
	- má unikátní jméno
- větvění ... rozdělení do více souběžných větví
	- spojení pomocí merge
	- proč? izolovanost jednotlivých funkcí, rozdělení podle vývojářů, oddělení pro různé verze
	- má vždy jméno (master, dev, testing, ...)
	- aktivní je vždy jen 1
- merge ... spojení
	- mohou nastat konflikty, jinak automatické
	- upravíme buď ručně nebo pomocí nějakého nástroje
- stash ... zásobník pro odležení rozpracované práce
	- pokud potřebujeme nutně jít dělat něco jiného
	- uložíme si jen pro sebe (není nikd epublikována)
- remote ... vzdálený repozitář
	- developement a bare
	- clone nebo fetch dat

- git má samozřejmě i alternativy, ale je nejpopiulárnější
	- mercurial
	- bazaar
#### Webové CVS
- *concurent version system*
- slouží především pro prezentaci
- rychlo prohlížení kódu i nevývojáři
- vizualizace větví
- GitHub
- GitLab
- BitBucket
#### Continuous integration (CI)
- snaha o co největší míru automatizace sestavení a testování
- úzce spolupracuje s verzovacím systémem
	- commit sestaven, otestován unit testy (někdy i integrační)
- vývojáři vyvíjí a současně a průběžně se integruje
##### CI server
- SW kontrolujícíc repozitáíř a vykonávající různé akce
	- kompilace
	- spouštění testů (i výpočet code coverage)
	- checking coding conventions
	- CI pipeline
- podporují weboví klienti Gitu
#### Continuous delivery
- zahrnuje správu configurací a přístupových údajů
- automaticky synchronizuje testovací a produkční prostředí
- delivery je pouze doručení nikoliv nasazení (to si obvykle žádá manuální zásah)
#### Continuous deployment (CD)
- automatizace nasazení aktuální verze
- není žádoucí přímo na produkci, takže vhodné do testovacího prostředí
- v produkci dobré na jedno kliknutí (neboli potvrzení zákazníka)