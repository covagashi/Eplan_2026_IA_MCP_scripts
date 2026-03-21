# DMPLAOBJECT_LINK_CHILD_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic844.html

---

PLC address: Address # 44023.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_ADDRESS( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_ADDRESS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. Enter here the PLC address. The individual PLC inputs and outputs are differentiated via the index, with a maximum of 50.
