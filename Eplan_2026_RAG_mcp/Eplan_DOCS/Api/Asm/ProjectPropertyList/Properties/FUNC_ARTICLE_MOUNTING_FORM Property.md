# FUNC_ARTICLE_MOUNTING_FORM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MOUNTING_FORM(Int32).html

---

Mounting configuration # 26274.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MOUNTING_FORM( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MOUNTING_FORM {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specific manner in which a part is installed or mounted. This includes, for example, the positioning, the alignment or the placement within a predefined geometric shape.
