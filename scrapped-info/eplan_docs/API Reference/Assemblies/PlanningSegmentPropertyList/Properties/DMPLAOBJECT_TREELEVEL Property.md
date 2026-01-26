# DMPLAOBJECT_TREELEVEL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_TREELEVEL().html

---

Level in tree # 44026.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_TREELEVEL {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_TREELEVEL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Indicates the hierarchy level of the planning object or structure segment in the tree view of the pre-planning navigator. The top level (directly below the project) has the value "1"; for the levels below, the value is incremented.
