- Každý uzel v počítačové síti je identifikován pomocí IP adresy. $\rightarrow$ nejsou lehce zapamatovatelné
- Řešením tohoto problému jsou doménová jména. Textová, snadněji zapamatovatelná identifikace uzlu v počítačové síti.

## Doménové jméno
- Doménová jména se zapisují jako textové řetězce o maximální délce $255$ znaků. 
- Při zápisu se využívají pouze ASCII znaky a nerozlišují se velká a malá písmena.
- Doménové jméno se skládá z několika částí, které se označují jako domény.
	- Pro jejich rozdělení se používá tečka (.)
- Domény jsou hierarchicky organizovány do stromové struktury, čímž vzniká vztah doména-subdoména.
  ![[MacBook-2024-04-17-001036.png| 500]]
- Pod kořenovou doménou se nachází top-level domény. (generické nebo národní)

## Jmenné servery
- Kořenová doména je umístěna na kořenovém (jmenném) serveru. 
- Ve skutečnosti existuje $13$ kořenových serverů, ty se značí písmeny $a-m$, jsou rozmístěny po celém světě a jsou spravovány různými institucemi.
- Každý z těchto serverů existuje v mnoha kopiích

## Překlad doménového jména na IP adresu
- Překlad je realizován jako klient-server služba, která zprostředkovává protokol DNS. Služba je bězně provozována na portu udp/53.
- Pokud je odpověď větší než $512$B, je využito TCP spojení pro získání kompletní odpovědi.

- Překlad řeší **resolver**.
- Na klientovi je resolver součástí operačního systému. Může být řešen i mimo klienta na serveru.
- Obvykle může překlad řešit lokální jmenný server nebo veřejný resolver. Z tohoto důvodu musí mít jmenné servery uloženy IP adresy kořenových serverů.

0. Klient chce zjistit IP adresu ke jménu www.example.com. Klient nejprve prohledá svoji lokální cache, zda v ní není uložena odpověď.
1. Klient pošle rekurzivní dotaz na DNS resolver. Pokud DNS resolver má odpověď uloženou v cache, pošle jí klientovi a překlad končí.
2. Pokud DNS resolver nezná odpověď, pošle nerekurzivní dotaz na kořenový jmenný server.
3. Kořenový jmenný server zcela určitě nezná odpověď, ale ví, kdo je zodpovědný za doménu com v našem dotazu. Kořenový server pošle DNS resolveru jeho adresu.
4. DNS resolver pošle nerekurzivní dotaz na jmenný server spravující doménu com.
5. Jmenný server zodpovědný za doménu com nezná odpověď, ale ví, kdo je zodpovědný za doménu exmaple.com, a pošle DNS resolveru jeho adresu.
6. DNS resolver pošle nerekurzivní dotaz na jmenný server spravující doménu example.com.
7. Jmenný server spravující doménu example.com zná odpověď (1.2.3.4) a pošle ji DNS resolveru.
8. DNS resolver přidá 1.2.3.4 klientovi a uloží si údaje do své cache.
9. Klient uloží 1.2.3.4 do své cache a kontaktuje 1.2.3.4.
![[MacBook-2024-04-17-001037.png]]

## Uložení DNS záznamů
- DNS záznamy jsou uloženy v RR (Resource Records) záznamech.
![[MacBook-2024-04-17-001038.png]]

##### Navigace
Předchozí:  [[Protokoly TCP a UDP - spojení a řízení toku dat]]
Následující: [[Aplikační služby a tvorba síťových aplikací]]
Celý okruh: [[2. Informační technologie]]