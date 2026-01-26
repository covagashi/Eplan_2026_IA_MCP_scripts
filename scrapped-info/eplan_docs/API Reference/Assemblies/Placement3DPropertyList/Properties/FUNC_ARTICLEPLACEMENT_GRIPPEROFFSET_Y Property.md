# FUNC_ARTICLEPLACEMENT_GRIPPEROFFSET_Y Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLEPLACEMENT_GRIPPEROFFSET_Y().html

---

Y coordinate Handle # 20209.

Syntax

**C#**



public PropertyValue FUNC_ARTICLEPLACEMENT_GRIPPEROFFSET_Y {get; set;}

public:

property PropertyValue^ FUNC_ARTICLEPLACEMENT_GRIPPEROFFSET_Y {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Y coordinate for the handle of a part placement or a function. For part placements, the handle is in the left center by default, so it is much easier to position the device on a mounting rail.
