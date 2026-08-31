- **Počítačová síť** _umožňuje komunikaci_ mezi zařízeními.
- Aby _zařízení mohlo komunikovat_ **potřebuje**:
  - **IP adresu** a **masku sítě**
  - **Výchozí bránu**
  - **DNS server**
  - (volitelně) _Hostname, doménu, NTP_, …

> [!info]
> ```
> IP:      192.168.1.25
> Maska:   255.255.255.0
> Brána:   192.168.1.1
> DNS:     8.8.8.8
> ```

# 1. Konfigurace připojení k počítačové síti

## 1.1 Nástroj `ip`

> [!success]
> `ip` je _univerzální nástroj_ z balíčku `iproute2` pro **správu síťové konfigurace v Linuxu**.
>
> Umožňuje _konfigurovat jak linkovou vrstvu_, tak _síťovou vrstvu_.
>
> Nahrazuje starší příkazy jako `ifconfig`, `route` nebo `arp`.

- **Linková vrstva (2. vrstva)**
  - práce se síťovými rozhraními
  - změna MAC adresy
  - zapnutí a vypnutí rozhraní
  - nastavení MTU
- **Síťová vrstva (3. vrstva)**
  - přidávání a odebírání IP adres
  - směrovací tabulka
  - pravidla směrování

> [!danger]
> Veškerá nastavení provedená příkazem `ip` platí **jen do restartu**.
>
> Po restartu se _síť načte z konfiguračních souborů_ nebo _ze správce sítě_ (NetworkManager, systemd-networkd apod.)

### 1.1.1 Zobrazení síťových rozhraní

- Každá síťová karta má své rozhraní (interface).

`ip link show` — Zobrazí všechna síťová rozhraní počítače.

```bash
root@DietPi:~# ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 2c:cf:67:00:b8:80 brd ff:ff:ff:ff:ff:ff
```

- U _každého rozhraní uvidíme_:
  - **Název** rozhraní,
  - **MAC adresu**,
  - **Maximální přenosovou jednotku** (MTU),
  - **Stav** rozhraní (`UP`, `DOWN`),
  - **Příznaky** (např. `BROADCAST`, `MULTICAST`).

### 1.1.2 Zobrazení IP adres

`ip addr show`

`ip a` (Zkrácená verze)

```bash
root@DietPi:~# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 2c:cf:67:00:b8:80 brd ff:ff:ff:ff:ff:ff
    inet 10.169.37.22/16 brd 10.169.255.255 scope global dynamic eth0
       valid_lft 81955sec preferred_lft 81955sec
    inet6 fe80::2ecf:67ff:fe00:b880/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
```

- Ukáže:
  - IPv4 adresy,
  - IPv6 adresy (pokud má),
  - Masku sítě,
  - Broadcast adresu,
  - Ke kterému rozhraní IP patří.
- Zajímavé přepínače:
  - `ip -4 addr show` — Zobrazení pouze IPv4 adres
  - `ip --color=always addr show` — Pouze barevně zvýrazní výpis (lépe čte)

### 1.1.3 Změna MAC adresy

- Každá síťová karta má svoji **MAC adresu**.
- Je to fyzická adresa zařízení na linkové vrstvě.

`ip link set eth0 address 00:11:22:33:44:55`

### 1.1.4 Zapnutí a vypnutí rozhraní

`ip link set eth0 down` — Rozhraní přestane komunikovat.

`ip link set eth0 up` — Rozhraní začne znovu komunikovat.

### 1.1.5 Přidání a odebrání adresy

`ip addr add 192.168.1.10/24 dev eth0` — Přidá

`ip addr del 192.168.1.10/24 dev eth0` — Odebere

- **Parametry**:
  - `10.0.2.32` → IP adresa
  - `/24` → maska sítě
  - `dev eth0` → zařízení (device)

### 1.1.6 Směrovací tabulka a výchozí brána

> [!note]
> Každý počítač obsahuje tabulku, podle které **rozhoduje**, _kam se mají jednotlivé pakety poslat_.

`ip route show` — Zobrazí směrovací tabulka

```
root@DietPi:~# ip route show
default via 10.169.0.1 dev eth0 
10.169.0.0/16 dev eth0 proto kernel scope link src 10.169.37.22
```

- _Každá směrovací tabulka_ by měla obsahovat alespoň **výchozí cestu** (_default route_), která určuje, _kam se mají odeslat pakety_, pokud pro jejich cílovou adresu _neexistuje konkrétnější záznam_. Typicky **vede na router** (výchozí bránu) _zajišťující komunikaci s ostatními sítěmi_.

> [!info]
> `10.169.0.0/16 dev eth0 proto kernel scope link src 10.169.37.22`
>
> _Pro všechna zařízení v síti_ `10.169.0.0/16` posílej **pakety přímo přes rozhraní** `eth0`. Toto pravidlo **vytvořilo automaticky jádro Linuxu** na základě nastavené IP adresy a při komunikaci používej jako _zdrojovou adresu_ `10.169.37.22`.

`ip route add default via 192.168.1.1` — Přidání pravidla výchozí cesty

`ip route add 10.0.0.0/8 via 192.168.1.254` — Přidání konkrétnějšího pravidla

## 1.2 Trvalá konfigurace sítě

- V Linuxu existuje několik způsobů, jak síť konfigurovat. Který z nich se použije, _závisí na distribuci a nainstalovaných nástrojích_.

### 1.2.1 `/etc/network/interfaces`

- Jedná se o **tradiční způsob konfigurace sítě**, který byl používán především **ve starších verzích** Debianu a Ubuntu. Konfigurace je uložena v textovém souboru `/etc/network/interfaces`
- V tomto souboru lze nastavit, zda se má _rozhraní aktivovat automaticky při startu systému_ a _jakým způsobem má získat síťovou konfiguraci_.

```bash
auto eth0  # rozhraní se aktivuje při startu systému

iface eth0 inet dhcp # nastavení získáno automaticky pomocí DHCP

iface eth0 inet static # statické nastavení
    address 192.168.1.20
    netmask 255.255.255.0
    gateway 192.168.1.1
```

> [!warning]
> Po změně konfigurace bylo obvykle potřeba restartovat síťovou službu nebo celý počítač.

### 1.2.2 `systemd-networkd`

- `systemd-networkd` je _moderní služba systému_ **systemd**, která zajišťuje _správu síťových rozhraní_.
- Často se používá na serverech nebo v minimalistických distribucích, kde není potřeba grafický správce sítě.
- Konfigurační soubory se ukládají do adresáře `/etc/systemd/network/`

- Příklad nastavení `/etc/systemd/network/20-wired.network`:

```ini
[Match] # sekce určuje, na které síťové rozhraní se konfigurace použije
Name=eth0

[Network] # vlastní síťová konfigurace
Address=192.168.1.10/24
Gateway=192.168.1.1
DNS=8.8.8.8
DNS=8.8.4.4
# nebo třeba DHCP=yes
```

- Správa služby

```bash
sudo systemctl enable systemd-networkd # zapnutí služby
networkctl # zobrazení stavu všech rozhraní
networkctl status enp0s3 # podrobnosti o konkrétním rozhraní
```

### 1.2.3 `netplan`

- **Netplan** je nástroj používaný především v novějších _verzích Ubuntu_.
- Jeho úkolem _není síť přímo spravovat_, ale **převést konfiguraci z YAML souborů na konfiguraci pro** `systemd-networkd` **nebo** `NetworkManager`.
- Konfigurační soubory se nacházejí v adresáři `/etc/netplan/`

- Příklad `/etc/netplan/01-netcfg.yaml`:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      addresses:
        - 192.168.1.10/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
      dhcp4: false
```

```bash
sudo netplan apply # Aplikace konfigurace (ověří a nastaví)
sudo netplan try # Vyzkoušení s automatickým rollbackem po 120 s
```

> [!info]
> `sudo netplan try` je užitečný zejména při vzdálené správě serverů, kdy by chybná konfigurace mohla způsobit ztrátu síťového připojení.

---

# 2. DNS

> [!success]
> **DNS (Domain Name System)** překládá doménová jména (`www.example.com`) na IP adresy (`93.184.216.34`) a naopak.

`/etc/resolv.conf` — soubor, kde jsou uvedeny adresy DNS serverů

```bash
root@DietPi:~# cat /etc/resolv.conf 
nameserver 10.169.188.49
nameserver 10.169.139.122
search example.com # definuje seznam domén, které se připojí za neúplné hostname dotazu
```

> [!danger]
> **Pozor:** Na moderních systémech je `/etc/resolv.conf` často **generován automaticky** (NetworkManager, systemd-resolved, Netplan). Ruční editace se přepíše po restartu.

`/etc/hosts` — soubor, kde jsou lokální statické překlady jmen

- Typické použití: aliasy pro lokální stroje, blokování domén

```bash
root@DietPi:~# cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 DietPi
```

`/etc/nsswitch.conf` — soubor, který určuje pořadí, odkud Linux získává informace.

```bash
root@DietPi:~# cat /etc/nsswitch.conf 
passwd:         files
group:          files
shadow:         files
gshadow:        files

hosts:          files dns # při prekladu se nejdříve prohledá /etc/hosts a potom se kdyžtak použije dns
networks:       files
...
```

---

# 3. DHCP

> [!success]
> **DHCP (Dynamic Host Configuration Protocol)** automaticky přiděluje klientům IP adresu, masku, bránu, DNS servery a další parametry.
>
> Proces probíhá ve 4 krocích: **DISCOVER → OFFER → REQUEST → ACK.**

- Zapůjčená adresa má omezenou platnost — klient ji periodicky obnovuje

---

## 5. Diagnostické síťové nástroje

| Nástroj | Co dělá | Příklad |
| --- | --- | --- |
| `ip addr` / `ip a` | Zobrazí adresy rozhraní | `ip a` |
| `ip route` / `ip r` | Zobrazí směrovací tabulku | `ip r` |
| `ping` | Ověří dosažitelnost hosta | `ping -c 4 8.8.8.8` |
| `traceroute` / `tracepath` | Zobrazí cestu paketu sítí | `traceroute 8.8.8.8` |
| `ss` | Zobrazí otevřené sokety | `ss -tlnp` |
| `dig` / `nslookup` / `host` | DNS dotazy | `dig A example.com` |
| `tcpdump` | Zachytávání paketů | `tcpdump -i ens33 port 80` |
| `nmap` | Skenování portů a služeb | `nmap -sV 192.168.1.1` |
| `netcat` | Vytváří TCP nebo UDP spojení | `netcat phoenix.inf.upol.cz 80` |

Příklad diagnostického workflow:

```bash
ip a # 1. Mám vůbec IP adresu?

ip r # 2. Mám výchozí bránu?

ping -c 2 192.168.1.1 # 3. Dostanu se na bránu?

ping -c 2 8.8.8.8 # 4. Dostanu se na internet?

dig google.com # 5. Funguje DNS?

ss -tlnp | grep :80 # 6. Poslouchá služba na správném portu?
```

---

# 4. Firewall

> [!success]
> **Firewall** je _bezpečnostní mechanismus_, který řídí síťovou komunikaci podle definovaných pravidel.
>
> **Netfilter** je _framework v linuxovém jádře_, který umožňuje filtrování, překlad adres (NAT) a úpravu paketů.

- Samotný netfilter neposkytuje uživatelský nástroj — k jeho ovládání slouží:
  - `iptables` — tradiční nástroj (od ~2001), rozhraní k netfilter přes tabulky a řetězy
  - `nftables` — _modernější náhrada_ (od jádra 3.13), příkaz `nft`
  - `firewalld` — _vysokoúrovňový správce firewallu_ s konceptem zón, interně používá `nftables`

> [!danger]
> Pravidla se vyhodnocují od _prvního k poslednímu_. Při naražení na **match** _vyhodnocování končí_.

## 4.1 `iptables`

- `iptables` je **starší nástroj** pro konfiguraci firewallu v Linuxu. Umožňuje vytvářet pravidla pro filtrování síťového provozu a dlouhou dobu byl standardem ve většině distribucí.

- Pravidla se organizují do **tabulek** (`filter`, `nat`, `mangle`, `raw`)a **řetězců** (_chains_), jako jsou:
  - `INPUT` – příchozí komunikace,
  - `OUTPUT` – odchozí komunikace,
  - `FORWARD` – komunikace procházející přes počítač.

Například povolení příchozího SSH:

```
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

> [!warning]
> V současnosti je `iptables` ve většině distribucí nahrazován nástrojem `nftables`, i když kvůli zpětné kompatibilitě bývá stále dostupný.

## 4.2 `nftables`

- `nftables` je **moderní framework pro správu firewallu**, který nahrazuje `iptables`, `ip6tables`, `arptables` i `ebtables`.
- Je součástí linuxového jádra od verze 3.13 a dnes představuje _doporučený způsob konfigurace firewallu_.
- Jeho výhodou je **jednodušší syntaxe**, **vyšší výkon** a **sjednocení pravidel pro IPv4 i IPv6**.

- `nftables`je postavena hierarchicky:

```
Ruleset
│
├── Table
│     ├── Chain
│     │      ├── Rule
│     │      ├── Rule
│     │      └── Rule
│     └── Chain
│
└── Table
      └── Chain
            └── Rule
```

- **Ruleset –** _celá konfigurace firewallu_.
- **Table –** _logické seskupení pravidel_.
  - Je dána **rodinou** tabulek (např. `ip`, `ip6`, `inet`, `arp`, `bridge` nebo `netdev`) a **názvem** tabulky (vybírá si uživatel, v `iptables`byli pevně dané)

```
 table inet filter
```

- **Chain –** _místo, kde se pakety zachytávají_.
  - Nejdůležitější jsou tzv. **base chains**, které jsou napojené na síťový stack jádra.
    - **INPUT** — příchozí komunikace
    - **OUTPUT** — odchozí komunikace
    - **FORWARD** — pakety, které zařízením prochází
- **Rule –** konkrétní podmínka a akce**.**

### 4.2.1 Výpis pravidel

```
nft -a list ruleset # Zobrazení celé konfigurace
```

> [!info]
> Parametr `-a` zobrazí u každého pravidla také jeho **handle**, který slouží například při mazání pravidel.

### 4.2.2 Načtení konfigurace

- Pravidla lze uložit do souboru `/etc/nftables.conf` a načíst příkazem `nft -f /etc/nftables.conf`

```bash
#!/usr/sbin/nft -f
flush ruleset

table inet filter {
    chain input {
        # vychozí politika
        type filter hook input priority 0; policy drop;

        # povolení příchozí komunikace na localhost
        iif lo accept 
        # povolení navázaní spojeni
        ct state established,related accept 

        # povolení portů
        tcp dport { 22, 80, 443 } accept 

        # logování zahozených paketů
        log prefix "nft-drop: " drop
    }

    chain forward {
        type filter hook forward priority 0; policy drop;
    }

    chain output {
        type filter hook output priority 0; policy accept;
    }
}
```

> [!danger]
> Jestli chceme, aby naše **konfigurace byla persistentní** musíme:
>
> `sudo systemctl enable nftables`
>
> Poté se pravidla načtou z `/etc/nftables.conf`

### 4.2.3 Přidání pravidla

Například:

```
nft add rule inet filter output ip daddr 158.194.80.13 accept
```

Význam:

- `inet` – pravidlo platí pro IPv4 i IPv6,
- `filter` – tabulka pro filtrování paketů,
- `output` – chain output,
- `ip daddr` – cílová IP adresa,
- `accept` – paket bude povolen.

### 4.2.4 Smazání pravidla

- První musíme zjistit číslo pravidla (handle) a poté jej odstraníme pomocí:

```
nft delete rule inet filter output handle 4
```

### 4.2.5 Výchozí politika řetězce

- Každý řetězec může mít nastavenou **výchozí politiku** (_policy_), která určuje, co se stane s pakety, které neodpovídají žádnému pravidlu.

```
nft chain inet filter output '{ policy drop ; }'
```

- Politika:
  - `accept` – vše je povoleno, pokud pravidlo neříká jinak,
  - `drop` – vše je zakázáno, pokud není výslovně povoleno.

> [!info]
> V praxi je z bezpečnostního hlediska vhodnější politika **drop**, protože se povoluje pouze nezbytná komunikace.

## 4.3 `firewalld`

- `firewalld` je služba, která představuje **vyšší vrstvu nad** `nftables` (dříve nad `iptables`).
- Uživatel _nemusí vytvářet jednotlivá pravidla ručně_, ale spravuje firewall _pomocí jednodušších příkazů_.
- Používá se především v distribucích **Fedora**, **RHEL** a **CentOS**.

- Hlavním pojmem jsou **zóny (zones)**. Každá zóna představuje určitou _úroveň důvěryhodnosti sítě_ (například domácí síť, veřejná síť nebo pracovní síť) a _obsahuje vlastní pravidla firewallu_.

```bash
# Stav firewallu
sudo firewall-cmd --state

# Výchozí zóna
sudo firewall-cmd --get-default-zone

# Nastavení výchozí zóny
sudo firewall-cmd --set-default-zone=public

# Přiřazení rozhraní do zóny
sudo firewall-cmd --zone=internal --change-interface=ens33 --permanent

# Výpis pravidel zóny
sudo firewall-cmd --zone=public --list-all

# Povolení služby (runtime — nepřežije restart)
sudo firewall-cmd --zone=public --add-service=http

# Povolení služby trvale
sudo firewall-cmd --zone=public --add-service=http --permanent
sudo firewall-cmd --reload    # nutné po --permanent změnách!

# Povolení konkrétního portu
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent

# Odebrání služby
sudo firewall-cmd --zone=public --remove-service=http --permanent

# Povolení masquerade (NAT)
sudo firewall-cmd --zone=public --add-masquerade --permanent

# Port forwarding
sudo firewall-cmd --zone=public \
  --add-forward-port=port=8080:proto=tcp:toport=80:toaddr=192.168.1.20 --permanent

# Seznam všech dostupných služeb
sudo firewall-cmd --get-services

# Reload (načtení permanent konfigurace)
sudo firewall-cmd --reload
```