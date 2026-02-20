# PAGE_MACRO_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_MACRO_DESCRIPTION(Int32).html

---

Macro: Description # 11014.

Syntax

**C#**



public PropertyValue PAGE_MACRO_DESCRIPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_MACRO_DESCRIPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 100.

Description text for the macro.
