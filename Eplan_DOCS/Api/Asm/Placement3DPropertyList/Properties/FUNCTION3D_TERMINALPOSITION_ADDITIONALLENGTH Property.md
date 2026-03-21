# FUNCTION3D_TERMINALPOSITION_ADDITIONALLENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic664.html

---

Connection point pattern: Additional length # 36060.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_ADDITIONALLENGTH( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_ADDITIONALLENGTH {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Additional length of an individual connection point in the connection point pattern.
