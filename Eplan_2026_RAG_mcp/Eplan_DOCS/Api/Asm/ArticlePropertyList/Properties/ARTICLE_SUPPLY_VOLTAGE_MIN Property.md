# ARTICLE_SUPPLY_VOLTAGE_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_MIN().html

---

Supply voltage, min. # 26173.

Syntax

**C#**



public PropertyValue ARTICLE_SUPPLY_VOLTAGE_MIN {get; set;}

public:

property PropertyValue^ ARTICLE_SUPPLY_VOLTAGE_MIN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum value of the voltage that must be applied to the supply input of a device temporarily or continuously in order for the device to function correctly. This voltage is specified in volts (V).
