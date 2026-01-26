# FUNC_PLCCONFIGURATIONPROJECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCONFIGURATIONPROJECT().html

---

Configuration project (at PLC boxes and bus ports) # 20161.

Syntax

**C#**



public PropertyValue FUNC_PLCCONFIGURATIONPROJECT {get; set;}

public:

property PropertyValue^ FUNC_PLCCONFIGURATIONPROJECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Main group orientation element of bus data. All objects to which the same configuration project is assigned belong together and represent the PLC configuration.
