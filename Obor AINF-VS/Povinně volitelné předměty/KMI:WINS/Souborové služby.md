# 1. Role File and Storage Services

> [!success]
> **File and Storage Services** je serverová role ve Windows Serveru, která sdružuje vše potřebné pro ukládání, sdílení a správu souborů v podnikové síti.

## 1.1 Instalace a komponenty

- Role se instaluje přes **Server Manager → Add Roles and Features**.  
  

> [!info]
> Hlavní podrole (features):
>
> - **File Server** — základní sdílení přes SMB.
> - **DFS Namespaces** — virtuální jmenný prostor sdílení.
> - **DFS Replication** — replikace dat mezi servery.
> - **File Server Resource Manager (FSRM)** — kvóty, screening, reporty.
> - **BranchCache for Network Files** — cachování souborů na pobočkách.
> - **Data Deduplication** — deduplikace dat na discích (od Server 2012).
> - **Work Folders** — synchronizace pracovních souborů na zařízení uživatelů.
> - **iSCSI Target Server** — server poskytující blokové úložiště přes iSCSI.
> - **Storage Replica** — synchronní/asynchronní replikace svazků (od Server 2016, plná verze pouze **Datacenter edice**).

---

# 2. Souborové systémy — NTFS a ReFS

## 2.1 NTFS (New Technology File System)

> [!success]
> **Výchozí souborový systém** Windows od verze NT 3.1.
>
> Podporuje oprávnění (ACL), šifrování (EFS), komprimaci, kvóty, žurnálování, hard/soft linky.

- Klíčové vlastnosti:
  - **Žurnálování** — transakční log chrání integritu metadat při výpadku napájení.
  - **Komprese** — na úrovni souborů/složek (transparentní pro uživatele, ale zvyšuje CPU zátěž).
  - **EFS (Encrypting File System)** — šifrování na úrovni souborů, vázané na certifikát uživatele.
    - Pozor: není BitLocker (ten šifruje celý svazek).
  - **Maximální velikost svazku i souboru:** 256 TB.
  - **Maximální délka cesty:** 260 znaků (tradiční limit); od Windows Server 2016 lze povolit dlouhé cesty přes GPO (`Enable Win32 long paths`).

### ReFS (Resilient File System)

> [!success]
> Souborový systém navržený pro odolnost a integritu dat (od Server 2012).

> [!info]
> Vylepšený FS pro velké datové svazky a virtualizaci — detekuje a opravuje poškození dat automaticky.

- Klíčové vlastnosti:
  - **Integrity Streams** — automatické ověřování checksumů metadat (a volitelně dat).
  - **Block Cloning** — rychlé kopírování bloků (využívá Hyper-V pro VHDX operace).
  - **Podpora Storage Spaces Direct** — primární FS pro S2D v Datacenter edici.
  - **Bez podpory:** komprese souborů, EFS, diskové kvóty na úrovni FS, hard linky, krátká jména.
  - **Nelze použít jako boot svazek** — systém musí běžet na NTFS.
  - **Max velikost svazku** — až 35 PB
- Typicky použito pro velké datasety, Hyper-V, zálohování.

---

# 3. Protokol SMB (Server Message Block)

> [!success]
> **SMB** — síťový protokol pro sdílení souborů, tiskáren a pojmenovaných rour (named pipes) v sítích Windows.

- Běží nad TCP port **445**.

#### Verze SMB

| Verze | Windows Server | Klíčové novinky |
| --- | --- | --- |
| SMB 1.0 | 2003 a starší | Zastaralý, zranitelný (WannaCry!). **Vypnout!** |
| SMB 2.0 | 2008 | Výrazné zrychlení, pipelining, větší buffery |
| SMB 2.1 | 2008 R2 | BranchCache, Durable Handles |
| SMB 3.0 | 2012 | SMB Multichannel, SMB Direct (RDMA), šifrování, transparentní failover |
| SMB 3.0.2 | 2012 R2 | Vylepšení výkonu, možnost úplného vypnutí SMB 1.0 |
| SMB 3.1.1 | 2016+ | Preauthentication integrity (SHA-512), povinné šifrování, cluster dialect fencing |


## 3.1 Důležité vlastnosti SMB 3.x

- **SMB Multichannel** — automatické využití více síťových karet pro vyšší propustnost a odolnost. Nevyžaduje NIC teaming, stačí více NIC na obou stranách.
- **SMB Direct (RDMA)** — přímý přístup do paměti přes síť. Vyžaduje RDMA-capable NIC.
- **SMB Encryption** — šifrování dat v přenosu (AES-128-CCM / AES-128-GCM od 3.1.1).
- **SMB Signing** — digitální podpis paketů proti manipulaci. Ve výchozím stavu povinný pro DC.

## 3.2 Bezpečnostní aspekty

- **SMB 1.0 = vypnout.** Zranitelnosti EternalBlue/WannaCry (2017). Od Server 2016 lze odebrat jako feature.
- **Šifrování** — zapnout minimálně na sdíleních s citlivými daty; na úrovni celého serveru zvažte dopad na výkon (cca 10–15 % overhead).
- **SMB Signing** — chrání proti man-in-the-middle; na DC je ve výchozím stavu povinné.

---

# 4. Sdílení složek (File Shares)

## 4.1 Vytvoření sdílení

- Server Manager → File and Storage Services → Shares → Tasks → New Share.
- Průvodce nabízí profily: **SMB Share – Quick**, **SMB Share – Advanced**, **NFS Share** (pro Linux klienty).

## 4.2 Share Permissions vs. NTFS Permissions

- **Share Permissions** — platí POUZE při přístupu přes síť (SMB).
  - Tři úrovně: Read, Change, Full Control.
- **NTFS Permissions** — platí VŽDY (lokálně i přes síť).
  - Granulární (Read, Write, Modify, Full Control, List Folder Contents, Read & Execute + speciální oprávnění).
- **Výsledné oprávnění → restriktivnější z obou**.
  - příklad: Share = Full Control, NTFS = Read → výsledek = Read.
- **Best practice:** Share permissions nastavit na **Everyone → Full Control** a vše řídit přes NTFS oprávnění.
  - Důvod: jednodušší správa, NTFS platí i lokálně.

---

# 5. NTFS oprávnění (NTFS Permissions)

## 5.1 Základní (Basic) oprávnění

| Oprávnění | Co umožňuje |
| --- | --- |
| **Full Control** | Vše včetně změny oprávnění a převzetí vlastnictví |
| **Modify** | Čtení, zápis, úprava, mazání souborů i podsložek |
| **Read & Execute** | Čtení + spouštění programů |
| **List Folder Contents** | Zobrazení obsahu složky (pouze složky) |
| **Read** | Zobrazení obsahu a vlastností souboru |
| **Write** | Vytváření souborů a složek, zápis dat |

## 5.2 Pokročilá (Advanced / Special) oprávnění

- Základní oprávnění jsou _kombinace speciálních._
  - např. Modify = Read + Write + Delete + Read & Execute.
- Speciální oprávnění umožňují **granulární řízení**:
  - Traverse Folder, Delete Subfolders and Files, Change Permissions, Take Ownership atd.
- Přístup: Properties → Security → Advanced.

## 5.3 Dědičnost (Inheritance)

- **Výchozí chování:** oprávnění se **dědí z nadřazené složky** na _podřízené objekty_.
- **Blokování dědičnosti:** Properties → Security → Advanced → _Disable inheritance_.
  - Dvě možnosti:
    - **Convert inherited permissions to explicit** — zachová stávající oprávnění jako explicitní.
    - **Remove all inherited permissions** — vyčistí vše.

## 5.4 Efektivní oprávnění (Effective Access)

- Výsledek kombinace všech ACE (Access Control Entries) aplikovaných na uživatele a jeho skupiny.
- **Deny vždy přepisuje Allow** (výjimka: explicitní Allow na objektu přepisuje zděděný Deny).

---

# 6. Access-Based Enumeration (ABE)

> [!success]
> **ABE** — funkce, která skrývá soubory a složky ve sdílení, ke kterým uživatel nemá oprávnění.

- „**Vidí jen to**, **co může otevřít**. Bez ABE vidí všechny složky, jen je nemůže otevřít."
- **Výkon:** Mírný dopad — server musí pro každý objekt ověřit ACL vůči tokenu uživatele.

---

# 7. Offline Files a BranchCache

## 7.1 Offline Files (Client-Side Caching)

> [!success]
> Mechanismus, který umožňuje klientům cachovat obsah sdílení lokálně a pracovat s ním i bez připojení k síti.

## 7.2 BranchCache

> [!success]
> Technologie cachování obsahu na pobočkách, aby se snížil provoz přes WAN.

- **Režimy:**
  - **Distributed Cache** — klienti na pobočce cachují a sdílejí obsah mezi sebou (peer-to-peer).
    - Vhodné pro malé pobočky (do ~50 klientů).
  - **Hosted Cache** — dedikovaný server na pobočce drží cache.
    - Pro větší pobočky.
- Vyžaduje zapnutí na serveru i na klientech.

---

# 8. DFS — Distributed File System

## 8.1 DFS Namespaces (DFS-N)

> [!success]
> **DFS Namespaces** — služba, která sdružuje sdílení z více serverů pod jeden virtuální UNC jmenný prostor.

> [!info]
> Místo `\\srv01\finance`, `\\srv02\hr`, `\\srv03\it` mají uživatelé **jednotný vstupní bod:** `\\firma.local\dfs\finance`, `\\firma.local\dfs\hr` atd.
>
> Pokud se server přestěhuje, změní se jen cíl za namespace — uživatelé nic nepoznají.

### 8.1.1 Typy namespace

- **Domain-based namespace**
  - Uložen v AD → Vyžaduje AD DS.
  - Dostupný jako `\\doména\NázevNamespace`.
  - Podporuje více namespace serverů (vysoká dostupnost).
- **Standalone namespace**
- Uložen na jednom serveru, dostupný jako `\\server\NázevNamespace`.
- Žádná replikace metadat, single point of failure.

## 8.2 DFS Replication (DFS-R)

> [!success]
> **DFS-R** — multi-master replikační engine, který synchronizuje obsah složek mezi servery.

### 8.2.1 Jak funguje

- **RDC (Remote Differential Compression)**
  - Replikuje pouze změněnou část souboru, ne celý soubor.
  - Dramaticky snižuje provoz přes WAN.
- **Conflict resolution**
  - „poslední zápis vyhrává" (last writer wins).
  - Prohraný soubor jde do složky `ConflictAndDeleted`.
- **Staging folder**
- Dočasná oblast, kam se soubory před replikací komprimují.

### 8.2.2 Replikační topologie

- **Hub and Spoke** — centrální server replikuje na pobočkové (nejčastější).
- **Full Mesh** — každý server replikuje s každým (pro malý počet členů).
- **Custom** — vlastní topologie dle potřeb.

---

# 9. File Server Resource Manager (FSRM)

> [!success]
> **FSRM** — role/feature pro správu a kontrolu dat uložených na file serveru. Umožňuje nastavit kvóty, screening souborů, klasifikaci a reporty.

- **Příklady:**
  - Admin chce vědět, kdo zabírá místo.
  - Zakázat ukládání .mp3 na firemní server.
  - Dostat report o využití disku.
- GUI: **File Server Resource Manager** (`fsrm.msc`).

## 9.1 Kvóty (Quotas)

> [!success]
> **Kvóta** — limit na objem dat v dané složce (nebo svazku).

- **Dva typy:**
  - **Hard quota** — striktní limit; po dosažení nelze zapisovat další data. Server vrátí chybu „disk full".
  - **Soft quota** — upozornění (e-mail, log, příkaz); zápis se neblokuje. Slouží pro monitorování.

## 9.2 File Screening

> [!success]
> **File Screen** — pravidlo, které blokuje nebo monitoruje ukládání určitých typů souborů.

- **File Groups** — sady přípon souborů (např. „Audio and Video Files" = .mp3, .avi, .mkv, …).

#### Typy

- **Active screening** — zablokuje uložení souboru odpovídajícího skupině (uživatel dostane chybu).
- **Passive screening** — pouze generuje upozornění/log, nezabrání uložení.

---

# 10. Volume Shadow Copy Service (VSS)

> [!success]
> **VSS** — služba Windows, která vytváří konzistentní snapshoty svazku v daném okamžiku.

> [!info]
> „_Uživatel omylem smazal soubor nebo ho přepsal_ — místo obnovy ze zálohy klikne pravým tlačítkem → Předchozí verze → vybere verzi z dopoledne. Hotovo za 10 sekund."

## 10.1 Jak to funguje

- **Snapshot** — zachycení stavu svazku v daném čase.
  - Nejedná se o plnou kopii — VSS používá **copy-on-write** (před přepsáním bloku se starý blok zkopíruje).
- **VSS Writer** — komponenta aplikace (SQL Server, Exchange, AD DS…), která zajistí konzistentní stav dat před vytvořením snapshotu.
- **VSS Requester** — nástroj, který požaduje vytvoření snapshotu.
- **VSS Provider** — implementace snapshotů.

## 10.2 Omezení

> [!danger]
> **Není záloha!** Shadow copies jsou na stejném (nebo lokálním) storage — při selhání disku jsou ztraceny.

---

# 11. Data Deduplication

> [!success]
> **Data Deduplication** — technologie, která identifikuje duplicitní datové bloky na svazku a nahradí je ukazateli na jednu sdílenou kopii.

> [!info]
> „100 uživatelů má ve svých složkách stejný instalační balíček — deduplikace ho uloží jednou a ušetří 99× místo."

## 11.1 Usage Types (profily)

| Typ | Popis | Typická úspora |
| --- | --- | --- |
| **General purpose file server** | Sdílení, home directories, Folder Redirection | 50–70 % |
| **VDI server** | VHD/VHDX soubory pro VDI | 80–95 % |
| **Backup** | Zálohovací cíle (např. DPM, VEEAM) | 50–80 % |

## 11.2 Omezení

- **Systémový svazek nelze deduplikovat.**
- Svazky menší než 2 GB se nedoporučují.
- Na ReFS je deduplikace podporována od **Server 2019**.
- V Server Standard edici je deduplikace omezena na svazky do **64 TB** (Datacenter bez omezení — od Server 2016).

---

## 12. iSCSI Target Server

> [!success]
> **iSCSI Target Server** — role Windows Serveru, která poskytuje blokové úložiště přes síť.

## 12.1 Klíčové pojmy

- **Target** — logický cílový bod na serveru (nabízí jeden nebo více LUNů).
- **LUN (Logical Unit Number)** — virtuální disk (VHDX soubor na serveru).
- **Initiator** — klient, který se připojuje k targetu (Windows má vestavěný iSCSI Initiator — `iscsicpl.exe`).
- **IQN (iSCSI Qualified Name)** — unikátní identifikátor targetu/initiatoru (např. `iqn.2024-01.local.firma:storage`).

## 12.2 Typické použití

- Sdílené úložiště pro **Failover Clustering** (Hyper-V, SQL Server).
- Levnější alternativa k HW SAN pro menší prostředí.

---

# 13. Storage Spaces

> [!success]
> Virtualizace úložiště ve Windows — sdružení fyzických disků do **Storage Pool**, ze kterého se vytváří **Virtual Disks** s odolností (mirror, parity, simple).

- „Softwarový RAID zabudovaný ve Windows — vezmete různé disky a uděláte z nich jeden pool."
- **Typy odolnosti:**
  - **Simple** — bez redundance (striping). Pouze výkon.
  - **Mirror** — zrcadlení dat (2-way nebo 3-way mirror). Obdoba RAID 1/10.
  - **Parity** — paritní ochrana (obdoba RAID 5/6). Pomalejší zápisy.

---

# 14. Storage Replica

> [!success]
> **Storage Replica** — technologie pro blokovou replikaci svazků mezi servery nebo clustery.

## 14.1 Režimy

- **Synchronní replikace** — zápis se potvrdí, až je replikován na obou stranách. Nulová ztráta dat (RPO = 0), ale vyžaduje nízkou latenci (< 5 ms).
- **Asynchronní replikace** — zápis se potvrdí ihned, replikace probíhá na pozadí. Vhodné pro větší vzdálenosti, riziko ztráty dat při výpadku.