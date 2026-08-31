# 1. DHCP — Dynamic Host Configuration Protocol

> [!success]
> **DHCP** je síťový protokol, který automaticky přiděluje IP adresy a další konfigurační parametry (maska, brána, DNS servery) klientům v síti.

- **Port:** server naslouchá na **UDP 67**, klient odesílá z **UDP 68**.

## 1.1 Proces DORA (**DHCP Lease Process**)

Probíhá broadcastem (klient ještě nemá IP):

1. **Discover** — Klient odešle broadcast `DHCPDISCOVER` do sítě.
2. **Offer** — DHCP server odpoví `DHCPOFFER` s nabídkou IP adresy a parametrů.
3. **Request** — Klient broadcastem potvrdí `DHCPREQUEST`.
  - Broadcast proto, aby ostatní DHCP servery věděly, že jejich nabídku odmítl.
4. **Acknowledge** — server potvrdí přidělení: `DHCPACK`. Klient si nastaví IP.

- Pokud server nemůže vyhovět → pošle `DHCPNAK` a klient začíná znovu.
- **Renewal:** klient se pokouší obnovit lease na 50 % doby trvání, pokud neuspěje, opakuje na 87,5 % (nyní broadcast).

## 1.2 Scope (rozsah)

> [!success]
> **Scope** je _rozsah IP adres_, které DHCP server **přiděluje klientům** v dané podsíti.

- Každý scope definuje:
  - **Rozsah adres** — např. `10.0.1.100 – 10.0.1.200`.
  - **Masku podsítě** — např. `255.255.255.0` nebo `/24`.
  - **Exclusion range** — rozsah adres vyloučených z přidělování.
  - **Lease duration** — doba platnosti zápůjčky.
  - **Scope options** — parametry specifické pro tento scope (brána, DNS, doménové jméno).

### 1.2.1 Rezervace (Reservation)

> [!success]
> Trvalé přiřazení konkrétní IP adresy konkrétnímu zařízení na základě jeho **MAC adresy**.

- **Intuice:** „Tiskárna vždy dostane 10.0.1.50, i když používá DHCP — nemusíte ji konfigurovat staticky."
- IP musí být uvnitř scope, ale mimo exclusion range.

## 1.3 DHCP Failover (vysoká dostupnost)

> [!success]
> Mechanismus, kdy dva DHCP servery **sdílejí jeden scope** a navzájem se zastupují.

- **Režimy:**
  - **Load Balance** — oba servery **aktivně přidělují** adresy. Vhodné, jsou-li oba ve stejné lokalitě.
  - **Hot Standby** — **jeden** server je **aktivní** (primární), **druhý** **čeká** jako záloha.
- **Auto State Switchover Interval** — doba, po které se partner automaticky přepne z `Partner Down` stavu do plného provozu.

> [!danger]
> DHCP Failover funguje pouze pro **IPv4 scope**. Pro IPv6 tato funkce nativně není — řeší se split-scope nebo clusteringem.

## 1.4 DHCP Relay Agent (IP Helper)

- **Problém:** DHCP Discover je broadcast → neprojde přes router.
- **Řešení:** Na routeru/L3 přepínači se konfiguruje **DHCP Relay Agent**, který broadcasty přeposílá unicastem na DHCP server v jiné podsíti.

## 1.5 DHCPv6

- DHCP pro IPv6 — dvě varianty:
  - **Stateful DHCPv6** — server přiděluje IPv6 adresy (jako u IPv4).
  - **Stateless DHCPv6** — klient si adresu generuje sám (SLAAC), od DHCPv6 serveru dostane jen doplňkové informace (DNS, doména).
- Scope v DHCPv6 se nazývá **prefix** (typicky /64).

## 1.6 DNS integrace (Dynamic DNS Update)

- DHCP server může automaticky registrovat A a PTR záznamy v DNS za klienty.
- Klienti Windows 2000+ standardně registrují svůj A záznam sami; DHCP server registruje PTR záznam.

## 1.7 Instalace role DHCP Server

- **GUI:** Server Manager → Add Roles and Features → **DHCP Server**.
- Po instalaci je nutná **autorizace v AD** (aby se v síti nemohl objevit rogue DHCP server).

---

# 2. DNS — Domain Name System

> [!success]
> **DNS** je hierarchický distribuovaný systém pro překlad doménových jmen na IP adresy (a naopak).

- Využívá port **TCP/UDP 53**.

> [!info]
> **Intuice:** „Telefonní seznam internetu — místo IP adresy 10.0.1.10 napíšete `dc01.firma.local` a DNS vám řekne, kam to směřuje."

- **DNS je kriticky důležitý pro Active Directory** — bez funkčního DNS nefunguje přihlašování, replikace, lokalizace služeb (SRV záznamy), Kerberos ani Group Policy.

## 2.1 Instalace role DNS Server

- **GUI:** Server Manager → Add Roles and Features → **DNS Server**.
- Při instalaci AD DS se DNS role obvykle instaluje automaticky na DC.
- **GUI nástroj:** **DNS Manager** (`dnsmgmt.msc`).

## 2.2 Typy DNS zón

### 2.2.1 Forward Lookup Zone

- Překládá **jméno → IP adresu** (např. `dc01.firma.local → 10.0.1.10`).
- Toto je nejpoužívanější typ zóny.

### 2.2.2 Reverse Lookup Zone

- Překládá **IP adresu → jméno** (např. `10.0.1.10 → dc01.firma.local`).
- Používá speciální doménu `in-addr.arpa` (IPv4) nebo `ip6.arpa` (IPv6).
- Není povinná, ale doporučená — potřebná pro `nslookup` bez parametrů, pro některé služby a logy.

### 2.2.3 Typy zón podle způsobu uložení a správy

| Typ zóny | Popis | Typické použití |
| --- | --- | --- |
| **Primary zone** | Čtení i zápis; hlavní kopie zónových dat. Uložena v souboru (`.dns`) nebo v AD. | Hlavní DNS server pro doménu |
| **Secondary zone** | Pouze čtení; kopie dat z primary zóny (přenos zón). Uložena v souboru. | Záložní DNS, odlehčení zátěže |
| **Stub zone** | Obsahuje pouze NS záznamy autoritativních serverů cizí zóny (aby věděl, kam se doptat). | Zrychlení delegace bez full transfer |
| **AD-Integrated zone** | Primary zone uložená v databázi AD (replikace přes AD replikaci, ne zone transfer). | Výchozí volba v AD prostředí |
| **Conditional Forwarder** | Pravidlo: dotazy na konkrétní doménu přeposílat na konkrétní DNS server. | Překlad jmen partnerské domény |

## 2.3 AD-Integrated Zones (podrobněji)

> [!success]
> DNS zóna uložená jako objekt v databázi Active Directory (v oddílu `DomainDnsZones` nebo `ForestDnsZones`).

- **Výhody oproti file-based zónám:**
  - **Multi-master replikace** — každý DC s DNS rolí může zónu editovat (ne jen jeden primary server).
  - **Secure Dynamic Updates** — pouze autentizované počítače (členové domény) mohou registrovat/měnit záznamy.
  - **Replikace přes AD replikaci** — efektivnější, šifrovaná, využívá existující topologii.
  - **Granulární oprávnění** — ACL na úrovni jednotlivých DNS záznamů.

## 2.4 DNS záznamy

| Typ záznamu | Název | Co dělá | Příklad |
| --- | --- | --- | --- |
| **A** | Address | Jméno → IPv4 adresa | `dc01.firma.local → 10.0.1.10` |
| **AAAA** | IPv6 Address | Jméno → IPv6 adresa | `dc01.firma.local → fd00::10` |
| **CNAME** | Canonical Name | Alias (ukazuje na jiné jméno) | `mail.firma.local → exchange01.firma.local` |
| **MX** | Mail Exchanger | Kam doručit e-mail pro doménu | `firma.local → mail.firma.local (priorita 10)` |
| **NS** | Name Server | Autoritativní DNS server pro zónu | `firma.local → dc01.firma.local` |
| **SOA** | Start of Authority | Metadata zóny (primary server, serial, refresh, TTL) |     |
| **SRV** | Service Locator | Umístění služby (port, protokol, server) | `_ldap._tcp.firma.local → dc01:389` |
| **PTR** | Pointer | IP adresa → jméno (reverzní) | `10.1.0.10 → dc01.firma.local` |
| **TXT** | Text | Textový záznam (SPF, DKIM, ověření) | `firma.local → "v=spf1 mx -all"` |

> [!info]
> **SRV záznamy jsou klíčové pro AD** — klienti přes ně nachází DC, GC, Kerberos KDC, LDAP servery.

## 2.5 Forwarding (přeposílání)

> [!success]
> **Forwarder** je DNS server, na který se přeposílají dotazy, které lokální server nedokáže vyřešit ze svých zón.

> [!info]
> **Intuice:** „Náš interní DNS server zná `firma.local`. Ale když se někdo ptá na `google.com`, dotaz přepošle na veřejný DNS (např. 8.8.8.8 nebo ISP DNS)."

- **Conditional Forwarder** — pravidlo pro konkrétní doménu: „Dotazy na `partner.cz` přeposílej na 192.168.50.1."
- Pokud forwarder neodpoví, DNS server může provést **rekurzivní dotaz** sám (root hints)
  - Může být zakázáno.

### 2.5.1 Root Hints

> [!success]
> Seznam kořenových DNS serverů (root servers), které DNS server použije pro rekurzivní překlad, pokud nemá forwarder nebo forwarder neodpovídá.

- Pokud DC je zároveň DNS server a obsahuje zónu „." (dot zone) — root hints nebudou fungovat (server se považuje za autoritativní pro root). Řešení: smazat zónu „." a nastavit forwardery.

## 2.6 Rekurze vs. iterace

- **Rekurzivní dotaz**
  - klient (nebo forwarder) žádá DNS server: _„Zjisti mi úplnou odpověď."_
  - **Server** sám **obchází** hierarchii.
- **Iterativní dotaz**
  - DNS server odpovídá: _„Nevím, ale zkus se zeptat tady."_
  - **Klient** se ptá dál **sám**.

> [!info]
> **V praxi:** Klienti posílají rekurzivní dotazy na svůj DNS server.
>
> DNS servery mezi sebou používají iterativní dotazy.

- **Bezpečnost:** Rekurzi lze omezit nebo vypnout — zabrání zneužití pro DNS amplification útoky.

## 2.7 Zone Transfer

> [!success]
> **Zone transfer** je replikace zóny na sekundární servery.

- **Full Transfer (AXFR)**
  - Přenos **celé zóny** ze primary na secondary server.
  - Provede se při _prvním nastavení secondary zóny_ nebo _při velké změně_.
- **Incremental Transfer (IXFR)**
  - Přenos **pouze změn** od poslední aktualizace (na základě serial number v SOA záznamu).
- **Notify** — primary server **oznamuje** secondary serverům, že _došlo ke změně_ → secondary si **vyžádá** IXFR nebo AXFR.
- **Bezpečnost:** Zone transfer by měl být omezen **jen** na **povolené servery**.

> [!info]
> V AD-Integrated zónách se zone transfer nepoužívá (replikace jde přes AD replikaci), ale je potřebný pro secondary zóny na non-DC serverech.

## 2.8 Scavenging (úklid zastaralých záznamů)

> [!warning]
> **Problém:** Dynamicky registrované záznamy **se hromadí** — počítače se přejmenují, odstaví, ale staré záznamy zůstávají.

> [!success]
> **Scavenging** je **automatický proces** mazání záznamů, které _nebyly obnoveny_ v nastaveném intervalu.

- Dva intervaly:
  - **No-Refresh Interval** — doba, po kterou server odmítá obnovení záznamu.
    - Prevence zbytečné replikace.
    - Výchozí 7 dní.
  - **Refresh Interval** — doba, po jejímž uplynutí se záznam považuje za zastaralý a může být smazán.
    - Výchozí 7 dní.

## 2.9 DNS Policies (od Server 2016)

> [!success]
> Pravidla, která umožňují DNS serveru odpovídat rozdílně na základě kritérií
>
> - zdrojová IP, čas, typ dotazu, rozhraní.

- **Použití:**
  - **Split-brain DNS** — stejná doména, různé odpovědi pro interní a externí klienty.
  - **Geo-location based routing** — odpověď podle lokace klienta.
  - **Time-of-day based** — různé odpovědi v různou denní dobu.

## 2.10 DNSSEC

> [!success]
> Rozšíření DNS o **digitální podpisy** záznamů, které **zajišťují integritu** a **autenticitu** odpovědí.

> [!info]
> **Intuice:** „Bez DNSSEC vám může útočník podstrčit falešnou DNS odpověď (DNS spoofing/cache poisoning). S DNSSEC je odpověď podepsaná a klient si může ověřit, že pochází z legitimního zdroje."

- V praxi v interním AD prostředí se DNSSEC nasazuje zřídka; běžnější na veřejných DNS serverech.

---

# 3. Integrace DHCP a DNS ve Windows Server prostředí

## 3.1 Typický scénář

1. Klient se zapne, pošle DHCP Discover.
2. DHCP server přidělí IP adresu a parametry (včetně adresy DNS serveru).
3. Klient (Windows) se zaregistruje v DNS (A záznam).
4. DHCP server zaregistruje PTR záznam (reverzní) za klienta.
5. Klient může být nalezen v DNS podle jména.

---

# 4. Typický deployment workflow

1. Nainstalovat první DC → automaticky se nainstaluje DNS → vytvoří se AD-Integrated zone pro doménu.
2. Nainstalovat DHCP roli → autorizovat v AD → vytvořit scope → nastavit options (DNS server = DC, brána).
3. Nakonfigurovat Dynamic DNS Updates (secure only) na DNS zóně.
4. Zapnout scavenging na zóně i serveru.
5. Volitelně: nastavit DHCP Failover s druhým DHCP serverem; přidat secondary DNS nebo další DC s DNS.