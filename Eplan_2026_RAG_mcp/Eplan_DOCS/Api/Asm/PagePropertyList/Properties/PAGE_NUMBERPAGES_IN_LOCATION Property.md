# PAGE_NUMBERPAGES_IN_LOCATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_NUMBERPAGES_IN_LOCATION().html

---

Number of pages per structure # 11004.

Syntax

**C#**



public PropertyValue PAGE_NUMBERPAGES_IN_LOCATION {get; set;}

public:

property PropertyValue^ PAGE_NUMBERPAGES_IN_LOCATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Indicates the number of pages within a structure identifier. For example, if three pages are available under the location designation "ET1", "3" is output here.
