# IsReadOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~IsReadOnly.html

---

Returns true if database is opened in readonly mode.

Syntax

**C#**



public bool IsReadOnly {get;}

public:

property bool IsReadOnly {

   bool get();

}


#### Property Value

True if database is opened in readonly mode.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
