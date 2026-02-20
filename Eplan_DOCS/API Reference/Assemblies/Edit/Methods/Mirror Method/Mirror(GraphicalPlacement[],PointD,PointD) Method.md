# Mirror(GraphicalPlacement[],PointD,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~Mirror(GraphicalPlacement[],PointD,PointD).html

---

Moves objects to its mirror position.

Syntax

**C#**



public void Mirror( 

   GraphicalPlacement[] plcmnts,

   PointD oPntStart,

   PointD oPntEnd

)

public:

void Mirror( 

   array<GraphicalPlacement^>^ plcmnts,

   PointD oPntStart,

   PointD oPntEnd

)


#### Parameters

*plcmnts*
:   Placements to move.

*oPntStart*
:   Starting point of a line(mirror)

*oPntEnd*
:   Ending point of a line(mirror)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
| [System.ArgumentException](#) | Is thrown in case of oPntStart is equal to oPntEnd |
