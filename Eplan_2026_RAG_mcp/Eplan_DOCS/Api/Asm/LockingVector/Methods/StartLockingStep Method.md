# StartLockingStep Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~StartLockingStep.html

---

Starts locking step. Use LockingStep instead.

Syntax

**C#**



public virtual int StartLockingStep()

public:

virtual int StartLockingStep();


Remarks

When it is not possible to use [LockingStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingStep.html) call this method to create locking steps. It is important to implement correct exception handling mechanism in order to end all started locking steps. It is also important to Start and End locking steps in appropriate order if created recursively.
