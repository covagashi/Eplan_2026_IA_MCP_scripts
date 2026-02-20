# XPamConvertPartDatabaseToArticleDatabaseAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPamConvertPartDatabaseToArticleDatabaseAction.html

---

```
  Converts parts databases from EPLAN Version V2.9 to Version V2022.

```

| Parameter | Description |
| --- | --- |
| ``` OldDatabase
 ``` | ``` Old database name (full qualified with extension "MDB") or SQL connection string
 ``` |
| ``` NewDatabase
 ``` | ``` New database name (full qualified with extension "alk") or SQL connection string
 ``` |

**Remarks**

```
 When no parameters are specified, a dialog for selecting the databases is displayed.

```

**Example**

```
    XPamConvertPartDatabaseToArticleDatabaseAction

         Parts data conversion for an Access database:

          XPamConvertPartDatabaseToArticleDatabaseAction

                /OldDatabase:"C:\<DataDirectory>\Article\EPLAN\ESS_part001.mdb"

                /NewDatabase:"C:\<DataDirectory>\Article\EPLAN\ESS_part001.alk"

         Parts data conversion for SQL databases:

    XPamConvertPartDatabaseToArticleDatabaseAction

                /OldDatabase:"SQLEXPRESS|parts_old|0"

                /NewDatabase:"SQLEXPRESS|parts_2022|0"

    XPamConvertPartDatabaseToArticleDatabaseAction

                /OldDatabase:"SQL2019|parts_old|2|Mustermann|12345"

                /NewDatabase:"SQL2019|parts_2022|2|Mustermann|12345"

```