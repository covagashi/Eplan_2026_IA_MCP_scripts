# CONNECTION_KINDOFWIRE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_KINDOFWIRE().html

---

Connection: Association # 31142.

Syntax

**C#**



public PropertyValue CONNECTION_KINDOFWIRE {get; set;}

public:

property PropertyValue^ CONNECTION_KINDOFWIRE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property specifies whether the connection is an individual connection or can be part of a cable, conduit, phase busbar, etc. Possible values are:

0 = Individual connection

1 = Cable

2 = Conduit

3 = Phase busbar

4 = Line.
