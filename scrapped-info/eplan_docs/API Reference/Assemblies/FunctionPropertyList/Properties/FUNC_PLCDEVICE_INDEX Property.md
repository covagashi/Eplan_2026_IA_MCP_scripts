# FUNC_PLCDEVICE_INDEX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCDEVICE_INDEX().html

---

Device description: Index in file # 20381.

Syntax

**C#**



public PropertyValue FUNC_PLCDEVICE_INDEX {get; set;}

public:

property PropertyValue^ FUNC_PLCDEVICE_INDEX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Index in the device description file of a PLC card. Through the index it is possible to select a device in a language-neutral form within such a file. During a part selection or device selection the property is filled with the corresponding value from the parts management. The property is taken into consideration during the PLC data exchange in AutomationML AR APC format.
