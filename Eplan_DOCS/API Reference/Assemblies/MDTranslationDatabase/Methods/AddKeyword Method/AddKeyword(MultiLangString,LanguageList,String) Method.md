# AddKeyword(MultiLangString,LanguageList,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1728.html

---

Adds keywords with texts in specified languages to the translation database.

Syntax

**C#**



public bool AddKeyword( 

   MultiLangString oText,

   LanguageList oLangs,

   string strComment

)

public:

bool AddKeyword( 

   MultiLangString^ oText,

   LanguageList^ oLangs,

   String^ strComment

)


#### Parameters

*oText*
:   Keyword to add as multilangual string.

*oLangs*
:   Specific languages used to select from text and to add to the database.

*strComment*
:   Comment to add as tring.

#### Return Value

True if operation was sucessfully completed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
