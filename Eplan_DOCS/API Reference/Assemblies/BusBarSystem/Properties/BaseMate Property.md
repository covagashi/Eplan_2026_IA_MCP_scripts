# BaseMate Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBarSystem~BaseMate.html

---

Returns default target mate used to place bus bar which will be located on the top in bus bar system.

Syntax

**C#**



public LineMate BaseMate {get;}

public:

property LineMate^ BaseMate {

   LineMate^ get();

}


Remarks

When snapping an item by a base mate, it is set as a child of a target Placement3D Also the orientation of an item is adjusted to a target Placement3D
