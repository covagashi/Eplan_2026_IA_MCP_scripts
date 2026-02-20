# FUNC_ARTICLE_ASSEMBLY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_ASSEMBLY(Int32).html

---

Assembly # 20905.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ASSEMBLY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ASSEMBLY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

A collection of parts that belong to a device (e.g. a pushbutton with a normally open contact, the appropriate mounting and the button). An assembly has its own part number and can also contain (sub) assemblies.

Changes done on this property are also visible on properties: \* ARTICLEREF\_ASSEMBLY of corresponding [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).
