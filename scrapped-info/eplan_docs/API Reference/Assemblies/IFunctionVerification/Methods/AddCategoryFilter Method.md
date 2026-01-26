# AddCategoryFilter Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IFunctionVerification~AddCategoryFilter.html

---

This type of check is only performed for a certain function category.

Syntax

**C#**



void AddCategoryFilter( 

   ref FunctionCategory eCategory

)

void AddCategoryFilter( 

   FunctionCategory% eCategory

)


#### Parameters

*eCategory*
:   Function category for which this check is to be made.

Remarks

Method AddCategoryFilter is called only when registering the Add-in (it is not executed every project checking).
