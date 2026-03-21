# ARTICLE_FLOW_FULL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FLOW_FULL().html

---

Flow (full) # 22232.

Syntax

**C#**



public MDPropertyValue ARTICLE_FLOW_FULL {get; set;}

public:

property MDPropertyValue^ ARTICLE_FLOW_FULL {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Flow with information about the unit. The full value with all decimal places is always stored; the value is not rounded up. This ensures precision is retained when converting to a different unit.
