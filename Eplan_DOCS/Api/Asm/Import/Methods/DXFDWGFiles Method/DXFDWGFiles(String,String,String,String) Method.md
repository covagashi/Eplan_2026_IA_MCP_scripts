# DXFDWGFiles(String,String,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Import~DXFDWGFiles(String,String,String,String).html

---

Creates an EPLAN macro from a DXF / DWG file.

Syntax

**C#**



public void DXFDWGFiles( 

   string strFullLinkFileName,

   string strDXFMacroDir,

   string strDestinationDir,

   string strScheme

)

public:

void DXFDWGFiles( 

   String^ strFullLinkFileName,

   String^ strDXFMacroDir,

   String^ strDestinationDir,

   String^ strScheme

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project for which the macros will be created. The macros will use the layer information from this project.

*strDXFMacroDir*
:   Directory from which the DXF / DWG files are imported.

*strDestinationDir*
:   Directory, to which the created macro files will be written.

*strScheme*
:   Scheme used for importing DXF / DWG files.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **SecurityException** | Access rights to the \file system are missing. |
| **ArgumentNullException** | null was passed to a parameter. |
| **NotSupportedException** | An argument contained invalid characters, e.g. a path contained a '\:'. |
| **PathTooLongException** | Invalid path. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. Please read the exception message. |

Remarks

This method uses a scheme from "USER.DXF.SCHEMES". All necessary settings are set in this scheme. If you pass an empty string to "strScheme", the last used scheme will be used which is currently set in GUI. If no scheme does exist with the given scheme name, an exception will be thrown.
