"Události v objektovém programování" jsou obvykle způsoby, jak třídy a objekty reagují na události nebo změny ve svém okolí. Události mohou být jakékoli události, které ovlivňují stav objektu nebo aplikace jako celek, jako je například kliknutí uživatele na tlačítko, načtení souboru nebo změna stavu síťového připojení.

V jazycích jako je C#, Java nebo JavaScript jsou události implementovány pomocí konceptů jako jsou událostní smyčky (event loops) a posluchači událostí (event listeners). Třídy nebo objekty mohou vydávat (trigger) události, na které mohou ostatní části kódu reagovat registrací posluchačů pro tyto události. Tímto způsobem může aplikace reagovat na uživatelské vstupy, změny stavu nebo jiné události a provádět odpovídající akce.

Použití událostí v objektovém programování může zvýšit modularitu a flexibilitu kódu tím, že umožní oddělit kód, který vydává události, od kódu, který na ně reaguje. To umožňuje snadnější údržbu a rozšíření aplikace v budoucnosti.

## Příklad

```Python
import tkinter as tk

def button_click():
    label.config(text="Tlačítko bylo stisknuto!")

# Vytvoření hlavního okna
root = tk.Tk()

# Vytvoření popisku
label = tk.Label(root, text="Stiskněte tlačítko")
label.pack()

# Vytvoření tlačítka
button = tk.Button(root, text="Stiskni mě", command=button_click)
button.pack()

# Spuštění hlavní smyčky událostí
root.mainloop()
```

1. **Event Loop (Událostní smyčka)**: Událostní smyčka je mechanismus, který neustále kontroluje události a volá odpovídající obslužné funkce (event handlers) pro tyto události. Je to vlastně nekonečná smyčka, která čeká na výskyt událostí a poté je zpracovává. V GUI aplikacích může být událostní smyčka zodpovědná za sledování uživatelských interakcí, jako jsou kliknutí myší nebo stisknutí kláves. V příkladě se spouští hlavní smyčka příkazem `root.mainloop`

2. **Event Listeners (Posluchači událostí)**: Posluchači událostí jsou funkce nebo objekty, které jsou registrovány k naslouchání (poslouchání) určitým událostem. Když je spuštěna událost, posluchači jsou aktivováni a provedou odpovídající kód reakce. V našem příkladu s knihovnou `tkinter` by funkce `button_click()` byla posluchačem události kliknutí na tlačítko.

3. **Trigger (Spouštěč)**: Spouštěč je část kódu, která vyvolává (trigger) určitou událost. To může být například kliknutí na tlačítko, načtení souboru, dokončení časovače apod. Když je událost vyvolána, událostní smyčka ji zaznamená a spustí příslušné posluchače událostí. V našem příkladu by kliknutí na tlačítko bylo triggerem události, která spustí funkci `button_click()`.

##### Navigace
Předchozí:  [[Principy objektového programování - zapouzdření, polymorfismus a dědičnost]]
Následující: [[Funkce vyšších řádů - mapování, filtrování, redukce a anonymní funkce]]
Celý okruh: [[3. Programovací jazyky a programování]]