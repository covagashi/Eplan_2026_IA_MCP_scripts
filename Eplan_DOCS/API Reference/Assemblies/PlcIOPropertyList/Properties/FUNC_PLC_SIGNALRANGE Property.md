# FUNC_PLC_SIGNALRANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLC_SIGNALRANGE().html

---

Signal range # 20388.

Syntax

**C#**



public PropertyValue FUNC_PLC_SIGNALRANGE {get; set;}

public:

property PropertyValue^ FUNC_PLC_SIGNALRANGE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Signal range that a PLC connection point has. Possible entries are, for example, ranges for the voltage or the amperage: 0...10 V or 0...20 mA or +/-5 V or 4...20 mA. The property can also be stored in the function templates of the parts and is then transferred to the PLC connection points during a part selection. The property is identifiying at the device selection. It can be used for filtering during external editing and editing in a table. In addition the property in the list view of the PLC navigator can be displayed as well as selected in the dialogs in which you select PLC connection points or addresses to place them blockwise.
