# 1. Group Policy

> [!success]
> **Group Policy** je mechanismus **centrální správy konfigurace** _uživatelů_ a _počítačů_ v _doménovém prostředí Active Directory_.
>
> Administrátor definuje _nastavení_ (politiky) a ty se a**utomaticky aplikují na cílové objekty** (uživatele, počítače) podle jejich umístění v OU hierarchii.

> [!info]
> **Intuice:** Group Policy je **dálkové ovládání stovek počítačů najednou** — místo abyste chodili ke každému PC a r_učně měnili nastavení_, **definujete pravidlo jednou** a Windows se o zbytek postará.
>
> Bez Group Policy by administrátor musel konfigurovat registry, nastavení zabezpečení, instalovat software a mapovat disky na každém stroji zvlášť — neškálovatelné.

## 1.1 Hlavní nástroje

- **Group Policy Management Console (GPMC)** — `gpmc.msc`.
  - _Centrální konzole_ pro vytváření, linkování, filtrování, zálohování a diagnostiku GPO.
- **Group Policy Management Editor (GPME)** — `gpedit.msc` nebo se otevírá z GPMC dvojklikem na GPO.
  - Slouží k editaci nastavení uvnitř GPO.
- **PowerShell modul GroupPolicy** — `Import-Module GroupPolicy`.

---

# 2. Group Policy Object (GPO) — struktura a anatomie

> [!success]
> **GPO** je kontejner nastavení, který se linkuje na _site, doménu_ nebo _OU_.
>
> Obsahuje dvě hlavní větve: _Computer Configuration_ a _User Configuration_.

## 2.1 Dvě větve GPO

| Větev | Aplikuje se na | Kdy se zpracovává | Příklad nastavení |
| --- | --- | --- | --- |
| **Computer Configuration** | Počítačové účty (objekty computer v AD) | Při startu počítače + periodicky (každých 90–120 min) | Firewall pravidla, audit policy, software installation, bezpečnostní nastavení |
| **User Configuration** | Uživatelské účty (objekty user v AD) | Při přihlášení uživatele + periodicky | Mapování disků, přesměrování složek, nastavení plochy, omezení Control Panelu |

## 2.2 GPO verze a `GPT.INI`

- Každé GPO má číslo verze zvlášť pro Computer a User část.
- `GPT.INI` v SYSVOL obsahuje `Version=<číslo>` — klient porovnává s verzí v AD. Pokud se neshodují, GPO se znovu aplikuje.

> [!danger]
> **Problém:** Pokud SYSVOL replikace zaostává za AD replikací, klient vidí novou verzí v AD, ale stáhne starý obsah ze SYSVOL → nekonzistence.

## 2.3 Výchozí GPO

- **Default Domain Policy** — linkováno na doménu. Obsahuje výchozí nastavení password policy, account lockout policy, Kerberos policy.
- **Default Domain Controllers Policy** — linkováno na `OU=Domain Controllers`.
  - Obsahuje výchozí audit policy a User Rights Assignment pro DC.
  - Doporučení: pokud možno nemodifikovat přímo, raději vytvořit nové GPO.
    - **Proč?** Výchozí GPO lze obnovit příkazem `dcgpofix`, ale ten přepíše jakékoli vlastní úpravy. Pokud si do Default Domain Policy přidáte další nastavení a pak musíte spustit `dcgpofix`, přijdete o ně.

---

# 3. Pořadí zpracování GPO

## 3.1 Pravidlo LSDOU

GPO se aplikují v tomto pořadí (od nejnižší po nejvyšší prioritu):

1. **L — Local Policy** (`gpedit.msc`) — lokální politika na samotném počítači. Má nejnižší prioritu; doménové GPO ji přepíší.
2. **S — Site** — GPO linkovaná na AD site (fyzickou lokalitu).
3. **D — Domain** — GPO linkovaná na doménu (např. Default Domain Policy).
4. **OU — Organizational Unit** — GPO linkovaná na OU. Pokud jsou vnořené OU, aplikují se od nejsvrchnější po nejhlubší (parent → child).

## 3.2 Více GPO na jedné úrovni — Link Order

- Na jedné OU může být linkováno více GPO.
  - Zpracovávají se **od nejvyššího Link Order čísla po nejnižší** (= GPO s Link Order 1 se aplikuje **poslední** a má **nejvyšší prioritu**).
- **Intuice:** Link Order 1 = „poslední slovo" = nejvyšší priorita.

> [!info]
> Pokud různé GPO konfigurují různá nastavení, výsledek je kumulativní — všechna nastavení se sloučí. Konflikt nastává pouze tehdy, když dvě GPO konfigurují **totéž nastavení** na jinou hodnotu.

---

## 4. Dědičnost, blokování a vynucení

## 4.1 Inheritance (Dědičnost)

- GPO linkované na vyšší úrovni (doména, parent OU) se automaticky dědí na nižší úrovně (child OU).
  - Tzn. pokud linkuji GPO na doménu, platí pro všechny OU v ní (pokud není blokováno).

### 4.1.1 Blokování dědičnosti

- Na OU lze zapnout _Block Inheritance_ — tím se **zablokují** všechny **zděděné GPO** z **vyšších úrovní**.

> [!danger]
> Blokujete i důležité bezpečnostní GPO! Používat opatrně.

### 4.1.2 Enforced (Vynucení)

- Na linku GPO lze zapnout _Enforced_ — tím se tato GPO **nemůže přepsat** žádným GPO na nižší úrovni **ani zablokovat** přes _Block Inheritance_.

> [!info]
> **Typický scénář:** Bezpečnostní baseline GPO linkované na doménu s Enforced — ani pobočka s Block Inheritance ho neobejde.

- **Enforced vždy vyhrává** nad Block Inheritance.
- Pokud mám GPO s Enforced na doméně a OU má Block Inheritance → **GPO se i tak aplikuje.**
- Pokud více GPO má Enforced, přednost má to **na vyšší úrovni**.

---

# 5. Filtrování GPO — Security Filtering a WMI Filtering

## 5.1 Security Filtering

> [!success]
> Mechanismus, který určuje, na koho se GPO skutečně aplikuje, na základě ACL na GPO objektu.

- **Výchozí stav:** Nově vytvořené GPO má ve Security Filtering skupinu **Authenticated Users** — tzn. aplikuje se na _všechny uživatele i počítače v linkované OU_.
- **Cílení na podmnožinu:**
  1. Odeberte _Authenticated Users_ ze Security Filtering.
  2. Přidejte konkrétní skupinu (např. `GRP_Marketing`).
  3. GPO se aplikuje pouze na členy této skupiny, kteří jsou v linkované OU.

> [!info]
> **Intuice:** Link GPO říká KDE se aplikuje (OU). Security Filtering říká NA KOHO v rámci toho KDE.

### 5.1.1 Důležitá změna: MS16-072 (2016)

- Od bezpečnostní záplaty MS16-072 nestačí, aby uživatelský účet měl Read + Apply Group Policy. **Počítačový účet musí mít alespoň oprávnění Read** na GPO, jinak se GPO nestáhne.
- **Praktický dopad:** Pokud v Security Filtering odstraníte Authenticated Users a přidáte jen uživatelskou skupinu, musíte na záložce Delegation přidat skupinu **Domain Computers** s oprávněním **Read**.

## 5.2 WMI Filtering

> [!success]
> Filtr založený na WQL dotazu (WMI Query Language), který vyhodnotí podmínku na cílovém počítači. Pokud dotaz vrátí `true`, GPO se aplikuje; pokud `false`, přeskočí se.

- **Typické použití:**
  - Aplikovat GPO na notebooky: `SELECT * FROM Win32_Battery`.
  - Aplikovat na 64-bit OS: `SELECT * FROM Win32_Processor WHERE AddressWidth = 64`.
- **Omezení:** WMI filtry se _vyhodnocují na klientovi_ a **mohou zpomalit** zpracování **GPO**.
  - Nepoužívat příliš složité dotazy.
- **WMI filtr se přiřazuje celému GPO** — nelze přiřadit jen jedné větvi (Computer/User).
- Na jedno GPO lze přiřadit **maximálně jeden WMI filtr**.

---

# 6. Group Policy Preferences (GPP) vs. Group Policy Settings (Policies)

| Vlastnost | **Policies** (nastavení politik) | **Preferences** (předvolby) |
| --- | --- | --- |
| Chování | **Vynucené (enforced)** — registry se zamknou | **Preferované** — uživatel může změnit; pokud GPO zmizí, nastavení zůstane |
| Registry | Zapisuje do **policy klíčů** | Zapisuje do **normálních klíčů** (kam by zapisovala i aplikace) |
| Tattooing | **Ne** u Policies větve — po odebrání GPO se nastavení odstraní (vrátí na Not Configured) | **Ano** ve výchozím stavu — po odebrání GPO nastavení v registru zůstane |
| Item-level targeting | **Ne** | **Ano** — granulární cílení (OS verze, IP rozsah, security group, OU, disk, RAM, atd.) |

- **Policies** → uživatel **nemůže změnit**, po zrušení GPO se **vrátí do neutrálního stavu**.
- **Preferences** → nastaví mapování disku, tiskárnu, zástupce, ale uživatel si to **může změnit**. Pokud GPO odstraníte, **nastavení na klientovi zůstane**.

## 6.1 Co všechno GPP umí (příklady)

- **Drive Maps** — mapování síťových disků.
- **Printers** — mapování tiskáren.
- **Scheduled Tasks** — vytvoření naplánovaných úloh.
- **Registry** — zápis do registrů.
- **Shortcuts** — vytvoření zástupců na ploše/Start menu.
- **Environment Variables** — nastavení systémových proměnných.
- **Files / Folders** — kopírování souborů, vytváření složek.
- **Local Users and Groups** — přidání doménových skupin do lokální skupiny.
- **Network Shares** — vytvoření sdílení na cílovém stroji.
- **Services** — změna startup type / spuštění/zastavení služby.
- **Data Sources (ODBC)** — konfigurace ODBC připojení.
- **Power Options, Internet Settings, INI Files** a další.

## 6.2 Item-Level Targeting (ILT)

> [!success]
> Jemný filtr uvnitř GPP položky — umožňuje cílit jednu _preference položku_ na _specifickou podmnožinu_ počítačů/uživatelů bez nutnosti vytvářet více GPO.

- **Typické podmínky:** Security Group, Operating System, IP Address Range, Computer Name, OU, Environment Variable, File Match, Registry Match, Disk Space, Portable Computer a další.

> [!info]
> **Intuice:** WMI filtr je hrubým sítem na celé GPO. Item-level targeting je jemný sítem na jednu konkrétní položku uvnitř GPO.

---

# 7. Administrative Templates (ADMX/ADML)

> [!success]
> **Administrative Templates** definují nastavení registru **formou** uživatelsky přívětivých **politik**.
>
> Každá šablona (.admx soubor) popisuje _klíč registru, hodnotu, datový typ a popis_.

- Nejrozsáhlejší sekce GPO.

## 7.1 Central Store

> [!warning]
> **Problém:** Pokud každý admin edituje GPO ze svého PC, vidí Administrative Templates podle ADMX souborů na svém lokálním PC — verze se mohou lišit.

> [!success]
> **Řešení: Central Store** — složka `\\<doména>\SYSVOL\<doména>\Policies\PolicyDefinitions\`, kam se zkopírují ADMX/ADML soubory.
>
> GPMC pak automaticky použije Central Store místo lokálních šablon.

- Při instalaci nové verze Windows / Office / aplikace, která přidá nové ADMX, je potřeba je **ručně zkopírovat do Central Store**.

---

# 8. Security Settings v GPO

Obsahují:

1. **Account Policies**:
  - **Password Policy** — min. délka, složitost, historie, max. stáří hesla.
  - **Account Lockout Policy** — počet neúspěšných pokusů, doba uzamčení, reset čítače.
  - **Kerberos Policy** — max. životnost tiketu, tolerance hodin.
2. **Local Policies:**
  - **Audit Policy** — co se loguje (přihlášení, přístup k objektům, změny politik…).
  - **User Rights Assignment** — kdo smí co (přihlásit se lokálně, přihlásit se přes síť, vypnout systém, …).
  - **Security Options** — renaming admin/guest účtu, UAC chování, SMB podpis, LAN Manager auth level…
3. **Event Log**: max. velikost logů, retence.
4. **Restricted Groups**:
  - vynucení členství v lokálních skupinách (např. zajistit, že ve skupině Administrators jsou jen povolené účty).
5. **System Services**: startup mode služeb.
6. **Registry**: oprávnění na klíče registru.
7. **File System**: oprávnění na soubory/složky.
8. **Windows Firewall with Advanced Security**: pravidla firewallu.
9. **Advanced Audit Policy Configuration**: granulární audit, nahrazuje starší Audit Policy.

## 8.1 Password Policy — důležité upozornění

- Account Policies z GPO **mají efekt pouze pokud jsou v GPO linkovaném přímo na doménu** (ne na OU!).
- GPO s Password Policy linkované na OU se **ignoruje**.
- Pro různé politiky hesel pro různé skupiny → **FGPP / PSO** (Fine-Grained Password Policy).
- **Efekt:** Na všech počítačích, kde se GPO aplikuje, bude lokální skupina Administrators obsahovat **výhradně** tyto členy — vše ostatní se odstraní.

---

# 9. Skripty v GPO (Logon, Logoff, Startup, Shutdown)

> [!success]
> **Skripty v GPO** slouží k _automatizaci úloh_ navázaných na _start/vypnutí_ počítače a _přihlášení/odhlášení_ uživatele (mapování disků, instalace, úklid dočasných dat) a mohou být psané jako dávkové soubory nebo v PowerShellu.

| Typ | Kdy běží | Větev GPO | Kontext |
| --- | --- | --- | --- |
| **Startup** | Při startu počítače (před přihlášením) | Computer Configuration | SYSTEM account |
| **Shutdown** | Při vypnutí počítače | Computer Configuration | SYSTEM account |
| **Logon** | Při přihlášení uživatele | User Configuration | Kontext uživatele |
| **Logoff** | Při odhlášení uživatele | User Configuration | Kontext uživatele |

---

# 10. Software Installation přes GPO

> [!success]
> Mechanismus pro centrální nasazení software balíčků (.msi) přes GPO.

- Nachází se v `Computer Configuration → Policies → Software Settings → Software installation` nebo _User Configuration_.

| Režim | Chování |
| --- | --- |
| **Assigned (Computer)** | Software se nainstaluje **automaticky při startu počítače**.   Uživatel nemusí nic dělat. |
| **Assigned (User)** | Zástupce se objeví v Start menu.   Instalace proběhne při prvním spuštění. |
| **Published (User)** | Software se objeví v „Programs and Features" → _„Install a program from the network"_.   Uživatel si ho nainstaluje sám. |

- Podporuje **pouze .msi** balíčky (ne .exe).
  - Pro .exe je potřeba vytvořit _.msi wrapper_.

---

# 11. Folder Redirection (Přesměrování složek)

> [!success]
> **Folder Redirection** — přesune vybrané uživatelské složky (Desktop, Documents, AppData…) ze složky profilu na síťové úložiště.

- Nachází se v `User Configuration → Policies → Windows Settings → Folder Redirection`.

## 11.1 Proč to použít

- Záloha dat uživatele na serveru.
- Zmenšení roaming profilů (profil neobsahuje data, jen odkaz).
- Rychlejší přihlašování (data se nestahují, jen se přesměruje cesta).

- **Oprávnění:** Na sdílení a NTFS musí mít uživatel právo vytvořit svou podsložku.
  - Doporučený NTFS: Creator Owner = Full Control, **uživatel nemá práva na cizí složky**.

---

# 12. Zpracování GPO na klientovi (Client-Side Extensions)

## 12.1 Jak klient zpracovává GPO

1. **Počítač se spustí** → kontaktuje DC (LDAP) → zjistí, které GPO se na něj vztahují.
2. Stáhne GPO šablony ze SYSVOL (SMB).
3. **Client-Side Extensions (CSE)** — DLL moduly na klientovi, které zpracovávají jednotlivé sekce GPO:
  - Registry CSE (Administrative Templates),
  - Security CSE (Security Settings),
  - Scripts CSE (skripty),
  - Software Installation CSE,
  - Folder Redirection CSE,
  - Disk Quota CSE,
  - Wireless/Wired Policy CSE,
  - atd.
4. **Uživatel se přihlásí** → stejný proces pro User Configuration GPO.

## 12.2 Obnovovací cyklus

- **Výchozí interval:** Každých **90 minut ± náhodný offset 0–30 minut**.
- **DC (Domain Controllers):** Každých **5 minut**.
- **Background refresh:** GPO se obnovují na pozadí i bez odhlášení/restartu.
- **Výjimky:** Některá nastavení se aplikují **pouze** při startu/přihlášení — Software Installation, Folder Redirection, Drive Maps.

---

# 13. Typický workflow nasazení GPO

1. **Navrhnout OU strukturu** podle potřeb GPO.
2. **Vytvořit GPO** v GPMC (pojmenovat dle konvence — např. `SRV-Firewall-Enable`, `USR-FolderRedirection`).
3. **Nakonfigurovat nastavení** v GPME.
4. **(Volitelně) Přidat WMI filtr** nebo upravit Security Filtering.
5. **Linkovat GPO na OU** (nebo doménu/site).
6. **Testovat:** `gpupdate /force` na testovacím klientovi → `gpresult /h` → ověřit.
7. **Nasadit do produkce** postupně.