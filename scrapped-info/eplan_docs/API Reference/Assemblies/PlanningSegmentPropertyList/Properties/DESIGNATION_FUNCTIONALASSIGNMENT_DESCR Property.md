# DESIGNATION_FUNCTIONALASSIGNMENT_DESCR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic778.html

---

Functional assignment (leading identifiers) # 1322.

Syntax

**C#**



public PropertyValue DESIGNATION_FUNCTIONALASSIGNMENT_LEADINGPARTS( 

   int index

) {get; set;}

public:

property PropertyValue^ DESIGNATION_FUNCTIONALASSIGNMENT_LEADINGPARTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.
