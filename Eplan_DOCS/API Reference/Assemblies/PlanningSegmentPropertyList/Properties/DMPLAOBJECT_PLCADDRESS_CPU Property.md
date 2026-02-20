# DMPLAOBJECT_PLCADDRESS_CPU Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_PLCADDRESS_CPU(Int32).html

---

PLC address: CPU # 44022.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_CPU( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_CPU {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. Enter here the processor to which the PLC connection point is assigned. A CPU is uniquely identified by specification of the CPU name in the form [Configuration project].[Station ID].[CPU identifier]. The individual PLC inputs and outputs are differentiated via the index, with a maximum of 50.
