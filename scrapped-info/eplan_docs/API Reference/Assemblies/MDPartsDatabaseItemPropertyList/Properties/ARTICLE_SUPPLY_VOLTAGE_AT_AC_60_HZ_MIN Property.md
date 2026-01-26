# ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1691.html

---

Supply voltage (AC 60 Hz), min. # 26167.

Syntax

**C#**



public MDPropertyValue ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MIN {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MIN {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum AC voltage that may be applied to the supply input of a device temporarily or continuously so that the device functions correctly at a frequency of 60 Hz. This voltage is specified in volts (V).
