# FUNC_ARTICLE_PROVISION_OF_THE_CABLE_GLAND Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1009.html

---

Transport capacity # 26325.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PUMPING_CAPACITY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PUMPING_CAPACITY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume of material or fluid that can be conveyed per unit of time.
