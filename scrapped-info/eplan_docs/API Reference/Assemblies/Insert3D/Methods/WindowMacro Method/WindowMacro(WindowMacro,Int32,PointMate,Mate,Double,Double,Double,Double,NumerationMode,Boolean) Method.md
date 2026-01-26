# WindowMacro(WindowMacro,Int32,PointMate,Mate,Double,Double,Double,Double,NumerationMode,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1374.html

---

Places a window macro with a given mate to another mate. That means, that the position and/or orientation of the associated placements will change, so that the given mate fits to the target mate.

Syntax

**C#**



public StorableObject[] WindowMacro( 

   WindowMacro oMacro,

   int nVariant,

   PointMate oSourceMate,

   Mate oTargetMate,

   double dRotationAngle,

   double dX,

   double dY,

   double dZ,

   WindowMacro.Enums.NumerationMode nNumerationMode,

   bool bUseSourceMateOnPlacementArea

)

public:

array<StorableObject^>^ WindowMacro( 

   WindowMacro^ oMacro,

   int nVariant,

   PointMate^ oSourceMate,

   Mate^ oTargetMate,

   double dRotationAngle,

   double dX,

   double dY,

   double dZ,

   WindowMacro.Enums.NumerationMode nNumerationMode,

   bool bUseSourceMateOnPlacementArea

)


#### Parameters

*oMacro*
:   Object with opened macro.

*nVariant*
:   Index of the macro variant to be placed (0 based).

*oSourceMate*
:   given mate of macro

*oTargetMate*
:   target mate

*dRotationAngle*
:   additional rotation angle (radian)

*dX*
:   additional offset in x direction

*dY*
:   additional offset in y direction

*dZ*
:   additional offset in z direction

*nNumerationMode*
:   numeration mode

*bUseSourceMateOnPlacementArea*
:   if true, the given mate of macro will project to the placement area of macro

#### Return Value

Inserted placements

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters.. |
| **ArgumentNullException** | Null was set to a parameter. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |
