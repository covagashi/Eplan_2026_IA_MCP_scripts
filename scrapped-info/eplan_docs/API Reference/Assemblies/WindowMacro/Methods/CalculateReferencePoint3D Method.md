# CalculateReferencePoint3D Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~CalculateReferencePoint3D.html

---

Calculates the reference point of the macro Used to calculate reference point if reference point has not been defined by the user, when creating a macro. When reference point has been defined for then given macro, then output parameter is equal to ReferencePoint property.

Syntax

**C#**



public bool CalculateReferencePoint3D( 

   ref PointD3D referencePoint

)

public:

bool CalculateReferencePoint3D( 

   PointD3D% referencePoint

)


#### Parameters

*referencePoint*
:   Output parameter - Reference point

#### Return Value

true : when calculation was successful.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro was not opend before or could not opened successfully. |
