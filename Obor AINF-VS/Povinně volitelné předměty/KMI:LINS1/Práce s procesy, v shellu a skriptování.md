# 1. Procesy

> [!success]
> **Proces** je spuštěná instance programu.
>
> Z pohledu programu se skládá z _kódu_, _dat_ (statických a dynamických), _zásobníku_ a _registrů_.
>
> Operační systém o každém procesu zároveň _vede řídicí informace_ v **Process Control Block (PCB)**, kde jsou uloženy například _PID_, _PPID_, _stav procesu_, _priorita_, _informace o otevřených souborech nebo vlastník procesu_.

- Každý proces _identifikován svým číslem_, které se označuje jako **proces ID (PID).** `PID 1` je vždy `init` nebo `systemd`.
- Procesy **tvoří stromovou hierarchii**, přičemž **v kořeni** tohoto stromu je proces označovaný **jako** `init` nebo `systemd`, který je _spuštěn jako první proces_ _po spuštění operačního systému._ **Každý proces** (kromě PID 1) má rodiče určeného **PPID**.

> [!warning]
> K vytvoření nového procesu slouží **systémové volání** `fork()` nebo `exec()`.
>
> - `fork()` vytváří **klon** _rodičovského procesu_ (rodič a potomek vykonávají stejný kód a každý má vlastní kopii dat)
> - `exec()` do paměti _nahraje kód programu_ a _začne jej vykonávat_

## 1.1 Zobrazení procesů

#### `ps`

- Vypíše právě běžící procesy

```bash
ps         # Vypíše pouze procesy aktuálního terminálu
ps -ef     # Vypíše všechny procesy. Používá POSIX syntaxi (s pomlčkami)
           # Hodí se hlavně při sledování vztahů mezi procesy     (obsahuje sloupec PPID)
ps aux     # Vypíše všechny procesy. Používá BSD syntaxi (bez pomlček)
           # Hodí se při sledování zetížení systému.
```

#### `top`

- Interaktivní sledování procesů.
- Ukazuje:
  - vytížení CPU,
  - RAM,
  - procesy podle spotřeby.
- Obnovuje se každých několik sekund.

#### `htop`

- Vylepšená verze `top`.
- Výhody:
  - barevné rozhraní,
  - strom procesů,
  - snadné ukončování,
  - filtrování.
- Není vždy předinstalovaný.

## 1.2 Vyhledání procesu

- Například příkazy `pgrep`a `pidof`, vrací PID

## 1.3 Signály

> [!success]
> **Signál** je _asynchronní notifikace_ zasílaná procesu jádrem nebo jiným procesem. Je to **nejjednodušší forma IPC** (Inter-Process Communication).

### 1.3.1 Nejdůležitější signály

| Číslo | Název | Výchozí akce | Typické použití |
| --- | --- | --- | --- |
| 1   | `SIGHUP` | Ukončení | Daemon znovu načte konfiguraci |
| 2   | `SIGINT` | Ukončení | `Ctrl+C` v terminálu |
| 9   | `SIGKILL` | Okamžité ukončení | Nelze zachytit ani ignorovat! |
| 15  | `SIGTERM` | Ukončení | Výchozí signál `kill` — čistý shutdown |
| 17  | `SIGCHLD` | Ignorovat | Rodič informován o ukončení potomka |
| 18  | `SIGCONT` | Pokračovat | Obnovit pozastavený proces |
| 19  | `SIGSTOP` | Pozastavení | Nelze zachytit ani ignorovat! |
| 20  | `SIGTSTP` | Pozastavení | `Ctrl+Z` v terminálu |

### 1.3.2 Příkazy pro zasílání signálů

```bash
kill 1234              # Pošle SIGTERM procesu PID 1234
kill -9 1234           # Pošle SIGKILL (vynucené ukončení)
kill -SIGHUP 1234      # Pošle SIGHUP (reload konfigurace)
killall nginx          # SIGTERM všem procesům se jménem nginx
pkill -u bob           # SIGTERM všem procesům uživatele bob
```

---

## 1.4 Priority procesů

> [!success]
> Linux přiděluje CPU čas procesům dle **nice hodnoty** v rozsahu **−20** **(nejvyšší priorita)** **až +19** **(nejnižší)**. Výchozí hodnota je 0.

- Snížit nice hodnotu pod 0 (zvýšit prioritu) může pouze **root**.
- Běžný uživatel může nice hodnotu pouze zvýšit (proces zpomalit).
- Příkaz `nice` _spustí proces s jinou prioritou_ a `renice` _změní prioritu_ _již běžícímu procesu_

---

## 1.5 Procesy na pozadí a jobs

> [!success]
> Proces v **popředí** (foreground) ovládá terminál — přijímá vstup, blokuje shell.
>
> Proces na **pozadí** (background) běží nezávisle na terminálu. Spustí pomocí `&` (např. `firefox &`)
>
> **Job (úloha)** je _seskupení jednoho nebo více procesů_, které _spravuje shell._ Je označován **%číslo**.

- `jobs` — Ukáže úlohy spuštěné z aktuálního shell
- `fg %1` — Přesune job do popředí
- `bg %1` — Přesune job na pozadí
- `nohup python server.py &` — Job běží i po zavření terminálu
- `disown %1` — Odpojí již běžící job od shellu

---

## 1.6 `systemd`

> [!success]
> `systemd` je **init systém** (PID 1) a **správce služeb**.
>
> Stará se o _start systému_, _paralelní spouštění služeb_, jejich závislosti, logování a správu zdrojů.

#### Základní příkazy `systemctl`

```bash
systemctl start nginx           # Spustit službu
systemctl stop nginx            # Zastavit službu
systemctl restart nginx         # Zastavit a znovu spustit
systemctl reload nginx          # Načíst konfiguraci bez restartu (pokud služba podporuje)
systemctl enable nginx          # Aktivovat při startu systému (vytvoří symlink)
systemctl disable nginx         # Deaktivovat při startu systému
systemctl status nginx          # Zobrazit stav, posledních pár řádků logu
systemctl daemon-reload         # Znovu načíst unit soubory po jejich změně
```

#### Unit soubory

- _Konfigurace služby je definována_ v **unit souboru** s příponou `.service`.
- Umístění:
  - `/usr/lib/systemd/system/` (samotná distribuce a balíčky),
  - `/etc/systemd/system/` (administrátor — má přednost).

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network.target         # Spustit až po síti

[Service]
Type=simple
ExecStart=/usr/bin/myapp --config /etc/myapp.conf
Restart=on-failure           # Restartovat při pádu
User=myapp                   # Spustit pod neprivilegovaným uživatelem

[Install]
WantedBy=multi-user.target   # Cíl, při kterém se aktivuje (enable)
```

- Po vytvoření/změně unit souboru vždy: `systemctl daemon-reload`.

---

# 2. Shell

> [!success]
> **Shell** je **příkazový interpret** — překládá příkazy uživatele na volání jádra.
>
> **Bash** je **výchozí shell** _většiny linuxových distribucí_. Další alternativy mohou být _Zsh, Fish, Dash_.

## 2.1 Proměnné

```bash
JMENO="Novak"           # Lokální proměnná shellu
echo $JMENO             # Vypsat hodnotu
unset JMENO             # Zrušit proměnnou
env                     # Výpis všech proměnných prostředí
```

> [!info]
> **Trvalé nastavení** → přidat do `~/.bashrc` nebo `/etc/environment`.

### 2.1.1 Důležité proměnné prostředí

| Proměnná | Obsah |
| --- | --- |
| `PATH` | Adresáře, kde shell hledá příkazy |
| `HOME` | Domovský adresář uživatele |
| `USER` | Přihlášený uživatel |
| `SHELL` | Cesta k aktuálnímu shellu |
| `LANG` | Nastavení jazykového prostředí |
| `$?` | Exit kód posledního příkazu |
| `$$` | PID aktuálního shellu |
| `$!` | PID posledního procesu na pozadí |

---

## 2.2 Přesměrování vstupu a výstupu

| Deskriptor | Číslo |
| --- | --- |
| stdin (standardní vstup) | 0   |
| stdout (standardní výstup) | 1   |
| stderr (chybový výstup) | 2   |

### 2.2.1 Operátory přesměrování

```bash
cmd > soubor          # stdout do souboru (přepíše)
cmd >> soubor         # stdout do souboru (přidá na konec)
cmd < soubor          # stdin ze souboru
cmd 2> chyby.log      # stderr do souboru
cmd 2> /dev/null      # Zahodit chybový výstup
cmd > vystup.log 2>&1 # stdout i stderr do jednoho souboru
cmd &> vystup.log     # Zkrácený zápis téhož (bash 4+)
```

### 2.2.2 Pipe (`|`)

- _Propojuje procesy v řetězci_ — **výstup jednoho je vstup druhého**, bez dočasného souboru.

```bash
ps aux | grep nginx | awk '{print $2}'    # PID procesů nginx
cat /var/log/auth.log | grep "Failed" | wc -l   # Počet neúspěšných přihlášení
```

## 2.3 Příkazy s textem

`head -n5` — zobrazí prvních `n` řádků (bez parametru 10)

`tail -n5` — zobrazí posledních `n` řádků (bez parametru 10)

`tee` — To, co dostane na vstup, tak pošle na výstup. Pokud má soubor jako parametr, tak do něj uloží.

### 2.4 Globální zástupné znaky

| Zástupný znak | Význam | Příklad | Co odpovídá |
| --- | --- | --- | --- |
| `*` | Libovolný počet znaků (i žádný) | `*.txt` | `a.txt`, `test.txt`, `soubor.txt` |
| `?` | Právě jeden znak | `a?.txt` | `ab.txt`, `a1.txt`, ale ne `a.txt` ani `abc.txt` |
| `[abc]` | Jeden znak z uvedených | `soubor[123].txt` | `soubor1.txt`, `soubor2.txt`, `soubor3.txt` |
| `[a-z]` | Jeden znak z daného rozsahu | `file[a-c].txt` | `filea.txt`, `fileb.txt`, `filec.txt` |
| `[0-9]` | Jedna číslice | `img[0-9].png` | `img1.png`, `img7.png` |
| `[!abc]` | Libovolný znak kromě uvedených | `file[!0-9].txt` | `filea.txt`, ale ne `file5.txt` |

---

# 3. Bash skriptování

> [!success]
> **Shellový skript** je _obyčejný textový soubor obsahující příkazy shellu_.
>
> První řádek se nazývá **shebang** a určuje, _jakým interpretem se má skript spustit._

```bash
#!/bin/bash 

echo "Hello, World!"
```

> [!danger]
> Skript musí mít právo spuštění: `chmod +x skript.sh`

> [!info]
> Spuštění: `./skript.sh` nebo `bash skript.sh`

## 3.1 Proměnné ve skriptech

```bash
JMENO="Karel"
echo "Ahoj, $JMENO"
echo "Ahoj, ${JMENO}!"      # Složené závorky s textem

# Výstup příkazu do proměnné
DATUM=$(date +%Y-%m-%d)     # Moderní syntaxe (preferovaná)
```

## 3.2 Parametry skriptu

```bash
$0   # Název skriptu
$1   # První argument
$2   # Druhý argument
$@   # Všechny argumenty jako seznam
$#   # Počet argumentů
$?   # Exit kód posledního příkazu (0 = úspěch)
$$   # PID aktuálního shellu/skriptu
```

## 3.3 Čtení vstupu

```
read jmeno 
read -p "Jméno: " jmeno
```

## 3.4 Podmínky

```bash
if [ podmínka ]; then
    příkazy
elif [ jiná_podmínka ]; then
    příkazy
else
    příkazy
fi
```

### **3.4.1 Porovnávání čísel**

```bash
[ $A -eq $B ]   # rovno
[ $A -ne $B ]   # není rovno
[ $A -lt $B ]   # menší než
[ $A -gt $B ]   # větší než
[ $A -le $B ]   # menší nebo rovno
[ $A -ge $B ]   # větší nebo rovno
```

### **3.4.2 Porovnávání řetězců:**

```bash
[ "$A" = "$B" ]    # rovno (pro řetězce = nebo ==)
[ "$A" != "$B" ]   # není rovno
[ -z "$A" ]        # je prázdný řetězec
[ -n "$A" ]        # není prázdný řetězec
```

### **3.4.3 Testy souborů:**

```bash
[ -f /etc/passwd ]   # existuje a je to regulérní soubor
[ -d /tmp ]          # existuje a je to adresář
[ -e /cesta ]        # existuje (cokoliv)
[ -r /soubor ]       # má právo čtení
[ -w /soubor ]       # má právo zápisu
[ -x /soubor ]       # má právo spuštění
[ -s /soubor ]       # existuje a není prázdný
```

> [!info]
> **Dvojité závorky** `[[ ]]` jsou **bashové rozšíření**
>
> - Bezpečnější pro řetězce, podporují `&&`, `||`, `=~` (regulární výrazy).
>
> `[[ "$JMENO" =~ ^[A-Z] ]] # Začíná velkým písmenem?`

## 3.5 Cykly

### 3.5.1 `for` **cyklus**

```bash
for i in 1 2 3 4 5; do
    echo "Číslo: $i"
done

for soubor in /etc/*.conf; do
    echo "Konfigurace: $soubor"
done

for ((i=0; i<10; i++)); do   # C-style
    echo $i
done
```

### 3.5.2 `while` **cyklus**

```bash
POCITADLO=0
while [ $POCITADLO -lt 5 ]; do
    echo $POCITADLO
    ((POCITADLO++))
done

# Čtení souboru řádek po řádku
while IFS= read -r radek; do
    echo "$radek"
done < /etc/passwd
```

### 3.5.3 `until` **cyklus**

```bash
until ping -c1 8.8.8.8 &>/dev/null; do
    echo "Čekám na síť..."
    sleep 5
done
```

## 3.6 Funkce

```bash
pozdrav() {
    echo "Ahoj, $1!"
    return 0    # Exit kód funkce
}
pozdrav "Karel"
```

## 3.7 Case

```
read -p "Zadej volbu (a/b): " volba

case $volba in
    a)
        echo "Vybral jsi možnost A"
        ;;
    b)
        echo "Vybral jsi možnost B"
        ;;
    *)
        echo "Neplatná volba"
        ;;
esac
```

## 3.8 Zpracování textu — základní nástroje

```bash
grep "pattern" soubor        # Hledání vzoru
grep -r "pattern" /etc/      # Rekurzivně
grep -v "pattern"            # Inverzní (řádky BEZ vzoru)
grep -i "pattern"            # Case-insensitive
grep -n "pattern"            # S čísly řádků

sed 's/stare/nove/g' soubor  # Nahrazení, pouze vypíše
sed -i 's/foo/bar/g' soubor  # Zapíše i do souboru

awk '{print $1, $3}' soubor  # Tisk 1. a 3. sloupce
awk -F: '{print $1}' /etc/passwd   # Oddělovač : (výpis uživatelů)

cut -d: -f1 /etc/passwd      # Totéž, jako awk výše
sort soubor                  # Řazení
sort -n soubor               # Numerické řazení
uniq                         # Odstranění duplicit (vyžaduje seřazený vstup)
wc -l soubor                 # Počet řádků
```

---

## 4. Plánování úloh

### 4.1 `cron` — opakující se úlohy

> [!success]
> Démon `crond` pravidelně spouští úlohy definované v **crontab** souborech.

```bash
crontab -e      # Editovat crontab aktuálního uživatele
crontab -l      # Zobrazit crontab aktuálního uživatele
crontab -r      # Smazat crontab (pozor, bez potvrzení!)
```

```bash
# ┌───── minuta (0-59)
# │ ┌───── hodina (0-23)
# │ │ ┌───── den měsíce (1-31)
# │ │ │ ┌───── měsíc (1-12)
# │ │ │ │ ┌───── den týdne (0-7, 0 a 7 = neděle)
# │ │ │ │ │
# * * * * *  příkaz

0 2 * * *   /usr/bin/backup.sh          # Každý den ve 2:00
*/15 * * * * /usr/bin/check_disk.sh     # Každých 15 minut
0 0 1 * *   /usr/bin/monthly_report.sh  # 1. den každého měsíce
0 9-17 * * 1-5 /usr/bin/work_task.sh    # Pracovní dny 9-17 hod.
```

### 4.2 `at` — jednorázové úlohy

> [!success]
> Naplánuje jednorázové spuštění příkazu v určený čas.

```bash
at 14:30         # Interaktivní zadání příkazů, ukončit Ctrl+D
at 02:00 tomorrow      # Zítra ve 2:00
echo "backup.sh" | at now + 1 hour   # Za hodinu
```