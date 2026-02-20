# BaseMate Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~BaseMate.html

---

Returns default target mate for placing devices on this bus bar.

Syntax

**C#**



public LineMate BaseMate {get;}

public:

property LineMate^ BaseMate {

   LineMate^ get();

}


Remarks

When snapping an item by a base mate, it is set as a child of a target Placement3D Also the orientation of an item is adjusted to a target Placement3D
