# PAGE_CREATIONTIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_CREATIONTIME().html

---

Creation time # 11002.

Syntax

**C#**



public PropertyValue PAGE_CREATIONTIME {get; set;}

public:

property PropertyValue^ PAGE_CREATIONTIME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The time the page was created. How the time is displayed can be configured in the project settings. The time is output in the local time of the user in accordance with the set time zone.
