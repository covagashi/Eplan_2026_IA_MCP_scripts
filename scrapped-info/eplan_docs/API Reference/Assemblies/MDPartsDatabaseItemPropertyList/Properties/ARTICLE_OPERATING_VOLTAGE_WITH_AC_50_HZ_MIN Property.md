# ARTICLE_OPERATING_VOLTAGE_WITH_AC_50_HZ_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1608.html

---

Operating voltage (AC 50 Hz), min. # 26088.

Syntax

**C#**



public MDPropertyValue ARTICLE_OPERATING_VOLTAGE_WITH_AC_50_HZ_MIN {get; set;}

public:

property MDPropertyValue^ ARTICLE_OPERATING_VOLTAGE_WITH_AC_50_HZ_MIN {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The minimum possible AC voltage value at 50 Hz specified by the manufacturer, which can be applied to an electrical device taking into account the conditions of use and which the various product-specific tests (inter alia insulation, switching capacity) reference.
