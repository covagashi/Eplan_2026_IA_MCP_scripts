# PXFProject(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~PXFProject(String,String).html

---

Exports a project in PXF format.

Syntax

**C#**



public void PXFProject( 

   string strFullLinkFileName,

   string strExportFilePath

)

public:

void PXFProject( 

   String^ strFullLinkFileName,

   String^ strExportFilePath

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project to be exported.

*strExportFilePath*
:   Path and file name of the \file to be created. The \file name extension is added automatically.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid \arguments. |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **UnauthorizedAccessException** | No user rights to create files on the \file system. |
| **ApplicationException** | The internal interface for PXF export could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |

Remarks

Master data will also be exported. Connections however will be ignored.
