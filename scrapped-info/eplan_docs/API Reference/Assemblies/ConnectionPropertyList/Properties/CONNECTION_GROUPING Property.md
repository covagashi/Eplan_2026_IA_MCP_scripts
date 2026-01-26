# CONNECTION_GROUPING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_GROUPING().html

---

Grouping # 31069.

Syntax

**C#**



public PropertyValue CONNECTION_GROUPING {get; set;}

public:

property PropertyValue^ CONNECTION_GROUPING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Using this property, free groups of connections can be defined that can then be given special names using connection numbering. This property is available for connections, connection definition points, potentials, signals, and potential definition points.
