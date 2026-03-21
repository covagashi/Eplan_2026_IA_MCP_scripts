# DMPLAOBJECT_COUNTER_IN_TREE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_COUNTER_IN_TREE().html

---

Sort code (segments) # 44092.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_COUNTER_IN_TREE {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_COUNTER_IN_TREE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

PCT loop functions that are subordinate to a PCT loop can be output by means of this property in reports in the same sequence as they are displayed in the tree view of the pre-planning navigator. You have to select this property as the "Category / property" in the sorting settings in the "Sorting" dialog so that the same sorting takes place in the reports as in the pre-planning navigator. This applies both for reports of the "Pre-planning: Planning object overview" (function lists for building automation to VDI 3814) type and for the export of manufacturing data / labeling data.
