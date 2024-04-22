## Vlastnosti
- IPv6 (Internet Protocol version 6) je nejnovější verze internetového protokolu navržená pro řešení nedostatků a omezení svého předchůdce, IPv4. 
- Hlavní vlastnosti IPv6 zahrnují:
	- **Rozšířený adresní prostor**: IPv6 používá 128bitové adresy.
	- **Zjednodušená hlavička:** Hlavička je jednodušší jak v IPv4. To zajišťuje jednodušší zpracování routerem.
	- **Lepší podpora pro multicast a unicast:** IPv6 efektivněji implementuje multicast (jedna zdrojová adresa na mnoho cílových adres) a anycast (jedna zdrojová adresa na nejbližší z mnoha cílových adres).
	- **Automatická konfigurace:** IPv6 podporuje stavovou (stateful) i stavově nezávislou (stateless) auto-konfiguraci zařízení, což umožňuje zařízením automaticky nakonfigurovat sebe sama bez potřeby DHCP serveru.
	- **Lepší zabezpečení**: Pv6 bylo navrženo s přihlédnutím na zabezpečení. IPsec, který je volitelný v IPv4, je v IPv6 integrován jako povinná součást, což zvyšuje bezpečnost komunikace na síti.

## IPv6 paket
- IPv6 paket obsahuje základní hlavičku a data. Hlavička IPv6 je jednodušší než hlavička IPv4 a má pevnou délku 40 bytů. Struktura hlavičky zahrnuje:
	- **Verze**: 4b, verze protokolu, vždy 6
	- **Traffic class**: 8b, prioritizace paketu
	- **Flow label**: 20b, umožňuje označení sekvence paketů pro speciální zpracování
	- **Payload length**: 16b, delka v B za hlavičkou
	- **Next header:** 8b, typ následující hlavičky
	- **Hop limit:** 8b, k určení maximálního počtu routerů na cestě 
	- **Source address**: 128b, adresa odesílatele
	- **Destination address:** 128b, adresa příjemnce
![[Pasted image 20240422162927.png | 500]]

## Typy IPv6
- IPv6 adresy jsou dlouhé 128 bitů a jsou obvykle zapisovány jako osm skupin čtyř hexadecimálních číslic oddělených dvojtečkami. 
- Existují různé typy adres:
	- **Unicast adresy:** Adresa jednoho rozhraní. Pakety odeslané na unicast adresu jsou doručeny přímo tomuto rozhraní.
	- **Multicast adresy:** Adresa skupiny rozhraní. Pakety jsou doručeny všem rozhraním ve skupině.
	- **Anycast adresy:** Adresa přidělená skupině rozhraní, ale pakety jsou doručeny pouze nejbližšímu rozhraní ve skupině podle směrovacího algoritmu.
	- **Link-local adresy:** Používají se pouze v lokální síti a pakety s těmito adresami nejsou směrovány na internet.

