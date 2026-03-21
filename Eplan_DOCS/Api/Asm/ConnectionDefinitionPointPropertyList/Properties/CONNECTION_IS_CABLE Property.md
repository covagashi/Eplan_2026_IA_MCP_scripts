# CONNECTION_IS_CABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CONNECTION_IS_CABLE().html

---

Cable connection # 31058.

Syntax

**C#**



public PropertyValue CONNECTION_IS_CABLE {get; set;}

public:

property PropertyValue^ CONNECTION_IS_CABLE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

This property is no longer in use and only taken into consideration in old projects. Indicates whether the connection can be part of a cable. If this property is not assigned to a connection or a connection definition point, the connection points determine whether this is a cable connection for the connection.
