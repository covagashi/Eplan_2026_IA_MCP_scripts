# DMPLAOBJECT_ANALOG_PLCINPUT_COUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic836.html

---

Total number of analog PLC outputs # 44031.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_ANALOG_PLCOUTPUT_COUNT {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_ANALOG_PLCOUTPUT_COUNT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Shows the sum of the analog PLC outputs for the current planning object and the subordinate planning objects and (in accordance with the tree structure in the pre-planning navigator). Analog PLC addresses are such addresses that have a data type that is not "BOOL". Inputs and outputs are recognized by the direction of the PLC address.
