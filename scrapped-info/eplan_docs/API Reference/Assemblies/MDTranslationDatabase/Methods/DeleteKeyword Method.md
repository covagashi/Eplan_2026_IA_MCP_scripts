# DeleteKeyword Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~DeleteKeyword.html

---

Deletes keyword.

Syntax

**C#**



public bool DeleteKeyword( 

   string strText,

   ISOCode.Language eLang

)

public:

bool DeleteKeyword( 

   String^ strText,

   ISOCode.Language eLang

)


#### Parameters

*strText*
:   Text to search for.

*eLang*
:   Language used for searching.

#### Return Value

True if operation was sucessfully completed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
