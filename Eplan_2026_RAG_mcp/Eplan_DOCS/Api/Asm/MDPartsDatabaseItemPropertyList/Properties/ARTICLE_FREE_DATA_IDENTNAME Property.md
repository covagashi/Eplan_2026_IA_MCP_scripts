# ARTICLE_FREE_DATA_IDENTNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FREE_DATA_IDENTNAME(Int32).html

---

User-defined properties: Identifying name # 22336.

Syntax

**C#**



public MDPropertyValue ARTICLE_FREE_DATA_IDENTNAME( 

   int index

) {get; set;}

public:

property MDPropertyValue^ ARTICLE_FREE_DATA_IDENTNAME {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Identifying name of the user-defined property. More than 1000 assignments can be made using the index.
