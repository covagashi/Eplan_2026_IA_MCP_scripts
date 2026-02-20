# EditKeyword(String,Language,MultiLangString,LanguageList,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1729.html

---

Edits keyword

Syntax

**C#**



public bool EditKeyword( 

   string strSearchedText,

   ISOCode.Language eSearchedLang,

   MultiLangString oText,

   LanguageList oLangs,

   string strComment

)

public:

bool EditKeyword( 

   String^ strSearchedText,

   ISOCode.Language eSearchedLang,

   MultiLangString^ oText,

   LanguageList^ oLangs,

   String^ strComment

)


#### Parameters

*strSearchedText*
:   Text to search for.

*eSearchedLang*
:   Language used for searching.

*oText*
:   Keyword inserted.

*oLangs*
:   Only texts of these languages will be added.

*strComment*
:   Comment for the keyword

#### Return Value

True if operation was sucessfully completed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |
