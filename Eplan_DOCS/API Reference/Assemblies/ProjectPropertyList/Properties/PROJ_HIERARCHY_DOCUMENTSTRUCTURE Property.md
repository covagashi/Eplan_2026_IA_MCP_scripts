# PROJ_HIERARCHY_DOCUMENTSTRUCTURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_DOCUMENTSTRUCTURE().html

---

Project structure: Document type # 10006.

Syntax

**C#**



public PropertyValue PROJ_HIERARCHY_DOCUMENTSTRUCTURE {get; set;}

public:

property PropertyValue^ PROJ_HIERARCHY_DOCUMENTSTRUCTURE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The document type valid only for pages and external documents is stored in this project structure. The KKS identifier is normally entered here.
