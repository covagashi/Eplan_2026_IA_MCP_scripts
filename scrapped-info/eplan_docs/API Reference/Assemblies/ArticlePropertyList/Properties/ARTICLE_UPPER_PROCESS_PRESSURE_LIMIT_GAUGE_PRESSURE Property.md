# ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_GAUGE_PRESSURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic41.html

---

Process pressure (overpressure), max. # 26520.

Syntax

**C#**



public PropertyValue ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_GAUGE_PRESSURE {get; set;}

public:

property PropertyValue^ ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_GAUGE_PRESSURE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Highest process overpressure to which parts of the device that are in contact with the media can be exposed without permanent limitation of the operating behavior. The process overpressure is measured relative to the atmospheric pressure and is the pressure which exceeds the normal atmospheric pressure.
