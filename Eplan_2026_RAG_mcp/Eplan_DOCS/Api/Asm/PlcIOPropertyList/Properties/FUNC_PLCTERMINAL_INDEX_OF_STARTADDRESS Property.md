# FUNC_PLCTERMINAL_INDEX_OF_STARTADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLCTERMINAL_INDEX_OF_STARTADDRESS().html

---

PLC subdevice: Index # 20384.

Syntax

**C#**



public PropertyValue FUNC_PLCTERMINAL_INDEX_OF_STARTADDRESS {get; set;}

public:

property PropertyValue^ FUNC_PLCTERMINAL_INDEX_OF_STARTADDRESS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

The value of this property specifies the position of the PLC subdevice to which the PLC connection point belongs. This information is required for automatic addressing. The property can also be stored in the function templates of the parts and is then transferred to the PLC connection points during a part selection.
