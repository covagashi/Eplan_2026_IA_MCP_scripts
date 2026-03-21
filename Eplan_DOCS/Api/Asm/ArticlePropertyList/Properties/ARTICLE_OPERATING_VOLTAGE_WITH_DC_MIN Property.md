# ARTICLE_OPERATING_VOLTAGE_WITH_DC_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_DC_MIN().html

---

Operating voltage (DC), min. # 26092.

Syntax

**C#**



public PropertyValue ARTICLE_OPERATING_VOLTAGE_WITH_DC_MIN {get; set;}

public:

property PropertyValue^ ARTICLE_OPERATING_VOLTAGE_WITH_DC_MIN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The minimum possible DC voltage value specified by the manufacturer, which can be applied to an electrical device taking into account the conditions of use and which the various product-specific tests (inter alia insulation, switching capacity) reference.
