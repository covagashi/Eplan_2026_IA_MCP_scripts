# PauseWriteProtection Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~PauseWriteProtection.html

---

Temporarily disables write protection. Note that current write protection flags are not cleared.

Syntax

**C#**



public virtual void PauseWriteProtection( 

   bool bPause

)

public:

virtual void PauseWriteProtection( 

   bool bPause

)


#### Parameters

*bPause*

Exceptions

| Exception | Description |
| --- | --- |
| [WriteProtectionNotSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WriteProtectionNotSet.html) | Thrown if object has no write protectection. |
