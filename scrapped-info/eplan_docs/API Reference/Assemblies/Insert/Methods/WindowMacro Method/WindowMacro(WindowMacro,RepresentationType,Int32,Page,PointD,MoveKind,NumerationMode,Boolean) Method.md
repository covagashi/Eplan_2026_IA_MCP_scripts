# WindowMacro(WindowMacro,RepresentationType,Int32,Page,PointD,MoveKind,NumerationMode,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1367.html

---

Places a window macro onto a given position of a page. You can set whether absolute coordinates or coordinates relative to its original position on the page should be used.

Syntax

**C#**



public StorableObject[] WindowMacro( 

   WindowMacro oMacro,

   WindowMacro.Enums.RepresentationType nRepType,

   int nVariant,

   Page oPage,

   PointD oPlacement,

   Insert.MoveKind moveCondition,

   WindowMacro.Enums.NumerationMode nNumerationMode,

   bool bDontResolveGroups

)

public:

array<StorableObject^>^ WindowMacro( 

   WindowMacro^ oMacro,

   WindowMacro.Enums.RepresentationType nRepType,

   int nVariant,

   Page^ oPage,

   PointD oPlacement,

   Insert.MoveKind moveCondition,

   WindowMacro.Enums.NumerationMode nNumerationMode,

   bool bDontResolveGroups

)


#### Parameters

*oMacro*
:   WindowMacro object to be placed.

*nRepType*
:   RepresentationType of Macro

*nVariant*
:   Index of the macro variant to be placed (0 based).

*oPage*
:   Page on which to place the macro.

*oPlacement*
:   Position on which to place he macro.

*moveCondition*
:   Determines if the macro will be placed with absolute coordinates or relatively to its original position

*nNumerationMode*
:   Numeration mode

*bDontResolveGroups*
:   Determines if groups will be resolved Default value : false

#### Return Value

Inserted placements

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters.. |
| **ArgumentNullException** | Null was set to a parameter. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |
