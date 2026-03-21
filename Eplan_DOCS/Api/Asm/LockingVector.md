# LockingVector

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector.html

---

This class manages locking, but is is not needed to call it directly. Use [LockingStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingStep.html) class instead.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.LockingVector**

Syntax

**C#**



public class LockingVector

public ref class LockingVector

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [LockingVector Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~_ctor.html) | Constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Enabled](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~Enabled.html) | Returns true if locking mechanism is enabled in this version. |
| Public Property | [LockingStepCount](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~LockingStepCount.html) | Returns the number of active LockingSteps. This is not the length of the vector, because the locking-operations are stored(represented) there (not the LockingSteps). |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~Dispose().html) | Destructor for deterministic finalization of LockingVector object. Deactivates objects and frees memory. |
| Public Method | [EndLockingStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~EndLockingStep.html) | Ends locking step. Use LockingStep instead. |
| Public Method | [LockAllObjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~LockAllObjects.html) |  |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~LockObject.html) |  |
| Public Method | [LockObjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~LockObjects.html) |  |
| Public Method | [PauseManualLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~PauseManualLock.html) | \Internal method, sets internal AutoLockActive flag to its original value (value before first locking step). Used for calling internal actions and methods which are not handling manual locking. |
| Public Method | [ResumeManualLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~ResumeManualLock.html) | Internal method, sets internal AutoLockActive flag to value before PauseManualLock. Used for calling internal actions and methods which are not handling manual locking. |
| Public Method | [SetAsInternal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~SetAsInternal.html) | Initializes LockingVectorProxy in API\_Framework. Used automatically, internally. |
| Public Method | [StartLockingStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~StartLockingStep.html) | Starts locking step. Use LockingStep instead. |


