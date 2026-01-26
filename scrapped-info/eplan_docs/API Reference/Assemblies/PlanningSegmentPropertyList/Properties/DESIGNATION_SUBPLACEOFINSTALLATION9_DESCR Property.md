# DESIGNATION_SUBPLACEOFINSTALLATION9_DESCR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic825.html

---

User-defined structure (leading identifiers) # 1622.

Syntax

**C#**



public PropertyValue DESIGNATION_USERDEFINED_LEADINGPARTS( 

   int index

) {get; set;}

public:

property PropertyValue^ DESIGNATION_USERDEFINED_LEADINGPARTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.
