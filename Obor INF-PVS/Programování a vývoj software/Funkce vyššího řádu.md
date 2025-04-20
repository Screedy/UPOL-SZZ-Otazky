- Musí být umožněno pracovat s funkcí jako s hodnotou
- **Funkce vyššího řádu** ... pokud pracuje s jinými funkcemi jako s hodnotami
- Úkon který se provádí se seznamy se jmenuje *mapování* (funkce `mapcar`)
#### Nepovinné parametry funkce
```lisp
(defun rest-test (a b &rest rest)
	(list a b rest))
```

- Posloupnost můžeme reprezentovat jako funkci
- Některé funkce za běhu dynamicky vytváří nové funkce (obvykle $\lambda$-funkce)
```lisp
; argument "seq" má být funkce -> jde o funkci vyssiho radu
(defun seq-to-list (seq len)
	(labels ((stl (index)
			(if (>= index len)
				'()
			(cons (mem seq index)
					(stl (+ index 1))))))
	(stl 0)))

; TEST
CL-USER 8 > (seq-to-list (lambda (x) (* x x)) 20)
(0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361)
```


