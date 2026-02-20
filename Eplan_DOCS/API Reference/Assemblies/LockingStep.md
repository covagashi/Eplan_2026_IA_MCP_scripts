# LockingStep

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingStep.html

---

Class for automatic unlocking project resources.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.LockingStep**

Syntax

**C#**



public class LockingStep

public ref class LockingStep


Remarks

This class collects information about all project resources which were locked since its creation. So it can be considered as an automatic-container of locking handles. These locks are disposed when the class is disposed, so a best way is to use it with "using" block (see Example 1). There are two possible locking modes: manual (done by LockingStep class) or automatic (used by EPLAN Platform internally). LockingStep is created and disposed implicitly by build-in API actions, but it must be created explicitly in following cases: \* Modeless dialog boxes \* API offline applications. \* Verifications LockingSteps can be nested. When disposing LockingStep, only these project resources which were locked exactly during LockingStep existance are unlocked. Multithreading is not supported.

Example

LockingStep must be created in every procedure which is accessing P8 in the modeless dialog box. Sample usage in the offline application

- [c#](#i-tab-content-e8ae8902-fc03-47d0-9589-955b44a5b1c7)

```
void MyModelessDialog::DoProcessing()

{

   using(LockingStep oLS = new LockingStep())

   {

        // ... accessing P8 data ...

   }

}
```

- [vb.net](#i-tab-content-b690d73a-b936-43ad-994f-40b102397712)

```
Dim oEplApp As EplApplication = New EplApplication

Dim strAppModifier As System.String = ""

oEplApp.Init(strAppModifier)

Dim pm As Eplan.EplApi.DataModel.ProjectManager

Dim p As Eplan.EplApi.DataModel.Project

Dim l As LockingStep

l = New LockingStep

pm = New ProjectManager

'pm.LockByDefault = true 'true by default in ProjectManager

p = pm.CreateProject("C:\\Program Files\\EPLAN\\Electric P8\\Projects\\EPLAN\\EPLAN_Sample_Project.elk", "C:\\Program Files\\EPLAN\\Electric P8\\Templates\\ESS\\EPLAN_Sample_Project.epb")

'project is locked

'Initialize()

'Processing(p)

p.Close() 'normally unlocks project

l.Dispose() 'unlocking all projects that were locked in this locking step

oEplApp.Exit()
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [LockingStep Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingStep~_ctor.html) | Starts a locking step. ManualLocking mode is set to ON; Gets the position in LockingVector (in order to restore locking state when LockingStep is disposed). |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingStep~Dispose().html) | Ends a locking step (identified by internal nLockingStepId). ManualLocking mode is set to its previous value; Original locking state is restored. The same as !LockingStep. |


