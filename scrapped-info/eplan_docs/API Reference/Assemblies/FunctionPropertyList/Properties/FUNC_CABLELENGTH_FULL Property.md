# FUNC_CABLELENGTH_FULL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CABLELENGTH_FULL().html

---

Cable / Conduit: Length (full) # 20257.

Syntax

**C#**



public PropertyValue FUNC_CABLELENGTH_FULL {get; set;}

public:

property PropertyValue^ FUNC_CABLELENGTH_FULL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Length of the cable or conduit including units. The full value with all decimal places is always stored; the value is not rounded up. This ensures precision is retained when converting to a different unit.
