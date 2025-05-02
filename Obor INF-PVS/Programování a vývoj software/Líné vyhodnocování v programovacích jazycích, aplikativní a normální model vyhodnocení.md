- Vyhodnocovací proces v běžných programovacích (C, C++, Java, C#) jazycích před aplikací funkce vyhodnotí všechny argumenty
- Je to tzv. *aplikativní model vyhodnocování*
## Aplikativní model
- Před aplikací funkce se vyhodnotí všechny argumenty
- Lepší pro debugování
- Lepší kontrola vedlejších efektů
- Nemožné pracovat s nekonečnými datovými strukturami
- Výjimku mají speciální operátory (a některá makra) - `if, and, or`

- Funkcionální programovací jazyky používají **normální vyhodnocovací model**
	- Používá myšlenku líného vyhodnocování
## Normální model
- **referenční transparentnost** ... výraz může být nahrazen hodnotou, jelikož to nemá vliv na výsledek
- např. Haskell
- Velmi efektivní
- Možnost práce s nekonečnými datovými strukturami
- Horší využití paměti
- Náchylné na *space leaks* využije mnohem více paměti než by se očekávalo (způsobí právě líné vyhodnocování)
#### Redukce v normálním modelu
![[Pasted image 20250424110206.png]]