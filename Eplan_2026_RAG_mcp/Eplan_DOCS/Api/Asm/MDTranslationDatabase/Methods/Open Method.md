# Open Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~Open.html

---

Opens translation database using user settings.

Syntax

**C#**



public bool Open( 

   bool bReadOnly

)

public:

bool Open( 

   bool bReadOnly

)


#### Parameters

*bReadOnly*
:   True if database is opened in readonly mode.

#### Return Value

True if operation was sucessfully completed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
