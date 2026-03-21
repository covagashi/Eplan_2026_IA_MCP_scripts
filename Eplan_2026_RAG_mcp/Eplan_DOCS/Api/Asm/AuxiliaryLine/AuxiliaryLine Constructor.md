# AuxiliaryLine Constructor

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.AuxiliaryLine~_ctor(Project,Boolean,PointD3D,PointD3D).html

---

Creates not placed AuxiliaryLine object with defined start and end position.

Syntax

**C#**



public AuxiliaryLine( 

   Project pProject,

   bool bTransient,

   PointD3D oStartPoint,

   PointD3D oEndPoint

)

public:

AuxiliaryLine( 

   Project^ pProject,

   bool bTransient,

   PointD3D oStartPoint,

   PointD3D oEndPoint

)


#### Parameters

*pProject*
:   Project to which this object will be assign. Can't be null.

*bTransient*
:   Flag to determine if object will be permanently store in database or will be transient.

*oStartPoint*
:   Position of the object beginning.

*oEndPoint*
:   Position of the AuxiliaryLine end.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the duct cannot be created. |

Remarks

Position of start and end points are expressed relatively to the parent which will be assign for this object.
