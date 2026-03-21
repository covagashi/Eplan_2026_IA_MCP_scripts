# DMPLAOBJECT_HAS_LINKS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_HAS_LINKS().html

---

Has linked segments # 44067.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_HAS_LINKS {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_HAS_LINKS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows whether links to other segments exist below the current segment. The property can be used for filtering in the pre-planning navigator and in the reports for the pre-planning.
