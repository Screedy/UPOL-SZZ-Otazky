# 1. Organizace dat v Linuxu

## 1.1 Hierarchie souborového systému v Linuxu (FHS)

- _Linux organizuje data_ pomocí jednotné adresářové struktury definované standardem **Filesystem Hierarchy Standard (FHS)**.

> [!success]
> **FHS (Filesystem Hierarchy Standard)** je konvence, která definuje strukturu adresářového stromu v unixových systémech.
>
> - Celý systém tvoří **jediný strom** _začínající kořenovým adresářem_ `/`
>   - Na rozdíl od Windows zde _neexistují písmena disků_ (`C:, D:`).

### 1.1.1 Klíčové adresáře

- `/` — Je kořen celého stromu
- `/boot` — Obsahuje jádro systému, zavaděč
- `/etc` — Obsahuje konfigurační soubory systému a služeb
- `/home` — Obsahuje domovské adresáře uživatelů
- `/root` — Je domovský adresář root
- `/var` — Obsahuje proměnná data (logy, databáze)
- `/tmp` — Obsahuje dočasné soubory (mazány při restartu)
- `/usr` — Obsahuje uživatelské programy, knihovny, dokumentace
- `/bin` — Obsahuje základní uživatelské příkazy potřebné pro běžnou práci se systémem.
- `/sbin` — Obsahuje systémové příkazy určené především pro správu systému.
- `/dev` — Obsahuje soubory představující zařízení (bloková: disky; znaková: terminály)
- `/proc` — Obsahuje informace o procesech a jádře
- `/sys` — Obsahuje informace o hardwaru a ovladačích
- `/mnt`, `/media` — Obsahuje dočasné připojení disků a médií

---

# 2. Bloková zařízení a pojmenování disků

> [!success]
> **Blokové zařízení** je zařízení, ke kterému se _přistupuje po blocích_ (typicky 512 B nebo 4 KiB [kibi bajt]).
>
> V Linuxu jsou disky (a jejich oddíly) reprezentovány jako soubory v adresáři `/dev`.

- _Příklady pojmenování_:

```
# Disky
/dev/sda
/dev/sdb
/dev/nvme0n1          
/dev/mmcblk0            

# Oddíly
/dev/sda1
/dev/sda2
/dev/nvme0n1p1
/dev/mmcblk0p1
```

> [!info]
> Pojmenování `sda`, `sdb` se **může** mezi restarty **měnit** (závisí na pořadí detekce).
>
> Pro trvalou identifikaci se používají **UUID** — viz sekce 4.4.2 `fstab`.

## 2.1 Zobrazení disků a oddílů

```bash
lsblk # Přehled blokových zařízení (stromový výpis)

lsblk -f # Podrobnější výpis s filesystémy a UUID

fdisk -l # Detailní info o oddílech

blkid # UUID a typy souborových systémů
```

- _Příklad výstupu_ `lsblk`:

```bash
root@DietPi:~# lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
mmcblk0     179:0    0 29.8G  0 disk 
├─mmcblk0p1 179:1    0  128M  0 part /boot/firmware
└─mmcblk0p2 179:2    0 29.7G  0 part /
```

---

# 3. Diskové oddíly

- Jeden _fyzický disk_ lze **rozdělit na několik oddílů**.
- Každý oddíl může _obsahovat vlastní souborový systém_ nebo být _použit jako LVM Physical Volume._

## 3.1 Typy tabulek oddílů

- Je na začátku disku, pro celý disk.

| Vlastnost | MBR (Master Boot Record) | GPT (GUID Partition Table) |
| --- | --- | --- |
| Maximální velikost disku | 2 TiB | 9,4 ZiB |
| Maximální počet primárních oddílů | 4   | 128 |
| Redundance tabulky | žádná | záložní kopie na konci disku |
| Bootování | BIOS / Legacy | UEFI (“novější BIOS”) |

> [!info]
> MBR je **starší formát** s _omezeními_. Na moderních systémech se téměř **vždy používá GPT.**

## 3.2 Nástroje pro správu oddílů

> [!info]
> Tabulka oddílů je **jen datová struktura** na začátku disku. Aby ji šlo vytvořit, číst a upravovat, existují **specializované nástroje**.

### 3.2.1 Nástroj `fdisk`

- Interaktivní nástroj pro **správu tabulky oddílů** na disku.
- Podporuje _MBR_ i _GPT_.
- Změny zapisuje až po potvrzení příkazem `w` (uložit)

```bash
# Interaktivní režim — správa oddílů na disku /dev/sdb
sudo fdisk /dev/sdb
```

### 3.2.2 Nástroj `parted`

- Modernější nástroj
- Použitelný **interaktivně** i **skriptovatelně** z příkazové řádky.
- Změny se provádí **okamžitě**.

```bash
# Vytvořit GPT tabulku
sudo parted /dev/sdb mklabel gpt

# Vytvořit oddíl zabírající celý disk
sudo parted /dev/sdb mkpart primary ext4 0% 100%

# Zobrazit oddíly
sudo parted /dev/sdb print
```

### 3.2.3 Nástroj `gdisk`

- Obdoba `fdisk` _specializovaná na GPT tabulky_ se stejným interaktivním ovládáním.
- Podporuje **pouze GPT**.

## 3.3 Informování jádra o změnách

- Při úpravě oddílů se _zapíší změny pouze na disk_. **Jádro** stále **vidí původní rozložení**.

```bash
# Znovunačtení tabulky oddílů
sudo partprobe /dev/sdb
```

---

# 4. Souborový systém

> [!success]
> **Souborový systém (filesystem, FS)** je způsob _organizace dat na blokovém zařízení_. Definuje, jak se _ukládají soubory, adresáře, metadata_ (oprávnění, časy) a jak _je spravováno volné místo_.

- Disk sám o sobě je jen _dlouhá řada bloků s bajty_ (posloupnost sektorů), se kterými _operační systém neumí pracovat_.

## 4.1 Hlavní souborové systémy v Linuxu

### 4.1.1 ext4 (Fourth Extended Filesystem)

- **Nejrozšířenější** výchozí FS na většině distribucí
- **Žurnálovací (journal)** — _Chrání konzistenci dat při výpadku_
- **Max. velikost souboru**: 16 TiB
- **Max. velikost FS**: 1 EiB
- _Zpětně kompatibilní_ s ext2/ext3

### 4.1.2 XFS

- **Výchozí na RHEL/CentOS 7+**
- Optimalizovaný pro _velké soubory_ a _paralelní I/O_
- **Žurnálovací**
- Lze _pouze zvětšovat oddíly_, **nelze zmenšit!** (důležitý rozdíl proti ext4)

### 4.1.3 Btrfs (B-tree Filesystem)

- **Výchozí na openSUSE, Fedora**
- Vestavěná _podpora pro RAID, komprese, deduplikaci_
- **Stále ve vývoji** — některé funkce (RAID5/6) nejsou plně stabilní

## 4.3 Vytvoření souborového systému

- Po vytvoření oddílu je potřeba vytvořit filesystem.

```bash
sudo mkfs.ext4 /dev/sdb1 # Vytvoření ext4
sudo mkfs.btrfs /dev/sdb1 # Vytvoření Btrfs

sudo mkswap /dev/sdb2 # Vytvoření swap prostoru
```

> [!danger]
> `mkfs`**formátuje oddíl** = smaže veškerá existující data.

## 4.4 Připojování souborových systémů

> [!success]
> `mount` je operace, kterou se souborový systém na blokovém zařízení **zpřístupní** v _adresářovém stromu_ jako **podadresář** (mount point).

> [!info]
> Disk sám o sobě _není přístupný_ — musíte ho _připojit_ k nějakému adresáři, a pak se obsah disku _zobrazí v tom adresáři_.

### 4.4.1 Dočasné připojení a odpojení

```bash
# Připojit oddíl do adresáře
sudo mount /dev/sdb1 /mnt/data

# Připojit jako read-only
sudo mount -o ro /dev/sdb1 /mnt/data

# Zobrazit všechna aktuální připojení
mount
```

- Před dokončením _zapíše nezapsaná data_ (flush) a uvolní mount point.

```bash
# Odpojit souborový systém
sudo umount /mnt/data
```

> [!info]
> `umount`před dokončením _zapíše nezapsaná data_ (flush) a uvolní mount point.

## 4.4.2 Trvalé připojení

> [!success]
> Soubor `/etc/fstab` obsahuje _záznamy o souborových systémech_, které se mají **připojit automaticky** při startu systému.

```bash
# Oddíl podle UUID (doporučeno — stabilní i při změně pojmenování disků)
UUID=a1b2c3d4-e5f6-7890-abcd-ef1234567890  /home  ext4  defaults  0  2

# Oddíl podle cesty zařízení (méně bezpečné — pořadí se může měnit)
/dev/sdb1  /mnt/data  xfs  defaults,noatime  0  0

# NFS síťový mount
server:/export/data  /mnt/nfs  nfs  defaults,_netdev  0  0
```

**Sloupce:**

1. **Zařízení** — `/dev/sda1`, `UUID=...`, síťová cesta
2. **Mount point** — Kam připojit?
3. **Typ FS** — `ext4`, `btrfs`, `nfs`
4. **Volby**
  - `defaults` = `rw,suid,dev,exec,auto,nouser,async`
  - `noatime` — Nezapisovat čas posledního přístupu (doporučeno na serverech)
  - `ro` / `rw` — Read-only / read-write
  - `noexec` — Zakáže spouštění binárních souborů z tohoto FS (bezpečnost)
  - `nosuid` — Ignoruje SUID/SGID bity
  - `_netdev` — Počkat na síťový stack (pro vzdálený disk)
  - `nofail` — Pokud zařízení neexistuje, boot pokračuje (bez tohoto boot zamrzne!)
  - `nodev` — Ignoruje speciální zařízení
5. **Dump** — Zálohovat pomocí programu `dump`?
  - `0` – **nezálohovat** (dnes téměř vždy používaná hodnota)
  - `1` – zahrnout do zálohování programem `dump`
6. **Pass** — Pořadí kontroly `fsck` při bootu
  - `0` = Souborový systém se při startu nekontroluje.
  - `1` = Kontroluje se jako první. Tuto hodnotu má mít pouze **kořenový souborový systém (**`/`**)**.
  - `2` = Kontroluje se po dokončení kontroly kořenového souborového systému. Používá se pro ostatní lokální souborové systémy.

### 4.4.1 Testování fstab bez restartu

```bash
# Připojit vše z fstab, co ještě není připojeno
sudo mount -a

# Specificky jeden záznam z fstab
sudo mount /mnt/data
```

> [!danger]
> Chyba v `/etc/fstab` může způsobit, že **systém nenastartuje.** Vždy po úpravě zkontrolujte `mount -a` a ověřte, že nehlásí chyby.

## 4.5 Kontrola a oprava FS

```bash
fsck /dev/sda1
```

- Kontroluje:
  - poškození
  - nekonzistence
  - chybějící bloky

## 4.6 Informace o využití místa

```
df -h # Obsazenost disků
du -sh * # Velikost adresářů
```

---

# 5. Odkládací prostor

> [!success]
> **Swap** je _prostor na disku_, který jádro používá jako rozšíření operační paměti. Když RAM nestačí, jádro přesune **méně používané stránky** do swapu (swap-out) a v případě potřeby je _načte zpět_ (swap-in).

## 5.1 Swap oddíl

```bash
sudo mkswap /dev/sdb2 # Vytvoření swap na oddílu
sudo swapon /dev/sdb2 # Aktivace swapu
```

## 5.2 Swap soubor (alternativa k oddílu)

- Jednodušší na vytvoření a zvětšení.

```bash
# Vytvořit swap soubor o velikosti 2 GiB
sudo dd if=/dev/zero of=/swapfile bs=1M count=2048

# Nastavit oprávnění (MUSÍ být 0600!)
sudo chmod 600 /swapfile

# Inicializovat jako swap
sudo mkswap /swapfile

# Aktivovat
sudo swapon /swapfile
```

---

# 6. LVM

> [!success]
> **LVM (Logical Volume Manager)** je _abstrakční vrstva_ mezi _fyzickými diskovými oddíly_ a _souborovými systémy_.
>
> Umožňuje flexibilně vytvářet, měnit velikost a spravovat logické svazky nezávisle na fyzickém rozložení disků.

> [!info]
> Bez LVM je každý oddíl pevně daný — pokud se `/home` zaplní, musíte přerozdělit disk.
>
> S LVM můžete `/home` za běhu zvětšit přidáním dalšího disku nebo přerozdělením volného místa z jiného svazku.

## 6.1 Tři vrstvy LVM

```
  Fyzické disky/oddíly        Vrstva LVM      Souborové systémy
  ┌─────────────┐
  │  /dev/sda2  │──→  PV ─┐
  └─────────────┘         │
                          ├──→  VG (vg0) ──→  LV (lv_root) ──→ ext4 → /
  ┌─────────────┐         │              ──→  LV (lv_home) ──→ ext4 → /home
  │  /dev/sdb1  │──→  PV ─┘              ──→  LV (lv_swap) ──→ swap
  └─────────────┘
```

1. **PV (Physical Volume)** — Fyzický svazek = disk nebo oddíl _inicializovaný pro LVM_
2. **VG (Volume Group)** — Skupina svazků = _pool_ z jednoho nebo více PV
3. **LV (Logical Volume)** — Logický svazek = _„virtuální oddíl"_ vytvořený z VG

## 6.2 Práce s PV (Physical Volumes)

```bash
# Inicializovat oddíl jako PV
sudo pvcreate /dev/sdb1

# Inicializovat celý disk jako PV (bez tabulky oddílů)
sudo pvcreate /dev/sdc

# Odebrat PV (musí být prázdný, tj. nepoužívaný ve VG)
sudo pvremove /dev/sdb1

# Výpis
pvs
pvdisplay
```

## 6.3 Práce s VG (Volume Groups)

```bash
# Vytvořit VG z jednoho nebo více PV
sudo vgcreate vg0 /dev/sdb1 /dev/sdc

# Přidat PV do existující VG (rozšíření!)
sudo vgextend vg0 /dev/sdd1

# Odebrat PV z VG (data se nejprve přesunou)
sudo pvmove /dev/sdb1        # přesunout data na jiné PV ve VG
sudo vgreduce vg0 /dev/sdb1  # odebrat prázdný PV z VG

# Výpis
vgs
```

## 6.4 Práce s LV (Logical Volumes)

```bash
# Vytvořit LV o velikosti 20 GiB
sudo lvcreate -L 20G -n lv_home vg0

# Vytvořit LV zabírající 50 % volného místa
sudo lvcreate -l 50%FREE -n lv_logs vg0

# Zobrazit LV
sudo lvs           # stručný přehled
sudo lvdisplay      # podrobný výpis

# Smazat LV (musí být nejdříve odpojen!)
sudo umount /dev/vg0/lv_home
sudo lvremove /dev/vg0/lv_home
```

### 6.4.1 Změna velikosti LV

```bash
# 1. Zvětšit LV o 10 GiB
sudo lvextend -L +10G /dev/vg0/lv_home

# 2. Zvětšit ext4 FS na celý LV (lze za běhu!)
sudo resize2fs /dev/vg0/lv_home
```

### 6.4.2 Zmenšení LV + souborového systému

```bash
# POUZE pro ext4! XFS nelze zmenšit!

# 1. Odpojit souborový systém
sudo umount /home

# 2. Zkontrolovat FS
sudo fsck.ext4 -f /dev/vg0/lv_home

# 3. Zmenšit FS na 15 GiB
sudo resize2fs /dev/vg0/lv_home 15G

# 4. Zmenšit LV na 15 GiB
sudo lvreduce -L 15G /dev/vg0/lv_home

# 5. Znovu připojit
sudo mount /dev/vg0/lv_home /home
```

> [!danger]
> Při zmenšování se NEJDŘÍVE zmenšuje souborový systém a až potom LV.
>
> Opačné pořadí = ztráta dat!
>
> Vždy **zálohujte** před zmenšováním.

## 6.5 LV snapshot

> [!success]
> **LVM snapshot** je _okamžitá kopie_ logického svazku v určitém časovém bodě.
>
> _Využívá princip Copy-on-Write_ — ukládá se jen to, co se od pořízení snapshotu změnilo.

```bash
# Vytvořit snapshot (10 GiB prostor pro změny)
sudo lvcreate -L 10G -s -n lv_home_snap /dev/vg0/lv_home

# Připojit snapshot (read-only pro zálohu)
sudo mount -o ro /dev/vg0/lv_home_snap /mnt/snapshot

# Obnovit ze snapshotu (vrátit LV do stavu snapshotu)
sudo lvconvert --merge /dev/vg0/lv_home_snap
# (vyžaduje umount nebo reboot)

# Smazat snapshot
sudo lvremove /dev/vg0/lv_home_snap
```

---

## 7. RAID — redundantní pole disků

> [!success]
> **RAID (Redundant Array of Independent Disks)** kombinuje více fyzických disků do jednoho logického celku za účelem zvýšení výkonu, odolnosti proti výpadku, nebo obojího.

## 7.1 Základní úrovně RAID

| Úroveň | Popis | Min. disků | Kapacita | Odolnost |
| --- | --- | --- | --- | --- |
| RAID 0 | Striping — prokládání dat | 2   | N × disk | žádná (1 disk selže = vše ztraceno) |
| RAID 1 | Mirroring — zrcadlení | 2   | 1 × disk | výpadek 1 disku |
| RAID 5 | Striping + distribuovaná parita | 3   | (N-1) × disk | výpadek 1 disku |
| RAID 6 | Striping + dvojitá parita | 4   | (N-2) × disk | výpadek 2 disků |
| RAID 10 | Mirror + Stripe (kombinace 1+0) | 4   | N/2 × disk | výpadek 1 disku na mirror |

## 7.2 Softwarový RAID v Linuxu

```bash
# Vytvořit RAID 1 ze dvou disků
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1

# Zobrazit stav
cat /proc/mdstat
sudo mdadm --detail /dev/md0

# Uložit konfiguraci
sudo mdadm --detail --scan >> /etc/mdadm/mdadm.conf

# Na /dev/md0 se pak vytvoří FS nebo PV pro LVM:
sudo mkfs.ext4 /dev/md0
# nebo
sudo pvcreate /dev/md0
```