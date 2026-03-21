# PAGE_LASTAUTOMODIFICATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_LASTAUTOMODIFICATIONDATE().html

---

Modification date (automatic) # 11024.

Syntax

**C#**



public PropertyValue PAGE_LASTAUTOMODIFICATIONDATE {get; set;}

public:

property PropertyValue^ PAGE_LASTAUTOMODIFICATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date of last change to the page. The time is output in the local time of the user in accordance with the set time zone.
