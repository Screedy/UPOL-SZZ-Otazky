- Zásahy mají v položce `"_score"` číslo nazývané skóre zásahu.
- Čím větší, tím lépe dokument vyhovuje dotazu.
- Zásahy jsou uspořádané podle skóre sestupně.

## Výpočet
- Výpočet probíhá posle algoritmu `BM25`. `BM` = Best Matching.
- Skóre dotazu $Q$ obsahující tokeny $q_{1}, ..., q_{n}$ na hodnotu zadané položky dokumentu $D$ je dáno výpočtem:
$$
score(D,Q) = \sum^{n}_{i=1}boost*IDF(q_{i})*tf(q_{i},D)
$$
- Základní hodnota $boost$ je $k_{1} + 1$. Výchozí hodnota parametru $k_{1}$ (*term saturation parameter*) je $1.2$. Základní hodnota $boost$ je tedy $2.2$
- Hodnota $IDF(q_{i})$ je dána vzorcem:
$$
ln(1+\frac{N-n(q_{i}+0.5)}{n(q_{i}+0.5)})
$$
- Hodnota $n(_q{i})$ udává počet dokumentů obsahující v zadané položce term $q_{i}$ a hodnota $N$ celkový počet dokumentů s položkou.
- Hodnota $tf(q_{i},D)$ je dána vzorcem:
$$
\frac{f(q_{i}, D)}{f(q_{i}, D) + k_{1} \cdot (1-b+b \cdot \frac{dl}{avgdl})}
$$
- Zkratka $tf$ znamená *term frequency*.
- Hodnota $f(q_{i}, D)$ udává počet výskytů termu $q_{i}$ v zadané položce dokumentu $D$
- $k_{1} = 1.2$ je *term saturation parameter*
- $b = 0.75$ je *length normalization parameter*
- $dl$ je *document length*, udává počet termá v zadané položce dokumentu $D$
- $avgdl$ je *average document length* a udává průměrný počet termů v zadané položce u všech dokumentů

## Výpočet (lidsky)
- Skóre zásahu se obvykle vypočítá na základě několika faktorů:
	1. **Term Frequency (TF)**: Četnost termínu, tedy kolikrát se hledaný termín vyskytuje v poli dokumentu. Čím častěji se termín vyskytuje, tím je považován za relevantnější.
	2. **Inverse Document Frequency (IDF)**: Tento faktor obráceně koreluje s počtem dokumentů ve kterých se termín vyskytuje. Pokud se termín vyskytuje v mnoha dokumentech, jeho význam pro určení relevance je menší.
	3. **Field-Length Norm**: Dokumenty s menším počtem slov v poli mohou získat vyšší skóre než delší dokumenty, protože se předpokládá, že pokud se hledaný termín vyskytuje v krátkém textu, je pravděpodobněji tématem celého dokumentu.
	4. **Boosting**: Určitá pole nebo termíny mohou být posíleny, tzn. výslovně jim může být přiděleno vyšší skóre, aby ovlivnily celkové skóre zásahu.

- Výsledné skóre zásahu pro každý dokument je potom využito pro řazení výsledků hledání. Dokumenty s vyšším skóre zásahu jsou považovány za relevantnější pro daný dotaz a jsou umístěny výše ve výsledcích vyhledávání.

## `explain`
- Podrobnosti o výpočtu skóre lze získat přidáním položky `"explain"` s hodnotou `true` k dotazu
```JSON
{  
	"query": query, 
	"explain": true
}
```

Například:
```JSON
GET /book/_search
{
  "query": {
    "match": {
      "title": {
        "query": "fellowship ring hobbit"
		}
	}
},
  "explain": true
}
```