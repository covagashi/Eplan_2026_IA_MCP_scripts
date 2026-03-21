# PROJ_CREATIONTIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATIONTIME().html

---

Creation time # 10046.

Syntax

**C#**



public PropertyValue PROJ_CREATIONTIME {get; set;}

public:

property PropertyValue^ PROJ_CREATIONTIME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The time the project was created. How the time is displayed can be configured in the project settings. The time is output in the local time of the user in accordance with the set time zone.
