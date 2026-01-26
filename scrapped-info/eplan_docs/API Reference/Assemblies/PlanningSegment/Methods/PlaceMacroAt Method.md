# PlaceMacroAt Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PlaceMacroAt.html

---

Places a macro on a given page.

Syntax

**C#**



public StorableObject[] PlaceMacroAt( 

   Page oPage,

   PointD oPlacement,

   string strMacroFileName,

   WindowMacro.Enums.RepresentationType nRepType,

   WindowMacro.Enums.NumerationMode nNumerationMode,

   int nVariant

)

public:

array<StorableObject^>^ PlaceMacroAt( 

   Page^ oPage,

   PointD oPlacement,

   String^ strMacroFileName,

   WindowMacro.Enums.RepresentationType nRepType,

   WindowMacro.Enums.NumerationMode nNumerationMode,

   int nVariant

)


#### Parameters

*oPage*
:   Page to insert the macro on.

*oPlacement*
:   Insertion point of the macro.

*strMacroFileName*
:   Path to the macro file

*nRepType*
:   Representation type that should be used from the macro.

*nNumerationMode*
:   Determins how devices located on the page will be renumbered

*nVariant*
:   Variant that should be taken from the macro

#### Return Value

Array of inserted StorableObject + source object.

Remarks

Method corresponds to the context menu point "Place->Macro selection"
