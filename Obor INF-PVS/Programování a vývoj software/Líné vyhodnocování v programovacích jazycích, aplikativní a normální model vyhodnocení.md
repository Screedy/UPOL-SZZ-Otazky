- Vyhodnocovací proces v běžných programovacích (C, C++, Java, C#) jazycích před aplikací funkce vyhodnotí všechny argumenty
- Je to tzv. *aplikativní model vyhodnocování*
#### Aplikativní model
- Lepší pro debugování
- Lepší kontrola vedlejších efektů
- Nemožné pracovat s nekonečnými datovými strukturami
- Výjimku mají speciální operátory (a některá makra)

- Funkcionální programovací jazyky používají **normální vyhodnocovací model**
	- Používá myšlenku líného vyhodnocování
#### Normální vyhodnocovací model
- **referenční transparentnost** ... výraz může být nahrazen hodnotou, jelikož to nemá vliv na výsledek
- např. Haskell
- Velmi efektivní
- Možnost práce s nekonečnými datovými strukturami
- Horší využití paměti
- Náchylné na *space leaks* využije mnohem více paměti než by se očekávalo (způsobí právě líné vyhodnocování)
