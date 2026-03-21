# ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MIN().html

---

Supply voltage (AC 50 Hz), min. # 26164.

Syntax

**C#**



public PropertyValue ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MIN {get; set;}

public:

property PropertyValue^ ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MIN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum AC voltage that may be applied to the supply input of a device temporarily or continuously so that the device functions correctly at a frequency of 50 Hz. This voltage is specified in volts (V).
