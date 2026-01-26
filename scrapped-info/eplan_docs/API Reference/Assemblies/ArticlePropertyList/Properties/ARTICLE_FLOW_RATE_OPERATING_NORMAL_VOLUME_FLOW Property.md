# ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW().html

---

Flow rate (operating / standard volume flow) # 26263.

Syntax

**C#**



public PropertyValue ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW {get; set;}

public:

property PropertyValue^ ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Substance quantity per time unit stated as operating or standard flow rate. The most common unit for a flow rate is cubic meters per second (m³/s). For certain orders of magnitude or applications, other units are also customary, for example milliliters per minute.
