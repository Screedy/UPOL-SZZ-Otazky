## Co jsou regulární výrazy?
- Regulární výrazy jsou **vzory**, které odpovídají určitým sadám řetězců a umožňují **komplexní vyhledávání** a **nahrazení** v textových datech. 
- Regex umožňuje specifikovat, jaký text by měl být nalezen pomocí různých symbolů, které reprezentují znaky nebo skupiny znaků.

### Základní komponenty regulárních výrazů
- **Literály**: Jsou obyčejné znaky, které odpovídají sami sobě, například `a`, `1`, `B`.
- **Metaznaky**: Mají speciální význam, jako např.:
    - `.`: Jakýkoliv jeden znak. (kromě nového řádku)
    - `^`: Začátek řádku.
    - `$`: Konec řádku.
    - `*`: Nula nebo více opakování předchozího znaku.
    - `+`: Jedno nebo více opakování předchozího znaku.
    - `?`: Nula nebo jedno opakování předchozího znaku.
    - `\s`: Odpovídá jakémukoli bílému znaku (mezera, tabulátor, nový řádek).
    - `\d`: Odpovídá jakémukoli číslici (0-9).
    - `\w`: Odpovídá jakémukoli alfanumerickému znaku (písmena a číslice) a podtržítku.
- **Závorky**:
    - `[]`: Umožňují definovat sadu znaků, z nichž kterýkoliv může být shodný. Například `[abc]` odpovídá `a`, `b`, nebo `c`.
    - `()`: Skupinování více znaků nebo výrazů do jednoho celku pro operace jako je kvantifikace (`*`, `+`, `?`) nebo pro zachytávání podvýrazů.

### Příklady použití regulárních výrazů
- **grep** - hledání v souborech
	- Najde všechny řádky, které začínají slovem "Error":
```bash
grep '^Error' filename.txt
```

- **sed** - úprava souborů
	- Nahradí všechny výskyty "oldtext" za "newtext" ve souboru:
```bash
sed -i 's/oldtext/newtext/g' filename.txt
```

- **awk** - skriptování a zpracování textu
	- Vytiskne všechny řádky, které začínají jednou nebo více číslicemi:
```bash
awk '/^[0-9]+/ { print $0 }' filename.txt
```

##### Navigace
Předchozí:  [[Příkazový interpret (shell), vstup a výstup programu a roura v unixových OS]]
Následující: [[Zpracování textu v unixových OS - základní utility, grep, sed, awk, jejich použití]]
Celý okruh: [[2. Informační technologie]]