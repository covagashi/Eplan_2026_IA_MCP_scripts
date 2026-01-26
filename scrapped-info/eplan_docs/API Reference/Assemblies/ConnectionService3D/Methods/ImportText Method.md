# ImportText Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D~ImportText.html

---

Imports the Connection3Ds from a text file into the given project using a scheme.

Syntax

**C#**



public Connection3D[] ImportText( 

   Project oProject,

   string strImportFilePath,

   string strSchemeName,

   string strSeparator,

   int nHeadLinePos,

   int nHeadLineCount,

   FunctionDefinition oFuncDef,

   string strIntern,

   string strExtern,

   ConnectionService3D.ImportMode eMode

)

public:

array<Connection3D^>^ ImportText( 

   Project^ oProject,

   String^ strImportFilePath,

   String^ strSchemeName,

   String^ strSeparator,

   int nHeadLinePos,

   int nHeadLineCount,

   FunctionDefinition^ oFuncDef,

   String^ strIntern,

   String^ strExtern,

   ConnectionService3D.ImportMode eMode

)


#### Parameters

*oProject*
:   Destination project.

*strImportFilePath*
:   Filename of the import file.

*strSchemeName*
:   Name of the import scheme. If the scheme name is empty, the last used scheme of the project will be used.

*strSeparator*
:   Which character is used as separator.

*nHeadLinePos*
:   The position of the head line that will be used to asssign the column values at the import.

*nHeadLineCount*
:   The count of head lines that will be skipped at the import.

*oFuncDef*
:   Default Function Definition

*strIntern*
:   Designation for 'internal'.

*strExtern*
:   Designation for 'external'.

*eMode*
:   The import mode can be a combination of the XPProcImportMode enum and controls the import action (in)(optional) eCreateMode = 1: The import create only missing device tags eChangeMode = 2: The import change only existing device tags eDeleteMode = 4: The import delete only unnecessary existing device tags

#### Return Value

An array of imported Connections3D.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. Please refer to the exception message. |

Remarks

If new scheme is not present, the old import method is used.
