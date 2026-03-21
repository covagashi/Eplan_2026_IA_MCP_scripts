# FindElementsOnLayer Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~FindElementsOnLayer.html

---

Checks if elements exists on given layer.

Syntax

**C#**



public StorableObject[] FindElementsOnLayer( 

   StorableObject[] elementsToCheck,

   GraphicalLayer oLayer

)

public:

array<StorableObject^>^ FindElementsOnLayer( 

   array<StorableObject^>^ elementsToCheck,

   GraphicalLayer^ oLayer

)


#### Parameters

*elementsToCheck*
:   Array of [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) which should be checked.

*oLayer*
:   Layer to check.

#### Return Value

Array of objects with the same layer as given to method.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |

Remarks

Method returns array of objects from given set which have the same layer as given to method.
