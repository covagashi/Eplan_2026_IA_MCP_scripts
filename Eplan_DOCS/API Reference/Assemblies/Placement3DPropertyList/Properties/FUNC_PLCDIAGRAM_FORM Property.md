# FUNC_PLCDIAGRAM_FORM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCDIAGRAM_FORM().html

---

PLC diagram form # 20187.

Syntax

**C#**



public PropertyValue FUNC_PLCDIAGRAM_FORM {get; set;}

public:

property PropertyValue^ FUNC_PLCDIAGRAM_FORM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This allows PLC cards (the PLC boxes) to each be assigned a separate report (a PLC diagram). The form set for the main function is only taken into account when generating reports.

If you assign a value using the Application Programming Interface, please ensure that the relevant master data exist in the project.
