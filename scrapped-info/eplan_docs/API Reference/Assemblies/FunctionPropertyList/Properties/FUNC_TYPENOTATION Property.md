# FUNC_TYPENOTATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TYPENOTATION(Int32).html

---

Type designation of part # 20200.

Syntax

**C#**



public PropertyValue FUNC_TYPENOTATION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_TYPENOTATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Provides the type designation of the part, is required for display in the part placement and contact image. Using the index you can differentiate between up to 50 entries.
