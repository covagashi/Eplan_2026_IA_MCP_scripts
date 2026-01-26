# PROJ_LASTMODIFICATIONTIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTMODIFICATIONTIME().html

---

Modification time # 10047.

Syntax

**C#**



public PropertyValue PROJ_LASTMODIFICATIONTIME {get; set;}

public:

property PropertyValue^ PROJ_LASTMODIFICATIONTIME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The time the project was last changed. How the time is displayed can be configured in the project settings. The time is output in the local time of the user in accordance with the set time zone.
