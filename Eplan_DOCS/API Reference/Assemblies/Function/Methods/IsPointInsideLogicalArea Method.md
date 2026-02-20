# IsPointInsideLogicalArea Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsPointInsideLogicalArea.html

---

Checks, if the point is inside logical area of the symbol. Returns true, if the symbol has a logical area and the point is inside. The logical area may be a rectangle or a polyline without arcs.

Syntax

**C#**



public override bool IsPointInsideLogicalArea( 

   PointD pnt

)

public:

bool IsPointInsideLogicalArea( 

   PointD pnt

) override


#### Parameters

*pnt*
:   examined point

#### Return Value

`false` the point is beyond the logical area

`true` the point is inside the logical area

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when this fact cannot be evaluated |
