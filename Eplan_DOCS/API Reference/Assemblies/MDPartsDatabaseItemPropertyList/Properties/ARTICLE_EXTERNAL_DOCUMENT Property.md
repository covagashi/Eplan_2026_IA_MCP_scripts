# ARTICLE_EXTERNAL_DOCUMENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_EXTERNAL_DOCUMENT(Int32).html

---

External document # 22210.

Syntax

**C#**



public MDPropertyValue ARTICLE_EXTERNAL_DOCUMENT( 

   int index

) {get; set;}

public:

property MDPropertyValue^ ARTICLE_EXTERNAL_DOCUMENT {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 20.
