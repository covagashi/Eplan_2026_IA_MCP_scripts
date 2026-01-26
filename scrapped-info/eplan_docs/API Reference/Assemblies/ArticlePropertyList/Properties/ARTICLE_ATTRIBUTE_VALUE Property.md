# ARTICLE_ATTRIBUTE_VALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ATTRIBUTE_VALUE(Int32).html

---

Attributes # 22051.

Syntax

**C#**



public PropertyValue ARTICLE_ATTRIBUTE_VALUE( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_ATTRIBUTE_VALUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 100.

Shows indexed the values of the attributes which have been assigned to a part variant in the parts management on the "Properties" > "Data" hierarchy level tab. Attributes are independent of the part type.
