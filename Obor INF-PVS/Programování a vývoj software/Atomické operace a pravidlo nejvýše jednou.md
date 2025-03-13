>[!info]
>**Pravidlo nejvýše jednou pro výraz**
>Proces splňuje pravidlo *nejvýše jednou* pokud odkazuje na nejvýše jednu proměnnou `x`, která může být změněna v jiném procesu a odkazuje na ni nejvýše jednou.

>[!info]
>**Pravidlo nejvýše jednou pro přiřazení** `x <- e`
>Buď výraz `e` splňuje pravidlo *nejvýše jednou* a `x` není čtena v jiném procesu,
 nebo `e` neodkazuje na žádnou proměnnou, která může být změněna v jiném procesu.

- výraz (přiřazení), který splňuje pravidlo nejvýše jednou považujeme za *atomický*
	- atomický výraz jsme označovali v hranatých závorkách `[výraz]`











