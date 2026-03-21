# FUNC_MANAGE_FUNCTIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_MANAGE_FUNCTIONS().html

---

Manage unplaced auxiliary functions at the main function # 20476.

Syntax

**C#**



public PropertyValue FUNC_MANAGE_FUNCTIONS {get; set;}

public:

property PropertyValue^ FUNC_MANAGE_FUNCTIONS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated at a main function, the assigned, unplaced auxiliary functions are managed together with the main function. This means that when the main function is copied and pasted, the unplaced auxiliary functions are also copied and pasted and automatically renamed - analog to the behavior at function templates. If the main function is deleted, the assigned unplaced auxiliary functions are also deleted.

This property calculates the value of the relevant main function for auxiliary functions.
