- Konečné automaty nacházejí velmi široké uplatnění v technické praxi. Z hlediska efektivity a nákladnosti implementace je důležité, aby počet stavů byl pokud možno co nejmenší. Přirozeným problémem je proto konstrukce minimálního automatu, který rozpoznává daný regulární jazyk $L$.
- Minimální automat lze sestrojit poměrně jednoduchým způsobem - stačí mít k dispozici nějaký konečný automat, který rozpoznává $L$. Minimální automat pak obdržíme ztotožněním některých jeho stavů.

## Nerozlišitelnost stavů
- Stavy $p, q \in Q$ v DFA A nazveme **nerozlišitelné**, právě když pro $\forall w \in \Sigma^{*}$ platí $$\hat{\delta}(p,w) \in F \Leftrightarrow \hat{\delta}(q,w) \in F$$
- **Nerozlišitelnost stavů** "$\equiv$" je binární relace na množině stavů $Q$, která je navíc ekvivalence
	- Pro každé $p,q,r \in Q$ platí
		- **reflexivní:** $p$ je **nerozlišitelné** s $p$
		- **symetrická**: když $p$ je **nerozlišitelné** se $q$, tak $q$ je **nerozlišitelné** s $p$
		- **tranzitivní**: když $p$ je **nerozlišitelné** s $q$ a $q$ je **nerozlišitelné** s $r$, pak $p$ je **nerozlišitelné** s $r$

- Pro stavy výsledného minimálního DFA $A_{m}$ platí, že jsou to třídy $\equiv$ a množina stavů $A_{m}$ tvoří rozklad $Q$ podle $\equiv$ (předpokládáme, že $A$ nemá nedosažitelné stavy)

### Postup
- Minimální DFA $A_{m}$ lze vypočítat pomocí tabulky dvojic stavů, která zachycuje $\equiv$
1. Nejprve označíme všechny dvojice, které obsahují pouze jeden koncový stav
	- (Ty jsme schopni rozlišit hned na začátku)
2. Postupně označujeme dvojice $<p,q>$, pro které existuje $a \in \Sigma$ takové, že dvojice $<\delta(p,a), \delta(q,a)>$ už je označena
	- Tento krok opakujeme dokud ještě lze označit nějakou další dvojici
3. Neoznačené dvojice nejsme schopni rozlišit a pomocí tranzitivního uzávěru vypočítáme celou odpovídající třídu $\equiv$, kterou v $A_{m}$ sloučíme do jednoho stavu

>[!Example] Příklad
>- minimalizujte DFA zadaný tabulkou ![[MacBook-2024-05-26-001348.png| 400]]
>1. Označím dvojice $<p,q>$ takové, že $(p \in F \land q \notin F) \lor (p \notin F \land q \in F)$ ![[MacBook-2024-05-26-001349.png| 400]]
>2. **Můj postup:** Kouknu na volný místa (např. u dvojice $<1,6>$) a kouknu do tabulky, jaké dvojice by museli být označeny, abych mohl označit danou dvojici (tabulka říká buď $<2,6>$ nebo $<3,6>$. A zkontroluju jestli taková není už zaškrtlá (dvojici $<2,6>$ nemáme, ale dvojici $<3,6>$ máme zaškrtlou, takže můžu zašktnout i $<1,6>$). Když pro nějakou ještě nemám zašktnutou dvojici, tak počkám na konec, může se ještě objevit.)
>   ![[MacBook-2024-05-26-001350.png| 400]]
>3. ![[MacBook-2024-05-26-001351.png| 400]]
>4. ![[MacBook-2024-05-26-001352.png| 400]]
>5. ![[MacBook-2024-05-26-001353.png| 400]]
>6. Dvojice $<1,2>$ a $<3,4>$ jsou pro nás **nerozlišitelné**. Tedy výsledný automat je:![[MacBook-2024-05-26-001354.png| 400]]

##### Navigace
Předchozí:  [[Regulární výrazy, automaty s e-přechody]]
Následující: [[Pumping lemma]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]