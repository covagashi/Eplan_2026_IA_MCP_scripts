# CanExport Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~CanExport.html

---

Indicates whether the converter provides an export option.

Syntax

**C#**



bool CanExport( 

   Context oContext,

   ref bool bSupportsProgress

)

bool CanExport( 

   Context^ oContext,

   bool% bSupportsProgress

)


#### Parameters

*oContext*
:   Context with parameters

*bSupportsProgress*
:   Indicates whether the converter supports a progress bar.

#### Return Value

true: export is possible; false: export is not possible
