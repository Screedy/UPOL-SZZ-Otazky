- Elasticsearch = systém pro fulltextové vyhledávání
- založen na Apache Lucene, používá strukturu Skip list

- Elasticsearch komunikuje pomocí REST (representational state transfer)
	- Pro komunikaci se serverem lze použít libovolého REST klienta.
		- Např. curl, rozšíření REST Client do VS Code, ...

## Rozdělení textu na termy (Tokenizace)
- V Elasticsearch se indexace dokumentů skládá z několika kroků, ve kterých je text rozdělen na menší části nazývané "termy" nebo "tokeny".
- Proces tokenizace:
	1. **Analýza**: Text je zpracován analyzátorem. To je kombinace tokenizeru a filterů
		- **Tokenizer** rozděluje text na tokeny, obvykle na základě mezery a interpunkce.
		- **Filtry** modifikují tokeny, například převádění na malá písmena, odstranění stop slov, synonyma, atd.
		- Například řetězec `"The Hobbit, or There and Back Again"` se přeloží na termy: `"the"`, `"hobbit"`, `"or"`, `"there"`, `"and"`, `"back"`, `"again"`.
	1. **Indexace (Indexing)**: Tokeny jsou poté přidány do invertovaného indexu, který mapuje termíny na místa jejich výskytu v dokumentech.

## Základní dotazy
- Dotazy jsou vyjádřeny pomocí JSON.

### Požadavek
- Požadavek na dotaz indexu má tvar:
```JSON
POST /index/_search 
{
	"query": query 
}
```
- kde `query` je objekt popisující *dotaz*

### Odpověď
- Tělo odpovědi obsahuje:
```JSON
{
	"hits": {
		"total": {
			"value": hits_count,
		},
		"hits": hits 
	}
}
```
- kde `hits_count` je počet zásahů a `hits` je pole zásahů.

- Zásah obsahuje:
```JSON
{
"_id": document_id
"_source": document
}
```
- kde `document` je zasažený dokument a `document_id` jeho identifikátor.

### match query
- Hledá dokumenty, které odpovídají poskytnutému textu.
- Dotaz `match_all` zasáhne každý dokument:
```JSON
{
	"match_all": { }
}
```

- Dotaz `match` zasáhne dokumenty, které mají v položce `name` hodnotu vyhovující predikátu `value_query`.
```JSON
{  
	"match": {
	name: value_query 
	}
}
```

- Konkrétní příklad:
```JSON
{  
	"query": {
	    "match": {
	      "title": {
			"query": "THE, HoBBit"
	      }
		} 
	}
}
```
- V tomto řetězci je `"THE, HoBBit"` rozložen na termy: `"the"`, `"hobbit"`.
- Dokument je zasažen, pokud se aspoň jeden term dotazu shoduje s termem položky.

- Pokud chceme, aby položka obsahovala všechny uvedené termy, použijeme predikát:
```JSON
{  
	"query": query_string, 
	"operator": "AND"
}
```