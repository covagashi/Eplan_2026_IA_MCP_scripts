# GraphicalLayer

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html

---

This class represents a graphical layer of the project. It can be used to modify layer's properties.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.Graphics.GraphicalLayer**

Syntax

**C#**



public class GraphicalLayer

public ref class GraphicalLayer


Remarks

This class, unlike others in DataModel, saves properties like Name,Description,Visible and others after calling Store() function. It is NOT done automatic. For properly work objects of this class, they have to be associated in a GraphicalLayerTable. Some properties of Data model classes are not linked with their owners even if from the syntax it may seem otherwise. Like in this line: oRectangle.Pen.ColorId = 5, the ColorId of the Pen is changed but oRectangle object doesn't know about it since the Pen property is a stand alone value not aware of oRectangle object existence. This remark applies to the following GraphicalLayer property: Pen.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [GraphicalLayer Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Alignment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Alignment.html) | Specifies the Justification. |
| Public Property | [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Description.html) | Layer's description |
| Public Property | [DrawTextBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~DrawTextBox.html) | Returns true if the text frame exist. |
| Public Property | [DrawTextBoxType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~DrawTextBoxType.html) | Returns the GraphicalLayer text box type |
| Public Property | [Id](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Id.html) | Gets layer Id. |
| Public Property | [Is3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Is3D.html) | Specifies if layer is used for 3D graphics It is not allowed to change this property for standard layers |
| Public Property | [IsBackGroundLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~IsBackGroundLayer.html) | Specifies, if the layer is background layer |
| Public Property | [isCustom](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~isCustom.html) | Returns true, if the layer is a custom layer. |
| Public Property | [isLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~isLocked.html) | Specifies, if the layer is locked |
| Public Property | [isPrinted](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~isPrinted.html) | Specifies, if the layer is printed |
| Public Property | [IsScalable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~IsScalable.html) | Specifies if scale is considered with this layer |
| Public Property | [isValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~isValid.html) | Checks, if layer object is attached to existing project's layer. |
| Public Property | [isVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~isVisible.html) | Specifies visibility of the layer |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Name.html) | Layer's name |
| Public Property | [ParagraphSpacing](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~ParagraphSpacing.html) | Specifies the Paragraph Spacing. This property is used for PropertyPlacemets attributes. |
| Public Property | [Pen](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Pen.html) | Layer's pen |
| Public Property | [RowSpacing](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~RowSpacing.html) | Specifies the Row Spacing. This property is used for PropertyPlacemets attributes. From layer: -16002, Single: 100, 1.5 lines: 150, Double: 200. |
| Public Property | [TextHeight](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~TextHeight.html) | Layer's text height |
| Public Property | [TextRotation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~TextRotation.html) | Layer's rotation of texts |
| Public Property | [Transparency](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Transparency.html) | Specifies transparency of layer as double with a value between 0.0 and 1.0 |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Create.html) | Creates new graphical layer in graphical table. This function calls Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable.AddLayer() and returned object is merged with created object. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Dispose().html) | Destructor for deterministic finalization of GraphicalLayer object. Destroys layer object without storing any changes into project. |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Equals.html) | .NET operator for comparing two GraphicalLayers. Comparison is made by comparing each of GraphicalLayers members instead of internal object id. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~GetHashCode.html) | Serves as the default hash function. |
| Public Method | [Store](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Store.html) | Stores modified layer's properties into project. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Equality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~op_Equality.html) | .NET operator for comparing two GraphicalLayers. Comparision is made by comparing each of GraphicalLayers members instead of internal object id. |


