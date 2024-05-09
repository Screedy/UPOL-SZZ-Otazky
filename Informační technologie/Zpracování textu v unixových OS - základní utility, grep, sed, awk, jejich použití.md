- V unixových operačních systémech je k dispozici mnoho nástrojů pro zpracování textu, které umožňují efektivní manipulaci s daty, vyhledávání vzorů, transformaci textu a zpracování souborů.
- Tři z nejzákladnějších a nejužitečnějších jsou `grep`, `sed` a `awk`.

## Utility
- `cat`, `tac` - vypíše soubor
- `less`, `more` - vypíše soubor s možností posunu dopředu a dozadu, nevyžaduje načtení celého souboru
- `cut` - slouží k vymazání specifikovaných výrazů
- `sort` - třídění

## grep
- Nástroj pro vyhledávání textu pomocí regulárních výrazů.
- Umožňuje rychle najít řádky v souboru nebo streamu, které odpovídají danému vzoru.
```bash
grep "search_pattern" filename.txt
```
- Základní přepínače:
	- `-i` - ignoruje malá/velká písmena
	- `-c` - počet výskytů vzorů
	- `-v` - zobrazení řádků, které neobsahují vzor
- `"search_pattern"` využítá regulární výrazy:

## sed
- Nástroj pro provádění různých operací na textových souborech nebo datových proudech, jako je nahrazování, vkládání, mazání nebo získání určitých řádků.
```bash
sed 's/old/new/' filename.txt      # nahrazení jednoho výskytu
sed 's/old/new/g' filename.txt     # nahrazení všech výskytů
sed '/pattern/d' filename.txt      # smazání řádků obsahující vzor
sed '/pattern/a "new line of text"' filename.txt  # přidání řádku po
sed '/pattern/i "new line of text"' filename.txt  # přidání řádku před
```

## awk
- `awk` je programovací jazyk a nástroj, který je ideální pro zpracování a analýzu dat.
- Výkonný při práci s poli, textovými řetězci a vzorovými operacemi, `awk` umožňuje snadné zpracování strukturovaných dat a generování formátovaných zpráv.
```bash
awk '{print $1}' filename.txt  # vypíše první sloupec každého řádku
awk '{sum += $1} END {print sum}' filename.txt # suma hodnot ve sloupci
awk '/pattern/ {print $2}' filename.txt  # vypíše druhý sloupec pro řádky obsahující "pattern"
awk '{if ($1 > 100) print $0}' filename.txt > newfile.txt  # vypíše do nového souboru řádky, kde první sloupec má hodnotu větší než 100
```

##### Navigace
Předchozí:  [[Text a regulární výrazy]]
Následující: [[Architektury a princip činnosti počítače]]
Celý okruh: [[2. Informační technologie]]