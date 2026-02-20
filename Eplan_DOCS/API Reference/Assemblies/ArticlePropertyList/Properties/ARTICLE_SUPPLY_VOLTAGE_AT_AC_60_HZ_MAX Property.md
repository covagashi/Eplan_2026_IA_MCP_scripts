# ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MAX().html

---

Supply voltage (AC 60 Hz), max. # 26166.

Syntax

**C#**



public PropertyValue ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MAX {get; set;}

public:

property PropertyValue^ ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MAX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum AC voltage that may be applied to the supply input of a device temporarily or continuously so that the device functions correctly at a frequency of 60 Hz. This voltage is specified in volts (V).
