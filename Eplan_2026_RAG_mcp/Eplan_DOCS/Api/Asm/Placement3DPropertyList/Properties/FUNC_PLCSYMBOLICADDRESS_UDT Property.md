# FUNC_PLCSYMBOLICADDRESS_UDT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCSYMBOLICADDRESS_UDT().html

---

Symbolic address: UDT (name) # 20618.

Syntax

**C#**



public PropertyValue FUNC_PLCSYMBOLICADDRESS_UDT {get; set;}

public:

property PropertyValue^ FUNC_PLCSYMBOLICADDRESS_UDT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

With this property you have the possibility to nestle and manage the symbolic address of the PLC connection point within a user-defined data type. "UDT" stands for "User Defined Type". The property is a monolingual text and is used and exchanged as of the AutomationML AR APC format Version 1.3.0. Entry of a decimal point is not permissible. When using this property you additionally have to specify the data type in the "Symbolic address: UDT (data type)" property.
