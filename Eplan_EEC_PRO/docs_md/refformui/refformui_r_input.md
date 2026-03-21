---
title: "input"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_input.htm"
file: "refformui_r_input"
category: "refformui"
---

# input

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  input The <input> element inserts a simple input field, a drop-down list box, a radio button, a check box or a button with toggle function, which serves for either entering a value or selecting one. In the hidden password input (type = "password"), instead of a character an asterisk (*) is displayed. The text can also be created as a link. Such links are not, as usual, made of blue and underlined text and the link can only be accessed if the [Alt] key is pressed. The content of the box can be calculated using the [Formula language](refformulas_r_formula_language.htm). The input of integer or double values is limited to reduce the risk of incorrect entries. Other characters except the following can not be entered:  
     * **Integer** : +/-, only numbers without decimal points
     * **Double** : +/-, numbers, decimal points, e
Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
autoselect | optional, only for type = combo | true, false | false | If the drop-down list box provides only one value, this one can automatically be set.   
Conditions: Attribute editable = false and no default value is set.  
true = if only one value is available, this one is set and displayed italic  
false = if only one value is available, this one has to be set manually  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
editable | optional, only for type = combo | true, false |  | true = any value can be added to the existing values  
false = only the predefined values can be selected  
font | optional | Font name-style-size | System font | Font name, style, and size for displaying text  
hSize | optional |  |  | Width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMax | optional |  |  | Maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element  
EEC = width in pixels  
Web application = width in pixels  
hSizeMin | optional |  |  | Minimum width of the element  
EEC = minimum width in characters  
Web application = minimum width in pixels  
hSizeMinPx | optional |  |  | Minimum width of the element  
EEC = minimum width in pixels  
Web application = minimum width in pixels  
hSizePx | optional |  |  | Width of the element  
EEC = width in pixels  
Web application = width in pixels  
id | required | any |  | Unique ID, which is referred to as reference  
img | only for type = toggle | png, gif, jpg |  | assigns another image to the element  
key | optional |  |  | field from which the value of the EO will be read  
link | optional |  |  | Formula to the object of the navigation target  
readonly | optional | true, false |  | true = field is read-only. When type = combo, the list can not be expanded.  
false = field may be written. When type = combo, the list can not be expanded and a value can be selected.  
receiver | required |  |  | Formula to the object  
style | only for type = text and radio | multi, right, center, left, horizontal, vertical, wrap |  |  Defines the attribute type more exactly. **The following combinations are possible for type="text":**   
multi = multiline input field with left-aligned text multi right = multiline input field with right-aligned text multi center = multiline input field with centered text vertical = multiline input field with left-aligned text and vertical scroll bar vertical right = multiline input field with right-aligned text and vertical scroll bar vertical center = multiline input field with centered text and vertical scroll bar horizontal = multiline input field with left-aligned text and horizontal scroll bar wrap = multiline input field with left-aligned text and automatic line break wrap vertical = multiline input field with left-aligned text, automatic line break and vertical scroll bar **The following specifications are possible for type="radio":** horizontal = horizontal arranged radio buttons  
vertical = vertical arranged radio buttons  
text | only for type = toggle |  |  | The text to display can be calculated using the formula language  
tooltip | optional |  |  | Text or Form-UI of the overlaying tooltip (see [tooltip](refformui_r_tooltip.htm))  
type | optional | text  
combo  
radio  
check  
password  
toggle | text | Type of input box:  
text = text box (valid for pureTable)  
combo = drop-down list box (valid for pureTable)  
radio = radio button  
check = check box (valid for pureTable)  
password = hidden password input  
toggle = button with toggle function  
values | only for type = combo |  |  | List of values to be displayed in a combo box.  
=List{Pair{1,'one'},Pair{2,'two'}}  
visible | optional |  |  | true = element is visible  
true = element is invisible  
visibleItemCount | optional, only for type = combo |  |  | Number of items to display in a drop-down list box without scrolling  
vSize | optional |  |  | Height of the element  
EEC = height in characters  
Web application = height in pixels  
vSizeMax | optional |  |  | Maximum height of the element  
EEC = maximum height in characters  
Web application = maximum height in pixels  
vSizeMaxPx | optional |  |  | Maximum height of the element  
EEC = maximum height in pixels  
Web application = maximum height in pixels  
vSizeMin | optional |  |  | Minimum height of the element  
EEC = minimum height in characters  
Web application = minimum height in pixels  
vSizeMinPx | optional |  |  | Minimum height of the element  
EEC = minimum height in pixels  
Web application = minimum height in pixels  
vSizePx | optional |  |  | Height of the element  
EEC = height in pixels  
Web application = height in pixels  
write | optional |  |  | Field of the EO the value is written to  
Allowed sub-elements | Quantity  
---|---  
[tooltip](refformui_r_tooltip.htm) | 0..1  
Note The selection values in DropDown list fields must always be unique. Otherwise, it may not be possible to distinguish between the values displayed. Note If the attributes hSizeMax and hSizeMaxPx are set, the hSizeMaxPx is used (hSizeMax is then ignored). Note A non-editable DropDown list box shows the following behavior when values are pasted from the Clipboard:   
Values, which accord to those in a list (attribute values) are assumed, but differing values are ignored. [Text box](javascript:void\(0\);) The text box is displayed as a rectangle, which contains a text. The height and width of the box depends on the content. This examples shows a text, which is stored in the "Name" field of the component. [Example code](javascript:void\(0\);)
    
        <input type="text" receiver="this" key="name"/>

Result: [Read-only text box](javascript:void\(0\);) The text box is displayed as a gray rectangle, which contains a text. The gray text box indicates that the text cannot be edited. [Example code](javascript:void\(0\);)
    
        <input type="text" receiver="this" key="name" readonly="true"/>

Result: Note For Windows 7 the presentation of read-only text fields varies depending on the selected design. This can lead to representations that are very difficult to read. [Text box for writing a comment](javascript:void\(0\);) The text box is displayed as a rectangle, where a text can be typed. This examples stores the typed text in the "Comment" field of the EO. [Example code](javascript:void\(0\);)
    
        <input type="text" receiver="this" key="comment" write="comment"/>

Result: [Text box with limited width](javascript:void\(0\);) The text box is displayed as a rectangular with limited width, which contains the text Documentation. By limiting the text box to 25 pixels, the text is truncated. [Example code](javascript:void\(0\);)
    
        <input hSizeMax="25" type="text" receiver="this" key="name"/>

Result: [Text box with link](javascript:void\(0\);) The text box stores the value of the parameter Place. The containing text is displayed with the font Arial with a size of 15 pt. By holding the [Alt] key you can follow the link to the parameter Place. [Example code](javascript:void\(0\);)
    
        <input link="parameter('Place')"
    font="Arial-regular-15"
    type="text"
    receiver="parameter('Place')"/>

Result: [Multiline input field for text](javascript:void\(0\);) The multiline input field for text is displayed as a rectangle, where a multiline text can be typed. This example shows a text, which is stored in the "Comment" field of the component. [Example code](javascript:void\(0\);)
    
        <input type="text"
    receiver="this"
    key="comment"/>

Result: [Multiline text box with link](javascript:void\(0\);) The multiline text box is displayed as a rectangle, which contains a multiline text. This example shows a text, which is stored in the Comment field of the EO. By holding the [Alt] key you can follow the link to the parameter Place. [Example code](javascript:void\(0\);)
    
        <input type="text"
    receiver="this"
    key="comment"
    link="parameter('Place')"/>

Result: [DropDown list box](javascript:void\(0\);) The DropDown list box is displayed as a rectangle with an arrow symbol at the side. By clicking on the arrow a list is expanded. The element of the list, which is marked by the mouse, appears then in the closed list box and is stored therein. [Example code](javascript:void\(0\);)
    
        <input type="combo"
    receiver="parameter('CardinalPoints')"/>

Result: [Editable DropDown list box](javascript:void\(0\);) The DropDown list box is displayed as a rectangle with an arrow symbol at the side. By clicking on the arrow a list is expanded. The element of the list, which is marked by the mouse, appears then in the closed list box and is stored therein. In addition any value can be entered, which is then stored in the list box. If the list box contains a value, which is entered, then the background color of the list box changes to yellow as well as any boxes, which also display this value. [Example code](javascript:void\(0\);)
    
        <input type="combo"
    editable="true"
    receiver="parameter('CardinalPoints')"/>

Result: [DropDown list box with tooltip](javascript:void\(0\);) When the mouse cursor is placed on the DropDown list box, the tooltip appears. [Example code](javascript:void\(0\);)
    
        <input type="combo"
    tooltip="Tooltip for combo box"
    receiver="parameter('CardinalPoints')"/>

Result: [DropDown list box with predefined elements](javascript:void\(0\);) The elements of the list are defined with the attribute values with the following syntax:
    
        values="=List{Pair{angezeigterWert,gespeicherterWert}, Pair{angezeigterWert,gespeicherterWert}

[Example code](javascript:void\(0\);)
    
        <input type="combo"
    values="=List{Pair{1,'eins'},Pair{2,'zwei'}}"
    receiver="parameter('Ort')"/>

Result: [DropDown list box with fixed number of visible elements](javascript:void\(0\);) The DropDown list box shows only a fixed number of elements with the attribute visibleItemCount in the expanded state. By scrolling further elements in the DropDown list box can be reached. [Example code](javascript:void\(0\);)
    
        <input type="combo"
    visibleItemCount="2"
    receiver="parameter('CardinalPoints')"/>

Result: [DropDown list box sets a single value automatically](javascript:void\(0\);) Only one parameter value is determined by a formula. By using the attribute autoselect="true" this value is automatically displayed. [Example code](javascript:void\(0\);)
    
        <input receiver="=parameter('Test')"
    values="=List{Pair{'one','1'}}"
    type="combo"
    **autoselect="true"** ></input>

Result: [DropDown list box with references to components](javascript:void\(0\);) The DropDown list box stores references to mechatronic or discipline-specific components. The elements of the list are defined by means of the formula language. [Example code](javascript:void\(0\);)
    
        <input type="combo"
    values="=List{Pair{'Station', this},Pair{'Documentation', mc}}"
    receiver="parameter('Component')"/>

Result: A formula, which is created by EEC, is the value of the parameter, which checks, whether the component is actually available (see Value field in the figure above). If the component is not available, then the formula returns the value null. The formula, created by EEC (in the Value field of the parameter) is for the selected component of the example:
    
        =if existsRef('Dokumentation_UI_   
    Configuration.Mechatronic.Documentation.Station') then ref('Dokumentation_UI_   
    Configuration.Mechatronic.Documentation.Station') else null endif.

[Radio buttons horizontal](javascript:void\(0\);) Radio buttons are arranged horizontal by default. To force the horizontal arrangement the attribute style with the value horizontal is defined. The displayed value and the value that is stored can be defined differently. For this purpose the following syntax is used:
    
        <input type="radio"
    values="=List{Pair{X,Y},Pair{X,Y}, Pair{X,Y}}"
    receiver="parameter('Component')"/>

X = value to be displayed X = value to be stored [Radio buttons with the same values for display and storage](javascript:void\(0\);) In the following example, radio buttons are defined that indicate the same value that is stored by the radio button. The number of radio buttons depends on the number of possible values of the parameter. In this example, the four cardinal points are predefined (North, East, South, West). [Example code](javascript:void\(0\);)
    
        <input type="radio" receiver="parameter('CardinalPoints')"/>

Result: [Radio buttons with different values for display and storage](javascript:void\(0\);) The following example shows how pairs of parameters are defined to display the values 1, 2 and 3, but save the values one, two and three. [Example code](javascript:void\(0\);)
    
        <input type="radio"
    values="=List{Pair{1,'one'},Pair{2,'two'}, Pair{3,'three'}}"
    receiver="parameter('Place')"/>

Result: [Radio buttons vertical](javascript:void\(0\);) For vertical arranged radio buttons the attribute style with the value vertical is defined. [Example code](javascript:void\(0\);)
    
        <input type="radio" style="vertical" receiver="parameter('CardinalPoints')"/>

Result: [Check box](javascript:void\(0\);) Check boxes store the value of a parameter of type Boolean. Typically, the parameter name is shown beside the box. [Example code](javascript:void\(0\);)
    
        <line><input type="check" receiver="parameter('found')"/>
    <label>found</label></line>

Result: [Button with toggle function](javascript:void\(0\);) A button with toggle function (latching function) stores the value of a parameter of type Boolean. If the button is pressed, the parameter value is true and the button keeps the pressed appearance. Pressing the button again changes the parameter value to false and the button returns to the appearance of the initial state. The two states are displayed with different images in the button. [Example code](javascript:void\(0\);)
    
        <input type="toggle"
    	receiver="parameter('found')"
    	img="=if $found = true
    		then type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.
    		Images.action').image
    		else type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.
    		Images.E_Mail').image  
    endif"/>

Result:
