# IsReadOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsReadOnly.html

---

Determines if Mate can be modified.

Syntax

**C#**



public bool IsReadOnly {get;}

public:

property bool IsReadOnly {

   bool get();

}


Remarks

Property `IsReadOnly` checks if object is user defined and if the 3d placement to which it is assign is ready only. Additionally it can return `true` if it can't be modified via API.
