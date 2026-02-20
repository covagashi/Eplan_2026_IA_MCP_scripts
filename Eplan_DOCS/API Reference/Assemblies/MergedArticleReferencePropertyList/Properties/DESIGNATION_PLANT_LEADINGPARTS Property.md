# DESIGNATION_PLANT_LEADINGPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic365.html

---

Function designation (leading identifiers) # 1122.

Syntax

**C#**



public PropertyValue DESIGNATION_PLANT_LEADINGPARTS( 

   int index

) {get; set;}

public:

property PropertyValue^ DESIGNATION_PLANT_LEADINGPARTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.

Supplies leading identifiers up to the hierarchy level specified by the index, for example, "A.UA.UA2" for index 3 for a function designation "A.UA.UA2.UA3.UA4".
