# XGedIaFormatGraphic

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XGedIaFormatGraphic.html

---

Formats simple graphic and "formatable" objects (having "Format" tab, like macro box, cable definition line, etc)

| Parameter | Description |
| --- | --- |
| ``` width
 ``` | ``` Line width in mm or In or "-16002" for "from layer" (optional).
 ``` |
| ``` color
 ``` | ``` Text color (optional).
  0 = black,
  1 = red,
  2 = yellow,
  3 = green,
  4 = cyan,
  5 = blue,
  6 = magenta,
  7 = black,
  8 = white,
  9 = light gray,
  252 = dark gray,
  253 = gray,
  -16002 = from layer;
  The user can set other values in the color selection. Possible values are from 0 to 256.
 ``` |
| ``` type
 ``` | ``` Line type (optional).
  0 = solid,
  1 = dashed,
  2 = dotted,
  3 = dash-dot,
  4 = dash-dot-dot,
  5 = dash-2 short dashes,
  26 = long dash-dot,
  -16002 = from layer
 ``` |
| ``` patternlength
 ``` | ``` Sample length in mm or In or "-16002" for "from layer" (optional).
 ``` |
| ``` lineendstyle
 ``` | ``` Line end format (optional).
  0 = fRound,
  1 = fRectangular,
  2 = fFlat,
  32 = fByLayer
 ``` |
| ``` visible
 ``` | ``` Graphic visibility (optional).
  0 = invisible,
  1 = visible,
  2 = from layer
 ``` |
| ``` filled
 ``` | ``` Fill surface (optional).
  Possible values are: 0 = not filled, 1 = filled
 ``` |
| ``` rounded
 ``` | ``` Corners rounded off (optional). For rectangles only.
  Possible values are: 0 = not rounded, 1 = rounded
 ``` |
| ``` radius
 ``` | ``` Arc radius in mm or In (optional). For rounded rectangles only.
 ``` |
| ``` transparency
 ``` | ``` Transparency value in % between 0 and 1.0 or "bylayer" for "from layer" setting (optional). For 3D volumes only.
 ``` |

**Remarks**

```
 In properties which should not be changed, simply leave a question mark ("?").

 The format is the same like in graphic dialog where properties can be adjusted.

```

**Example**

```
 Set the thickness of a line to 5.5 mm, the color of the graphic to cyan and the visibility of the graphic element to everyone:

   XGedStartInteractionAction /Name:XGedIaFormatGraphic /width:5.5 /color:4 /type:? /patternlength:? /lineendstyle:? /visible:1 /filled:? /rounded:? /radius:?

```