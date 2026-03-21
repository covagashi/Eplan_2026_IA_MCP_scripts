# FUNC_PLC_SUBNETMASK Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_SUBNETMASK().html

---

Subnet mask # 20446.

Syntax

**C#**



public PropertyValue FUNC_PLC_SUBNETMASK {get; set;}

public:

property PropertyValue^ FUNC_PLC_SUBNETMASK {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The subnet mask defines the splitting of a bus ID (IP address within an Ethernet-based bus system) into a network component and a device / station component. The subnet mask can be used to specify how many devices can be addressed within a subnet.
