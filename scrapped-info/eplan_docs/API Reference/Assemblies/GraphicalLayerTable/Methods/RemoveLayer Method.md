# RemoveLayer Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~RemoveLayer(GraphicalLayer).html

---

Removes specified layer from the table. Note: Only custom layer can be removed.

Syntax

**C#**



public bool RemoveLayer( 

   GraphicalLayer layer

)

public:

bool RemoveLayer( 

   GraphicalLayer^ layer

)


#### Parameters

*layer*
:   Layer object to remove.

#### Return Value

true : Layer removed successfully.

false : Removing failed (invalid layer was specified for removal).

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | This exception is thrown if the layer couldn't be removed. This may happen if the layer still contains some graphical objects. |
