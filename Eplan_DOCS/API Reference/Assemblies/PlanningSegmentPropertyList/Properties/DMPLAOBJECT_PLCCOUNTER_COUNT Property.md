# DMPLAOBJECT_PLCCOUNTER_COUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_PLCCOUNTER_COUNT().html

---

Total number of PLC counter inputs # 44059.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCCOUNTER_COUNT {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCCOUNTER_COUNT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Shows the sum of the PLC counter inputs (meaning PLC inputs identified as counters) for the current planning object and the subordinate planning objects (same as the tree structure in the pre-planning navigator).
