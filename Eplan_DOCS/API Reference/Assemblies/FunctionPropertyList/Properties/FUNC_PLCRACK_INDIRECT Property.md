# FUNC_PLCRACK_INDIRECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCRACK_INDIRECT().html

---

PLC card is placed on rack ID (indirect) # 20421.

Syntax

**C#**



public PropertyValue FUNC_PLCRACK_INDIRECT {get; set;}

public:

property PropertyValue^ FUNC_PLCRACK_INDIRECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

For a PLC connection point this outputs the rack on which the associated PLC card is placed.
