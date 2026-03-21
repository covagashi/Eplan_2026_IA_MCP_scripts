# INSTANCE_PAGENAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_PAGENAME().html

---

Page name # 19022.

Syntax

**C#**



public PropertyValue INSTANCE_PAGENAME {get; set;}

public:

property PropertyValue^ INSTANCE_PAGENAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

For component or part placements, outputs the page names (page counters + subcounters) of the page on which the corresponding component or item is placed.
