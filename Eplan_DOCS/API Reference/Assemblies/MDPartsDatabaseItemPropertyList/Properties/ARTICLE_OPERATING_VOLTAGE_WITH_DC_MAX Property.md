# ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1611.html

---

Operating voltage (DC), max. # 26091.

Syntax

**C#**



public MDPropertyValue ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The maximum possible DC voltage value specified by the manufacturer, which can be applied to an electrical device taking into account the conditions of use and which the various product-specific tests (inter alia insulation, switching capacity) reference.
