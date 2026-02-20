# PROJ_HIERARCHY_CODEDNESTINGSETTINGS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_CODEDNESTINGSETTINGS().html

---

Nested device tags # 10019.

Syntax

**C#**



public PropertyValue PROJ_HIERARCHY_CODEDNESTINGSETTINGS {get; set;}

public:

property PropertyValue^ PROJ_HIERARCHY_CODEDNESTINGSETTINGS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This stores a coded value defining which device tags are nested and in what manner.

Format: Number of entries and then each setting separated by tabs (as 0 or 1 coded Boolean variables).
