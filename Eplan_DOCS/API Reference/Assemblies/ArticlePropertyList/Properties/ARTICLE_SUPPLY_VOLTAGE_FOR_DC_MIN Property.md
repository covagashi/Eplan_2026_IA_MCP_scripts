# ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN().html

---

Supply voltage (DC), min. # 26170.

Syntax

**C#**



public PropertyValue ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN {get; set;}

public:

property PropertyValue^ ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum DC voltage that may be applied to the supply input of a device temporarily or continuously in order for the device to function correctly. This voltage is specified in volts (V).
