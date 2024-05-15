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
```javascript
{ field: { $eq: argument } }
db.collection.find({ age: { $gt: 18 } })

{ field: { $exists: boolean_value } }
db.collection.find({ email: { $exists: true } })

{ $type: type }
db.collection.find({ name: { $type: "string" } })
```

## Logické operátory
- Podmínky lze skládat za použití logických operátorů.
- Dokument splňuje podmínku:
```javascript
{ $and: [ condition1, condition2, ...] }
db.collection.find({ $and: [ { title: "Dracula"}, { year: 1992 } ] })
```
- pokud splňuje všechny podmínky `condition1`, `condition2`, ...

- Dokument splňuje podmínku:
```javascript
{ $or: [ condition1, condition2, ... ] }
```
- pokud splňuje aspoň jednu z podmínek `condition1`, `condition2`, ...

- Hodnota splňuje podmínku:
```javascript
{ $not: condition }
```
- pokud nesplňuje podmínku `condition`.

## Implicitní operátory
- V dotazech, kde není specifikován žádný operátor, MongoDB implicitně používá `$eq`. 
```javascript
db.collection.find({ name: "John" }) 
// je ekvivalentní k:
db.collection.find({ name: { $eq: "John" } })
```
- Operátor `$and` je implicitně použit, pokud jsou ve vyhledávacím dotazu specifikovány více podmínky jako samostatné klíče ve stejném objektu.
```javascript
db.collection.find({ age: { $gt: 18 }, status: "active" })
// je ekvivalentní k:
db.collection.find({ $and: [ { age: { $gt: 18 } }, { status: "active" } ] })
```
- Operátor `$elemMatch` je implicitně použit v některých případech, kdy se provádí dotazy na pole objektů, které mají více podmínek.
```javascript
db.collection.find({ "orders.product": "Laptop", "orders.quantity": { $gt: 1 } })
// je ekvivalentní k:
db.collection.find({ orders: { $elemMatch: { product: "Laptop", quantity: { $gt: 1 } } } })
```
- Operátor `$all` je implicitně použit, když je pole porovnáváno s více hodnotami.
```javascript
db.collection.find({ tags: ["tag1", "tag2"] })
// je ekvivalentní k:
db.collection.find({ tags: { $all: ["tag1", "tag2"] } })
```
## Dotazy na vnořené dokumenty
- Dotazování na vnořené dokumenty vyžaduje použití tečkové notace. 
- Příklad dotazu na vnořený objekt by mohl vypadat takto:
```mongodb
{ "vydavatel.nazev": "Databáze Pro Všechny" }
```


##### Navigace
Předchozí:  [[Dokumentový model databáze - dokumenty, kolekce, atomické hodnoty, pole]]
Následující: [[Elasticsearch - rozdělení textu na termy a základní dotazy]]
Celý okruh: [[2. Informační technologie]]