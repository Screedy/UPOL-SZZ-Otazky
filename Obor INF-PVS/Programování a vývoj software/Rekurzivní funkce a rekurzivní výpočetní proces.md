## Definice funkce
- Používáme makro `defun`
```lisp
(defun triangle-area (b h)
	(* 1/2 b h))
```
>[!tip] Popis funkce
>![[Pasted image 20250320214832.png]]
>**Název funkce** ... libovolný symbol
>**Parametry** ... symboly
>**Tělo** ... libovolný výraz
- Primitivní *vs* uživatelsky definovaná funkce

## Rekurzivní funkce
- Taková funkce, která ve svém těle volá sebe samu (poznáme ze zdrojového kódu)
- Výpočetní proces je rekurzivní pokud během aplikace funkce dojde k aplikaci téže funkce (poznáme při běhu programu)
- Nutné mít *ukončovací podmínku*, jinak dojde k zacyklení
>[!info]
>Výpočetní proces je **iterativní** když na konci aplikace funkce dojde opět k aplikaci stejné funkce.

```lisp
; Neni iterativni
(defun power (a n)
	(if (= n 0)
		1
	(* a (power a (- n 1)))))

; Je iterativni
(defun fact-iter (n ir)
	(if (= n 0)
		ir
	(fact-iter (- n 1) (* ir n))))

(defun fact (n)
	(fact-iter n 1))
```

> [!info] Výpočetní proces
> **Lineárně rekurzivní** ... pokud během aplikace funkce dojde po skončení jedné její rekurzivní aplikace nenásleduje další
> 
> **Stromově rekurzivní** ... pokud alespoň jednou během aplikace funkce po skončení jedné její rekurzivní aplikace následuje další

```lisp
; stromove rekurzivni
(defun fib (n)
	(cond ((= n 0) 0)
			((= n 1) 1)
			(t (+ (fib (- n 2)) (fib (- n 1))))))
```

