# PLACEHOLDER_VALUESET_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolderPropertyList~PLACEHOLDER_VALUESET_NAME(Int32).html

---

Value set name # 19303.

Syntax

**C#**



public PropertyValue PLACEHOLDER_VALUESET_NAME( 

   int index

) {get; set;}

public:

property PropertyValue^ PLACEHOLDER_VALUESET_NAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

Required to generate the value set table in placeholder object overview screens and shows the names of the value sets in indexed form.
