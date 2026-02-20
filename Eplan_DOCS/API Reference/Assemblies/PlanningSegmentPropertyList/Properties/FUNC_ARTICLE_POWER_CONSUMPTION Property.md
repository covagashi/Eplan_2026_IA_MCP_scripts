# FUNC_ARTICLE_POWER_CONSUMPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic993.html

---

Performance description (item, device) # 26428.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_POWER_DESCRIPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_POWER_DESCRIPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Describing texts or notes on an item or device. Example: The performance description of a motor can contain information about its maximum performance, rotation speed, efficiency class and operating areas.
