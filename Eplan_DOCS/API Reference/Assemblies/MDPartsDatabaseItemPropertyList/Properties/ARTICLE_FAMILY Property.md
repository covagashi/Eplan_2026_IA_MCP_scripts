# ARTICLE_FAMILY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FAMILY().html

---

Family # 22885.

Syntax

**C#**



public MDPropertyValue ARTICLE_FAMILY {get; set;}

public:

property MDPropertyValue^ ARTICLE_FAMILY {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Used to group several cables of the same type. This allows searching for alternatives to a cable in Cable proD (for example for prefabricated cables with the same plugs but different lengths).
