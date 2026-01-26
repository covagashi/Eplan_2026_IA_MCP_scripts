# FindKeyword Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~FindKeyword.html

---

Finds keyword.

Syntax

**C#**



public bool FindKeyword( 

   ISOCode.Language eLang,

   ref MultiLangString oTexts,

   ref string strComment

)

public:

bool FindKeyword( 

   ISOCode.Language eLang,

   MultiLangString^% oTexts,

   String^% strComment

)


#### Parameters

*eLang*
:   Language used for searching.

*oTexts*
:   Text to search for.

*strComment*
:   Comment for a keyword.

#### Return Value

True if operation was sucessfully completed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
