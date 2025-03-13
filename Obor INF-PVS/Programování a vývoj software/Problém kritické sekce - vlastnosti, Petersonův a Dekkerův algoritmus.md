## Vlastnosti programu
- *vlastnost programu* je dána tvrzením o jeho historii
- program tuto vlastnost má, pokud je pravdivé pro **každou** historii
1) **vlastnost bezpečnosti** - tvrzení o nežádoucím stavu, musí být nepravdivé v každém stavu historie
2) **vlastnost živosti** - program se dostane do žádoucího stavu
## Kritická sekce
- platí zde několik pravidel
1) **vzájemné vyloučení** - maximálně 1 proces je v kritické sekci - *bezpečnost*
2) **absence uváznutí** - pokud se 2 procesy snaží vstoupit do kritické sekce, alespoň 1 uspěje - *životnost*
3) **absence zbytečného čekání** - pokud se proces snaží vstoupit do kritické sekce a další v ní nejsou nebo již skončili, tak musí uspět - *bezpečnost*
4) **zaručení vstupu** - pokud se proces snaží vstoupit do kritické sekce, jednou musí uspět - *životnost*
>[!info]
>**Test and set**
>Atomicky provede zjištění hodnoty `V` proměnné `var`, nastaví proměnnou `var` na pravdu a vrátí hodnotu `V`.

## Dekkerův algortimus
- řeší problém vzájemného vyloučení
- používá se pro 2 procesy
- nevyžaduje atomické operace
- není zdaleka tak efektivní, protože neustále testuje podmínku (nevyužívá uspání)
- proměnné pro to, kdo chce vstoupit do kritické sekce `bool wantA`, `bool wantB`
- proměnná určující kdo má přednost `int turn`
![[dekkeruv-algoritmus.png]]
## Petersonův algortimus (tie-breaker)
- vychází z *Dekkerova algoritmu*
- proměnná `last` indikuje, kdo poslední začal vykonávat vstup
- akce `await not in2 or last = 2` nemusí být aotmické
- zobecnění je opět kompikované (obvykle 2 procesy)
![[petersonuv-algoritmus.png]]