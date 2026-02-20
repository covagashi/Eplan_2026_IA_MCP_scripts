# AddDaisyChain Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint~AddDaisyChain(NetConnectionPoint[]).html

---

Creates new DaisyChain object

Syntax

**C#**



public DaisyChain AddDaisyChain( 

   NetDefinitionPoint.NetConnectionPoint[] netConnectionPoints

)

public:

DaisyChain^ AddDaisyChain( 

   array<NetDefinitionPoint.NetConnectionPoint^>^ netConnectionPoints

)


#### Parameters

*netConnectionPoints*
:   [NetDefinitionPoint.NetConnectionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint+NetConnectionPoint.html)s between which new connections are made.

#### Return Value

New created DaisyChain

Exceptions

| Exception | Description |
| --- | --- |
| [NoSuchPinException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NoSuchPinException.html) | Thrown when one of a given [PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html) is not in NetDefinitionPoint connectionPoints. |
