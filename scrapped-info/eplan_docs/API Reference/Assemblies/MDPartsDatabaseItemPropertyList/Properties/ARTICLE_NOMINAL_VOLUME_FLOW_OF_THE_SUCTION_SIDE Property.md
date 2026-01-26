# ARTICLE_NOMINAL_VOLUME_FLOW_OF_THE_SUCTION_SIDE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1592.html

---

Nominal flow rate (intake side) # 26508.

Syntax

**C#**



public MDPropertyValue ARTICLE_NOMINAL_VOLUME_FLOW_OF_THE_SUCTION_SIDE {get; set;}

public:

property MDPropertyValue^ ARTICLE_NOMINAL_VOLUME_FLOW_OF_THE_SUCTION_SIDE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Flow rate that flows through the suction side of an appliance or system when it is operated under the specified nominal conditions. In the case of devices such as fans, pumps and compressors, this indicates the quantity of medium (for example air or liquid) which is sucked in per unit of time.
