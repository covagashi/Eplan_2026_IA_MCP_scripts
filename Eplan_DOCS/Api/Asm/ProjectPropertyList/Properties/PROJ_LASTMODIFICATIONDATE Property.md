# PROJ_LASTMODIFICATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTMODIFICATIONDATE().html

---

Modification date # 10023.

Syntax

**C#**



public PropertyValue PROJ_LASTMODIFICATIONDATE {get; set;}

public:

property PropertyValue^ PROJ_LASTMODIFICATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

This property is read-only..

Date of last changes to the project. The time is output in the local time of the user in accordance with the set time zone.
