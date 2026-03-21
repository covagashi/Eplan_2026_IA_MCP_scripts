# DMPLAOBJECT_IS_LINKED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_IS_LINKED().html

---

Is linked to superior segments # 44066.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_IS_LINKED {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_IS_LINKED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows whether the current segment is linked to different superior segments. The property can be used for filtering in the pre-planning navigator and in the reports for the pre-planning.
