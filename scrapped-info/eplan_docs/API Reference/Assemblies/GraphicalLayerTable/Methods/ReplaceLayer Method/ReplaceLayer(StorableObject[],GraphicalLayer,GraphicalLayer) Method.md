# ReplaceLayer(StorableObject[],GraphicalLayer,GraphicalLayer) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic708.html

---

Replace [Eplan::EplApi::DataModel:](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html) for given array of objects.

Syntax

**C#**



public void ReplaceLayer( 

   StorableObject[] elementsToReplace,

   GraphicalLayer oldLayer,

   GraphicalLayer newLayer

)

public:

void ReplaceLayer( 

   array<StorableObject^>^ elementsToReplace,

   GraphicalLayer^ oldLayer,

   GraphicalLayer^ newLayer

)


#### Parameters

*elementsToReplace*
:   Array of [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) for which layer should be changed.

*oldLayer*
:   Only objects from `elementsToReplace` which have this layer used will have layer changed.

*newLayer*
:   Layer which will be set.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |

Remarks

This method takes also `oldLayer` parameter so layer will be changed only for objects which use this layer.
