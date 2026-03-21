# ARTICLE_EXTERNAL_DOCUMENT_8 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_EXTERNAL_DOCUMENT_8().html

---

External document 8 # 22239.

Syntax

**C#**



public MDPropertyValue ARTICLE_EXTERNAL_DOCUMENT_8 {get; set;}

public:

property MDPropertyValue^ ARTICLE_EXTERNAL_DOCUMENT_8 {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The "External document [n]" properties always show the nth external document assigned to the part. For example "External document 1" shows the first external document assigned to the part.
