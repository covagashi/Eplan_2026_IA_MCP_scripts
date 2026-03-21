# WindowMacro(WindowMacro,Int32,Mate,MoveKind,NumerationMode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D~WindowMacro(WindowMacro,Int32,Mate,MoveKind,NumerationMode).html

---

Places objects from window macro into layout space.

Syntax

**C#**



public StorableObject[] WindowMacro( 

   WindowMacro oMacro,

   int nVariant,

   Mate oTargetMate,

   Insert3D.MoveKind nMoveCondition,

   WindowMacro.Enums.NumerationMode nNumerationMode

)

public:

array<StorableObject^>^ WindowMacro( 

   WindowMacro^ oMacro,

   int nVariant,

   Mate^ oTargetMate,

   Insert3D.MoveKind nMoveCondition,

   WindowMacro.Enums.NumerationMode nNumerationMode

)


#### Parameters

*oMacro*
:   Opened macro object.

*nVariant*
:   Index of the macro variant to be placed (0 based).

*oTargetMate*
:   target mate

*nMoveCondition*
:   Determines if the macro will be placed with absolute coordinates or relatively to the target's mate Placement3D

*nNumerationMode*
:   Numeration mode used during inserting objects.

#### Return Value

Inserted placements.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ArgumentNullException** | Null was set to a parameter. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |

Remarks

Method places items according to macro's handle and a target mate, similarly as in GUI.
