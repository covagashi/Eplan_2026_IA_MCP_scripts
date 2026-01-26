# SynchronizeProjects(Project,Project,SynchronizationMode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1431.html

---

Synchronizes all projects data from source project into the target project.

Syntax

**C#**



public bool SynchronizeProjects( 

   Project oSourceProject,

   Project oTargetProject,

   ProjectManagement.SynchronizationMode eSynchronizationMode

)

public:

bool SynchronizeProjects( 

   Project^ oSourceProject,

   Project^ oTargetProject,

   ProjectManagement.SynchronizationMode eSynchronizationMode

)


#### Parameters

*oSourceProject*
:   Source project from which it gets data.

*oTargetProject*
:   Target project to synchronize.

*eSynchronizationMode*
:   Determines what mode of synchronization will be used. Update - Replaces all outdated and different project data in the target project by the data of the source project. Complete - Supplements the project data of the target project with data which so far was only available in the source project.

#### Return Value

True if the synchronization was successful.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if source or target project is null. |
| **ApplicationException** | Thrown if the internal action could not be found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |
