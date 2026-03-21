# ARTICLE_CONTROL_PRESSURE_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CONTROL_PRESSURE_MIN().html

---

Pilot pressure, min. # 26151.

Syntax

**C#**



public MDPropertyValue ARTICLE_CONTROL_PRESSURE_MIN {get; set;}

public:

property MDPropertyValue^ ARTICLE_CONTROL_PRESSURE_MIN {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum pressure required to control a pneumatic or hydraulic system. This value is usually specified in bar or pascal. Minimum pressure for actuating fluid power valves with a pneumatic or pilot-controlled electrical actuating device.
