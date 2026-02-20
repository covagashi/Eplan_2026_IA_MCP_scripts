# ARTICLE_EXTERNAL_DOCUMENT_10 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_EXTERNAL_DOCUMENT_10().html

---

External document 10 # 22241.

Syntax

**C#**



public MDPropertyValue ARTICLE_EXTERNAL_DOCUMENT_10 {get; set;}

public:

property MDPropertyValue^ ARTICLE_EXTERNAL_DOCUMENT_10 {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The "External document [n]" properties always show the nth external document assigned to the part. For example "External document 1" shows the first external document assigned to the part.
