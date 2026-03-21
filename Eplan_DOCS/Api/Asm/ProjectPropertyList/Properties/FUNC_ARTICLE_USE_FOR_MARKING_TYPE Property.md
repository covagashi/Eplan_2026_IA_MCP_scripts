# FUNC_ARTICLE_USE_FOR_MARKING_TYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_USE_FOR_MARKING_TYPE(Int32).html

---

Usage for labeling type # 26626.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_USE_FOR_MARKING_TYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_USE_FOR_MARKING_TYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The way in which a product can be labeled or identified. This can include various methods and materials used for labeling, e.g. thermal printing or inkjet printing.
