# ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1548.html

---

Current carrying capacity (resistive load, DC), max. # 26156.

Syntax

**C#**



public MDPropertyValue ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The maximum electrical current with which a device or item may be loaded so that the device or item is in the specification range if only external ohmic resistors are connected in the closed circuit.
