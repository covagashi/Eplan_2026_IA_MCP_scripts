# ARTICLE_MAKING_CAPACITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MAKING_CAPACITY().html

---

Rated ultimate short-circuit making capacity (Icm) # 26589.

Syntax

**C#**



public MDPropertyValue ARTICLE_MAKING_CAPACITY {get; set;}

public:

property MDPropertyValue^ ARTICLE_MAKING_CAPACITY {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The rated ultimate short-circuit making capacity (abbreviated "Icm") is the maximum short-circuit current that a power circuit breaker can withstand at the moment of closing without damage. It is a one-time peak value that is typically higher than the rated short-circuit breaking capacity ("Icn").
