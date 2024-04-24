## Systémy souborů
- Unixové systémy používají **hierarchický systém souborů**, kde vše je soubor, včetně hardware zařízení a procesů.
- Nejvyšší úroveň tohoto systému je kořenový adresář, značený jako `/`.
- Pod ním se nachází další důležité adresáře:
	- `/bin`: Obsahuje binární soubory základních příkazů.
	- `/etc`: Systémová konfigurace a skripty.
	- `/home`: Osobní adresáře uživatelů.
	- `/usr`: Aplikace a soubory, které nejsou nezbytné pro spuštění systému.
	- `/var`: Proměnlivá data, jako jsou logy a databáze.
	- `/dev`: Soubory zařízení, které reprezentují hardware.
- Systém souborů tvoří stromovou strukturu, například **UFS**.

## Systém procesů
- V Unixu **každý** spuštěný program tvoří proces.
- Procesy mají jedinečné ID (PID) a jsou organizovány do stromové struktury, kde každý proces může mít potomky.
- Procesy mohou být **uživatelské** (spuštěné uživateli) nebo **systémové** (spuštěné operačním systémem).

- Základní příkazy pro správu procesů:
	- `ps`: Zobrazuje aktuálně spuštěné procesy.
	- `top`: Dynamicky zobrazuje procesy a jejich spotřebu zdrojů.
	- `kill`: Ukončuje procesy na základě jejich PID.
	- `nice`/`renice`: Mění prioritu procesu.

## Základní programy a nástroje
- **Textové editory**: `vi`/`vim`, `nano`, `emacs`.
- **Správa souborů**: `ls`, `cp`, `mv`, `rm`, `find`, `touch`.
- **Zpracování textu**: `grep`, `sed`, `awk`, `cat`, `cut`, `sort`, `wc`.
- **Komprese a archivace**: `tar`, `gzip`, `bzip2`.
- **Síťové nástroje**: `ping`, `netstat`, `ssh`, `scp`, `curl`, `wget`.
- **Zabezpečení a monitoring**: `chmod`, `chown`, `top`, `htop`, `iptables`.