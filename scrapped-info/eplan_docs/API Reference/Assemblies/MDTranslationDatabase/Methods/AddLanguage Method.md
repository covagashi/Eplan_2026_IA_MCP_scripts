# AddLanguage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~AddLanguage.html

---

Adds new translation database language.

Syntax

**C#**



public bool AddLanguage( 

   ISOCode.Language eLang

)

public:

bool AddLanguage( 

   ISOCode.Language eLang

)


#### Parameters

*eLang*
:   New language.

#### Return Value

True if operation was sucessfully completed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
