# EndConnectionPointPosition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D~EndConnectionPointPosition.html

---

[Eplan.EplApi.DataModel.ConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition.html) by which this connection is connected to [Eplan.EplApi.DataModel.Connection.EndSymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~EndSymbolReference.html).

Syntax

**C#**



public ConnectionPointPosition EndConnectionPointPosition {get;}

public:

property ConnectionPointPosition^ EndConnectionPointPosition {

   ConnectionPointPosition^ get();

}


Remarks

This property is `null` if end symbol references has no connection point positions.
