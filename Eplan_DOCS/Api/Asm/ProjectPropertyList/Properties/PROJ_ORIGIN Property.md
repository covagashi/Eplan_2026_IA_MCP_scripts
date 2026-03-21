# PROJ_ORIGIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ORIGIN().html

---

Project: Template # 10069.

Syntax

**C#**



public PropertyValue PROJ_ORIGIN {get; set;}

public:

property PropertyValue^ PROJ_ORIGIN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Displays the template (basic project, or, for a copied project, the source project) from which the project was created. To differentiate, the file extension is displayed in addition to the file name.
