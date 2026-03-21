# GraphicalLayerTable

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable.html

---

This class represents the table of all graphical layers of the project. It can be used for creating, deleting, merging, and retrieving project's layers.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable**

Syntax

**C#**



[DefaultMember("Layer")]

public class GraphicalLayerTable

[DefaultMember("Layer")]

public ref class GraphicalLayerTable

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Layer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Layer.html) | Overloaded. Returns one the project's layer as GraphicalLayer object. If specified layer not exist, null is returned. |
| Public Property | [Layers](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Layers.html) | Returns an array of all existing project's layers. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~AddLayer.html) | Overloaded. Creates new layer with specified name and description. Note: Layer name must be unique in the table. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Dispose().html) | Destructor for deterministic finalization of GraphicalLayerTable object. |
| Public Method | [Export](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Export.html) | Exports the layers into an XML file. |
| Public Method | [FindElementsOnLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~FindElementsOnLayer.html) | Checks if elements exists on given layer. |
| Public Method | [FindLayerUsage](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~FindLayerUsage.html) | Get all objects from layer. |
| Public Method | [Import](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Import.html) | Imports layers from an XML file. |
| Public Method | [MergeLayers](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~MergeLayers.html) | Merges one layer with another. Note: Only custom layer can be merged. |
| Public Method | [ReassignLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~ReassignLayer.html) | Reassign all elements from `sourceLayer` to `targetLayer`. |
| Public Method | [Reload](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Reload.html) | Updates table's content with the project |
| Public Method | [RemoveLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~RemoveLayer(GraphicalLayer).html) | Removes specified layer from the table. Note: Only custom layer can be removed. |
| Public Method | [ReplaceLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~ReplaceLayer.html) | Overloaded. Replace [Eplan::EplApi::DataModel:](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html) for given array of objects. |


