# DMPLAOBJECT_PLCADDRESS_CONFIGURATIONPROJECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic846.html

---

PLC address: Counter # 44064.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_COUNTER( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_COUNTER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. Specify a (unique) single component of the symbolic address for each input and output. The individual PLC inputs and outputs are differentiated via the index, with a maximum of 50. These single components are used to determine the symbolic address and are attached to the single components of the symbolic address that was entered at the superior segments. The automatically determined symbolic address thus results as a combination of the single components that were entered at the current planning object and at all the superior segments.
