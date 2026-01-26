# FUNC_IDENTNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_IDENTNAME().html

---

Name (identifying) # 20000.

Syntax

**C#**



public PropertyValue FUNC_IDENTNAME {get; set;}

public:

property PropertyValue^ FUNC_IDENTNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Identifying name of the function, consisting of the identifying device tag, the connection point designation for connection points, and the terminal designation for terminals.
