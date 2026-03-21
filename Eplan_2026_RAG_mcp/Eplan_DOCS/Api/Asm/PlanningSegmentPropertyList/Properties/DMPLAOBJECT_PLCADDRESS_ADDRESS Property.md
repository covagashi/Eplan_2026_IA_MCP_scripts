# DMPLAOBJECT_PLCADDRESS_ADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic845.html

---

PLC address: Configuration project # 44048.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_CONFIGURATIONPROJECT( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_CONFIGURATIONPROJECT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. Enter here the configuration project to which the PLC connection point is assigned. (A CPU is identified uniquely through the specification of the configuration project, station ID, and CPU name.) The individual PLC inputs and outputs are differentiated via the index, with a maximum of 50.
