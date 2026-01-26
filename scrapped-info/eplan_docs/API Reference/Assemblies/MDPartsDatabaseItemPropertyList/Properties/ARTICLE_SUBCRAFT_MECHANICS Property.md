# ARTICLE_SUBCRAFT_MECHANICS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_SUBCRAFT_MECHANICS(Int32).html

---

Subtrade 'Mechanics' # 22094.

Syntax

**C#**



public MDPropertyValue ARTICLE_SUBCRAFT_MECHANICS( 

   int index

) {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUBCRAFT_MECHANICS {

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
