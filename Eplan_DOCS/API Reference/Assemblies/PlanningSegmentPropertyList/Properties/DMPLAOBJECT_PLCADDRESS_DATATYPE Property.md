# DMPLAOBJECT_PLCADDRESS_DATATYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic848.html

---

PLC address: Direction # 44020.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_DIRECTION( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_DIRECTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. Enter the direction here (input, output, undefined). The individual PLC inputs and outputs are differentiated via the index, with a maximum of 50.
