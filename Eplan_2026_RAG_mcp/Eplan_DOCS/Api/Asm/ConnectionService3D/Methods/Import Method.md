# Import Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D~Import.html

---

Imports the Connection3Ds from a file into the given project using a scheme.

Syntax

**C#**



public Connection3D[] Import( 

   Project oProject,

   string strImportFilePath,

   string strSchemeName

)

public:

array<Connection3D^>^ Import( 

   Project^ oProject,

   String^ strImportFilePath,

   String^ strSchemeName

)


#### Parameters

*oProject*
:   Destination project.

*strImportFilePath*
:   Filename of the import file.

*strSchemeName*
:   Name of the import scheme. If the scheme name is empty, the last used scheme of the project will be used.

#### Return Value

An array of imported Connections3D.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. Please refer to the exception message. |
