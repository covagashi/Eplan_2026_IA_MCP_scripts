# Color

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color.html

---

Defines color of graphical placements or 3d placements Color can be stored as a) a colorId as reference into an internal color table (Default) b) RGB values of the color c) a special color id ByLayer, that says: color is defined by layer Usually the color is defined by color id. Imported 3d graphics may store RGB values directly If the ColorId==ByLayer then the color must be taken from layer If the TransparencyDefinedByLayer is true, then the transparency must be taken from layer otherwise the transparency is stored in this object The mapping between R,G,B values and colorId is done in a way that at first there is checked background-dependant palette and afterwards extended one.

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      **Eplan.EplApi.DataModel.Graphics.Color**

Syntax

**C#**



public struct Color : System.ValueType

public value class Color : public System.ValueType

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Color Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [B](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color~B.html) | Gets or sets the blue channel value of color (0-255) |
| Public Property | [ColorId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color~ColorId.html) | Gets or sets Color id |
| Public Property | [G](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color~G.html) | Gets or sets the green channel value of color (0-255) |
| Public Property | [R](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color~R.html) | Gets or sets the red channel value of color (0-255) |
| Public Property | [Transparency](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color~Transparency.html) | Gets or sets transparency (0-255) due to internal technical limitations transparency is always stored as even value so 13 will be stored as 12 for example |
| Public Property | [TransparencyDefinedByLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Color~TransparencyDefinedByLayer.html) | if true, then transparency must be taken from layer |


