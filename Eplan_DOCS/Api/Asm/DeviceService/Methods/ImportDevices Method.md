# ImportDevices Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~ImportDevices.html

---

This function imports devices into a given project.

Syntax

**C#**



public StorableObject[] ImportDevices( 

   Project oProject,

   string strImportFilePath,

   string strSchemeName

)

public:

array<StorableObject^>^ ImportDevices( 

   Project^ oProject,

   String^ strImportFilePath,

   String^ strSchemeName

)


#### Parameters

*oProject*
:   Project into which the devices will be imported.

*strImportFilePath*
:   Full file name of the devices file to import.

*strSchemeName*
:   Name of the import scheme. If the scheme name is empty the last used scheme of the project will be used.

#### Return Value

Result is returned as array of StorableObjects.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing devices could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import of devices. Please refer to the exception message. |
