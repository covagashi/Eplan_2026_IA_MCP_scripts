# FUNC_CONTINUEPLCNUM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CONTINUEPLCNUM().html

---

Continue numbering with PLC data beyond this function # 20813.

Syntax

**C#**



public PropertyValue FUNC_CONTINUEPLCNUM {get; set;}

public:

property PropertyValue^ FUNC_CONTINUEPLCNUM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated at a function where the end of the numbering has been reached, then functions connected to this function are also numbered.
