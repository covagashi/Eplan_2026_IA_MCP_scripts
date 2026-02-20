# TranslateDatabase Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslateDatabase.html

---

Returns or sets the complete filename of the current translate database or connection string if SQL connection is selected.

Syntax

**C#**



public string TranslateDatabase {get; set;}

public:

property String^ TranslateDatabase {

   String^ get();

   void set (    String^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments (strTranslateDatabase is not valid or file does not exist). |

Remarks

The complete filename can contain pathmap variables. Note that password value in connection string is encrypted so You can use it when you don't have clear password (not encrypted). If You want to set translate database for SQL connection and you have clear password use [SetSQLServerConnectionParameters](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~SetSQLServerConnectionParameters.html)
