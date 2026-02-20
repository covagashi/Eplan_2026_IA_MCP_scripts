# ARTICLE_POWER_LOSS_STATIC_CURRENT_INDEPENDENT_PVS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1656.html

---

Power dissipation (static), current-independent # 26160.

Syntax

**C#**



public MDPropertyValue ARTICLE_POWER_LOSS_STATIC_CURRENT_INDEPENDENT_PVS {get; set;}

public:

property MDPropertyValue^ ARTICLE_POWER_LOSS_STATIC_CURRENT_INDEPENDENT_PVS {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Power dissipation (electrical heat losses) of a device which is independent of the current flowing through, that is to say without load-current-dependent components. This power dissipation is specified in watts (W) and remains constant, irrespective of whether the device is in operation or not. Example: An LED element has a static power dissipation of 0.45 W.
