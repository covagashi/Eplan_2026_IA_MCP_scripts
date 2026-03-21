# ARTICLE_EXTERNAL_DOCUMENT_12 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_EXTERNAL_DOCUMENT_12().html

---

External document 12 # 22243.

Syntax

**C#**



public MDPropertyValue ARTICLE_EXTERNAL_DOCUMENT_12 {get; set;}

public:

property MDPropertyValue^ ARTICLE_EXTERNAL_DOCUMENT_12 {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The "External document [n]" properties always show the nth external document assigned to the part. For example "External document 1" shows the first external document assigned to the part.
