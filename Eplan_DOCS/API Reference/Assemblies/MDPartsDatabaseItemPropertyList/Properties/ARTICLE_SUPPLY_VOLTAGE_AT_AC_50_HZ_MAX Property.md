# ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1688.html

---

Supply voltage (AC 50 Hz), max. # 26163.

Syntax

**C#**



public MDPropertyValue ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum AC voltage that may be applied to the supply input of a device temporarily or continuously so that the device functions correctly at a frequency of 50 Hz. This voltage is specified in volts (V).
