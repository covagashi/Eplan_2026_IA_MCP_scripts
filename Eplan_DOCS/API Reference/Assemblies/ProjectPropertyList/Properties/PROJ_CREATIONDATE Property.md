# PROJ_CREATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATIONDATE().html

---

Creation date # 10021.

Syntax

**C#**



public PropertyValue PROJ_CREATIONDATE {get; set;}

public:

property PropertyValue^ PROJ_CREATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date the project was created. The property is automatically assigned and cannot be changed. The time is output in the local time of the user in accordance with the set time zone.
