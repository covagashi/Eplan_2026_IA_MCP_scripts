# FUNC_PLCGROUP_DATALENGTH_OUTPUTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCGROUP_DATALENGTH_OUTPUTS().html

---

PLC device: Data length (outputs) # 20550.

Syntax

**C#**



public PropertyValue FUNC_PLCGROUP_DATALENGTH_OUTPUTS {get; set;}

public:

property PropertyValue^ FUNC_PLCGROUP_DATALENGTH_OUTPUTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Required length in address space for the outputs of the PLC card. The specification is in bits. The address range of the PLC card is determined from the data length together with the start address. Note that there are PLC cards, for example technology modules, which are only assigned to a few inputs / outputs, but still require a larger address range than the one currently occupied. Always enter the maximum required length for the address range of the outputs here.
