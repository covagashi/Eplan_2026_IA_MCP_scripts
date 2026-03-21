# FUNC_TERMINAL_FORM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINAL_FORM().html

---

Terminal / plug diagram form # 20806.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_FORM {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_FORM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of the terminal or plug diagram form to be used for reporting the terminal strip or plug.

If you assign a value using the Application Programming Interface, please ensure that the relevant master data are available in the project.
