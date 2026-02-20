# DockText Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~DockText.html

---

Docks one text to another. You can see how it works in GUI. Select element on schematic, display properties, show property placements and dock / undock them.

Syntax

**C#**



public void DockText( 

   TextBase pMaster

)

public:

void DockText( 

   TextBase^ pMaster

)


#### Parameters

*pMaster*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when invalid pMaster object is used i.e. it is not possible to dock PropertyPlacement from SymbolReference to PropertyPlacement from another SymbolReference. |

Remarks

In case of PropertyPlacements from SymbolReference you can dock only to the directly preceding PropertyPlacement. For reordering PropertyPlacements please use Eplan.EplApi.DataModel.SymbolReference.ReorderPropertyPlacements()
