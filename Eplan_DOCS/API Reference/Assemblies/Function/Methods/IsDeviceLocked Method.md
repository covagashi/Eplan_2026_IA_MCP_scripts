# IsDeviceLocked Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsDeviceLocked.html

---

Determines if the the Device (which can refer to several objects, such as all function's representations) is locked.

The LockDevice is locked when it was explicitly or implicitly locked.

Syntax

**C#**



public bool IsDeviceLocked( 

   bool bWithCDPs

)

public:

bool IsDeviceLocked( 

   bool bWithCDPs

)


#### Parameters

*bWithCDPs*

#### Return Value

true : the Device is locked

false : the Device (or at least one component) is not locked
