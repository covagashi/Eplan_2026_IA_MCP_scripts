# FUNCTION3D_TERMINALPOSITION_STRIPPINGLENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic691.html

---

Stripping length # 36096.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_STRIPPINGLENGTH( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_STRIPPINGLENGTH {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Length in millimeters in which the wire fabrication machine is to cut off the insulation.
