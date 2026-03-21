# XGedIaFormatText

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XGedIaFormatText.html

---

Sets text format. Can be offered for configurable ribbonbar.

| Parameter | Description |
| --- | --- |
| ``` language
 ``` | ``` Language (optional).
  Possible values are: "AllLanguagesColumn", "AllLanguagesRow", "OneLanguageVariable", "de_DE", "en_US", ...
 ``` |
| ``` height
 ``` | ``` Text height (optional). Value in mm or In or "-16002" for "from layer".
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
| ``` justification
 ``` | ``` Adjustment (optional).
  1 = kTopLeft,
  2 = kTopCenter,
  3 = kTopRight,
  4 = kMiddleLeft,
  5 = kMiddleCenter,
  6 = kMiddleRight,
  7 = kBottomLeft,
  8 = kBottomCenter,
  9 = kBottomRight,
  10 = kBaseLineLeft,
  11 = kBaseLineCenter,
  12 = kBaseLineRight,
  13 = kSpecialLeft (Special Attachment-Types for PathTexts in DIN- and USA-Project),
  14 = kSpecialCenter (Should not be used in new projects, just to be compatible to E5),
  15 = kSpecialRight,
  16 = kJicSpecialLeft (Special Attachment-Types for PathTexts in JIC-Project),
  17 = kJicSpecialCenter (Should not be used in new projects, just to be compatible to E5),
  18 = kJicSpecialRight
 ``` |
| ``` angle
 ``` | ``` Angle to the X-axis in ° (optional).
  Possible values are: 0°, 45°, 90°, 135°, 180°, -45°, -90°, -135°
 ``` |
| ``` font
 ``` | ``` Text font (optional).
  Possible values are:
  0 = font 1 of company settings,
  1 = font 2 of company settings,
  ...,
  9 = font 10 of company settings
 ``` |
| ``` visible
 ``` | ``` Text visibility (optional).
  Possible values are: 0 = invisible, 1 = visible, 2 = from layer
 ``` |
| ``` bold
 ``` | ``` Text accentuation (optional). Possible values are: 0 = normal, 1 = bold
 ``` |
| ``` italic
 ``` | ``` Text accentuation (optional). Possible values are: 0 = normal, 1 = italic
 ``` |
| ``` underline
 ``` | ``` Text accentuation (optional). Possible values are: 0 = normal, 1 = underlined
 ``` |
| ``` showtextbox
 ``` | ``` Defines whether to use a text box (optional).
  Possible values are:
  0 = no text box
  1 = rectangular text box
  2 = elliptic text box
  3 = from layer
  4 = Oval text box
 ``` |
| ``` setframeactive
 ``` | ``` Defines whether there should be an activate frame (optional). Possible values are:
  0 = should not be active,
  1 = should be active
 ``` |
| ``` showframe
 ``` | ``` Defines whether to show a frame (optional). Possible values are:
  0 = no alignment box,
  1 = show alignment box
 ``` |
| ``` framewidth
 ``` | ``` Frame width in mm or In (optional).
 ``` |
| ``` frameheight
 ``` | ``` Frame height in mm or In (optional).
 ``` |
| ``` adjustframe
 ``` | ``` Adjustment of frame (optional).
  1 = do not fit in,
  16 = Text: width fixed - never word-wrap,
  32 = Text: height fixed - never word-wrap,
  64 = Text: word-wrap,
  80 = Text: width fixed - word-wrap,
  128 = Text: remove line breaks,
  144 = Text: width fixed - never word-wrap - remove line breaks,
  208 = Text: width fixed - word-wrap - remove line breaks
 ``` |
| ``` sizefromsettings
 ``` | ``` Defines whether to use the frame size from the project settings (optional).
  Possible values are: 0 = should not be activated, 1 = should be active
 ``` |
| ``` leaderline
 ``` | ``` Defines whether to activate a leader line (optional). Possible values are: 0 = should not be active, 1 = should be active
 ``` |
| ``` donttranslate
 ``` | ``` Defines whether to translate automatically (optional). Possible values are: 0 = text is translated automatically, 1 = text is not translated automatically
 ``` |
| ``` linespacing
 ``` | ``` Row spacing in number of lines (optional).
 ``` |
| ``` layer
 ``` | ``` Layer name (optional). Example: "EPLAN501"
 ``` |

**Remarks**

```
 In properties which should not be changed, simply leave a question mark ("?").

 The settings are the same as in the characteristic text dialog.

```

**Example**

```
 Changes height, angle, font and shows a frame:

  XGedStartInteractionAction /Name:XGedIaFormatText /height:3.5 /angle:-90 /font:2 /setframeactive:1 /showframe:1 /framewidth:20 /frameheight:10 /adjustframe:208

 Changes the layer to "EPLAN501" and sets height and color to the new layer's standard:

  XGedStartInteractionAction /Name:XGedIaFormatText /height:-16002 /color:-16002 /layer:EPLAN501

```