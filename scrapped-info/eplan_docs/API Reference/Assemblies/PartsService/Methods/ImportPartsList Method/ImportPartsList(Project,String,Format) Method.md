# ImportPartsList(Project,String,Format) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~ImportPartsList(Project,String,Format).html

---

Method to import a parts list file into the project.

Syntax

**C#**



public void ImportPartsList( 

   Project oProject,

   string strImportFilePath,

   PartsService.Format fileformat

)

public:

void ImportPartsList( 

   Project^ oProject,

   String^ strImportFilePath,

   PartsService.Format fileformat

)


#### Parameters

*oProject*
:   Project, into which the parts (Articles) will be imported.

*strImportFilePath*
:   Full file name of the parts list file to import.

*fileformat*
:   Parameter for setting the predefined file formats XML and CSV. The enumeration [PartsService.Format](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService+Format.html) defines the necessary values. If an invalid value is set, the file is expected to be XML.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid \arguments. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during import. |
| **\Exceptions\:\:InvalidConverter** | Thrown when given parameter `fileformat` isn't valid converter or such conversion doesn't exist at all. |
