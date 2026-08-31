# 1. Active Directory Domain Services (AD DS)

> [!success]
> **AD DS** je serverová role Windows Serveru, která implementuje **adresářovou službu** založenou na protokolech LDAP, Kerberos a DNS.
>
> Umožňuje **centrální správu identit** (uživatelů, počítačů, skupin), **autentizaci**, **autorizaci** a aplikaci politik v podnikovém prostředí.

> [!info]
> **Intuice**: „AD DS je telefonní seznam a vrátnice zároveň — ví, kdo existuje v organizaci (adresář), ověřuje, že jste to opravdu vy (autentizace), a říká, kam smíte (autorizace)."
>
> Bez AD DS by každý server musel mít **vlastní lokální účty a oprávnění** — neškálovatelné.

## 1.1 Klíčové protokoly AD DS

| Protokol | Co dělá | Typické použití |
| --- | --- | --- |
| **LDAP** | Dotazy a modifikace objektů v adresáři | Vyhledávání uživatelů, čtení atributů, správa OU |
| **Kerberos** | Autentizace pomocí tiketů | Přihlášení do domény, SSO |
| **DNS** | Lokalizace řadičů domény (SRV záznamy) | Klient hledá DC, GC, KDC |
| **SMB/CIFS** | Replikace SYSVOL, Group Policy, přihlašovací skripty | Stahování GPO, logon skriptů |
| **RPC** | AD replikace, vzdálená správa | Replikace mezi DC |

## 1.2 Instalace role AD DS

- **GUI:** Server Manager → Add Roles and Features → Active Directory Domain Services → po instalaci spustit **Promote this server to a domain controller**.

---

# 2. Logická struktura AD — doména, strom, forest

## 2.1 Doména (Domain)

> [!success]
> Základní administrativní a bezpečnostní jednotka v AD.
>
> Sdílí společnou databázi, bezpečnostní politiky a jmenný prostor (např. `firma.local`).

> [!info]
> **Intuice:** „Jedna doména = jedna organizace se společnou sadou uživatelů, politik a pravidel."

- Každá doména má alespoň jeden řadič domény (DC — Domain Controller).
- Doména definuje **hranici replikace** — všechny DC v doméně replikují stejnou databázi.
- Doména definuje **hranici bezpečnostní politiky** — password policy, account lockout policy, Kerberos policy platí na úrovni domény.

## 2.2 Strom (Tree)

> [!success]
> Hierarchie domén se sdíleným jmenným prostorem DNS, propojených automatickým obousměrným tranzitivním trustem.

- **Příklad:** `firma.local` (root) → `praha.firma.local` → `brno.firma.local`.

> [!info]
> **Intuice:** „Strom je rodina domén se stejným příjmením (DNS suffixem)."

## 2.3 Les (Forrest)

> [!success]
> Nejvyšší organizační kontejner v AD.
>
> Jeden nebo více stromů, které sdílejí společné **schéma**, **konfigurační oddíl** a **Global Catalog**, propojené tranzitivním forest trustem.

- **Příklad:** Les může obsahovat stromy `firma.local` a `subsidiary.com` — různé jmenné prostory, ale společná struktura.
- **Klíčové vlastnosti lesu:**
  - **Společné schéma** (AD Schema) — definuje, jaké _typy objektů_ a _atributů_ existují
    - Např. objekt _User_ má atribut _mail_.
  - **Společný Configuration partition** — sites, services, replikační topologie.
  - **Global Catalog (GC)** — viz dále.
  - **Enterprise Admins** a **Schema Admins** existují jen v root doméně lesu.

## 2.4 Schéma AD (AD Schema)

> [!success]
> **Formální definice všech tříd objektů** (classSchema) a **atributů** (attributeSchema) v celém lesu. Uloženo v Schema partition.

> [!info]
> **Intuice:** **Schéma je šablona** — říká, jaké '_typy formulářů'_ (objekty) existují a jaká mají '_políčka_' (atributy). Bez rozšíření schématu nelze přidat nový atribut.

## 2.5 Diagram logické struktury

```
Forest (firma.local)
├── Tree: firma.local
│   ├── Doména: firma.local (forest root domain)
│   ├── Doména: praha.firma.local (child domain)
│   └── Doména: brno.firma.local (child domain)
└── Tree: subsidiary.com
    └── Doména: subsidiary.com (tree root domain)
```

---

# 3. Fyzická struktura AD — Sites, Subnets, Replikace

## 3.1 Sites (lokality)

> [!success]
> Objekt v AD reprezentující fyzickou lokaci s dobrou síťovou konektivitou (typicky LAN). Uložen v Configuration partition → Sites container.

> [!info]
> **Intuice:** Site = budova nebo pobočka, kde jsou stroje propojené rychlou sítí (Gigabit LAN +). Mezi sites je pomalý WAN link.

- **K čemu slouží:**
  - **Optimalizace replikace** — uvnitř _site_ se replikuje **okamžitě**. Mezi _sites_ se replikuje **podle plánu**.
  - **Lokalizace služeb** — klient se přihlašuje na DC ve _svém site_.

## 3.2 Subnets (podsítě)

> [!success]
> Podsíť IP přiřazená k site.
>
> Klient určí svůj site podle IP adresy — AD porovná IP klienta se seznamem subnetů.

- **Příklad:** Subnet `10.0.1.0/24` přiřazen k site `Praha`, subnet `10.0.2.0/24` k site `Brno`.

## 3.3 Site Links (spojení mezi sites)

> [!success]
> Objekt definující replikační cestu mezi dvěma nebo více sites.
>
> Určuje náklady (cost), frekvenci replikace a plán.

- **Atributy site linku:**
  - **Cost** — nižší cost = preferovaná cesta.
  - **Replication interval** — jak často se replikuje.
  - **Schedule** — kdy je replikace povolena.
- **Protokoly:** IP (RPC over IP, výchozí a doporučený) nebo SMTP (pouze pro schema a configuration partition — prakticky nepoužívaný).

## 3.4 Replikace AD

### 3.4.1 Intrasite replikace (uvnitř site)

- **Automatická, okamžitá** — _po změně_ DC **notifikuje partnery**.
- Latence typicky **15 sekund**.

### 3.4.2 Intersite replikace (mezi sites)

- **Plánovaná** — podle intervalu a schedule na site linku.
- Data se **komprimují**.

---

# 4. Organizational Units (OU) — organizační jednotky

> [!info]
> **OU** je kontejner v doméně sloužící k logickému seskupení objektů (uživatelů, počítačů, skupin) pro účely **delegace správy** a **aplikace Group Policy (GPO)**.

## 4.1 Návrh OU struktury

- **Podle organizačního uspořádání:** OU pro oddělení (`OU=IT`, `OU=Finance`, `OU=HR`).
- **Podle geografického umístění:** OU pro pobočky (`OU=Praha`, `OU=Brno`).
- **Podle typu objektu:** Oddělení uživatelů a počítačů (`OU=Uzivatele`, `OU=Pocitace`, `OU=Servery`).
- **Kombinace:** Často se kombinují — např. `OU=Praha\OU=Uzivatele`, `OU=Praha\OU=Pocitace`.

> [!note]
> **Best practice:** Navrhujte OU primárně podle potřeb GPO a delegace, ne podle org-chartu. Pokud dvě oddělení mají totožné politiky, nemusí mít separátní OU.

## 4.2 Ochrana OU před smazáním

- Ve výchozím stavu mají OU zapnutou ochranu _„Protect object from accidental deletion"_ — **nelze je smazat** bez odškrtnutí.

## 4.3 Delegace správy (Delegation of Control)

- **Co to je:** Přidělení specifických oprávnění na OU skupině administrátorů — např. helpdesk smí resetovat hesla v `OU=Uzivatele`, ale nesmí vytvářet uživatele.
- **Jak:** ADUC → pravý klik na OU → **Delegate Control** → průvodce s předdefinovanými úlohami:
  - Reset user passwords and force password change at next logon
  - Create, delete, and manage user accounts
  - Join a computer to the domain
  - Manage Group Policy links
  - a další...

---

# 5. Domain Controller (DC) — řadič domény

> [!success]
> **DC (Domain Controller)** — server s nainstalovanou rolí AD DS, který uchovává kopii doménové databáze, provádí autentizaci a autorizaci, a replikuje změny s ostatními DC.

## 5.1 Read-Only Domain Controller (RODC)

> [!success]
> DC s read-only kopií AD databáze. Nemůže přijímat zápisy přímo — všechny změny přeposílá na zapisovatelný DC.

> [!info]
> **Intuice:** RODC je bezpečný DC na pobočku, kde nemáte serverovnu pod zámkem. Pokud ho někdo ukradne, nedostane z něj kompletní hesla.

- **Klíčové vlastnosti:**
  - **Password Replication Policy (PRP)**
    - Definuje, která hesla se cachují na RODC. Ve **výchozím** stavu se **necachuje** nic.
  - **Filtered attribute set**
    - Některé _citlivé atributy_ (např. bitlocker recovery keys) se na RODC vůbec nereplikují.
  - **Delegovaná správa** — lokální admin RODC nemusí být Domain Admin.
  - **Read-only DNS** — pokud je RODC i DNS serverem, DNS zóny jsou read-only.

## 5.2 Vztah DC a DNS

- AD je **závislé na DNS** — klienti nachází DC přes SRV záznamy.
- Proto se při instalaci prvního DC automaticky nabídne instalace DNS role.
- Doporučení: **každý DC by měl být zároveň DNS server** s AD-Integrated zones.

---

# 6. FSMO role (Flexible Single Master Operations)

## 6.1 Proč FSMO existuje

- AD replikace je **multi-master** — jakýkoliv DC může přijímat zápisy. Ale některé operace musí být koordinovány jedním serverem, aby nedocházelo ke konfliktům
  - Např. _přidělování unikátních ID_, změna schématu.
- **FSMO role** = „ten jediný DC, který smí provádět konkrétní typ operace."

## 6.2 Umístění FSMO rolí — best practice

- Ve forestu s jednou doménou a dvěma DC:
  - Všechny role typicky na jednom DC (forest root DC), druhý DC je záloha.
- **Infrastructure Master by neměl být na DC, který je zároveň Global Catalog**.
  - (v single-domain forestu to nevadí, protože GC má i tak všechna data; problém je jen v multi-domain prostředí).

---

# 7. Global Catalog (GC)

> [!success]
> **Global Catalog (GC)** — speciální role DC, který uchovává **částečnou, read-only kopii všech objektů ze všech domén ve forestu**.
>
> GC navíc uchovává plnou kopii objektů své vlastní domény.

> [!info]
> **Intuice**: GC je _index celého forestu_ — když potřebujete najít uživatele z jiné domény, ptáte se GC, ne DC vzdálené domény.

## 7.1 K čemu GC slouží

- **Universal Group Membership** — při přihlášení Kerberos ověřuje membership v Universal skupinách přes GC. Pokud GC není dostupný, přihlášení selže.
- **Vyhledávání v celém forestu** — LDAP dotazy prohledávají celý forest.
- **Exchange / aplikace** — mnoho aplikací vyžaduje GC pro vyhledávání příjemců.
- **UPN přihlášení** — `jnovak@firma.local` se ověřuje přes GC.

---

# 8. Trusts (důvěry)

> [!success]
> **Trust (důvěra)** — vztah mezi dvěma doménami, který _umožňuje_ uživatelům z jedné domény _přistupovat_ ke _zdrojům v druhé doméně_.

> [!info]
> **Intuice:** „Trust je dohoda: 'Já věřím tvým uživatelům, takže je nechám přistupovat k mým zdrojům.'
>
> Trust nevytváří oprávnění — jen otevírá možnost je přidělit."

## 8.1 Vlastnosti trustů

| Vlastnost | Význam |
| --- | --- |
| **Směr (Direction)** | One-way (jednosměrný) nebo Two-way (obousměrný). |
| **Tranzitivita** | Tranzitivní = pokud A věří B a B věří C, pak A věří C. |

## 8.2 Vytvoření trustu

- **GUI:** Active Directory Domains and Trusts (`domain.msc`) → pravý klik na doménu → Properties → Trusts → New Trust.

---

## 9. AD Recycle Bin

> [!success]
> **AD Recycle Bin** — funkce umožňující obnovu smazaných objektů AD se **všemi atributy**.

- Bez Recycle Bin se _smazaný objekt stává „tombstone"_ — většina atributů je odstraněna, _obnova je částečná_ a komplikovaná.

> [!info]
> **Intuice**: Někdo smazal celou OU s 200 uživateli. S Recycle Bin je obnovíte jedním příkazem se všemi skupinami a oprávněními. Bez něj máte problém.

## 9.1 Zapnutí

- **GUI:** ADAC → pravý klik na doménu → Enable Recycle Bin.
- **Pozor:** Nelze vypnout. Ale žádný důvod to dělat — _vždy zapínat_.

---

# 10. LDAP — Lightweight Directory Access Protocol

> [!success]
> **LDAP** — standardní protokol pro přístup k adresářovým službám. V AD se používá pro dotazování, přidávání, modifikaci a mazání objektů.

## 10.1 Klíčové koncepty

- **Distinguished Name (DN)** — unikátní cesta k objektu v adresáři.
  - Příklad: `CN=Jan Novak,OU=IT,DC=firma,DC=local`.
- **CN** = Common Name, **OU** = Organizational Unit, **DC** = Domain Component.
- **Bind** — přihlášení k LDAP serveru (autentizace).
  - Simple bind (jméno + heslo),
  - SASL bind (Kerberos, NTLM).
- **Search base** — odkud hledat (např. `DC=firma`).
- **Search scope** —
  - Base (jen objekt),
  - OneLevel (přímí potomci),
  - Subtree (celý podstrom).
- **LDAP Filter** — syntaxe pro filtrování: `(&(objectClass=user)(department=IT))`.

---

# 12. AD objekty — uživatelé, počítače, skupiny

## 12.1 Uživatelské objekty

- Podrobně pokryto v Okruhu 1 (typy účtů, MSA, gMSA, vestavěné účty).

## 12.2 Počítačové objekty (Computer accounts)

- Každý počítač připojený do domény má svůj účet v AD (objekt typu `computer`).
- **Computer account password** — automaticky se mění každých 30 dní (machine account password). Pokud počítač 30+ dní nebyl v síti, může ztratit trust s doménou.

## 12.3 Skupiny

- Podrobně pokryto v Okruhu 1 (typy, scope, AGDLP).
- Pro AD okruh důležité: **Universal skupiny se replikují do GC** — nadměrné používání Universal skupin zvyšuje replikační provoz.

---

# 13. Active Directory Backup a Recovery

## 13.1 Co zálohovat

- **System State** — zahrnuje AD databázi (NTDS.DIT), SYSVOL, registr, boot soubory, certifikáty, Cluster DB.
- **Nástroj:** Windows Server Backup (`wbadmin`), nebo enterprise řešení (Veeam, Commvault).

## 13.2 DSRM (Directory Services Restore Mode)

- Speciální boot mód DC, kdy AD DS služba neběží — lze provádět offline operace s databází.
- Přihlášení lokálním DSRM heslem.

> [!danger]
> DSRM heslo je separátní od doménového — pokud ho zapomenete, nelze provést obnovu.

---

# 14. Typický deployment workflow AD DS

1. **Nainstalovat prvního DC** → automaticky nainstalovat DNS → vytvořit forest root domain → vytvořit AD-Integrated DNS zone.
2. **Nainstalovat druhý DC** ve stejném site (redundance) → replikace → přidat GC roli.
3. **Vytvořit OU strukturu** podle potřeb GPO a delegace.
4. **Zapnout AD Recycle Bin** (ireverzibilní, ale žádný důvod nezapínat).
5. **Nakonfigurovat sites a subnets** podle fyzické topologie.
6. **Vytvořit FGPP** (PSO) pro různé skupiny uživatelů.
7. **Nastavit zálohu System State** na všech DC.
8. **Zvýšit Functional Level** po odebrání starých DC.