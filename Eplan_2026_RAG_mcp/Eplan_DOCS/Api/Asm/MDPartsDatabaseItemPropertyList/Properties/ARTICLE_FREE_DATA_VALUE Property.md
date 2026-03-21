# ARTICLE_FREE_DATA_VALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FREE_DATA_VALUE(Int32).html

---

Free properties: Value # 22147.

Syntax

**C#**



public MDPropertyValue ARTICLE_FREE_DATA_VALUE( 

   int index

) {get; set;}

public:

property MDPropertyValue^ ARTICLE_FREE_DATA_VALUE {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Value of the free property. More than 1000 assignments can be made using the index.
