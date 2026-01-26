# LockDevice Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~LockDevice.html

---

Tries to lock current device (which can refer to several objects, such as all function's representations) in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. If locked device in placed, corresponding page(s) will be locked as well.

Syntax

**C#**



public void LockDevice( 

   bool bWithCDPs

)

public:

void LockDevice( 

   bool bWithCDPs

)


#### Parameters

*bWithCDPs*
:   If true, then Connection Definition Points will locked as well and the call is equivalent to SmartLock()
