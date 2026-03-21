---
title: "tooltip"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_tooltip.htm"
file: "refformui_r_tooltip"
category: "refformui"
---

# tooltip

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  tooltip The element <tooltip> creates a tooltip, that appears as a pop-up window. This is typically a Form-UI. If the Form-UI as a tooltip permits the changing of data, a decision can be taken while closing the dialog whether the changed data should be stored or rejected. By specifying as an element, further attributes may be set. The element <tooltip> is valid as a sub-element for the following elements:
     * [action](refformui_r_action.htm)
     * [img](refformui_r_img.htm)
     * [input](refformui_r_input.htm)
     * [instantiation](refformui_r_instantiation.htm)
     * [label](refformui_r_label.htm)
     * [mailto](refformui_r_mailto.htm)
     * [open](refformui_r_open.htm)
If the movable attribute is set to true, the tooltip overlay can be moved to another position. To do so, the mouse cursor must be moved on a free area of the overlay. When the cursor changes, the overlay can be moved with pressed left mouse key. If only the showMenu attribute is set to true, the menu items Move and Resize are displayed. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
hSize | optional |  |  | Width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMin | optional |  |  | minimum width of the element  
EEC = minimum width in characters  
Web application = minimum width in pixels  
page | optional |  |  | Form-UI displayed as a tooltip  
movable | optional | true, false | true | true = tooltip window is movable  
false = tooltip window is fixed  
resizable | optional | true, false | true | true = size of the tooltip window is modifiable  
true = size of the tooltip window is fixed  
showMenu | optional | true, false | true | true = displays a menu on the top right corne  
false = no menu is displayed  
vSize | optional |  |  | Height of the element  
EEC = height in characters  
Web application = height in pixels  
vSizeMax | optional |  |  | maximum height of the element  
EEC = maximum height in characters  
Web application = maximum height in pixels  
vSizeMin | optional |  |  | minimum height of the element  
EEC = minimum height in characters  
Web application = minimum height in pixels  
Allowed sub-elements | Quantity  
---|---  
none |   
Note Tooltips cannot be displayed in the environment of Web EEC. A tooltip, which displays a Form-UI in a pop-up window with fixed size: [Example code](javascript:void\(0\);)
    
        <label>Label with tooltip in a fixed popup-window  
     <tooltip page="start" />  
    </label>

Result: A tooltip, which displays a Form-UI in a pop-up window with predefined size: The content is created in a Form-UI, that is located in the same component. [Example code](javascript:void\(0\);)
    
        <label>Label with tooltip in a popup-window of predefined size  
     <tooltip page="start" hSizeMax="250" vSizeMax="150" movable="true"/>  
    </label>

Result: A tooltip, that can be modified in position and size, with expanded menu: The content is created in a Form-UI, that is located in the same component. [Example code](javascript:void\(0\);)
    
        <label>Label mit einem Tooltip in einem Popup-Fenster mit MenÃ¼  
     <tooltip page="start" resizable="true" movable="true" showMenu="true"/>  
    </label>

Result:
