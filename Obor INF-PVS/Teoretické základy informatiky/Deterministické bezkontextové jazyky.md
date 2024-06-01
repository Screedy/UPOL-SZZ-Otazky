- V řadě (i praktických) aplkikací je třeba zjistit, zda daný jazyk $L$ je (a nebo není) DCFL.
- K důkazu, že je **DCFL stačí nalézt odpovídající DPDA**. Obrácená situace, kdy chceme ukázat, že $L$ není DCFL, může být složitější. Pokud by $L$ nebyl ani CFL, můžeme použít pumping lemma, ale často $L$ může být CFL, ale ne DCFL. Jelikož není známo žádné pumping lemma, které by platilo specialně do DCFL, **musíme se spolehnout jen na uzávěrové vlastnosti**. Naštěstí DCFL jsou uzavřeny na některé operace, například vůči doplňku, na něž CFL obecně uzavřeny nejsou.

- Třída DCFL **není** uzavřena vzhledem k operaci **průniku**.
- Třída deterministických bezkontextových jazyků je uzavřena vůči doplňku.
- Třída DCFL **není** uzavřena vzhledem ke **sjednocení**.

>[!Example] Příklad
>![[MacBook-2024-05-29-001400.png]]

##### Navigace
Předchozí:  [[Deterministické zásobníkové automaty]]
Následující: [[Turingův stroj, nedeterministický TS]]
Celý okruh: [[Obor INF-PVS/1. Teoretické základy informatiky]]