# FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_US Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_US(Int32).html

---

Energy efficiency class US # 26308.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_US( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ENERGY_EFFICIENCY_CLASS_US {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Energy efficiency class for the United States. There are three different energy efficiency classes in the United States: 1. DOA standard: Minimum standard that must be met. 2. Energy Star: Energy-efficient devices. 3. Most efficient: Especially energy-efficient devices.
