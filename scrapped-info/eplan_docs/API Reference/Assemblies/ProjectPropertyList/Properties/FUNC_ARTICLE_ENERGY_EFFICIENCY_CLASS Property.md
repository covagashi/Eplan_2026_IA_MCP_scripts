# FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS(Int32).html

---

Energy efficiency class # 26302.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Assessment scale that shows how much energy an electrical device uses compared to other devices. The energy efficiency class can be determined, for example, in accordance with the EU-wide standard method "Energy Label Classification" and can be specified in the graduations A to G.
