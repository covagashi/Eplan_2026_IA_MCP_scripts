---
title: "progressBar"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_progressbar.htm"
file: "refformui_r_progressbar"
category: "refformui"
---

# progressBar

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  progressBar The <progressBar> element inserts a progress bar. The progress is displayed as a progress bar, as a percentage value or as a combination of both. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
fColor | optional | 0,0,0 to 255,255,255 | System color | Foreground color as RGB value  
font | optional | Font name-style-size | System font | Font name, style, and size for displaying text  
type | optional | both, graphic, text | text | both = progress is indicated as progress bar with percentage value  
graphic = progress is indicated as progress bar  
text = progress is indicated as percentage value  
visible | optional | true, false | true | true = progress indication is visible  
false = progress indication is invisible  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
Allowed sub-elements | Quantity  
---|---  
none |   
[Example code](javascript:void\(0\);)
    
        <progressBar visible="true" type="both" bColor="200,200,200"
    fColor="0,0,200" font="Arial-bold-14" />

Result:
