# XGedIaFormatDefPoints

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XGedIaFormatDefPoints.html

---

Formats the diagram of connecting and points of potential definition. Can be offered for configurable ribbonbar.

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
  -16002 = from layer
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

**Remarks**

```
 In properties which should not be changed, simply leave a question mark ("?").

 The format is the same like in graphic dialog where properties can be adjusted.

```

**Example**

```
 See Interaction "XGedIaFormatGraphic"

```