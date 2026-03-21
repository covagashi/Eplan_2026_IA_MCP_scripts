# FUNC_ARTICLE_NOMINAL_VOLUME_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic965.html

---

Nominal flow rate (intake side) # 26509.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_VOLUME_FLOW_OF_THE_SUCTION_SIDE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_VOLUME_FLOW_OF_THE_SUCTION_SIDE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Flow rate that flows through the suction side of an appliance or system when it is operated under the specified nominal conditions. In the case of devices such as fans, pumps and compressors, this indicates the quantity of medium (for example air or liquid) which is sucked in per unit of time.
