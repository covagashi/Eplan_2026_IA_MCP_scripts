# INTERRUPTIONPOINT_CROSSREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList~INTERRUPTIONPOINT_CROSSREFERENCE().html

---

Cross-reference (configurable) # 24300.

Syntax

**C#**



public PropertyValue INTERRUPTIONPOINT_CROSSREFERENCE {get; set;}

public:

property PropertyValue^ INTERRUPTIONPOINT_CROSSREFERENCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

For interruption points and structure boxes, this outputs the cross-reference. This also outputs target information when the "Display of all counter targets" (ID 24021) property is enabled.
