# ARTICLE_MOUNTINGSPACE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MOUNTINGSPACE().html

---

Space requirement # 22047.

Syntax

**C#**



public MDPropertyValue ARTICLE_MOUNTINGSPACE {get; set;}

public:

property MDPropertyValue^ ARTICLE_MOUNTINGSPACE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Specify the space requirement of the part here. If values are entered for the properties Width and Height, the space requirement is determined automatically in accordance with the following formula: (w\*h) with w = Width and h = Height.
