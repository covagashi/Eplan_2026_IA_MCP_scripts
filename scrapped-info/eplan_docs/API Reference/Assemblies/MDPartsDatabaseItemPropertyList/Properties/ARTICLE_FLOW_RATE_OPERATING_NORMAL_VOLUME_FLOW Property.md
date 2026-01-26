# ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1562.html

---

Flow rate (operating / standard volume flow) # 26263.

Syntax

**C#**



public MDPropertyValue ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW {get; set;}

public:

property MDPropertyValue^ ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Substance quantity per time unit stated as operating or standard flow rate. The most common unit for a flow rate is cubic meters per second (m³/s). For certain orders of magnitude or applications, other units are also customary, for example milliliters per minute.
