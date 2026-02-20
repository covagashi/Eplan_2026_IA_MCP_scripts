# PAGE_MACRO_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_MACRO_NAME(Int32).html

---

Macro: Name # 11008.

Syntax

**C#**



public PropertyValue PAGE_MACRO_NAME( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_MACRO_NAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 100.

File name of the macro.
