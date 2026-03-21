# AUTOMATIONML_OBJECTID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~AUTOMATIONML_OBJECTID().html

---

AutomationML GUID # 25030.

Syntax

**C#**



public PropertyValue AUTOMATIONML_OBJECTID {get; set;}

public:

property PropertyValue^ AUTOMATIONML_OBJECTID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is required for the AutomationML export and import. Each object is identified in AutomationML by a GUID (Globally Unique Identifier) that is unique worldwide. The GUID is generated automatically and should normally not be modified manually.
