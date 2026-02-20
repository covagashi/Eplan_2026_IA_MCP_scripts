# SymbolMacro Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D~SymbolMacro.html

---

Places objects from symbol macro into layout space.

Syntax

**C#**



public StorableObject[] SymbolMacro( 

   string strEMSFileName,

   int nVariant,

   Placement3D oParent,

   Matrix3D oMatrix,

   Insert3D.MoveKind nMoveCondition,

   WindowMacro.Enums.NumerationMode nNumerationMode

)

public:

array<StorableObject^>^ SymbolMacro( 

   String^ strEMSFileName,

   int nVariant,

   Placement3D^ oParent,

   Matrix3D oMatrix,

   Insert3D.MoveKind nMoveCondition,

   WindowMacro.Enums.NumerationMode nNumerationMode

)


#### Parameters

*strEMSFileName*
:   Full file name of the SymbolMacro file (.ems) to be placed.

*nVariant*
:   Index of the macro variant to be placed (0 based).

*oParent*
:   Object from EPLAN project to which top most objects from macro will be assigned.

*oMatrix*
:   Transformation by which objects from macro will be multiplied.

*nMoveCondition*
:   Determines if the macro will be placed with absolute coordinates or relatively to the parent

*nNumerationMode*
:   numeration mode

#### Return Value

Inserted placements

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters.. |
| **ArgumentNullException** | Null was set to a parameter. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |
