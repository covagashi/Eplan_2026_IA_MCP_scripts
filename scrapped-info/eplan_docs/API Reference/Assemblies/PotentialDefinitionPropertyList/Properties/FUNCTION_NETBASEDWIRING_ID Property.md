# FUNCTION_NETBASEDWIRING_ID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~FUNCTION_NETBASEDWIRING_ID(Int32).html

---

ID for net-based connections # 20218.

Syntax

**C#**



public PropertyValue FUNCTION_NETBASEDWIRING_ID( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION_NETBASEDWIRING_ID {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 100.

ID for identifying connection points for net-based connections. Every connection point has a unique ID.
