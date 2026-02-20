# CreateFunctionTemplatesFromMacro Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~CreateFunctionTemplatesFromMacro.html

---

Creates new function templates out of the macro that is referenced from all the parts in the parts database.

Syntax

**C#**



public void CreateFunctionTemplatesFromMacro( 

   bool overwriteExistingFunctionTemplates

)

public:

void CreateFunctionTemplatesFromMacro( 

   bool overwriteExistingFunctionTemplates

)


#### Parameters

*overwriteExistingFunctionTemplates*

Remarks

Existing function templates will be removed before, if overwriteExistingFunctionTemplates is set true. Otherwise that part will stay unchanged.
