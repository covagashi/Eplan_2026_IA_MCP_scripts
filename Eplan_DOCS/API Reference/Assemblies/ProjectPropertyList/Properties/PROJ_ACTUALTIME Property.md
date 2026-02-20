# PROJ_ACTUALTIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ACTUALTIME().html

---

Time of the day # 10058.

Syntax

**C#**



public PropertyValue PROJ_ACTUALTIME {get; set;}

public:

property PropertyValue^ PROJ_ACTUALTIME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

This property is read-only..

Provides the current date as a character string corresponding to the currently defined formatting. The time is output in the local time of the user in accordance with the set time zone.
