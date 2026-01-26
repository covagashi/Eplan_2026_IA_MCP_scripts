# FindLayerUsage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~FindLayerUsage.html

---

Get all objects from layer.

Syntax

**C#**



public StorableObject[] FindLayerUsage( 

   GraphicalLayer oLayer

)

public:

array<StorableObject^>^ FindLayerUsage( 

   GraphicalLayer^ oLayer

)


#### Parameters

*oLayer*
:   Layer from which elements are returned.

#### Return Value

Array of objects with given layer.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |
