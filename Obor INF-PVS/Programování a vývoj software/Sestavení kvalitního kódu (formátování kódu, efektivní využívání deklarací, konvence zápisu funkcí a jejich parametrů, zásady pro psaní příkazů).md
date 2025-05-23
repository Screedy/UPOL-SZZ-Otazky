## Kvalitní kód a jeho čitelnost
- více metriky pro "kvalitní kód" (musí splňovat, ale nestačí)
	- dělá co má dělat
	- je naprogramován rychle/levně
	- splňuje emergentní vlastnosti
#### Vnější vlastnosti (od uživatele)
1) korektnost ... dělá co má
2) použitelnost ... jak rychle se uživatel naučí používat
3) spolehlivost ... jak často spadne
4) integrita ... zabránění neoprávněnému přístupu
5) robustnost ... chování při ztížených podmínkách
#### Vnitřní vlastnosti (od programátora)
1) udržovatelnost ... snadnost přidání nových funkcí
2) flexibilita ... úprava pro jiné než původně zamýšlené použití
3) přenositelnost ... běh v jiných prostředích
4) znovupoužitelnost ... kolik % můžeme použít i jinde
5) čitelnost ... čtení zdrojáků
6) testovatelnost ... nutné úsilí při tvorbě testů
7) srozumitelnost ... pochopení architektury
#### Formátování
- zkombinovat obojí je náročné (i drahé)
- vazba vlastností? vyžadují se navzájem? není nutné, požadavky se celkem doplňují
	- př. špatný srozumitelnost -> horší přidání funkcí -> větší pravděpodobnost chybovosti
- software by měl být flexibilní (měnící se požadavky uživatelů), zároveň ale musí mít rozumnou míru, aby programátorům nedal moc zabrat
- čitelnost se nedá exaktně měřit a je subjektivní
- existují pouze doporučení
- nejvíce bychom se měli držet konzistentnosti (`tab` vs `mezerník`, 2 vs 4, `camelCase` vs `snake_case`)
	- coding conventions
	- celkově ovlivněno IDE
- zásadně ovlivňuje jazyk (jeho abstrakce atd.)
	- to obvykle programátor neovlivní (dostane zadání)
- rozdělení metod (ty co se volají navzájem blízko u sebe)
- dělení do více souborů (co třída to soubor)
- délka řádku (do 80 dříve, do 120 dnes) - kvůli řetězení metod
	- např. LINQ
#### Pojmenování
- jméno je nositelem informace
	- **krátké a výstižné** (logicky to není easy vymyslet)
	- dostatečně specifické
	- jednoznačný (nemělo by jít vyložit 2 způsoby)
- mohou být i komplexní (pokud vyjádří přesně co mají)
- iterátory a zažitá jména (`i, j, k, it, iter`)
- pracujeme-li s jednotkami (sekundy, dny, ...) uvádíme je v názvu
	- `public void Delay (int delaySec)`
- vyhnout se magickým konstantám
- rozsahy - včetně obou, bez krajních hodnot, ...
	- `first, last`
	- `begin, end`
#### Složité výrazy
- rozdělit na podproblémy => najdeme obecnejší, abstrakci
- De Morganovy zákony využít ke zjednodušení podmínek
#### Komentáře
- dvousečné
- pokud je kód dobře napsaný nepotřebuje moc komentovat
- naopak může vysvětlit optimlizační úpravy či jiné "hacky"
- dočasné komentáře (@TODO, @FIXME atd.), které zvýrazní IDE
#### Proměnné
- rozumné proměnné => zvýší čitelnost i udržitelnost
- rozsah platnosti
- oblast života (měla by být co nejkratší)
- každá deklarovaná by měla být použita
- do 16 znaků délky
- 1 proměnná = 1 účel
## Techniky zvyšující kvalitu kódu
- v průběhu let ověřené metody jak psát kvalitní kód (jejich dodržení zaručí částečnou kvalitu)
- podstatná je sebekázeň
#### Defenzivní programování
- preventivní opatření před špatnými daty (všichni nám lžou, i my sobě)
1) kontrola všeho z externích zdrojů (síť, UI, ...)
2) kontrola vstupních hodnot parametrů funkcí
3) rozhodnutí co dělat při špatných datech
- zvýšení kvalita za cenu snížení čitelnosti
> [!info]
> **Assertion**
> `1 assert(delitel != 0);`
> `2 assert(pocet <= MAXPOCET);`
> - součást pouze vývoje, nikoliv produkce

- minimalizace vzájemné závislosti komponent na sobě (ideálně žádná, ale v praxi nedosažitelné)

>[!info]
>**KISS** = keep it simple stupid
>- obecně věci fungují dobře pokud jsou jednoduché
>- komponenta by měla dělat 1 věc, ale pořádně
