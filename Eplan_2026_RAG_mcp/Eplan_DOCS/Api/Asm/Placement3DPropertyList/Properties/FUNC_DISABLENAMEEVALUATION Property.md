# FUNC_DISABLENAMEEVALUATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_DISABLENAMEEVALUATION().html

---

Use displayed DT as full DT # 20051.

Syntax

**C#**



public PropertyValue FUNC_DISABLENAMEEVALUATION {get; set;}

public:

property PropertyValue^ FUNC_DISABLENAMEEVALUATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is enabled, the DT calculation, i.e. the calculation of the full DT from the visible DT, is entirely disabled. Instead, the visible DT is used directly as the full DT. This helps prevent an undesired transfer of hierarchy properties or nested elements on a full DT.
