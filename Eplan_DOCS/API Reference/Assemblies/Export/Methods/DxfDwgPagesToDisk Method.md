# DxfDwgPagesToDisk Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~DxfDwgPagesToDisk.html

---

Exports pages of a project as a DXF/DWG file. Export settings are taken from the scheme passed in the 'sScheme' parameter

Syntax

**C#**



public void DxfDwgPagesToDisk( 

   Page[] pages,

   string sScheme,

   string sTargetDir,

   string sLanguage

)

public:

void DxfDwgPagesToDisk( 

   array<Page^>^ pages,

   String^ sScheme,

   String^ sTargetDir,

   String^ sLanguage

)


#### Parameters

*pages*
:   An array of pages to be exported.

*sScheme*
:   Settings scheme to use.

*sTargetDir*
:   The output directory.

*sLanguage*
:   Specifies the language to translate the project into before the export.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments, for \example a wrong scheme. |
| **UnauthorizedAccessException** | No user rights to create files on the \file system. |
| **ApplicationException** | The internal interface for exporting could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |
| **InvalidOperationException** | Thrown when `sLanguage` is not available in project translation. |

Remarks

This method uses a scheme from "USER.DXF.SCHEMES". All necessary settings are set in this scheme. If you pass an empty string to "sScheme", the last used scheme will be used which is currently set in GUI. If no scheme does exist with the given scheme name, a BaseException will be thrown. Depending on the scheme settings, exported pages' names can be prefixed to create a folder-like structure. Options available in the scheme for sub-folder generation are: none, from page tree, from page properties.
