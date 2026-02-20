# WindowMacro(WindowMacro,Int32,Placement3D,Matrix3D,MoveKind,NumerationMode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1375.html

---

Places objects from window macro into layout space.

Syntax

**C#**



public StorableObject[] WindowMacro( 

   WindowMacro oMacro,

   int nVariant,

   Placement3D oParent,

   Matrix3D oMatrix,

   Insert3D.MoveKind nMoveCondition,

   WindowMacro.Enums.NumerationMode nNumerationMode

)

public:

array<StorableObject^>^ WindowMacro( 

   WindowMacro^ oMacro,

   int nVariant,

   Placement3D^ oParent,

   Matrix3D oMatrix,

   Insert3D.MoveKind nMoveCondition,

   WindowMacro.Enums.NumerationMode nNumerationMode

)


#### Parameters

*oMacro*
:   Opened macro object.

*nVariant*
:   Index of the macro variant to be placed (0 based).

*oParent*
:   Object from EPLAN project to which top most objects from macro will be assigned.

*oMatrix*
:   Transformation by which objects from macro will be multiplied.

*nMoveCondition*
:   Determines if the macro will be placed with absolute coordinates or relatively to the parent

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
