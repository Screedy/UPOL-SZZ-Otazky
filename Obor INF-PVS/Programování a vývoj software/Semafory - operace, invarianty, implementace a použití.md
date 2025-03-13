## Semafory
- synchronizační nástroj (primitivum)
- vytvořil Dijkstra, analogie semaforů na železnici
- v rozumných programovacích jazycích již implementovány
- jedná se o datovou strukturu
`k` ... počet zdrojů (zadá se při vytváření)
`P` ... operace wait/počkat (= `k--` nebo pokud je `k = 0`, zablokuje běžící proces)
`V` ... operace signal/vyhlásit (= pokud existuje zablokovaný proces, tak 1 odblokuje nebo `k++`)
- čekající procesy jsou ve *frontě* (FIFO)
#### Invarianty semaforů
- hodnota semaforu `k` nesmí být menší než `0` (pokud by to `P` mělo způsobit, proces čeká)
- operace `V` musí případný čekající proces korektně probudit

- aktuální počet zdrojů: $s = k + c_V − c_P$
#### Implementace
![[semafor-nacrtek.png]]
- `s` ... aktuální počet zdrojů
- pro operaci `P(s)` --> `[await s > 0; s = s - 1]`
- pro operaci `V(s)` --> `[s = s + 1]`
#### Použití
- obecně pro synchronizaci (řešení problému kritické sekce)
- dají se pomocí nich implementovat *bariéry*



