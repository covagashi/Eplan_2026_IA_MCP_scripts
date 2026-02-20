# GetProjectByObjectId Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProjectByObjectId.html

---

Gets the project of an object id string. This is the project the object belongs to.

Syntax

**C#**



public Project GetProjectByObjectId( 

   string objectId

)

public:

Project^ GetProjectByObjectId( 

   String^ objectId

)


#### Parameters

*objectId*

#### Return Value

Project : project object. When there is no project found the return value is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when the object id is invalid. |
| [System.ArgumentNullException](#) | Thrown when `objectId` is `null`. |
