# PAGE_SCALE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_SCALE().html

---

Scale # 11048.

Syntax

**C#**



public PropertyValue PAGE_SCALE {get; set;}

public:

property PropertyValue^ PAGE_SCALE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Scale 1:x. A dimension definition can be added to every page, regardless of type. This is required when you are using dimensions or to correctly scale graphical macros when inserting them.
