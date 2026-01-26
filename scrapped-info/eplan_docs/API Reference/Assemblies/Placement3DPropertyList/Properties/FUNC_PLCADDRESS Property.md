# FUNC_PLCADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCADDRESS().html

---

PLC address # 20400.

Syntax

**C#**



public PropertyValue FUNC_PLCADDRESS {get; set;}

public:

property PropertyValue^ FUNC_PLCADDRESS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Full PLC address for channel or PLC connection point. The address is not an identifying characteristic. The format of the address depends on the PLC type. The address must be unique within a CPU. In this context the CPU is identified by means of the full CPU name in the form [Configuration project].[Station ID].[CPU name].
