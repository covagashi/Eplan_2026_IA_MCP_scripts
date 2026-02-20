# INTERRUPTIONPOINT_DESTINATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList~INTERRUPTIONPOINT_DESTINATION().html

---

Target of interruption point # 24000.

Syntax

**C#**



public PropertyValue INTERRUPTIONPOINT_DESTINATION {get; set;}

public:

property PropertyValue^ INTERRUPTIONPOINT_DESTINATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the (first) target of an interruption point for display in the cross-reference; only used internally.
