# FUNC_PLC_IGNORE_BUSADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_IGNORE_BUSADDRESS().html

---

Ignore missing bus ID # 20412.

Syntax

**C#**



public PropertyValue FUNC_PLC_IGNORE_BUSADDRESS {get; set;}

public:

property PropertyValue^ FUNC_PLC_IGNORE_BUSADDRESS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This settings possibility is designed for devices in bus systems that do not require a bus ID. If this property is activated at a bus port, the missing bus ID is ignored during the execution of check run 004037, and no check run message is issued for this bus port.
