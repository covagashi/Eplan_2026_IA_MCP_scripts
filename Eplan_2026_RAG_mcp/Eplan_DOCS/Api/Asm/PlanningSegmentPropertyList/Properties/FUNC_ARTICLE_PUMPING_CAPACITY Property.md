# FUNC_ARTICLE_PUMPING_CAPACITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1010.html

---

Transport capacity of the operating fluid # 26327.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PUMPING_CAPACITY_OF_THE_OPERATING_LIQUID( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PUMPING_CAPACITY_OF_THE_OPERATING_LIQUID {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume of the operating fluid that flows through the device per unit of time.
