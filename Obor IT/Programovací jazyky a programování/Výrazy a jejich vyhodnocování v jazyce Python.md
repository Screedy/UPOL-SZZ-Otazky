- Výrazy (expressions) jsou kombinace hodnot a operátorů, které Python vyhodnocuje s cílem získat novou hodnotu. Například `3 * (5 + 2)`.

## Typy operátorů
- **Aritmetické operátory**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Relační operátory** (porovnávají hodnoty): `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logické operátory**: `and`, `or`, `not`
- **Bitové operátory**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (bitový posun vlevo), `>>` (bitový posun vpravo)

## Priorita operátorů
- Python vyhodnocuje výrazy na základě priority operátorů.
- `*` a `/` mají vyšší prioritu než `+` a `-`. Tedy `*` a `/` bude vyhodnoceno dříve.
- Pomocí závorek `()` můžeme změnit pořadí vyhodnocování operací.

## Vyhodnocování výrazů
- Když Python narazí na výraz, začne jej vyhodnocovat od nejvyšší priority operátoru k nejnižší.
- Pokud narazí na dva operátory se stejnou prioritou, vyhodnocuje se zleva doprava (s výjimkou exponenciály, která se vyhodnocuje zprava doleva).

## Vyhodnocení podmínek
- Python umožňuje vyhodnocování podmínek pomocí konstrukcí jako `if`-`else` výrazy. Tyto výrazy umožňují rozhodnutí na základě logických podmínek.


##### Navigace
Předchozí:  [[Řízení vykonávání programu v jazyce Python - bloky, cykly, větvení, funkce]]
Následující: [[Základní datové typy v jazyce Python]]
Celý okruh: [[3. Programovací jazyky a programování]]