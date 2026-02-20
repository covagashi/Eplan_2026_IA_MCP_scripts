# CONNECTION_IS_PIPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CONNECTION_IS_PIPE().html

---

Line # 31146.

Syntax

**C#**



public PropertyValue CONNECTION_IS_PIPE {get; set;}

public:

property PropertyValue^ CONNECTION_IS_PIPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Indicates whether the connection can be part of a line. This property is activated or deactivated in accordance with the set value for the Connection: Association (ID 31142) property.
