# ARTICLE_EXTERNAL_DOCUMENT_3 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_EXTERNAL_DOCUMENT_3().html

---

External document 3 # 22151.

Syntax

**C#**



public MDPropertyValue ARTICLE_EXTERNAL_DOCUMENT_3 {get; set;}

public:

property MDPropertyValue^ ARTICLE_EXTERNAL_DOCUMENT_3 {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The "External document [n]" properties always show the nth external document assigned to the part. For example "External document 1" shows the first external document assigned to the part.
