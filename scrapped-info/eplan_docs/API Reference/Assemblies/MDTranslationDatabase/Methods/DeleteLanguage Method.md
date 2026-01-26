# DeleteLanguage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~DeleteLanguage.html

---

Deletes translation database language.

Syntax

**C#**



public bool DeleteLanguage( 

   ISOCode.Language eLang

)

public:

bool DeleteLanguage( 

   ISOCode.Language eLang

)


#### Parameters

*eLang*
:   Language to delete.

#### Return Value

True if operation was sucessfully completed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
