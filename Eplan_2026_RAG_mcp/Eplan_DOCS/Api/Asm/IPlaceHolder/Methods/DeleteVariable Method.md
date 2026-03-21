# DeleteVariable Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~DeleteVariable.html

---

Deletes a variable.

Syntax

**C#**



void DeleteVariable( 

   string strVarName

)

void DeleteVariable( 

   String^ strVarName

)


#### Parameters

*strVarName*
:   Name of a variable.

Remarks

After deleting a variable, the indices of the existing variables are invalid and have to determined again using FindRecord.
