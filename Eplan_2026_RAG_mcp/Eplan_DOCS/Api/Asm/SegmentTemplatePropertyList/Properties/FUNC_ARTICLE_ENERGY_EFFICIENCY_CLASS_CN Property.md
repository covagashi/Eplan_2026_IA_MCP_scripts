# FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_CN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1134.html

---

Energy efficiency class (motor) # 26304.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_MOTOR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_MOTOR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Characterization of the energy efficiency of electric motors in accordance with international standards.
