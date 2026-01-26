# DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_UDT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic855.html

---

PLC address: Symbolic address: UDT (data type) # 44089.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_UDT_DATATYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_UDT_DATATYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. When using the "PLC address: Symbolic address: UDT (name)" property specify the associated user-defined data type here. With these two properties you have the possibility to nestle and manage the symbolic address of the PLC connection point within a user-defined data type. "UDT" stands for "User Defined Type". The property is a monolingual text and is used and exchanged as of the AutomationML AR APC format Version 1.3.0. Entry of a decimal point is not permissible. The actual structure of the UDT is only required in the PLC configuration program and only specified there.
