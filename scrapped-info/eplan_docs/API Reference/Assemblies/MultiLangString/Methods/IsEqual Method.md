# IsEqual Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~IsEqual.html

---

Compares every string in every language. If a string is different in one language, then == returns FALSE. If an language string exists in one of the MultiLangStrings but not in the others, this function returns FALSE even if the language string is empty.

Syntax

**C#**



public bool IsEqual( 

   MultiLangString otherVal

)

public:

bool IsEqual( 

   MultiLangString^ otherVal

)


#### Parameters

*otherVal*
:   MultiLangString to be compared.

#### Return Value

True: Values are identical.

False: Values are not identical.
