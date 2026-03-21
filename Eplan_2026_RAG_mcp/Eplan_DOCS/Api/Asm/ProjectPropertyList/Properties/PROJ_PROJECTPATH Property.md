# PROJ_PROJECTPATH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_PROJECTPATH().html

---

Project path # 10010.

Syntax

**C#**



public PropertyValue PROJ_PROJECTPATH {get; set;}

public:

property PropertyValue^ PROJ_PROJECTPATH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Relative file path of the project file, starting from the directory entered in the user settings as the general project directory. Only one value can then be displayed when there is a discrepancy between the project directory entered in the user settings and the current project path.
