# FUNC_PLCCOMMUNICATIONENTITY_SUPPLEMENTARYFIELD01 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic259.html

---

Supplementary field 1 # 20140.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_SUPPLEMENTARYFIELD01( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_SUPPLEMENTARYFIELD01 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. Using the index, you can differentiate between up to 10 supplementary fields.
