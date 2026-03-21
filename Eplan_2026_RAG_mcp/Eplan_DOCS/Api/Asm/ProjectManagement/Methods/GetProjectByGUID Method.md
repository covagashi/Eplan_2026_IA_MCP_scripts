# GetProjectByGUID Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~GetProjectByGUID.html

---

Method for searching a project by a given project ID from the project management database.

Syntax

**C#**



public bool GetProjectByGUID( 

   string strProjectGUID,

   ref string strProjectPath,

   ref string strWorkStation

)

public:

bool GetProjectByGUID( 

   String^ strProjectGUID,

   String^% strProjectPath,

   String^% strWorkStation

)


#### Parameters

*strProjectGUID*
:   Unique project ID of the wanted project.

*strProjectPath*
:   [out] Full link file name of the found project.

*strWorkStation*
:   [out] Name of the workstation on which the project is located. The parameter returns an empty string, if the project is not found or it is located on the local workstation.

#### Return Value

return = true: project was found. return = false: project was not found.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |
| [System.ApplicationException](#) | Thrown, if the \internal interface of the project management module could no be created. |

Remarks

It may happen, that a project appears more than once in the database. This may for example happen, if the project was registered as well by a local path as by a UNC path. In this case, the path, which is found first will be written to `strProjectPath`. Opening a project via API does not registers it in the ProjectManagement database. Please use XPrjActionProjectUpdate action or [LoadDirectory](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~LoadDirectory.html) method in order to add it.
