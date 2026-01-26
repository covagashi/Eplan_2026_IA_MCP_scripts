# FUNC_PLCSOCKET_INDIRECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCSOCKET_INDIRECT().html

---

Position / (slot / module) (indirect) # 20422.

Syntax

**C#**



public PropertyValue FUNC_PLCSOCKET_INDIRECT {get; set;}

public:

property PropertyValue^ FUNC_PLCSOCKET_INDIRECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

For a PLC connection point, this shows the slot / module of the associated PLC card. Describes the slot / position where this PLC card is plugged on the rack.
