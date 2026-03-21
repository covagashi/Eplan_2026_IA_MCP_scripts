# ImportDirect Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor~ImportDirect.html

---

Imports the file to the system EContext may point to an EProgress object to support a progress bar. Returns true if successful.

Syntax

**C#**



bool ImportDirect( 

   string strInputFile,

   Context oContext

)

bool ImportDirect( 

   String^ strInputFile,

   Context^ oContext

)


#### Parameters

*strInputFile*
:   Input file

*oContext*
:   Context with parameters
