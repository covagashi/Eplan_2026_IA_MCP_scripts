# AddKeyword(MultiLangString,LanguageList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~AddKeyword(MultiLangString,LanguageList).html

---

Adds keywords with texts in specified languages to the translation database.

Syntax

**C#**



public bool AddKeyword( 

   MultiLangString oTexts,

   LanguageList oLangs

)

public:

bool AddKeyword( 

   MultiLangString^ oTexts,

   LanguageList^ oLangs

)


#### Parameters

*oTexts*
:   Keyword to add as multilangual string.

*oLangs*
:   Specific languages used to select from text and to add to the database.

#### Return Value

True if operation was sucessfully completed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
