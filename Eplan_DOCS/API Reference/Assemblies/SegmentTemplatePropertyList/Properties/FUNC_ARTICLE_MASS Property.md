# FUNC_ARTICLE_MASS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_MASS(Int32).html

---

Mass # 26441.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MASS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MASS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Weight of a product or a component. Example: A motor has a mass of 50 kg.
