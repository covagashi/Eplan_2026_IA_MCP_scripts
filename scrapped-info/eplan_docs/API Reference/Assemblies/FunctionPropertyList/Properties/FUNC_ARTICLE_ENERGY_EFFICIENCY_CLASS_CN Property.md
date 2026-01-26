# FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_CN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_CN(Int32).html

---

Energy efficiency class CN # 26306.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_CN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_CN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Energy efficiency class for China. In China, energy efficiency is often indicated by the China Energy Label (CEL).
