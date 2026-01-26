# DESIGNATION_INSTALLATIONNUMBER_LEADINGPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic499.html

---

Higher-level function number (leading identifiers) # 1722.

Syntax

**C#**



public PropertyValue DESIGNATION_INSTALLATIONNUMBER_LEADINGPARTS( 

   int index

) {get; set;}

public:

property PropertyValue^ DESIGNATION_INSTALLATIONNUMBER_LEADINGPARTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.
