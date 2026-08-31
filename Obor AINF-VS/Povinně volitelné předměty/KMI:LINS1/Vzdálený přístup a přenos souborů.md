# 1. Vzdálený přístup

> [!note]
> **Vzdálený přístup** umožňuje ovládat jiný počítač přes síť, jako bychom seděli přímo u něj.

- Nejpoužívanější protokoly jsou:

| Protokol | Účel | Šifrování |
| --- | --- | --- |
| SSH | vzdálený terminál | ✔   |
| SCP | kopírování souborů | ✔   |
| SFTP | přenos souborů | ✔   |
| rsync | synchronizace souborů | ✔ (přes SSH) |
| FTP | přenos souborů | ✖   |
| FTPS | FTP přes TLS | ✔   |
| TFTP | jednoduchý přenos souborů | ✖   |

# 2. SSH

> [!success]
> **SSH (Secure Shell)** je _síťový protokol aplikační vrstvy_ pro **šifrovaný vzdálený přístup k příkazové řádce**, přenos souborů a tunelování síťového provozu. Pracuje nad **TCP**, _výchozí port_ **22**.

- SSH nahrazuje _starší nešifrované protokoly_ (telnet, rsh, rlogin).
- **Verze protokolu:** SSH-1 (zastaralý, zranitelný), **SSH-2** (aktuální standard, nyní pouze ten)
- **Implementace:** Nejrozšířenější je **OpenSSH** (balíky `openssh-server`, `openssh-client`). _Alternativy_ jsou Dropbear (embedded zařízení), libssh.

## 2.1 Princip fungování

1. **Připojení** `ssh uzivatel@server`
2. **TCP handshake**
3. **Výměna verzí protokolu**. Obě strany si oznámí verzi SSH.
4. **Vyjednání algoritmů**. Dohodne se šifra (AES-256-GCM, ChaCha20-Poly1305…), MAC, komprese a algoritmus výměny klíčů (Diffie-Hellman, ECDH).
5. **Výměna klíčů (key exchange)**.
6. **Ověření serveru**. Klient ověří hostitelský klíč serveru (host key) proti svému souboru `~/.ssh/known_hosts`. Při prvním připojení je třeba otisk potvrdit (TOFU — Trust On First Use).
  - **Při změně klíče serveru** (reinstalace serveru, MITM útok) SSH odmítne připojení s varováním `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`.
7. **Autentizace uživatele**
8. **Šifrovaná relace**

## 2.2 Metody autentizace

| Metoda | Jak funguje | Kdy použít |
| --- | --- | --- |
| **Heslo** | Klient pošle heslo šifrovaným kanálem, server ověří (např. přes `/etc/shadow`) | Jednoduché nastavení, ale slabší zabezpečení (brute-force). |
| **Veřejný klíč** | Klient drží **privátní klíč**, na serveru je odpovídající **veřejný klíč** v `~/.ssh/authorized_keys`. Server _pošle výzvu_, klient _ji podepíše_. | **Doporučená metoda**. Bezpečnější, umožňuje bezheslový přístup. |

### 2.2.1 Správa klíčů

#### Generování klíčového páru

```bash
# Doporučený algoritmus Ed25519 (kratší klíč, rychlejší, bezpečný)
ssh-keygen -t ed25519 -C "admin@server01"

# Starší RSA — minimálně 4096 bitů
ssh-keygen -t rsa -b 4096 -C "admin@server01"
```

- Výchozí umístění: `~/.ssh/id_ed25519` (privátní) a `~/.ssh/id_ed25519.pub` (veřejný).

> [!warning]
> **Passphrase:** _Heslo chránící privátní klíč na disku._ Doporučeno nastavit. Pokud někdo ukradne soubor s klíčem, bez passphrase ho nemůže použít.

#### Distribuce veřejného klíče na server

```bash
# Automatický způsob — zkopíruje veřejný klíč do ~/.ssh/authorized_keys na serveru
ssh-copy-id uzivatel@server
ssh-copy-id -i ~/.ssh/id_ed25519.pub uzivatel@server
```

## 2.3 Konfigurace SSH serveru

- `/etc/ssh/sshd_config`je hlavní konfigurační soubor démona `sshd`.

```bash
# Výchozí port 
Port 22

# Povolit pouze SSH-2
Protocol 2

# Zakázat přihlášení roota heslem (doporučeno)
PermitRootLogin prohibit-password
# Varianty: yes | no | prohibit-password | forced-commands-only

# Zakázat přihlášení heslem úplně (vynutit klíče)
PasswordAuthentication no

# Povolit autentizaci veřejným klíčem
PubkeyAuthentication yes

# Cesta k authorized_keys
AuthorizedKeysFile .ssh/authorized_keys

# Omezit přístup na konkrétní uživatele nebo skupiny
AllowUsers admin deployer
AllowGroups ssh-users

# Časový limit na přihlášení (sekundy)
LoginGraceTime 30

# Maximální počet pokusů o autentizaci v jednom spojení, lepší je fail2ban
MaxAuthTries 3

# Zakázat prázdná hesla
PermitEmptyPasswords no

# Banner zobrazený před přihlášením
Banner /etc/ssh/banner.txt
```

> [!warning]
> **Důležité:** Po úpravě souboru vždy otestujte syntaxi před restartem.
>
> `sudo sshd -t`

## 2.4 Konfigurace SSH klienta

- `~/.ssh/config`. Umožňuje definovat zkratky a výchozí parametry pro jednotlivé servery

```bash
Host webserver
    HostName 192.168.1.50
    User admin
    Port 2222
    IdentityFile ~/.ssh/id_ed25519_web # Můžeme např použít jiný klíč

Host db
    HostName db.example.com
    User dbadmin
    IdentityFile ~/.ssh/id_ed25519_db
    LocalForward 5432 localhost:5432

Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    AddKeysToAgent yes
```

- Pro přihlášení pak stačí:

```bash
ssh webserver          # Místo: ssh -p 2222 admin@192.168.1.50
```

## 2.5 SSH tunelování (port forwarding)

- SSH umožňuje **šifrovaně tunelovat jiné protokoly**. Existují tři typy:

### 2.5.1 Lokální tunelování (`-L`)

- **Co dělá:** Provoz z _lokálního portu_ se pošle _přes SSH_ server na cílový stroj.
- **Použití:** Přístup ke službě, která je dostupná jen ze serveru (např. databáze na interní síti).

```bash
ssh -L 3307:db.internal.local:3306 uzivatel@gateway.example.com
```

- `3307` — lokální port na počítači
- `db.internal.local:3306` — cílová databáze
- Po navázání spojení se mohu dostat na databází přes `127.0.0.1:3307`.

### 2.5.2 Vzdálené tunelování (`-R`)

- **Opačný směr:** Zpřístupní _lokální službu_ na vzdáleném serveru.
- **Použití:** Zpřístupnění lokálně běžící služby ven, i když je za NATem.

```bash
# Port 8080 na serveru → přes ssh zpět → localhost:80 na lokálním stroji
ssh -R 8080:localhost:80 admin@server
```

### 2.5.3 Dynamické tunelování (`-D`) — SOCKS proxy

- **Co dělá:** Vytvoří SOCKS proxy na lokálním portu. Aplikace, které proxy podporují, mohou směrovat veškerý provoz přes SSH tunel.
- **Použití:** Obcházení firewallu/geoblokace, prohlížení "jako by" ses připojoval ze serveru.

```bash
ssh -D 1080 admin@server
# Pak nastavte prohlížeč na SOCKS5 proxy localhost:1080
```

### 2.6 Připojení vzdáleného adresáře

- Pomocí SSH lze vzdálený adresář připojit jako lokální.

```bash
sshfs uzivatel@server:/home/data ~/server
fusermount -u ~/server # odpojení
```

---

# 3. Přenos souborů

## 3.1 SCP

> [!success]
> **SCP (Secure Copy)** je nástroj pro kopírování souborů přes SSH. Používá SSH protokol pro autentizaci i šifrování přenosu.

```bash
# Kopírování souboru na server
scp soubor.txt admin@server:/home/admin/

# Kopírování ze serveru na lokální stroj
scp admin@server:/var/log/syslog ./syslog-backup.log

# Rekurzivní kopírování adresáře
scp -r /local/adresar admin@server:/cesta/

# Specifikace portu
scp -P 2222 soubor.txt admin@server:/cesta/
```

## 3.2 SFTP

> [!success]
> **SFTP (SSH File Transport Protocol)** je subsystém SSH protokolu poskytující interaktivní rozhraní pro práci se soubory na vzdáleném serveru (výpis adresáře, nahrávání, stahování, mazání, přejmenování…).

> [!warning]
> **SFTP ≠ FTPS**. SFTP je subsystém SSH. FTPS je FTP zabezpečené TLS (port 990 nebo 21+STARTTLS). Na _Linuxových serverech se upřednostňuje SFTP_.

```bash
# Interaktivní relace
sftp admin@server

# Uvnitř SFTP:
sftp> ls                      # Výpis vzdáleného adresáře
sftp> cd /var/www             # Změna vzdáleného adresáře
sftp> lcd /tmp                # Změna lokálního adresáře
sftp> get soubor.txt          # Stáhnout soubor
sftp> put nahraj.tar.gz       # Nahrát soubor
sftp> mkdir novy_adresar      # Vytvořit adresář
sftp> rm stary_soubor.txt     # Smazat soubor
sftp> bye                     # Ukončit

# Jednorázové stažení bez interaktivní relace
sftp admin@server:/cesta/soubor.txt ./lokalni_kopie.txt
```

## 3.3 rsync

> [!success]
> Nástroj pro efektivní synchronizaci souborů a adresářů, lokálně i vzdáleně. Přenáší pouze rozdíly (delta transfer) pomocí algoritmu rolling checksum.

- Ideální pro _zálohování, zrcadlení a nasazování._
- Standardně přes SSH (`-e ssh`), lze i přes vlastní rsync démon (port 873).

```bash
# Základní synchronizace lokální → server
rsync -avz /local/adresar/ admin@server:/remote/adresar/

# Server → lokální
rsync -avz admin@server:/remote/adresar/ /local/adresar/

# Smazat na cíli soubory, které neexistují ve zdroji (zrcadlo)
rsync -avz --delete /zdroj/ admin@server:/cil/

# Suchý běh — ukáže, co by se změnilo, ale nic neprovede
rsync -avzn /zdroj/ admin@server:/cil/

# Vyloučení souborů
rsync -avz --exclude='*.log' --exclude='.git' /zdroj/ /cil/
```

**Klíčové přepínače:**

| Přepínač | Význam |
| --- | --- |
| `-a` | Archivní režim: zachová oprávnění, vlastníka, časy, symlinky, rekurzivně. |
| `-v` | Verbose |
| `-z` | Komprese dat během přenosu. |
| `-n` | Dry run. |
| `--delete` | Smaže na cíli soubory, které ve zdroji neexistují. |
| `--exclude` | Vyloučí soubory odpovídající vzoru. |
| `-e ssh` | Použije SSH jako transportní vrstvu (výchozí chování). |
| `--progress` | Zobrazí průběh přenosu. |

> [!warning]
> **Pozor na trailing slash:**
>
> - `rsync /zdroj /cil/` — zkopíruje adresář `zdroj` dovnitř `/cil/`
> - `rsync /zdroj/ /cil/` — zkopíruje **obsah** adresáře `zdroj` do `/cil/`

---

# 4. VNC a RDP

> [!success]
> **VNC (Virtual Network Computing):** Protokol pro vzdálenou grafickou plochu. **Samo o sobě nešifrované!** Port 5900 (změna když je více obrazovek)
>
> **RDP (Remote Desktop Protocol):** Protokol Microsoftu. Na Linuxu `xrdp`. Port 3389.