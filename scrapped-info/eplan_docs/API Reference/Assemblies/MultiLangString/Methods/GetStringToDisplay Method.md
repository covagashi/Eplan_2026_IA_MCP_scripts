# GetStringToDisplay Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~GetStringToDisplay.html

---

Returns the string that is to be displayed in accordance with the passed language. This may be the string saved for this language or, if there is no such string, a language-independent string.

Syntax

**C#**



public string GetStringToDisplay( 

   ISOCode.Language lang

)

public:

String^ GetStringToDisplay( 

   ISOCode.Language lang

)


#### Parameters

*lang*
:   Language to be returned

#### Return Value

Returns the string in the requested language
