# DMPLAOBJECT_PLCADDRESS_STATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic851.html

---

PLC address: Symbolic address # 44024.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. Enter here the symbolic address. The individual PLC inputs and outputs are differentiated via the index, with a maximum of 50.
