# DMPLAOBJECT_SEGMENT_DIGITAL_PLCINPUT_COUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic861.html

---

Number of digital PLC outputs # 44080.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_SEGMENT_DIGITAL_PLCOUTPUT_COUNT {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_SEGMENT_DIGITAL_PLCOUTPUT_COUNT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Shows the sum of the digital PLC outputs for the current planning object. Digital PLC addresses are such addresses that have the data type "BOOL". This is not case-sensitive. Inputs and outputs are recognized by the direction of the PLC address.
