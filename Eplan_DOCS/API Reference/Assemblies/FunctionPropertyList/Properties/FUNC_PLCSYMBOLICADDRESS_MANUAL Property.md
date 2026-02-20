# FUNC_PLCSYMBOLICADDRESS_MANUAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCSYMBOLICADDRESS_MANUAL().html

---

Symbolic address # 20402.

Syntax

**C#**



public PropertyValue FUNC_PLCSYMBOLICADDRESS_MANUAL {get; set;}

public:

property PropertyValue^ FUNC_PLCSYMBOLICADDRESS_MANUAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Manually entered symbolic PLC address of a PLC connection point. This property, if it exists, is transferred on synchronization between overview and schematic.
