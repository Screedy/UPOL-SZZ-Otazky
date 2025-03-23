>[!info] Dirichletův (šuplíkový/přihrádkový) princip
>- Je-li alespoň $r+1$ **objektů rozděleno do $r$ šuplíků**, pak musí existovat **šuplík s nejméně dvěma objekty**.

>[!Example] Příklad 1
>- Zřejmě žádné zobrazení z množiny $A$ do množiny $B$ nemůže být prosté, **jestliže $|A| > |B|$**.

>[!Example] Příklad 2
>- V šuplíku mám pár bílých ponožek, pár černých ponožek a pár žlutých ponožek.
>- Do **šuplíku nevidím**, pouze vytahuju ponožky.
>- Kolik ponožek musím vytáhnout, abych **si byl jistý,** že mám pár?
>- Řešení:![[MacBook-2024-05-31-001430.png]]
>	- $r$ šuplůků ... $3$ šuplíky, pro každou barvu vlastní.
>	- objektů tedy musí být alespoň $r+1$, tedy $4$
>	- Musím vytáhnout **alespoň $4$ ponožky**, abych si byl jistý, že mám pár.

>[!info] Dirichletův (zobezněný) princip
>- Pro přirozená čísla $r$ a $m$ platí: je-li **alespoň $rm+1$ objektů rozděleno do $r$ šuplíků,** pak musí existovat **šuplík, který má více než $m$ objektů**

>[!Example] Příklad 1
>- Dokažte, že v libovolné skupině $97$ lidí je určitě alespoň $9$ z nich narozeno ve stejný měsíc: ![[MacBook-2024-05-31-001431.png]]
>	- $r$ šuplíků ... $12$ šuplíků, pro každý měsíc jeden
>	- $m$ objektů ... $8$ objektů bude v každém šuplíku (v jednom chci mít $9$)
>	- objektů tedy musí být alespoň $mr+1$, tedy $12 * 8 + 1 = 97$
>	- V libovolné skupině $97$ lidí je určitě $9$ z nich narozeno ve stejný měsíc.

>[!Example] Příklad 2
>- Kolikrát musím hodit dvěma kostkami, abych určitě měl $3\times$ stejný součet na konstkách?![[MacBook-2024-05-31-001432.png]]
>	- $r$ šuplíků ... $11 šuplíků, pro každý součet $(2 - 12)$
>	- $m$ objektů ... $2$ objekty budou v každém šuplíku (v jednom chci mít $3$)
>	- objektů tedy musí být alespoň $mr+1$, tedy $11 * 2 + 1 = 23$
>	- Kostkami musím hodit alespoň $23 \times$, abych dostal $3\times$ stejný součet.

