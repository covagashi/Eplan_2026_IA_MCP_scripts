# PXFProject(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Import~PXFProject(String,String).html

---

Creates a project from an imported PXF file.

Syntax

**C#**



public void PXFProject( 

   string strPXFFilePath,

   string strDestinationPath

)

public:

void PXFProject( 

   String^ strPXFFilePath,

   String^ strDestinationPath

)


#### Parameters

*strPXFFilePath*
:   Full file name of the PXF \file to import.

*strDestinationPath*
:   Destination directory. If an empty string is set to this parameter, the standard project directory will be used.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the PXF file or the destination path does not exist. |
| **SecurityException** | Missing rights for the file system. |
| **ArgumentNullException** | A null reference was set to a parameter. |
| **ApplicationException** | An internal interface necessary for the import could not be created. |
| **NotSupportedException** | A path contains invalid characters. |
| **PathTooLongException** | Invalid path. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. Please refer to the system messages for further information. |
