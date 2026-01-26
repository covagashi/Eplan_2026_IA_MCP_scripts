# DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1087.html

---

PLC address: Symbolic address: UDT (name) # 44088.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_UDT( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_UDT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. With this property you have the possibility to nestle and manage the symbolic address of the PLC connection point within a user-defined data type. "UDT" stands for "User Defined Type". The property is a monolingual text and is used and exchanged as of the AutomationML AR APC format Version 1.3.0. Entry of a decimal point is not permissible. When using this property you additionally have to specify the data type in the "PLC address: Symbolic address: UDT (data type)" property.
