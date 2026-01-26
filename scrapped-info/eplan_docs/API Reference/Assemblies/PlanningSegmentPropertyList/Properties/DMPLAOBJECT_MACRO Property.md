# DMPLAOBJECT_MACRO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_MACRO().html

---

Macro # 44008.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_MACRO {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_MACRO {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

At each planning object in the tree view of the pre-planning navigator, a macro can be entered that contains parts of the circuit or the entire circuit. This macro is used when creating the detailed planning. The property is also taken into consideration during the export and import of pre-planning data for external editing as well as during the pre-planning import.
