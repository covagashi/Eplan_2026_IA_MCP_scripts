# ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX().html

---

Operating voltage (DC), max. # 26091.

Syntax

**C#**



public PropertyValue ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX {get; set;}

public:

property PropertyValue^ ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The maximum possible DC voltage value specified by the manufacturer, which can be applied to an electrical device taking into account the conditions of use and which the various product-specific tests (inter alia insulation, switching capacity) reference.
