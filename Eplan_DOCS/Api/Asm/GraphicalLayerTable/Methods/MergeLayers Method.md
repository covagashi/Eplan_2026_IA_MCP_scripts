# MergeLayers Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~MergeLayers.html

---

Merges one layer with another. Note: Only custom layer can be merged.

Syntax

**C#**



public bool MergeLayers( 

   GraphicalLayer layerToMergeWith,

   GraphicalLayer layerToMerge

)

public:

bool MergeLayers( 

   GraphicalLayer^ layerToMergeWith,

   GraphicalLayer^ layerToMerge

)


#### Parameters

*layerToMergeWith*
:   Layer object to merge with

*layerToMerge*
:   Layer object to merge

#### Return Value

true : Layers merged successfully.

false : Merging failed.
