# ARTICLE_MIDDLEOFFSET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MIDDLEOFFSET().html

---

Center mismatch # 22215.

Syntax

**C#**



public MDPropertyValue ARTICLE_MIDDLEOFFSET {get; set;}

public:

property MDPropertyValue^ ARTICLE_MIDDLEOFFSET {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

If you do not want the part to be centered in the front view, enter the offset relative to the middle of the mounting rail. The item will then be automatically offset by this value.
