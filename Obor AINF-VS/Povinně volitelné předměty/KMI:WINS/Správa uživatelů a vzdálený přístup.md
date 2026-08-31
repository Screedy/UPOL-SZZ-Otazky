# 1. Typy uživatelských účtů

## 1.1 Lokální účty

- Existuje pouze na jednom _konkrétním počítači_.
- Uloženy v lokální databázi SAM (`Security Accounts Manager`).
  - Použití: samostatné servery (workgroup), nouzové účty, servisní účty pro lokální služby.
  - Spravuje se přes `lusrmgr.msc` (Local Users and Groups) nebo `net user`.

## 1.2 Doménové účty

- Uloženy v _Active Directory_ **na** **řadičích domény**, použitelný na všech členských strojích domény.
  - Centrální správa, jednotné přihlášení (SSO).
  - Spravuje se přes
    - **Active Directory Users and Computers** **(**`dsa.msc`**)**
    - nebo **Active Directory Administrative Center** **(**`dsac.exe`**)**.

## 1.3 Vestavěné účty (built-in)

- **Administrator** — plná kontrola; v doméně členem Domain Admins, Enterprise Admins.
- **Guest** — ve výchozím stavu zakázaný (bezpečnostní riziko).
- **DefaultAccount, krbtgt** — systémové; `krbtgt` je klíčový pro Kerberos (jeho heslo šifruje TGT — Ticket Granting Ticket).

## 1.4 Servisní účty (service accounts)

- **Managed Service Account (MSA)**
  - Účet pro spouštění služby s _automatickou rotací hesla_.
  - Použitelný pouze na _jednom stroji_.
- **Group Managed Service Account (gMSA)**
  - Rozšíření MSA, použitelné _na více strojích současně_.
    - Vyžaduje **KDS Root Key** v doméně: `Add-KdsRootKey -EffectiveImmediately`.

---

# 2. Skupiny a princip AGDLP

## 2.1 Typy skupin v AD

> [!success]
> Určují, k čemu skupina slouží.

- **Security group** — slouží k přidělování oprávnění (má SID).
- **Distribution group** — pouze pro e-mailové distribuce (Exchange), nemá SID.

## 2.2 Rozsah skupin (scope)

> [!success]
> Určuje, odkud může skupina brát členy a kde v rámci lesa/domény jí lze přidělit oprávnění.

| Rozsah | Členové z | Použitelná pro oprávnění |
| --- | --- | --- |
| **Domain Local** | celý les | jen v dané doméně |
| **Global** | jen vlastní doména | celý les |
| **Universal** | celý les | celý les (replikuje se do GC) |

#### Vysvětlení pojmu Doména/strom/les

- **Doména** = jedna „organizační jednotka" se společnou databází uživatelů (např. `firma.local`).
- **Strom (tree)** = doména a její subdomény se sdíleným jmenným prostorem (`firma.local`, `praha.firma.local`, `brno.firma.local`).
- **Les (forest)** = jeden nebo více stromů, které sdílejí společné **schéma**, **konfiguraci** a **Global Catalog**, ale můžou mít úplně jiné jmenné prostory (`firma.local` + `firma-cz.com`).


## 2.3 Princip AGDLP / AGUDLP

- **Account → Global → (Universal) → Domain Local → Permission**
- Příklad:
  - Uživatele dáme do globální skupiny podle role (např. „Účetní")
  - Tu vložíme do doménově lokální skupiny svázané s konkrétním zdrojem (např. „Přístup_Sdílení_Faktury")
  - Té přiřadíme oprávnění.
- Cíl: oddělit „kdo je kdo" (G) od „co může na zdroji" (DL) → změny rolí nevyžadují zásahy do ACL.

## 2.4 Vestavěné skupiny

- **Domain Admins** — admini celé domény.
- **Enterprise Admins** — admini celého lesa (existuje jen v root doméně).
- **Schema Admins** — mohou měnit schéma AD; do této skupiny by se mělo přidávat jen dočasně.
- **Account Operators, Server Operators, Backup Operators** — delegovaná oprávnění na konkrétní operace.

---

# 3. Profily uživatelů

- **Lokální profil**
  - uložen v `C:\Users\<uživatel>` na konkrétním PC.
- **Roaming profile**
  - Uložen na síťovém share.
  - Stahuje se při přihlášení.
  - Změny se synchronizují při odhlášení.
- **Mandatory profile**
  - Roaming profil, který se po odhlášení neukládá.
  - Vhodné pro kiosky.

- **Folder Redirection**
  - Přesměrování složek (Dokumenty, Plocha) na síťový share přes GPO.
  - Často se dává **místo** roaming profilu nebo **s ním**, protože řeší jeho hlavní slabinu: _kopírování velkých dat při každém_ přihlášení/odhlášení. Data zůstávají na serveru, profil je pak malý a rychlý.
- **User Profile Disks (UPD) / FSLogix**
  - Moderní řešení pro RDS/VDI.

---

# 4. Autentizace a autorizace

## 4.1 Autentizace (kdo jsi)

- **Kerberos** (od Windows 2000 výchozí v doméně) — tiketový systém, využívá **KDC** běžící na DC.
  - Vyžaduje synchronizovaný čas (max. odchylka 5 minut).
  - **SPN (Service Principal Name)**
    - Identifikátor služby v AD, např. `MSSQLSvc/srv1.firma.local:1433`.
    - Bez správného SPN Kerberos nefunguje a klient padne na NTLM.
- **NTLM**
  - Starší challenge-response
  - Používá se v workgroup, při přihlašování přes IP adresu, mimo AD.
  - Považován za méně bezpečný.
- **LDAP bind**
- Autentizace proti AD přes LDAP (port 389) nebo LDAPS (636).

## 4.2 Autorizace (co smíš)

- **ACL (Access Control List)** — seznam přístupových položek, dělí se na:
  - **DACL (Discretionary ACL)** — kdo má co dovoleno (čtení, zápis…).
  - **SACL (System ACL)** — co se má auditovat (úspěšné/neúspěšné přístupy).
- **SID (Security Identifier)**
  - Unikátní identifikátor uživatele/skupiny
  - Oprávnění jsou vázána na SID, ne na jméno.
- **Token** — při přihlášení se vytvoří přístupový token obsahující SID uživatele a SID všech jeho skupin. Token se porovnává s DACL.

---

# 5. Vzdálená správa serveru

## 5.1 Remote Desktop Protocol (RDP)

> [!success]
> Microsoftem vyvinutý protokol (port **3389**) pro přenos vzdálené plochy.

- Aktivace: Server Manager → _Local Server_ → _Remote Desktop_ → Enable.
- **Network Level Authentication (NLA)**
  - Ověření před zobrazením přihlašovací obrazovky
  - Chrání proti DoS a brute-force.
  - Doporučeno mít zapnuté.

> [!danger]
> Pro připojení musí být uživatel v lokální skupině **Remote Desktop Users** (nebo administrátor).

## 5.2 WinRM a PowerShell Remoting

- **WinRM (Windows Remote Management)** — implementace WS-Management, port **5985 (HTTP)** / **5986 (HTTPS)**.
- **Intuice:** „SSH pro Windows" — místo grafiky posílá příkazy a strukturované objekty.
- Zapnutí: `Enable-PSRemoting -Force`.
- **Trusted Hosts** — pro připojení mimo doménu nutno explicitně povolit:
  - `Set-Item WSMan:\localhost\Client\TrustedHosts "srv01"`

## 5.3 Server Manager a RSAT

> [!success]
> **Server Manager** — centrální GUI pro správu lokálního i vzdálených serverů (lze přidat servery a spravovat je z jedné konzole).

> [!success]
> **RSAT (Remote Server Administration Tools)** — sada nástrojů pro Windows 10/11, umožňuje správu serveru z klientského PC.

- **Windows Admin Center (WAC)**
  - Moderní webové GUI pro správu serverů z prohlížeče.
  - Doporučovaný nástupce některých funkcí Server Manageru.

## 5.4 Server Core

- **Server Core**
  - Instalace bez GUI
  - spravuje se výhradně vzdáleně (PowerShell, WAC, Server Manager) nebo lokálně přes `sconfig`.
  - Šetří RAM, disk, attack surface

---

# 6. Remote Desktop Services (RDS)

> [!success]
> **RDS** je role poskytující vzdálené pracovní plochy a aplikace více uživatelům současně.

- Místo aby každý uživatel měl plnohodnotný PC, přihlásí se na server a tam mu „běží" plocha nebo jen konkrétní aplikace.

## 6.1 Komponenty RDS

- **RD Session Host** — server, na kterém běží uživatelské sezení.
- **RD Connection Broker** — rozhoduje, kam uživatele přesměrovat
  - Např. load balancing, reconnect na rozpojené sezení
- **RD Gateway** — poskytuje přístup zvenčí přes HTTPS.
  - Tuneluje RDP — není nutné otevírat 3389 do internetu.
- **RD Web Access** — webové rozhraní s ikonami publikovaných RemoteApp.
- **RD Licensing** — server pro správu CAL (Client Access License).
  - Bez něj funguje jen 120 dní v grace period.

#### Typy CAL

- **Per User CAL** — licence vázána na uživatele (může se připojit z více zařízení).
- **Per Device CAL** — licence vázána na zařízení (více uživatelů, jeden PC).

---

# 7. VPN a vzdálený přístup zvenčí

- Instaluje se přes Server Manager → _Add Roles and Features_ → **Remote Access**, podrole **DirectAccess and VPN (RAS)**.

## 7.1 VPN protokoly ve Windows Serveru

| Protokol | Port | Charakteristika | Stav |
| --- | --- | --- | --- |
| **PPTP** | TCP 1723 + GRE | Starý, slabé šifrování (MS-CHAPv2 prolomeno) | **Nepoužívat** |
| **L2TP/IPsec** | UDP 500, 4500, 1701 | L2TP tuneluje, IPsec šifruje | OK, ale problémy s NAT |
| **SSTP** | TCP 443 | RDP-like nad SSL/TLS, projde firewallem | Doporučeno pro Windows klienty |
| **IKEv2** | UDP 500, 4500 | Rychlé přepojení (mobilita), MOBIKE | Doporučeno |

#### DirectAccess

- _B_ez nutnosti uživatelské akce; klient se automaticky připojí, jakmile má internet.
- Vyžaduje IPv6 (interně tuneluje přes IP-HTTPS), klienty Enterprise edice, doménově připojené.
- **Postupně nahrazován Always On VPN**.

#### Always On VPN (AOVPN)

- Moderní nástupce DirectAccess, od Server 2016/Win 10 1607+.
- Dva tunely: **device tunnel** (před přihlášením, např. pro správu) a **user tunnel** (po přihlášení).
- Konfigurace přes **ProfileXML** distribuovaný např. přes Intune/SCCM.

---

# 8. Autentizace a autorizace přístupu

## 8.1 NPS (Network Policy Server) a RADIUS

- **RADIUS (Remote Authentication Dial-In User Service)**
  - Protokol pro centralizovanou AAA (Authentication, Authorization, Accounting).
- **NPS** — Microsoft implementace RADIUS serveru, role ve Windows Serveru.

> [!info]
> Jeden centrální bod, který všem zařízením (VPN, Wi-Fi APs, switche s 802.1X) říká, kdo se smí přihlásit a co může dělat.

- Konfigurace: **NPS console (**`nps.msc`**)** → Policies → Connection Request Policies + Network Policies.

## 8.2 Vícefaktorová autentizace a moderní bezpečnost

- **Smart Card / certifikát**
- Místo hesla čip s certifikátem.
- Integrace s AD přes EAP-TLS.
- **Windows Hello for Business**
  - Biometrie/PIN vázané na hardware (TPM).
  - Od Server 2016 podporováno na úrovni AD.
- **MFA pro VPN**
  - Typicky NPS Extension for Azure MFA.
  - NPS po ověření hesla pošle požadavek do Azure AD MFA, který si vyžádá druhý faktor.
- **LAPS (Local Administrator Password Solution)**
  - Automatická rotace lokálního admin hesla, uložení v AD.
  - Od Windows 11/Server 2022 vestavěný.