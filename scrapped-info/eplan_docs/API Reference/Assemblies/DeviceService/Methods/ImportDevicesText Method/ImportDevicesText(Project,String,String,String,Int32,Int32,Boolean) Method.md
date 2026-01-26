# ImportDevicesText(Project,String,String,String,Int32,Int32,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1332.html

---

This function imports devices from a text file into a given project.

Syntax

**C#**



public StorableObject[] ImportDevicesText( 

   Project oProject,

   string strImportFilePath,

   string strSchemeName,

   string strSeparator,

   int nHeadLinePos,

   int nHeadLineCount,

   FunctionDefinition oFuncDef,

   FunctionDefinition oTermFuncDef,

   DeviceService.ImportMode eMode

)

public:

array<StorableObject^>^ ImportDevicesText( 

   Project^ oProject,

   String^ strImportFilePath,

   String^ strSchemeName,

   String^ strSeparator,

   int nHeadLinePos,

   int nHeadLineCount,

   FunctionDefinition^ oFuncDef,

   FunctionDefinition^ oTermFuncDef,

   DeviceService.ImportMode eMode

)


#### Parameters

*oProject*
:   Project into which the devices will be imported.

*strImportFilePath*
:   Full file name of the devices file to import.

*strSchemeName*
:   Name of the import scheme. If the scheme name is empty, the last used scheme of the project will be used.

*strSeparator*
:   Char to separate column values of the text.

*nHeadLinePos*
:   The position of the head line that will be used to assign the column values at the import.

*nHeadLineCount*
:   The count of head lines that will be skipped at the import.

*oFuncDef*
:   Default Function Definition

*oTermFuncDef*
:   Default Terminal Function Definition

*eMode*
:   The import mode can be a combination of the XPProcImportMode enum and controls the import action (input parameter, optional):  
    '¢ eCreateMode = 1: The import create only missing device tags  
    '¢ eChangeMode = 2: The import change only existing device tags  
    '¢ eDeleteMode = 4: The import delete only unnecessary existing device tags

#### Return Value

Result is returned as an array of StorableObjects.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing devices could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import of devices. Please refer to the exception message. |

Remarks

If new scheme is not present, the old import method is used.
