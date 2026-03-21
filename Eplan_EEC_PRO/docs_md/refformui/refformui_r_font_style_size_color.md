---
title: "Font type, style, size and color"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_font_style_size_color.htm"
file: "refformui_r_font_style_size_color"
category: "refformui"
---

# Font type, style, size and color

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Font type, style, size and color Text between the opening and closing tag of an element is displayed in the Form-UI according to the attributes font and fColor. The attribute font affects the font type, style and size of the text. This declaration is made in the manner font type-font style-font size. The font style declaration is necessary, the following declarations are possible:  
     * regular, e.g., Segoe UI Semibold-regular-14 results in Hello world
     * bold, e.g., Arial-bold-14 results in **Hello world**
     * italic, e.g., Arial-italic-14 results in _Hello World_
Note It is recommended to always specify the font type, font style and font size so that differing displays do not arise depending on whether the Form-UI is displayed in the context of a desktop installation or a Web EEC installation. The attribute fColor controls the color of the text. The color is specified as a RGB value in the manner of three decimal numbers for red, green and blue beginning at 0,0,0 (black) until 255,255,255 (white). If fColor is not specified, the text appears in black. The following example shows the specification for the font type, font style and font size as well as for the color: [Example code](javascript:void\(0\);)
    
        <label font="Arial-bold-15" fColor="255,0,0">Red font</label>

Result:
