# PROJECT_SITE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_SITE().html

---

AutomationML: Works # 10951.

Syntax

**C#**



public PropertyValue PROJECT_SITE {get; set;}

public:

property PropertyValue^ PROJECT_SITE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property can be used for the AutomationML export to specify an additional structure. If this property is filled, it is output in the AML file above the project structure defined by the identifier blocks.
