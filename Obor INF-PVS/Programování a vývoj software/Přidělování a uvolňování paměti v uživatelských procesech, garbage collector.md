- Práce s pamětí uživatelských procesů (aplikací) se liší od OS
- Dva základní typy
	- **zásobník** (stack)
	- **halda** (heap)
- Obvykle řeší běhové prostředí (např. JVM) či standardní knihovna (např. dlmalloc)

## Linux - `ptmalloc`
- `ptmalloc` (verze 3, Céčko)
- rozhraní `malloc, free, realloc, ...`
- od OS získá souvislý blok paměti (pomocí systémového volání `brk/sbrk` či mapování souborů do paměti `/dev/zero`)
```C
void * simple_malloc(int size){
	return sbrk(size);
}

void * simple_free(int size){
	return sbrk(-size);
}
```

- `brk()` ... argument je adresa "do které" má pamět rozšířit
- `sbrk()` ... argument je velikost o kterou má být paměť rozšířena

- uvolnění je jednoduché, ale způsobuje fragmentaci (do `size` se uvede záporná hodnota)
- **bloky zaokrouhleny** na dvojnásobek velikosti slova (32/64 bitů) -> minimálně 8 B
- každé vlákno může mít svůj alokátor
- nejmenší alokovatelný blok jsou **4 slova**
- vždy začíná/vrací sudý násobek slova
- `malloc` nejdříve hledá volný blok, který byl již uvolněn, pokud nenajde -> oblast se rozšíří
	- hledání pomocí 2 strategií - *FIFO* v seznamech, *best fit* ve stromech
- alokátor si udržuje informaci o tom, které bloky byly uvolněny
	- menší bloky v 32 frontách
	- větší bloky v 16 trie
	- ostatní (největší) mají speciální strom
- zavolání `free` funguje na principu *buddy systému* pro následující a předchozí blok (slučování)

## Windows
- API + frontend + backend
 - každý objekt má hlavičku (8 B)
- **frontend**
	- optimalizuje alokaci menších bloků
	- 2 strategie
		1) LAL (look aside list) - 127 s objekty velikosti `n * 8 B`
		2) LF (low fragmentation) - až pro objekty do 16 kB
- **backend**
	- podobný ptmalloc
	- velké bloky přímo přes VM
	- není k dispozici malý -> rozdělí se větší

## Garbage collector
- Automatická správa paměti
- zjednodušený vývoj aplikací na úkor režie počítače (a aplikace jsou pomalejší)
- **escape analysis** - analýza zda daný objekt může uniknout z daného kontextu (např. funkce)
- **region/aréna** = alokace velkého bloku paměti (předpoklad na společné uvolnění, menší režie než `malloc` a `free`)
- jak řešit automatickou správu?
1) **počítání odkazů - (ARC ... automatic reference counting)**
	- kolik na něj odkazuje objektů => pokud 0, tak smažu
	- např. PHP, Python
	-  problém cyklické závislosti
		![[memory_leak_reference.png]]
	- řeší to překladač (Swift, ObjectiveC)
2) **objekty rozděleny do 3 množin**
	1) **bílé** - kandidáti na uvolnění
	2) **šedé** - odkazované z kořenu (musí se prověřit)
	3) **černé** - mají odkazy na bílé objekty
	- algoritmus
		1) jeden šedý objekt se přebarví na černo
		2) z něj odkazovné bílé objekty se barví na šedo
		3) opakuje se dokud existují šedé
##### Varianty GC
1) **přesunující vs nepřesunující**
	- přeskupení objektů, aby vytvořily souvislý blok
2) **generační**
	- předpoklad: krátce žijící objekty budou žít krátce
	- u starších objektů nemusí probíhat sběr příliš často
3) **přesné** vs **konzervatinví**
	- v Javě, .NET
	- odhadují zda je daná část objektu ukazatel
	- finalizace: fronta objektů ke zrušení (`finalize()`, není zaručeno zda bude vůbec zavolána a kdy, spíše NEPOUŽÍVAT)
1) **inkrementální** vs **stop the world**
	- inkrementální uvolňuje objekty po menších částech
	- stop the world vše uvolní najednou (musí se zastavit)
	- vylepšení paralelním zpracováním
2) **mark and sweep**
	- každý objekt má příznak zda-li se používá
	- při úklidu se objekty podle potřeby označí a ty neoznačené se uvolní
	- nevýhody: špatná cache, vnější fragmentace
3) **kopírující GC**
	- přesouvá objekty mezi aktivní a neaktivní částí (kopírovaných objektů je značně méně - jsou to ty aktivní)
	- řeší problémy "mark and sweep"
	- *následující vizualizace je animace (gif)*
	![[copying_gc.gif]]