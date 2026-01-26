# FUNC_ARTICLE_LABELLING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_LABELLING(Int32).html

---

Identification # 26406.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_LABELLING( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_LABELLING {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Marking or labeling of a product by applying numbers, letters, labels, symbols or colors with the aim of identifying the product and giving instructions for transport, handling and storage. Example: CE certification.
