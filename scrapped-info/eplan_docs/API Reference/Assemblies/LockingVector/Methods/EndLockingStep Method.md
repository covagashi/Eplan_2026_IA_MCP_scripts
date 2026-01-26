# EndLockingStep Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~EndLockingStep.html

---

Ends locking step. Use LockingStep instead.

Syntax

**C#**



public virtual bool EndLockingStep( 

   int nLockingStepId

)

public:

virtual bool EndLockingStep( 

   int nLockingStepId

)


#### Parameters

*nLockingStepId*
:   Id of last step to unlock.

Remarks

When it is not possible to use [LockingStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingStep.html) call this method to end locking steps. It is important to implement correct exception handling mechanism in order to end all started locking steps. It is also important to Start and End locking steps in appropriate order if created recursively.
