# PAGE_LASTMANUMODIFICATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_LASTMANUMODIFICATIONDATE().html

---

Modification date (manual) # 11023.

Syntax

**C#**



public PropertyValue PAGE_LASTMANUMODIFICATIONDATE {get; set;}

public:

property PropertyValue^ PAGE_LASTMANUMODIFICATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Manually entered modification date. The time is output in the local time of the user in accordance with the set time zone.
