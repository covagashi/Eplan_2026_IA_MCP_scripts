# JT Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Import3D~JT.html

---

Imports a 3D file

Syntax

**C#**



public InstallationSpace JT( 

   Project oProject,

   string strFileName

)

public:

InstallationSpace^ JT( 

   Project^ oProject,

   String^ strFileName

)


#### Parameters

*oProject*
:   Project to which the JT file will be imported

*strFileName*
:   Full name of the file being imported.

#### Return Value

The installation space to which the JT file was imported

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **ArgumentNullException** | null was passed to a parameter. |
| **ApplicationException** | An action or internal interface for the import could not be created. A reason for this could be the lack of necessary rights or licenses. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. Please read the exception message. |

Remarks

This method requires a license for the pro panel 3D add-on
