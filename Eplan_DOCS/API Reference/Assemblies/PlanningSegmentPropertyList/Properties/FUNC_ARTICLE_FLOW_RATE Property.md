# FUNC_ARTICLE_FLOW_RATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_FLOW_RATE(Int32).html

---

Flow rate # 26266.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FLOW_RATE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FLOW_RATE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Quotient of the volume of a substance flowing through the device and the time required for this.
