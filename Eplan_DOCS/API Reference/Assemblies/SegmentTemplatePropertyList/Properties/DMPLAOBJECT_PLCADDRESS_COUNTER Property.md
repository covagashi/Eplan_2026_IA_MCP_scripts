# DMPLAOBJECT_PLCADDRESS_COUNTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1080.html

---

PLC address: Data type # 44021.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_DATATYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_DATATYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. Enter here the data type here. The individual PLC inputs and outputs are differentiated via the index, with a maximum of 50.
