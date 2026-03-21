# FUNC_CABLEAUTONAMED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CABLEAUTONAMED().html

---

Name automatically assigned # 20091.

Syntax

**C#**



public PropertyValue FUNC_CABLEAUTONAMED {get; set;}

public:

property PropertyValue^ FUNC_CABLEAUTONAMED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Unnamed cable definitions, shields, and connection definition points are assigned to this property during automatic cable generation. Automatically assigned names are deleted and newly assigned in the next automatic run; manually assigned names are retained.
