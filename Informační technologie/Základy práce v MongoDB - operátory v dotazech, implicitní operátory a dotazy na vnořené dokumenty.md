- MongoDB je databázový systém založený na dokumentech.

## Základy
- Výraz jazyka je příkazem, který se vykoná tak, že se vyhodnotí výraz a vytiskne jeho hodnota.
- Databázi lze změnit výrazem:
```mongodb
use(dbname)
```

- Přidání dokumentu `document` do kolekce `collection`:
```mongodb
db.collection.insertOne(document)
```
- Konkrétně:
```mongodb
db.movies.insertOne({ _id: 1, title: "Dracula", year: 1992 })
```

- Hodnotou výrazu `db.collection.find()` je pole všech dokumentů v kolekci.
```mongodb
moviedb> db.movies.find()
[
  { _id: 1, title: ’Dracula’, year: 1992 },
  {
    _id: ObjectId("63591ff5b5c9d364805b4ac1"),
    title: ’The Godfather’,
    year: 1972
} ]
```

- Dále přidání více dokumentů najednou:
```mongodb
db.collection .insertMany(documents)
```
- Konkrétně:
```mongodb
db.movies.insertMany([
	{
	  title: "The Conversation",
	  year: 1974

	}, 
	{
	  title: "Apocalypse Now",
	  year: 1979
	}
])
```

- Výraz `db.collection.drop()` zruší kolekci `collection`. Kolekce se stane prázdnou.

## Operátory v dotazech
- MongoDB používá různé operátory pro vyhledávání a manipulaci s daty.
- Tyto operátory se mohou objevit v dotazech, aktualizacích, a při agregačních operacích. 
- Názvy operátorů začínají znakem `$`:
	- `$eq`: rovná se
	- `$gt`, `$gte`: větší než, větší nebo rovno
	- `$lt`, `$lte`: menší než, menší nebo rovno
	- `$ne`: není rovno
	- `$in`: hodnota je v poli
	- `$nin`: hodnota není v poli
	- `$and`: logický operátor AND
	- `$or`: logický operátor OR
	- `$not`: logický operátor NOT
	- `$exists`: zda klíč existuje
	- `$type`: typ hodnoty klíče
- Použití například:
```mongodb
{ field: { $eq: argument } }
{ field: { $exists: boolean_value } }
{ $type: type }
```

## Logické operátory
- Podmínky lze skládat za použití logických operátorů.
- Dokument splňuje podmínku:
```mongodb
{ $and: [ condition1, condition2, ...] }
{ $and: [ { title: "Dracula"}, { year: 1992 } ] }
```
- pokud splňuje všechny podmínky `condition1`, `condition2`, ...

- Dokument splňuje podmínku:
```mongodb
{ $or: [ condition1, condition2, ... ] }
```
- pokud splňuje aspoň jednu z podmínek `condition1`, `condition2`, ...

- Hodnota splňuje podmínku:
```mongodb
{ $not: condition }
```
- pokud nesplňuje podmínku `condition`.

## Implicitní operátory
- V dotazech, kde není specifikován žádný operátor, MongoDB implicitně používá `$eq`. Například:
```mongodb
{ "jmeno": "Jan" }
```
- Tento dotaz vybere dokumenty, kde hodnota klíče `jmeno` je rovna "Jan", což je ekvivalentní k:
```mongodb
{ "jmeno": { "$eq": "Jan" } }
```

## Dotazy na vnořené dokumenty
- Dotazování na vnořené dokumenty vyžaduje použití tečkové notace. 
- Příklad dotazu na vnořený objekt by mohl vypadat takto:
```mongodb
{ "vydavatel.nazev": "Databáze Pro Všechny" }
```

