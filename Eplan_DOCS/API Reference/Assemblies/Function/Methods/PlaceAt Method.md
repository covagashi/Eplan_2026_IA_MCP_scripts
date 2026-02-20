# PlaceAt Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~PlaceAt.html

---

Places the function onto the given page, in the given location and with the symbol specified by the placementType and the pSymbolVariant parameters.

Syntax

**C#**



public void PlaceAt( 

   Page oPage,

   PointD pntLocation,

   DocumentTypeManager.DocumentType placementType,

   SymbolVariant pSymbolVariant

)

public:

void PlaceAt( 

   Page^ oPage,

   PointD pntLocation,

   DocumentTypeManager.DocumentType placementType,

   SymbolVariant^ pSymbolVariant

)


#### Parameters

*oPage*
:   A page to insert the function's symbol on.

*pntLocation*
:   Insertion point of the symbol being inserted.

*placementType*
:   Placement type of the symbol being inserted.

*pSymbolVariant*
:   The actual symbol's variant to insert.

Remarks

If this object is a transient object representing a function template, it is instantiated first. If this object is an already instantiated function, a new function is created in the project. If the placementType parameter is [DocumentTypeManager.DocumentType.Functional](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html), a special symbol configured in settings is inserted together with the function's symbol. Then, the special symbol's representation type is set to 'Functional' and the function's symbol is converted to graphics. If the function has no valid symbol assigned, the symbol specified by the pSymbolVariant parameter will be used as the function's symbol. If the function has a valid symbol assigned, in case the placementType parameter is 'Functional', the pSymbolVariant parameter is ignored.

Placing the template on page updates parameter `IsCoveredTemplate`. Note that this is not done on other objects which represents this template and were collected from function before using the method `PlaceAt`.
