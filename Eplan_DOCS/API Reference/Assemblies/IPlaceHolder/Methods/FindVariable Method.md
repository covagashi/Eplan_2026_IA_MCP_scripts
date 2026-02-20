# FindVariable Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~FindVariable.html

---

Finds a variable, specified by its name.

Syntax

**C#**



int FindVariable( 

   string strVarName

)

int FindVariable( 

   String^ strVarName

)


#### Parameters

*strVarName*
:   Name of the variable to search for.

#### Return Value

The index of the variable or -1, if the variable was not found.
