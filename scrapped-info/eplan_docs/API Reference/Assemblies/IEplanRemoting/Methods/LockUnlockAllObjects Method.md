# LockUnlockAllObjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~LockUnlockAllObjects.html

---

Lock or unlock all Objects.

Syntax

**C#**



EplanResponse LockUnlockAllObjects( 

   string strFullProjectName,

   bool bLock

)

EplanResponse^ LockUnlockAllObjects( 

   String^ strFullProjectName,

   bool bLock

)


#### Parameters

*strFullProjectName*
:   Full project path name.

*bLock*
:   lock or unlock flag.

#### Return Value

Eplan response.

Remarks

This call is executed synchronously.
