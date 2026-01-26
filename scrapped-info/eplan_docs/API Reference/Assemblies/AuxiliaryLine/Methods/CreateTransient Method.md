# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.AuxiliaryLine~CreateTransient.html

---

Creates transient, not placed AuxiliaryLine object with defined start and end position.

Syntax

**C#**



public static AuxiliaryLine CreateTransient( 

   Project pProject,

   PointD3D oStartPoint,

   PointD3D oEndPoint

)

public:

static AuxiliaryLine^ CreateTransient( 

   Project^ pProject,

   PointD3D oStartPoint,

   PointD3D oEndPoint

)


#### Parameters

*pProject*
:   Project to which this object will be assign. Can't be null.

*oStartPoint*
:   Position of the object beginning.

*oEndPoint*
:   Position of the AuxiliaryLine end.

#### Return Value

Created and stored in database AuxiliaryLine object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the duct cannot be created. |
