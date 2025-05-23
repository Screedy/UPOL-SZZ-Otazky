- Liší se od běžných jazyků, proto se operace pro aritmetiku obvykle provádí pomocí speciálních operátorů
- Bavíme o jazyku `PROLOG` a jazyku založeném na Scheme vytvořeném na PP4
## Prolog
- Poskytuje předdefinovaná operátory
- Vyhodnocení je potřeba vynutit procedurou `is`
```prolog
?- X=1+2.
% odpoved: X=1+2.

?- X is 1+2.
% odpoved: X=3.
```
- Ostatní operace fungují obdobně
	- `+, -, *, /,  **, //, mod`
- Je umožněno i porovnávání
```prolog
?- 277*37>10000.

true.
```
- Speciální operátor pro rovná se a nerovná se `=:=` a `=\=`
## Přirozená čísla s nulou
- Čísla jsou reprezentovány jako následující objekty:
	1) číslo nula označíme `zero`
	2) pokud `n` je číslo, pak `(succ n)` je následník čísla n
- Př. `(succ (succ zero)` odpovídá číslu $2$
#### Sčítání
 - Pomocí následníků, takže jakoby "rekurzivně"
 ```lisp
 ;; SCITANI - 3 arg - prvni 2 jsou cisla k souctu, 3. je vysledek
(<- (+ zero ?a ?a)
    (number ?a))

(<- (+ (succ ?a) ?b (succ ?c))
    (+ ?a ?b ?c))

;; tady s vyuzitim operátorů v Lispu
(rules 
  (<- (+ ?x ?y ?z)
      (equal ?z (+ ?x ?y))))
; (? (+ 2 3 ?x))

(rules
  (<- (<= ?x ?y)
      (equal t (if (<= ?x ?y) t nil))))

(rules
  (<- (- ?x ?y ?z)
      (equal ?z (- ?x ?y))))
```
- Odčítání by se udělalo podobně