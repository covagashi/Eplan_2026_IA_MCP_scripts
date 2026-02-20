# SafetyPoint

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SafetyPoint.html

---

Provides mechanism for automatic locking of DataModel objects

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.SafetyPoint**

Syntax

**C#**



public sealed class SafetyPoint

public ref class SafetyPoint sealed


Remarks

The mechanism is enabled since creation and until disposing of a SafetyPoint object, so the recommended way is to use it with 'using' keyword

Example

**C#**

```
var project = new ProjectManager {LockProjectByDefault = false}.OpenProject(@"$(MD_PROJECTS)\EPLAN-DEMO.elk");

//view placement '8' (on page =EB3+ETM/4)

ViewPlacement viewPlacement8 = project

    .Pages[42]

    .AllFirstLevelPlacements

    .OfType<ViewPlacement>()

    .FirstOrDefault(item => item.Properties.DMG_VIEWPLACEMENT_DESIGNATION.ToString() == "8");

using (SafetyPoint safetyPoint = SafetyPoint.Create())

{                

    Console.WriteLine(viewPlacement8.IsLocked);     //false

    viewPlacement8.Scale = 44.44;                   //set another scale

    Console.WriteLine(viewPlacement8.IsLocked);     //true                   

    safetyPoint.Commit();                           //necessary, otherwise changes from the block are rolled-back

}

Console.WriteLine(viewPlacement8.IsLocked);         //again false

```

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Commit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SafetyPoint~Commit.html) | All changes done up to this point should be accepted. Locked objects are freed. |
| Public Methodstatic (Shared in Visual Basic) | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SafetyPoint~Create.html) | Creates SafetyPoint object and starts recording changes. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SafetyPoint~Dispose().html) | Virtual deterministic destructor. |
| Public Methodstatic (Shared in Visual Basic) | [GetAutoLockingState](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SafetyPoint~GetAutoLockingState.html) | Gets internal AutoLocking flag. When it's true AutoLocking is active. |
| Public Method | [Rollback](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SafetyPoint~Rollback.html) | All recorded changed (if any) will be undone without redo. |
| Public Method | [Start](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SafetyPoint~Start.html) | Start recording changes. If already started, has no effect. |


