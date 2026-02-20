# INSTANCE_REVISION_LOG_MARKER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~INSTANCE_REVISION_LOG_MARKER().html

---

Revision marker (change tracking) # 19030.

Syntax

**C#**



public PropertyValue INSTANCE_REVISION_LOG_MARKER {get; set;}

public:

property PropertyValue^ INSTANCE_REVISION_LOG_MARKER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Automatically entered marker text at modified objects in a revision. The marker text is composed from a number of different properties, e.g. revision name, creator, and modification date.
