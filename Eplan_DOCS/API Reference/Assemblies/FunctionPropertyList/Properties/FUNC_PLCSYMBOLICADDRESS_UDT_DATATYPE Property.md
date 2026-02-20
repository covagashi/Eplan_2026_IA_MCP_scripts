# FUNC_PLCSYMBOLICADDRESS_UDT_DATATYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCSYMBOLICADDRESS_UDT_DATATYPE().html

---

Symbolic address: UDT (data type) # 20619.

Syntax

**C#**



public PropertyValue FUNC_PLCSYMBOLICADDRESS_UDT_DATATYPE {get; set;}

public:

property PropertyValue^ FUNC_PLCSYMBOLICADDRESS_UDT_DATATYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

When using the "Symbolic address: UDT (name)" property specify the associated user-defined data type here. With these two properties you have the possibility to nestle and manage the symbolic address of the PLC connection point within a user-defined data type. "UDT" stands for "User Defined Type". The property is a monolingual text and is used and exchanged as of the AutomationML AR APC format Version 1.3.0. Entry of a decimal point is not permissible. The actual structure of the UDT is only required in the PLC configuration program and only specified there.
