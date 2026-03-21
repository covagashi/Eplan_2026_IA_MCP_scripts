# ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_ABSOLUTE_PRESSURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1713.html

---

Process pressure (absolute pressure), max. # 26518.

Syntax

**C#**



public MDPropertyValue ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_ABSOLUTE_PRESSURE {get; set;}

public:

property MDPropertyValue^ ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_ABSOLUTE_PRESSURE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Highest absolute process pressure to which the parts of the device that are in contact with the media can be exposed without permanent limitation of the operating behavior. The absolute process pressure is measured in comparison to the absolute vacuum and is composed of the atmospheric pressure and the process pressure.
