# PAGE_CREATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_CREATIONDATE().html

---

Creation date # 11021.

Syntax

**C#**



public PropertyValue PAGE_CREATIONDATE {get; set;}

public:

property PropertyValue^ PAGE_CREATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date the page was created. The time is output in the local time of the user in accordance with the set time zone.
