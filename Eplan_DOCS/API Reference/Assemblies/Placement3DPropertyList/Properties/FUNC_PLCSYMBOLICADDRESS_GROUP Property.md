# FUNC_PLCSYMBOLICADDRESS_GROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCSYMBOLICADDRESS_GROUP().html

---

Symbolic address: Group # 20610.

Syntax

**C#**



public PropertyValue FUNC_PLCSYMBOLICADDRESS_GROUP {get; set;}

public:

property PropertyValue^ FUNC_PLCSYMBOLICADDRESS_GROUP {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

With this property you can group areas of symbolic addresses in the assignment list, for example inputs, outputs, safety addresses, etc. The property is used during the PLC data exchange in AutomationML AR APC format.
