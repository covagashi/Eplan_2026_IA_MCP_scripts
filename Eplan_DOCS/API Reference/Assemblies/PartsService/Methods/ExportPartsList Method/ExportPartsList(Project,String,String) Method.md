# ExportPartsList(Project,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~ExportPartsList(Project,String,String).html

---

Method to export the parts list of a project to an XML/CSV \file or as a custom format, defined by an existing XMLConverter.

Syntax

**C#**



public void ExportPartsList( 

   Project oProject,

   string strExportFilePath,

   string strConverter

)

public:

void ExportPartsList( 

   Project^ oProject,

   String^ strExportFilePath,

   String^ strConverter

)


#### Parameters

*oProject*
:   Project of which the parts list will be exported.

*strExportFilePath*
:   Path and file name of the export file. The extension is added automatically.

*strConverter*
:   Converter long name, see [XPamExport](XPamExport.html) converters

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid \arguments. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurred during export. |
| **ApplicationException** | \Internal action for exporting the parts list was not found. (Missing rights?). |
| **\Exceptions\:\:InvalidConverter** | Thrown when given parameter `strConverter` isn't valid converter or such conversion doesn't exist at all. |
