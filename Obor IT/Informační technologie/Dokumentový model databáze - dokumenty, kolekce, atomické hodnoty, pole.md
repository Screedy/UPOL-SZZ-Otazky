- Dokumentový model databáze, často spojovaný s NoSQL databázemi, je flexibilní alternativa k tradičním relačním databázím.
- V dokumentovém modelu jsou data uložena ve formátu, který je blízký datovým typům používaným ve většině programovacích jazyků, čímž se snižuje složitost při práci s daty.

## Dokumenty
- Vezmeme-li dvojice řetězců a hodnot `name1` a `value1`, `name2` a `value2`, ... můžeme z nich vytvořit **dokument**.
- Dokument je hodnota, která obsahuje určené hodnoty v zadaném pořadí a každou z nich označuje zadaným jménem.
- Dvojice jméno a hodnota se nazývá **položka**.

- Například uvazujme dokument:
```JSON
{
	_id: 1,
	title: "The Godfather",
	year: 1972
	actors: [
		"Gary Oldman",
		"Winona Ryder",
		"Anthony Hopkins"
	]
}
```
- Položka `title` je řetězec `The Godfather` a pod `actors` se nalézá pole, které má tři prvky: `Gary Oldman`, `Winona Ryder` a `Anthony Hopkins`.
- Prvek s názvem `_id` se nazývá **identifikátor** dokumentu.
- Názvy dokumentu píšeme anglicky malými písmeny. Slova spojujeme tak, že první písmeno následujícího slova změníme na velké (velbloudí notace): `movieTitle`

## Kolekce
- Kolekce jsou skupiny dokumentů.
- V dokumentové databázi jsou dokumenty uloženy v kolekcích, což je ekvivalent tabulek v relačních databázích.
- Dokumenty v jedné kolekci mohou mít různou strukturu, což poskytuje flexibilitu při práci s různorodými daty.

## Atomické hodnoty
- Pro reprezentaci formátu jsme používali JSON.
- Hodnoty v JSON dělíme na **atomické** a **složené**.
- Atomické hodnoty:
	1. čísla ($1939$, $0.25$)
	2. řetězce (`"Dracula"`, `""`)
	3. logické hodnoty (`true`, `false`)
	4. `null` (prázdné místo)

## Složené hodnoty
- **Složené** hodnoty:
	- Složené hodnoty dělíme na **objekty** a **pole**.
		- **Objekt** má tvar `{ pairs }`, kde `pairs` jsou čárkou oddělené páry. Pár má tvar `name: value`. Například `{ "title": "Dracula", "year": 1992 }`.
		- **Pole** má tvar: `[ items ]`, kde `items` jsou libovolné hodnoty oddělené čárkou. Například: `[]`, `[1972, 1974, 1990]`.



##### Navigace
Předchozí:  [[Integrita dat - primární a cizí klíč]]
Následující: [[Základy práce v MongoDB - operátory v dotazech, implicitní operátory a dotazy na vnořené dokumenty]]
Celý okruh: [[2. Informační technologie]]