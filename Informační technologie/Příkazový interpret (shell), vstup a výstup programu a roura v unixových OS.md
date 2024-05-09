## Příkazový interpret (shell)
- V unixových operačních systémech slouží jako **primární rozhraní pro komunikaci** uživatelů s operačním systémem.
- Shell **zpracovává** příkazy vložené uživatelem, **spouští** programy, a **manipuluje** s daty a procesy na systému.
- Existují různé typy shellů, jako je Bash, sh, zsh, csh, ...

## Vstup a výstup programu
- V unixových systémech každý program má tři standardní datové proudy:
	1. **Standardní vstup (stdin)**: Proud pro data vstupující do programu. Standardně je to klávesnice uživatele.
	2. **Standardní výstup (stdout)**: Proud pro data vycházející z programu. Standardně se zobrazuje na obrazovku uživatele.
	3. **Standardní chybový výstup (stderr)**: Proud používaný programem k vypisování chybových zpráv nebo diagnostických informací, nezávisle na běžném výstupu programu. Také standardně vede na obrazovku.
```bash
program > soubor        # Standardní výstup do souboru, vytvoří pokud neexistuje
program 2> soubor       # Chybový výstup do souboru, vytvoří pokud neexistuje
program &> soubor       # Oba výstupy do souboru, vytvoří pokud neexistuje
program >> soubor       # vytvoří soubor pokud neexistuje, jinak ho appendne

program < soubor        # přesměruje soubor na vstup do programu
```

## Roura
-  Roura (`|`) je **nástroj**, který umožňuje **výstupy jednoho programu** použít jako **vstupy pro jiný program**.
- To umožňuje vytvářet **řetězce programů**, kde každý program transformuje data a předává je dalšímu.
- Např:
```bash
cat /var/log/system.log | grep 'error' | wc -l
```
- `cat /var/log/system.log` čte soubor a posílá jeho obsah do stdout.
- `grep 'error'` přijímá vstup z předchozího příkazu (proud dat z `cat`), filtruje řádky obsahující "error", a výstupy posílá dále.
- `wc -l` počítá řádky ze svého vstupu, které přijal od `grep`.

##### Navigace
Předchozí:  [[Unixové systémy souborů a procesů, základní programy]]
Následující: [[Text a regulární výrazy]]
Celý okruh: [[2. Informační technologie]]