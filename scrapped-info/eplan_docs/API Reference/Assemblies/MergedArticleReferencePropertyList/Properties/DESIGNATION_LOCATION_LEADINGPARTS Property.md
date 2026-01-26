# DESIGNATION_LOCATION_LEADINGPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic362.html

---

Location designation (leading identifiers) # 1222.

Syntax

**C#**



public PropertyValue DESIGNATION_LOCATION_LEADINGPARTS( 

   int index

) {get; set;}

public:

property PropertyValue^ DESIGNATION_LOCATION_LEADINGPARTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.

Supplies leading identifiers up to the hierarchy level specified by the index, for example, "O.UO.UO2" for index 3 for a location designation "O.UO.UO2.UO3.UO4".
