# 1. Uživatelé v Linuxu

- Linux je **víceuživatelský operační systém**, což znamená, že na jednom systému může současně pracovat více uživatelů.

> [!success]
> Každý uživatel je jednoznačně identifikován:
>
> - **Uživatelským jménem** **(username)**
> - **UID (User ID)** (Běžní uživatelé mají UID od 1000 výše)
> - **Primární skupinou (GID)**
> - Domovským adresářem
> - Přihlašovacím shellem

```
Username: franta
UID: 1000
GID: 1000
Home: /home/franta
Shell: /bin/bash
```

> [!info]
> Systémoví uživatelé (daemony, služby) mají zpravidla _UID v rozsahu 1–999_.

## 1.1 Root

> [!success]
> Speciálním uživatelem je **root**, který představuje administrátora systému.

- UID = **0**
- Má neomezená oprávnění
- Může číst, zapisovat a měnit všechny soubory
- Může vytvářet a mazat uživatele
- Může měnit systémovou konfiguraci

> [!danger]
> _Z bezpečnostních důvodů_ se **běžná práce neprovádí přímo pod účtem root**. Pokud je potřeba vykonat _administrátorskou operaci, používá se příkaz_ `sudo` který umožní běžnému _uživateli dočasně získat oprávnění root_ — **pokud je k tomu oprávněn** → je ve skupině `sudoers`(soubor `/etc/sudoers`).

## 1.2 Klíčové soubory správy uživatelů

| Soubor | Obsah |
| --- | --- |
| `/etc/passwd` | Základní informace o uživatelích (login, UID, GID, domovský adresář, shell) |
| `/etc/shadow` | Hash hesla a politiky hesel (expirace, minimální stáří…) |
| `/etc/group` | Definice skupin a jejich členů |
| `/etc/skel` | Šablona domovského adresáře — soubory se zkopírují novému uživateli |

## 1.3 Správa uživatelů

| Příkaz | Co dělá | Příklad |
| --- | --- | --- |
| `useradd` | **Vytvoří** nového uživatele (**low-level**) | `useradd -m -s /bin/bash -G sudo franta` |
| `adduser` | **Interaktivní** nadstavba nad `useradd` | `adduser franta` |
| `usermod` | **Modifikuje** existujícího uživatele | `usermod -aG docker franta` |
| `userdel` | **Smaže** uživatele | `userdel -r franta` (s `-r` smaže i domovský adresář) |
| `passwd` | **Nastaví/změní heslo** | `passwd franta` |
| `chage` | _Spravuje politiky expirace hesla_ | `chage -l franta` (zobrazí), `chage -M 90 franta` (max 90 dní) |
| `id` | **Zobrazí** _UID, GID a skupiny uživatele_ | `id franta` |
| `su` | **Přepnutí** _uživatele_ | `su - pepa` |

**Důležité přepínače** `useradd`**:**

- `-m` — vytvoří domovský adresář (zkopíruje `/etc/skel`)
- `-s /bin/bash` — nastaví shell
- `-G skupina1,skupina2` — přidá do doplňkových skupin
- `-g skupina` — nastaví primární skupinu
- `-d /cesta` — vlastní cesta domovského adresáře
- `-e YYYY-MM-DD` — datum expirace účtu

**Důležitá vlastnost** `usermod`**:**

- `usermod -G docker franta` (bez `-a`) — **nahradí všechny** _doplňkové skupiny_ **jedinou** skupinou `docker`

> [!info]
> **Zamčení vs. nologin vs. expirace** (tři různé mechanismy, lze je kombinovat)
>
> - Zamčení **blokuje** jen _autentizaci heslem._ (SSH klíč stále funguje!)
>   - `sudo usermod -L franta`
> - `nologin` _zabrání_ **interaktivnímu** _shell_. (Stále přístup např. k SFTP)
>   - `sudo usermod -s /usr/sbin/nologin franta`
> - Expirace **zablokuje** _účet kompletně_.
>   - `sudo usermod -e 2026-08-01 franta`

---

# 2. Skupiny

> [!success]
> Skupina umožňuje _sdílet oprávnění mezi více uživateli_.

- Každý uživatel má jednu **primární skupinu**
  - = **GID** v `/etc/passwd`
  - Používá se jako _výchozí skupina pro nově vytvořené soubory_.
- Uživatel může být členem libovolného počtu **doplňkových (supplementary) skupin**
  - Ty se vypisují v `/etc/group` ve formátu:

```text
developers:x:1002:franta,pkral
```

## 2.2 Správa skupin

| Příkaz | Co dělá | Příklad |
| --- | --- | --- |
| `groupadd` | **Vytvoří** skupinu | `groupadd developers` |
| `groupmod` | **Modifikuje** skupinu | `groupmod -n devs developers` (přejmenuje) |
| `groupdel` | **Smaže** skupinu | `groupdel developers` |
| `groups` | **Zobrazí** _skupiny uživatele_ | `groups franta` |

### 2.2.1 Mechanismus UPG (User Private Group)

- _Většina moderních distribucí_ používá schéma **UPG** = Při vytvoření uživatele se **automaticky vytvoří stejnojmenná skupina**
  - Např. uživatel `franta` → skupina `franta`
- **Primární skupina** uživatele je tato _soukromá skupina_
  - Výchozí umask `0022` nebo `0002` zajistí, že _soubory nejsou přístupné jiným uživatelům_.

---

# 3. Sudo

> [!success]
> `sudo`**(Substitute User DO)** = mechanismus _delegované eskalace oprávnění_

- Umožňuje běžnému uživateli spouštět příkazy s právy root, aniž by znal jeho heslo.

1. `sudo` ověří identitu volajícího uživatele (jeho vlastním heslem)
2. Zkontroluje politiku v konfiguračním souboru `/etc/sudoers`
3. Pokud je povoleno, spustí příkaz s požadovanými oprávněními
4. Veškeré použití se **loguje** (typicky do `/var/log/auth.log` nebo journal).

---

# 4. POSIX přístupová práva

> [!success]
> _Každý soubor a adresář_ má **tři sady oprávnění** pro **tři kategorie**:
>
> - **u** (user/owner) — vlastník souboru
> - **g** (group) — skupina souboru
> - **o** (others) — všichni ostatní
>
> Tři typy oprávnění:
>
> - **r** (read, 4) — čtení obsahu souboru / výpis adresáře
> - **w** (write, 2) — zápis do souboru / vytváření a mazání v adresáři
> - **x** (execute, 1) — spuštění souboru / vstup do adresáře (`cd`)

> [!danger]
> **Důležité:** K smazání souboru potřebujete `w` a `x` na **adresáři**, ne na samotném souboru! Práva na souboru určují, zda můžete číst/měnit obsah, ale mazání řídí adresář.

## 4.1 Příkazy `chmod`, `chown`, `chgrp`

```bash
# Symbolický zápis
chmod u+x skript.sh             # přidá spuštění pro vlastníka
chmod g-w soubor.txt            # odebere zápis pro skupinu
chmod o=r soubor.txt            # nastaví ostatním jen čtení
chmod a+r soubor.txt            # přidá čtení pro všechny (a = all)
chmod u=rwx,g=rx,o= soubor.txt  # vlastník vše, skupina čtení+spuštění, ostatní nic

# Oktálový (číselný) zápis
chmod 755 skript.sh         # rwxr-xr-x
chmod 644 soubor.txt        # rw-r--r--
chmod 700 tajne/            # rwx------
chmod 660 sdileny.txt       # rw-rw----

# Rekurzivně
chmod -R 750 /srv/web/

# Změna vlastníka a skupiny
chown franta soubor.txt              # vlastník
chown franta:developers soubor.txt   # vlastník a skupina
chown :developers soubor.txt         # jen skupina (alternativa k chgrp)
chgrp developers soubor.txt          # jen skupina

# Rekurzivně
chown -R franta:developers /srv/web/
```

## 4.2 Výchozí oprávnění — umask

> [!success]
> Při vytváření nových souborů a složek se práva získávají podle masky
>
> **umask** = maska, která se **odečítá** od _výchozích oprávnění_ při vytváření souborů a adresářů
>
> **Výchozí oprávnění** = soubory `666`, adresáře `777`.

```bash
# Zobrazit aktuální umask
umask          # např. 0022

# Nastavit přísnější umask
umask 0077     # soubory 600, adresáře 700
```

---

# 5. Speciální příznaky oprávnění

## 5.1 SUID (Set User ID) — `4xxx`

> [!success]
> Když se spustí soubor s nastaveným SUID bitem, proces běží s UID **vlastníka souboru** (ne volajícího uživatele).

- **Zobrazuje** se jako `s` místo `x` _na pozici vlastníka_: `-rwsr-xr-x`.

> [!info]
> Vezměme si **příkaz** `passwd`. _Změna vlastního hesla_ znamená zápis do `/etc/shadow`, který je _zapisovatelný pouze root_. Běžným uživatelům ale samozřejmě musíte umožnit změnu vlastního hesla. Bez SUID byste potřebovali nějaký jiný mechanismus pro eskalaci oprávnění jen pro tuhle jednu operaci.

> [!info]
> **SUID na skriptech nefunguje** — Linux z bezpečnostních důvodů ignoruje SUID bit na shellových skriptech (interpretovaných souborech). SUID funguje jen na zkompilovaných binárkách.

## 5.2 SGID (Set Group ID) — `2xxx`

> [!success]
> **Na souboru:** Proces běží _s GID skupiny souboru_ (analogicky k SUID).
>
> **Na adresáři:** Nově vytvořené soubory a podadresáře uvnitř **dědí skupinu adresáře** (ne primární skupinu uživatele). Toto je klíčové pro sdílené adresáře.

- **Zobrazuje** se jako `s` _na pozici skupiny_: `drwxrwsr-x`.

```bash
# Sdílený adresář pro tým — SGID zajistí dědění skupiny
mkdir /srv/projekt
chown root:developers /srv/projekt
chmod 2775 /srv/projekt
```

## 5.3 Sticky bit — `1x xx`

> [!success]
> **Na souboru:** Tento soubor se nebude swapovat, bude celý v paměti (historicky, už neplatí)
>
> **Na adresáři:** Soubory v něm může smazat/přejmenovat **pouze jejich vlastník** (nebo root), i když ostatní mají na adresář právo `w`.

- **Zobrazuje** se jako `t` _na pozici ostatní_: `drwxrwxr-t`.
- Typický příklad: `/tmp`

---

# 6. ACL (Access Control Lists)

- POSIX oprávnění umožňují nastavit práva jen pro **jednoho** vlastníka, **jednu** skupinu a ostatní. Co když potřebujete dát přístup dvěma různým skupinám s různými právy?

> [!success]
> **ACL** rozšiřují tradiční model o libovolný počet pravidel pro konkrétní uživatele a skupiny.

- Pokud má soubor nastavené ACL, **zobrazí** se `+` _za oprávněními_: `-rw-r--r--+`.

> [!info]
> ACL se využívají zejména na _souborových serverech_ nebo ve _sdílených adresářích_.

## 6.1 Základní příkazy

`getfacl` **= Zobrazí všechna ACL oprávnění souboru nebo adresáře**

- `getfacl projekt.docx`
- Výstup může vypadat takto:

```bash
# file: projekt.docx
# owner: franta
# group: studenti

user::rw-      # oprávnění vlastníka
user:jan:rwx   # uživatel jan má navíc plná práva 
group::r--     # skupina studenti může pouze číst
mask::rwx      # maska = maximální oprávnění
other::---     # ostatní nemají žádný přístup
```

`setfacl -m` **= Modify (upravit nebo přidat pravidlo)**

- `setfacl -m u:jan:rwx soubor.txt`
  - `setfacl -m` — _měníme oprávnění_ (modify)
  - `u` — uživatel (user)
  - `jan` — jméno uživatele (username)
  - `rwx` — oprávnění

`setfacl -x` **= Remove (odebrat pravidlo)**

- `setfacl -x u:jan soubor.txt`

`setfacl -b` **= Remove all (zruší všechna rozšířená oprávnění)**

`setfacl -d` = **Default ACL (automaticky se dědí)**