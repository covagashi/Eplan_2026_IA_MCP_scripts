# LockAllObjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~LockAllObjects.html

---

Locks all data model objects in the project.

Syntax

**C#**



public void LockAllObjects()

public:

void LockAllObjects();


Exceptions

| Exception | Description |
| --- | --- |
| [ProjectLockingException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectLockingException.html) | Thrown when the project cannot be locked. |

Remarks

Result is the same as when getting a project from a [ProjectManager](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager.html) object with the [ProjectManager.LockProjectByDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~LockProjectByDefault.html) property set to TRUE (i.e. all project's objects are locked for an exclusive write and cannot be modified by other users).

Example

**C#**

```
using (LockingStep ls = new LockingStep())

{

 try

 {

 	_prj.LockAllObjects();

 	// all project's objects are locked now

 }

 catch (ProjectLockingException ex)

 {

 	// the whole project couldn't be locked

 }

}

// here, when the LockingStep object is disposed, the project is unlocked again
```
