# DMPLAOBJECT_DESIGNATION_VISIBLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_DESIGNATION_VISIBLE().html

---

Designation (visible) # 44065.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_DESIGNATION_VISIBLE {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_DESIGNATION_VISIBLE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

By means of this property you can have a "reduced" designation displayed at the PCT loops / PCT loop functions which are placed in a structure box in the P&I diagram. In this property the designation of the superior structure box is abbreviated, meaning that the partial structure in which the PCT loop / PCT loop function is located is displayed.

If a PCT loop / PCT loop function belongs to a different structure, a "reduced" designation is displayed. In this case a ">" is displayed before the designation.
