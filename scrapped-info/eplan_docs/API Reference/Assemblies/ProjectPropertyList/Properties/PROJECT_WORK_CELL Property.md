# PROJECT_WORK_CELL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJECT_WORK_CELL().html

---

AutomationML: Area # 10954.

Syntax

**C#**



public PropertyValue PROJECT_WORK_CELL {get; set;}

public:

property PropertyValue^ PROJECT_WORK_CELL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property can be used for the AutomationML export to specify an additional structure. If this property is filled, it is output in the AML file above the project structure defined by the identifier blocks.
