# DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic852.html

---

PLC address: Symbolic address: Group # 44087.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_GROUP( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_GROUP {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. With this property you can group areas of symbolic addresses in the assignment list, for example inputs, outputs, safety addresses, etc. The property is used during the PLC data exchange in AutomationML AR APC format.
