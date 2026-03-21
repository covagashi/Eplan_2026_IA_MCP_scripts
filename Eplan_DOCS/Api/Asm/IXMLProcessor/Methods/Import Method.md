# Import Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~Import.html

---

Conversion from sImportFile to sXmlFile. sXmlFile might be passed as "". In this case, the converter must set a file name. EContext may point to an EProgress object to support a progress bar. Returns true if successful.

Syntax

**C#**



bool Import( 

   string strInputFile,

   string strXmlFile,

   Context oContext

)

bool Import( 

   String^ strInputFile,

   String^ strXmlFile,

   Context^ oContext

)


#### Parameters

*strInputFile*
:   Input file

*strXmlFile*
:   Output file

*oContext*
:   Context with parameters
