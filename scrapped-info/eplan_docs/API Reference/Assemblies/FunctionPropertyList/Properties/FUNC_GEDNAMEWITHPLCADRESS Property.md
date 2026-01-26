# FUNC_GEDNAMEWITHPLCADRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_GEDNAMEWITHPLCADRESS().html

---

PLC address (with displayed DT) # 20037.

Syntax

**C#**



public PropertyValue FUNC_GEDNAMEWITHPLCADRESS {get; set;}

public:

property PropertyValue^ FUNC_GEDNAMEWITHPLCADRESS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the entered designation for PLC connection points. This consists of the combination of a "normal DT" and PLC address, separated by a colon (or a character that can be freely defined).
