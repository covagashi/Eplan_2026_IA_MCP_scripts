# ReorderPropertyPlacements Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~ReorderPropertyPlacements.html

---

Reorders property placements of one type, which are assigned to this SymbolReference.

Syntax

**C#**



public List<PropertyPlacement> ReorderPropertyPlacements( 

   List<PropertyPlacement> lstPropertyPlacements

)

public:

List<PropertyPlacement^>^ ReorderPropertyPlacements( 

   List<PropertyPlacement^>^ lstPropertyPlacements

)


#### Parameters

*lstPropertyPlacements*
:   List of property placements in requested order.

#### Return Value

Resulting list of property placements.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when input list contains property placements of different type or from different SymbolReferences or not local ones. |

Remarks

All property placements which are not in the input list, will be removed from original symbol reference. Property placement objects that were acessed before calling this method will be invalid - get and use the list of property placements returned by the method instead.

Example

**C#**

```


var lComponentPPToReorder = oNewTerminal.GetPropertyPlacements(SymbolReference.PropertyPlacementType.Component);

var iPPToMoveIndex = 2;

var oPPToMove = lComponentPP[iPPToMoveIndex];

lComponentPPToReorder.RemoveAt(iPPToMoveIndex);

lComponentPPToReorder.Insert(1, oPPToMove);

iPPToMoveIndex = 7;

oPPToMove = lComponentPP[iPPToMoveIndex];

lComponentPPToReorder.RemoveAt(iPPToMoveIndex);

lComponentPPToReorder.Add(oPPToMove);

var lReorderedComponentPP = oNewTerminal.ReorderPropertyPlacements(lComponentPPToReorder);

```
