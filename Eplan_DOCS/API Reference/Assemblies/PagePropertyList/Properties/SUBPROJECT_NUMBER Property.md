# SUBPROJECT_NUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~SUBPROJECT_NUMBER().html

---

Subproject number # 25101.

Syntax

**C#**



public PropertyValue SUBPROJECT_NUMBER {get; set;}

public:

property PropertyValue^ SUBPROJECT_NUMBER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Number of the subproject. During the creation of subprojects a name is assigned automatically to each subproject. This is made up of the name of the original project and the subproject number. The subproject numbers are assigned in accordance with the order of defined working sections.
