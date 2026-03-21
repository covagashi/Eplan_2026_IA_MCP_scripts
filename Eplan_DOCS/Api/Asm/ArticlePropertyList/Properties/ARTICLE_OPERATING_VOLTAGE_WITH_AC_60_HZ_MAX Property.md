# ARTICLE_OPERATING_VOLTAGE_WITH_AC_60_HZ_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_AC_60_HZ_MAX().html

---

Operating voltage (AC 60 Hz), max. # 26089.

Syntax

**C#**



public PropertyValue ARTICLE_OPERATING_VOLTAGE_WITH_AC_60_HZ_MAX {get; set;}

public:

property PropertyValue^ ARTICLE_OPERATING_VOLTAGE_WITH_AC_60_HZ_MAX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The maximum possible AC voltage value at 60 Hz specified by the manufacturer, which can be applied to an electrical device taking into account the conditions of use and which the various product-specific tests (inter alia insulation, switching capacity) reference.
