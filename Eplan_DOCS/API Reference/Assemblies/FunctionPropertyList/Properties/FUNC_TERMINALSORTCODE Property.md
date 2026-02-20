# FUNC_TERMINALSORTCODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINALSORTCODE().html

---

Sort code (terminal / pin) # 20809.

Syntax

**C#**



public PropertyValue FUNC_TERMINALSORTCODE {get; set;}

public:

property PropertyValue^ FUNC_TERMINALSORTCODE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Specifies the order of the pins at plugs.

Specifies the order within the terminal device at terminals. If several terminals/pins have the same sort code or the sort code is empty; these are sorted in the sequence of their designation.
