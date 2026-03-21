---
title: "label"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_label.htm"
file: "refformui_r_label"
category: "refformui"
---

# label

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  label The element <label> inserts a text. If the text is to be determined by a formula, the formula is the value of the text attribute, for example text="this.name". The text can also be created as a link. Such links are not, as usual, made of blue and underlined text and the link can only be accessed if the [Alt] key is pressed. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
fColor | optional | 0,0,0 to 255,255,255 | System color | Font color as RGB value  
font | optional | Font name-style-size | System font | Font name, style, and size for displaying text  
hSize | optional |  |  | Width of the element in characters  
hSizePx | optional |  |  | Width of the element in pixels  
hSizeMax | optional |  |  | maximum width of the element in characters  
hSizeMaxPx | optional |  |  | maximum width of the element in pixels  
hSizeMin | optional |  |  | minimum width of the element in characters  
hSizeMinPx | optional |  |  | minimum width of the element in pixels  
link | optional |  |  | Formula to the object of the navigation target  
style | optional |  left,  
center,  
right,  
multi,  
multi center,  
multi right,  
horizontal,  
vertical,  
vertical center,  
vertical right,  
multi horizontal vertical,  
multi horizontal,  
wrap  
wrap vertical |  |  left = text is left-aligned  
center = text is centered  
right = text in is right-aligned  
multi = text is wrapped across several lines if line breaks are inserted by using &#10;  
multi center = text is centered and wrapped  
multi right = text is right-aligned and wrapped  
horizontal = text is left-aligned and a horizontal scroll bar is displayed  
Vertical = text is left-aligned, wrapped when line breaks are inserted with &#10; and a vertical scroll bar is displayed  
vertical center = text is centered, wrapped and a vertical scroll bar is displayed  
vertical right = text is right-aligned, wrapped and a vertical scroll bar is displayed  
multi horizontal vertical = text is left-aligned, wrapped when line breaks are inserted with &#10; and a vertical and a horizontal scroll bar are displayed  
multi horizontal = text is left-aligned, wrapped when line breaks are inserted with &#10; and a horizontal scroll bar is displayed  
wrap = text wraps automatically  
wrap vertical = text is wrapped automatically and a vertical scroll bar is displayed  
text | optional |  |  | Text that is determined by a formula. The formula has no preceding =-sign (e.g.: text="this.name").  
tooltip | optional |  |  | Text or Form-UI of the overlaying tooltip (see [tooltip](refformui_r_tooltip.htm))  
visible | optional | true, false | true | true = label is visible  
false = label is invisible  
vSize | optional |  |  | Height of the element in characters  
vSizePx | optional |  |  | Height of the element in pixels  
vSizeMin | optional |  |  | minimum height of the element in characters  
vSizeMinPx | optional |  |  | minimum height of the element in pixels  
Allowed sub-elements | Quantity  
---|---  
[tooltip](refformui_r_tooltip.htm) | 0..1  
The following figure shows some design possibilities for the representation of the element <label>: Label with link: The text is not displayed as a link, but defined with the formatting. The example shows a link to the parameter CardinalPoints. [Example code](javascript:void\(0\);)
    
        <line>
    	<label font="Arial-bold-10" link="parameter('CardinalPoints')">Parameter CardinalPoints:</label>
    	<label font="Courier-bold-15" text="$CardinalPoints" link="parameter('CardinalPoints')"/>
    </line>

Result:
