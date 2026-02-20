# ImportPartsList(String,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~ImportPartsList(String,String,String).html

---

Method to import a parts list file into the project.

Syntax

**C#**



public void ImportPartsList( 

   string strFullLinkFileName,

   string strImportFilePath,

   string strConverter

)

public:

void ImportPartsList( 

   String^ strFullLinkFileName,

   String^ strImportFilePath,

   String^ strConverter

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project, into which the parts (Articles) will be imported.

*strImportFilePath*
:   Full file name of the parts list file to import.

*strConverter*
:   Converter long name [XPamImport](XPamImport.html) converters

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid \arguments. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during import. |
| **\Exceptions\:\:InvalidConverter** | Thrown when given parameter `strConverter` isn't valid converter or such conversion doesn't exist at all. |
