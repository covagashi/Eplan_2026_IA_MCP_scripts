# IsLocked Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~IsLocked.html

---

Determines if the the StorableObject is locked.

The StorableObject is locked when it was explicitly or implicitly locked.

Syntax

**C#**



public override bool IsLocked {get;}

public:

property bool IsLocked {

   bool get() override;

}


#### Property Value

true : the StorableObject is locked

false : the StorableObject is not locked

Remarks

The method returns the information whether an object is locked generally (not only by the current process).
