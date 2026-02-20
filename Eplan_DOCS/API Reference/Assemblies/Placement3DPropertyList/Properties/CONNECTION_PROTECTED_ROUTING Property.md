# CONNECTION_PROTECTED_ROUTING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~CONNECTION_PROTECTED_ROUTING().html

---

Protected routing # 31113.

Syntax

**C#**



public PropertyValue CONNECTION_PROTECTED_ROUTING {get; set;}

public:

property PropertyValue^ CONNECTION_PROTECTED_ROUTING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Prevents a routing connection from being re-routed and overwritten. Also prevents that a cable is rerouted and overwritten in the topology.
