# CreateTransient(Project,SymbolReference,SymbolReference,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1293.html

---

Creates new transient unplaced segment and assign to it start and end symbol.

Syntax

**C#**



public void CreateTransient( 

   Project pProject,

   SymbolReference pStartSymbol,

   SymbolReference pEndSymbol

)

public:

void CreateTransient( 

   Project^ pProject,

   SymbolReference^ pStartSymbol,

   SymbolReference^ pEndSymbol

)


#### Parameters

*pProject*
:   Project to which this object will be assigned. Can't be `null`.

*pStartSymbol*
:   Symbol which will be assign as beggining of segment.

*pEndSymbol*
:   Symbol which will be assign as end of segment.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `pProject` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the `Segment` cannot be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal error has occured. Please see the exception message for details. |

Remarks

After using this method members [StartPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment~StartPoint.html) and [EndPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment~EndPoint.html) are not automaticly updated. To update it, please use method UpdatePage() or UpdateTopologySegment() of class Eplan.EplApi.HEServices.TopologyService
