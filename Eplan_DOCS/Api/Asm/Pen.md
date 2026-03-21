# Pen

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen.html

---

The Pen class represents the drawing settings of graphical objects.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.Graphics.Pen**

Syntax

**C#**



public class Pen

public ref class Pen


Remarks

To change a graphical object, the Pen object must first be changed and then reassigned to the graphical object (see code example below).

Example

Setting graphical properties of a Line object by Pen

**C#**

```


// Create a Line object and place it on the page "testPage"

Line line = new Line();

PointD startPoint = new PointD(10, 70);

PointD endPoint = new PointD(85, 120);

line.Create(testPage, startPoint, endPoint);

// Get the Pen object of the Line object

Pen pen = line.Pen;

// Edit the line color, style and width on the Pen object

pen.ColorId = 4;

pen.StyleId = 6;

pen.Width = 2;

// Reassign the Pen object to the Line object to make the changes take effect on the Line object

line.Pen = pen;

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Pen Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ColorId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~ColorId.html) | Color index (0-255). Please use "-16002" for "from layer" value. Predefined values for line color index are:  0 = black  1 = red  2 = yellow  3 = green  4 = cyan  5 = blue  6 = magenta  7 = white  252 = darkgray  253 = gray  -16002 = from layer |
| Public Property | [LineEndType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~LineEndType.html) | Type of line end (0-2) |
| Public Property | [PatternLength](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~PatternLength.html) | Pattern length. The pattern will be stretched, so that the whole pattern fits to the length of PatternLength. This is like in EPLAN 5. Please use "-16002" as "from layer" value. |
| Public Property | [StyleFactor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~StyleFactor.html) | Line Style Factor when positive or Pattern Length when negative. Default value = 1. Please use "-16002" as "from layer" value. |
| Public Property | [StyleId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~StyleId.html) | Line style identifier (0-6) Please use "-16002" as "from layer" value. Predefined line type index values are:  0 = continous: ------  1 = dash: - - - - -  2 = dot: .......  3 = dashdot: \_.\_.\_.\_  4 = dashdotdot: \_..\_..\_  5 = dash: \_ \_  6 = dashlongdot: \_\_ \_  -16002 = from layer |
| Public Property | [Width](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~Width.html) | Line width. Normally it is 0.13 - 2. Please use "-16002" as "from layer" value. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~Dispose().html) | Destructor for deterministic finalization of Pen object. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~GetHashCode.html) | Serves as the default hash function. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Equality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~op_Equality.html) | .NET operator for comparing two GraphicalLayers. Comparison is made by comparing each of GraphicalLayers members instead of internal object id. |


