# SymbolMacro(SymbolMacro,Int32,Page,PointD,MoveKind) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~SymbolMacro(SymbolMacro,Int32,Page,PointD,MoveKind).html

---

Places a symbol macro onto a given position of a page. You can set whether absolute coordinates or coordinates relative to its original position on the page should be used.

Syntax

**C#**



public StorableObject[] SymbolMacro( 

   SymbolMacro oMacro,

   int nVariant,

   Page oPage,

   PointD oPlacement,

   Insert.MoveKind moveCondition

)

public:

array<StorableObject^>^ SymbolMacro( 

   SymbolMacro^ oMacro,

   int nVariant,

   Page^ oPage,

   PointD oPlacement,

   Insert.MoveKind moveCondition

)


#### Parameters

*oMacro*
:   SymbolMacro object to be placed.

*nVariant*
:   Index of the macro variant to be placed (0 based).

*oPage*
:   Page on which to place the macro.

*oPlacement*
:   Position on which to place he macro.

*moveCondition*
:   Should the will the macro be placed with absolute coordinates or relatively to its original position?

#### Return Value

Inserted placements

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters.. |
| **ArgumentNullException** | Null was set to a parameter. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |
