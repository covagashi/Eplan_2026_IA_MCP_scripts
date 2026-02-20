# DMPLAOBJECT_DEFINITIONDISPLAYNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic839.html

---

Total number of digital PLC inputs # 44028.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_DIGITAL_PLCINPUT_COUNT {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_DIGITAL_PLCINPUT_COUNT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Shows the sum of the digital PLC inputs for the current planning object and the subordinate planning objects and (in accordance with the tree structure in the pre-planning navigator). Digital PLC addresses are such addresses that have the data type "BOOL". This is not case-sensitive. Inputs and outputs are recognized by the direction of the PLC address.
