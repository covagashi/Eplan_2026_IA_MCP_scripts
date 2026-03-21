# ARTICLE_SERVICE_BREAKING_CAPACITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_SERVICE_BREAKING_CAPACITY().html

---

Service short-circuit breaking capacity (Ics) # 26588.

Syntax

**C#**



public MDPropertyValue ARTICLE_SERVICE_BREAKING_CAPACITY {get; set;}

public:

property MDPropertyValue^ ARTICLE_SERVICE_BREAKING_CAPACITY {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The service short-circuit breaking capacity (abbreviated "Ics") describes the repeated breaking capacity during normal operation. The value indicates the maximum short-circuit current that a power circuit breaker can switch off without damage.
