# DMPLAOBJECT_FULLDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_FULLDESIGNATION().html

---

Designation (full) # 44009.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_FULLDESIGNATION {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_FULLDESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows the full designation from the top structure level in the tree up to this planning object. In the P&I diagram the property shows the complete designation of the PCT loop / PCT loop function including the structure identifiers of all the superior segments.
