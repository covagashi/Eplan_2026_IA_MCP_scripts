# GetLanguageList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~GetLanguageList.html

---

Returns the list of the languages currently saved in this [MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Syntax

**C#**



public int GetLanguageList( 

   ref LanguageList rLanguageList

)

public:

int GetLanguageList( 

   LanguageList^% rLanguageList

)


#### Parameters

*rLanguageList*
:   The existing language codes are entered in this list.

#### Return Value

Number of all languages included in this [MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).
