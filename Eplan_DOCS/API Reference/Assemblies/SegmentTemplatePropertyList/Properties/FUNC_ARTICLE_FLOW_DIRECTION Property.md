# FUNC_ARTICLE_FLOW_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1161.html

---

Flow rate (operating / standard volume flow) # 26264.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Substance quantity per time unit stated as operating or standard flow rate. The most common unit for a flow rate is cubic meters per second (m³/s). For certain orders of magnitude or applications, other units are also customary, for example milliliters per minute.
