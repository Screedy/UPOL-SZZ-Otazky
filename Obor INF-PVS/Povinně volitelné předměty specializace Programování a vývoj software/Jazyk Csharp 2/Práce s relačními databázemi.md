## Co je databáze?
- Databáze je perzistentní úložiště dat. Umožňuje efektivní ukládání, vyhledávání a manipulaci s daty.
- Typicky obsahuje **tabulky**, kde **řádky** odpovídají záznamům a **sloupce** jednotlivým vlastnostem.
- Pro práci s daty se používá dotazovací jazyk **SQL (Structured Query Language)**.
- V jazyce C# se připojujeme k databázi pomocí **connection stringu** a třídy `SqlConnection`.
## SQL – základní dotazy

#### Výběr dat
```sql
SELECT sloupec1, sloupec2 FROM tabulka WHERE podmínka;
SELECT * FROM students WHERE year = 3;
```

#### Řazení
```sql
SELECT * FROM students ORDER BY surname DESC;
```

#### Vložení dat
```sql
INSERT INTO students (name, surname) VALUES ('Petr', 'Novák');
```

#### Úprava dat
```sql
UPDATE students SET year = 3 WHERE surname = 'Novák';
```

#### Smazání dat
```sql
DELETE FROM students WHERE id = 10;
```

## Připojení k databázi v C\#

- Pro připojení k databázi z C# používáme knihovnu `System.Data.SqlClient`.
#### Základní postup:
```csharp
using (SqlConnection conn = new SqlConnection(connectionString)) {
    conn.Open();
    SqlCommand cmd = new SqlCommand("SELECT * FROM students;", conn);
    using (SqlDataReader reader = cmd.ExecuteReader()) {
        while (reader.Read()) {
            Console.WriteLine($"{reader[0]}, {reader[1]}");
        }
    }
}
```

#### Získání `connectionString`:
Najdeme v *Properties* připojené databáze ve Visual Studiu nebo si jej vygenerujeme ručně.
## Parametrizované dotazy
- Nikdy nevkládat data od uživatele přímo do SQL řetězce – hrozí **SQL Injection**!

```csharp
// !! SPATNE
SqlCommand cmd = new SqlCommand($"SELECT * FROM students WHERE name = '{name}'", conn);

// SPRAVNE
SqlCommand cmd = new SqlCommand("SELECT * FROM students WHERE name = @name", conn);
cmd.Parameters.Add(new SqlParameter("name", name));
```

- Používáme `@parametr` a metodu `Add` k ochraně dotazu.
- Automaticky se ošetří speciální znaky a formát.

## Psaní a vykonání změn – `ExecuteNonQuery`
- Pokud potřebujeme **vložit**, **smazat** nebo **upravit** data, použijeme `ExecuteNonQuery`.
```csharp
SqlCommand cmd = new SqlCommand("INSERT INTO students (id, name) VALUES (@id, @name);", conn);
cmd.Parameters.AddWithValue("id", 1);
cmd.Parameters.AddWithValue("name", "Tomáš");
int affected = cmd.ExecuteNonQuery();
Console.WriteLine($"Změněno řádků: {affected}");
```
- Metoda vrací počet ovlivněných řádků.

---
## Shrnutí
- SQL umožňuje dotazovat se, měnit a mazat data v relační databázi.
- C# poskytuje plnou podporu přes `SqlConnection`, `SqlCommand`, `SqlDataReader`.
- **Používej vždy parametrizované dotazy** – chrání proti chybám a útokům.
- Pro změny používej `ExecuteNonQuery()`, pro čtení `ExecuteReader()`.
#### Důležité třídy v C# pro práci s databází:
| Třída             | Účel                                       |
|------------------|---------------------------------------------|
| `SqlConnection`   | Navázání spojení s databází                 |
| `SqlCommand`      | Reprezentace SQL dotazu                     |
| `SqlDataReader`   | Čtení výsledků dotazu                       |
| `SqlParameter`    | Předání hodnot bezpečně do SQL dotazu       |
