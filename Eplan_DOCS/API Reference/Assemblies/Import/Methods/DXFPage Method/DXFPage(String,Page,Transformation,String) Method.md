# DXFPage(String,Page,Transformation,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Import~DXFPage(String,Page,Transformation,String).html

---

Imports a DXF or DWG file into an existing page. You have the possibility to move and scale the drawings.

Syntax

**C#**



public void DXFPage( 

   string strDXFFileName,

   Page oPage,

   Transformation oTransformation,

   string strScheme

)

public:

void DXFPage( 

   String^ strDXFFileName,

   Page^ oPage,

   Transformation^ oTransformation,

   String^ strScheme

)


#### Parameters

*strDXFFileName*
:   Full file name of the CAD drawing to be imported.

*oPage*
:   Page into which the CAD drawing will be placed.

*oTransformation*
:   Information about the scaling and the insertion point on the page.

*strScheme*
:   Name of the scheme used for the import.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **SecurityException** | Access rights to the \file system are missing. |
| **ArgumentNullException** | null was passed to a parameter. |
| **ApplicationException** | \Internal interface necessary for the import cannot be created. |
| **NotSupportedException** | An argument contained invalid characters, e.g. a path contained a '\:'. |
| **PathTooLongException** | Invalid path. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. Please refer to the exception message. |

Remarks

This method uses a scheme from "USER.DXF.SCHEMES". All necessary settings for DXF import are set in this scheme. If you pass an empty string to "strScheme", the last used scheme will be used which is currently set in GUI. If no scheme does exist with the given scheme name, an exception will be thrown.
