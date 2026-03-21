# Exit Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~Exit.html

---

Exits the Eplan runtime system.

Syntax

**C#**



public void Exit()

public:

void Exit();


Remarks

EplApplication instance should be deinitialized explicitly by the main thread. When `Exit` method is called by thread of garbage collector or after leaving main function of application it can cause application crash.
