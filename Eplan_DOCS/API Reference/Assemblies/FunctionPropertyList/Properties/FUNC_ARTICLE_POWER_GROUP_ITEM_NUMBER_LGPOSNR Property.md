# FUNC_ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic231.html

---

Performance description, standardized: Performance group item number # 26432.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Unique identification number for a specific service item within a service group in the bill of quantities. Each service group contains several service items that can be identified by such a unique number. Example: In a performance group "Piping and support systems" a specific number stands for the position "Drilling through walls and ceilings made of masonry".
