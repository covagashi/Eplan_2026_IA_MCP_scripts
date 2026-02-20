# INTERRUPTIONPOINT_DESCRIPTIONAUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList~INTERRUPTIONPOINT_DESCRIPTIONAUTOMATIC().html

---

Interruption point: Description (automatic) # 24811.

Syntax

**C#**



public PropertyValue INTERRUPTIONPOINT_DESCRIPTIONAUTOMATIC {get; set;}

public:

property PropertyValue^ INTERRUPTIONPOINT_DESCRIPTIONAUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

Shows the interruption point description. The value is automatically taken from the first interruption point (according to the position in the schematic).
