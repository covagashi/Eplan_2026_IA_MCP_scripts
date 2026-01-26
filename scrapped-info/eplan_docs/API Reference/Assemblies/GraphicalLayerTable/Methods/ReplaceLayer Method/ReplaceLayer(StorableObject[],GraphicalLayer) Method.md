# ReplaceLayer(StorableObject[],GraphicalLayer) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic707.html

---

Replace [Eplan::EplApi::DataModel:](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html) for given array of objects.

Syntax

**C#**



public void ReplaceLayer( 

   StorableObject[] elementsToReplace,

   GraphicalLayer newLayer

)

public:

void ReplaceLayer( 

   array<StorableObject^>^ elementsToReplace,

   GraphicalLayer^ newLayer

)


#### Parameters

*elementsToReplace*
:   Array of [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) for which layer should be changed.

*newLayer*
:   Layer which will be set.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |

Remarks

This method set new layer for all objects given in array.
