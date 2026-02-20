# ExportPartsList(String,String,Format) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~ExportPartsList(String,String,Format).html

---

Method to export the parts list of a project to an XML/CSV \file.

Syntax

**C#**



public void ExportPartsList( 

   string strFullLinkFileName,

   string strExportFilePath,

   PartsService.Format fileFormat

)

public:

void ExportPartsList( 

   String^ strFullLinkFileName,

   String^ strExportFilePath,

   PartsService.Format fileFormat

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project of which the parts list will be exported.

*strExportFilePath*
:   Path and file name of the export file. The extension is added automatically.

*fileFormat*
:   Parameter for setting the predefined export formats XML and CSV. The enumeration [PartsService.Format](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService+Format.html) defines the necessary values. If an invalid value is set, the file will be exported as XML.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid \arguments. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurred during export. |
| **ApplicationException** | \Internal action for exporting the parts list was not found. (Missing rights?). |
| **\Exceptions\:\:InvalidConverter** | Thrown when given parameter `fileFormat` isn't valid converter or such conversion doesn't exist at all. |
