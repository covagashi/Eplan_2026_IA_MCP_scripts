# ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MAX().html

---

Supply voltage (DC), max. # 26169.

Syntax

**C#**



public MDPropertyValue ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum DC voltage that may be applied to the supply input of a device temporarily or continuously in order for the device to function correctly. This voltage is specified in volts (V).
