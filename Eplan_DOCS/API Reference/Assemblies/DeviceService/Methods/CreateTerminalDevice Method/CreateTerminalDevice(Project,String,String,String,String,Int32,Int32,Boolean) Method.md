# CreateTerminalDevice(Project,String,String,String,String,Int32,Int32,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1331.html

---

This function imports devices from an text file into a given project.

Syntax

**C#**



public StorableObject[] ImportDevicesText( 

   Project oProject,

   string strImportFilePath,

   string strSchemeName,

   string strSeparator,

   int nHeadLinePos,

   int nHeadLineCount,

   bool bAdjustDialog

)

public:

array<StorableObject^>^ ImportDevicesText( 

   Project^ oProject,

   String^ strImportFilePath,

   String^ strSchemeName,

   String^ strSeparator,

   int nHeadLinePos,

   int nHeadLineCount,

   bool bAdjustDialog

)


#### Parameters

*oProject*
:   Project into which the devices will be imported.

*strImportFilePath*
:   Full file name of the devices file to import.

*strSchemeName*
:   Name of the import scheme.

*strSeparator*
:   Char to separate column values of the text.

*nHeadLinePos*
:   The position of the head line that will be used to asssign the column values at the import.

*nHeadLineCount*
:   The count of head lines that will be skipped at the import.

*bAdjustDialog*
:   Additional dialog for adjust devices import.

#### Return Value

Result is returned as array of StorableObjects.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing devices could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import of devices. Please refer to the exception message. |
