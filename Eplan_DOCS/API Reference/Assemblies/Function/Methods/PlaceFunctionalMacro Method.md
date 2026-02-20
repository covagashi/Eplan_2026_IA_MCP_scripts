# PlaceFunctionalMacro Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~PlaceFunctionalMacro.html

---

Places a macro assigned to this function together with a special symbol configured in settings. The symbol placed has 'Functional' representation type and the macro is converted to graphics after insertion. If no macro is assigned to the function in its article data (ARTICLE\_GROUPSYMBOLMACRO property), the macro specified by the third parameter ('strMacroFileName') will be inserted.

Syntax

**C#**



public StorableObject[] PlaceFunctionalMacro( 

   Page oPage,

   PointD pntLocation,

   string strMacroFileName,

   WindowMacro.Enums.RepresentationType nRepType,

   int nVariant

)

public:

array<StorableObject^>^ PlaceFunctionalMacro( 

   Page^ oPage,

   PointD pntLocation,

   String^ strMacroFileName,

   WindowMacro.Enums.RepresentationType nRepType,

   int nVariant

)


#### Parameters

*oPage*
:   A page to insert the macro on.

*pntLocation*
:   Insertion point of the macro.

*strMacroFileName*
:   A macro file name. This parameter is ignored if a macro is assigned to the function in its article data.

*nRepType*
:   Representation type that should be taken from the macro.

*nVariant*
:   A variant that should be taken from the macro. Possible values are 0 through 15 (they map to A through P values in EPLAN P8 GUI).

#### Return Value

Returns an array of placements inserted onto the page.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when a functional macro cannot be created |

Remarks

Variant of the macro (either the one from article or the one specified by the 'strMacroFileName' parameter) is determined by the 'nRepType' and 'nVariant' parameters. If the specified variant doesn't exist in the macro, an exception is thrown.
