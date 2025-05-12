>[!info]
>**Pravidlo nejvýše jednou pro výraz**
>Proces splňuje pravidlo *nejvýše jednou* pokud odkazuje na nejvýše jednu proměnnou `x`, která může být změněna v jiném procesu a odkazuje na ni nejvýše jednou.

>[!info]
>**Pravidlo nejvýše jednou pro přiřazení** `x <- e`
>Buď výraz `e` splňuje pravidlo *nejvýše jednou* a `x` není čtena v jiném procesu,
 nebo `e` neodkazuje na žádnou proměnnou, která může být změněna v jiném procesu.

- výraz (přiřazení), který splňuje pravidlo nejvýše jednou považujeme za *atomický*
	- atomický výraz jsme označovali v hranatých závorkách `[výraz]`
## Atomická operace
- Jedná se o operace, která se provede celá a nemůže být její provádění přerušeno jiným procesem (případně se neprovede vůbec)
- Jsou důležité při paralelním programování a synchronizaci
- Na úrovni assembleru se jedná o jednu instrukci
- Používají se taktéž v databázích (často nazývané jako *transakce*)
1) test and set - použit v semaforech
2) swap
3) compare and swap
4) fetch and add
5) load link/store conditional










