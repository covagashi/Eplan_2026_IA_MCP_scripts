# PROJ_HIERARCHY_CODEDSEPARATORS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_CODEDSEPARATORS().html

---

Separator for structures # 10018.

Syntax

**C#**



public PropertyValue PROJ_HIERARCHY_CODEDSEPARATORS {get; set;}

public:

property PropertyValue^ PROJ_HIERARCHY_CODEDSEPARATORS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Contains all structure separators in coded form (except the document structure).

Format: Number of entries and then, separated by tabs, higher-level and lower level structure identifier.
