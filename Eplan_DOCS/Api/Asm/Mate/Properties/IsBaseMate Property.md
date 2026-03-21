# IsBaseMate Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsBaseMate.html

---

Return true, if mate is base mate.

Syntax

**C#**



public bool IsBaseMate {get; set;}

public:

property bool IsBaseMate {

   bool get();

   void set (    bool value);

}


Remarks

When snapping an item by a base mate, it is set as a child of a target Placement3D. Also the orientation of an item is adjusted to a target Placement3D.
