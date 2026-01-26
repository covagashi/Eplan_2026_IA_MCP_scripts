# ImportPartsList(Project,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~ImportPartsList(Project,String,String).html

---

Method to import a parts list file into the project. The import file may be an XML/CSV file or may have a custom format, defined by an existing XML import converter.

Syntax

**C#**



public void ImportPartsList( 

   Project oProject,

   string strImportFilePath,

   string strConverter

)

public:

void ImportPartsList( 

   Project^ oProject,

   String^ strImportFilePath,

   String^ strConverter

)


#### Parameters

*oProject*
:   Project, into which the parts (Articles) will be imported.

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
