# FUNC_ARTICLE_ACCURACY_FOR_OPERATING_VOLUME_FLOW_RATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic212.html

---

Actual volume flow: Accuracy # 26361.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ACCURACY_FOR_OPERATING_VOLUME_FLOW_RATE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ACCURACY_FOR_OPERATING_VOLUME_FLOW_RATE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Describes the precision with which a device or system can measure the flow rate of an operating volume. This specification is often expressed as a percentage (%) and indicates how accurate the measurements are compared to the actual flow rate.
