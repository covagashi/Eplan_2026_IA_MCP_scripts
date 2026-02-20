# ARTICLE_SUBCRAFT_FLUID_UNDEFINED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1683.html

---

Subtrade 'Fluid power (undefined)' # 22267.

Syntax

**C#**



public MDPropertyValue ARTICLE_SUBCRAFT_FLUID_UNDEFINED( 

   int index

) {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUBCRAFT_FLUID_UNDEFINED {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 20.

This property can be used to create several subtrades for a trade.
