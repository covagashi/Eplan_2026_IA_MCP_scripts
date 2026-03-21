---
title: "instantiation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_instantiation.htm"
file: "refformui_r_instantiation"
category: "refformui"
---

# instantiation

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  instantiation The <instantiation> element is used to instantiate objects on placeholders. Five different representations of this element can be set by the type attribute:
     * **link:** as a hyperlink with preceding image,
     * **button:** as a button with image,
     * **combo:** as a drop-down list box,
     * **combo link:** as a combination of drop-down list box and hyperlink with preceding image,
     * **combo button:** as a combination of drop-down list box and button with image.
The default image of the placeholder is replaced by the img attribute (see also [img](refformui_r_img.htm)). For a drop-down list box (type = combo) the inserting is performed directly after the selection. Inserting explicitly is realized by the types combo link and combo button. For these types the hyperlink or the button has to be pressed after the selection within the drop-down list box. In order to achieve a fluent operation, selection lists in finders, drop-down list boxes, etc. can be filled while opening a Form-UI. For this purpose the prefetch attribute is specified with the value true. This is available for all types (link, button, combo, combo link and combo button) of the element <instantiation>. The default value of the prefetch attribute is false, in order not to fill all library components into the selection list, if a placeholder is declared for e.g. Engineering.Component. Note If a filter allows to many components, this may lead to long loading periods. If only one component can be determined, the finder dialog is not appearing, instead the component is inserted directly. In case of a drop-down list box and if prefetch="true" then the first component is automatically selected. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
alwaysShowDialog | optional | false  
true | false | Displays a dialogue if an instance is to be created with a button or a hyperlink.  
true = always displays the selection dialog  
false= suppresses the selection dialog  
font | optional | Font name-style-size | System font | Font name, style, and size for displaying text  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element  
EEC = width in pixels  
Web application = width in pixels  
img | optional | png, gif, jpg |  | assigns another image to the element  
name | optional |  |  | Name of the new instance (name of the placeholder). If the Name is determined by the formula language, the origin of the formula equals the place of the new instance. If the attribute is not specified, the project component gets the name of the library component. If the name of a project component is already present, the new name is supplemented with a running serial number.  
prefetch | optional | true, false | false | true = selection lists are filled while opening the Form-UI  
false = selection lists are filled while opening the list  
readonly | optional | true, false |  | true = placeholder is disabled  
false = placeholder is enabled  
receiver | required |  |  | Formula to the object  
text | optional |  |  | the text to display can be calculated using the formula language  
tooltip | optional |  |  | Text or Form-UI of the overlaying tooltip (see [tooltip](refformui_r_tooltip.htm))  
type | required | button,  
combo,  
combo link,  
combo button,  
link |  | Representation type of the placeholder:  
button = button  
combo = drop-down list box  
combo link = drop-down list box  
combo button = button  
link = text as a hyperlink  
visible | optional | true, false | true | true = placeholder is visible  
false = placeholder is invisible  
visibleItemCount | optional |  |  | Number of visible elements  
Allowed sub-elements | Quantity  
---|---  
[tooltip](refformui_r_tooltip.htm) | 0..1  
type="link": [Example code](javascript:void\(0\);)
    
        <instantiation
    	type="link"
    	alwaysShowDialog="true"
    	receiver="mosWithPlaceholders.select(x|x.isPlaceholder).first"
    	name="='St'+(mos.indexOf(this)+1)+type.name" />

Result: On clicking the hyperlink, the following selection dialog is displayed: The selection dialog is structured like a search dialog for library components. The library components found by the formula are listed in the table. If several library components are found, the one to be instanced must be marked. Next, how many project components are to be created in one step can be specified in the field Number of Project Components:. type="link" with a different image and calculated text: [Example code](javascript:void\(0\);)
    
        <instantiation
    	type="link" 
    	text="=('add '+ mos.first.name.right(7))"
    	receiver="mosWithPlaceholders.select(x|x.isPlaceholder).first"
    	img="install\icon-collection\level4.png"
    	name="='St'+(mos.indexOf(this)+1)+type.name"/>

Result: type="button". The selected component is instantly instantiated: [Example code](javascript:void\(0\);)
    
        <instantiation
    	type="button"
    	receiver="mosWithPlaceholders.select(x|x.isPlaceholder).first"
    	name="='St'+(mos.indexOf(this)+1)+type.name"/>

Result: type="combo": [Example code](javascript:void\(0\);)
    
        <instantiation
    	type="combo"
    	receiver="mosWithPlaceholders.select(x|x.isPlaceholder).first"
    	name="='St'+(mos.indexOf(this)+1)+type.name"/>

Result: type="combo link". The selected component is instantiated only after clicking the hyperlink: [Example code](javascript:void\(0\);)
    
        <instantiation
    	type="combo link"
    	receiver="mosWithPlaceholders.select(x|x.isPlaceholder).first"
    	name="='St'+(mos.indexOf(this)+1)+type.name"/>

Result: type="combo button". The selected component is instantiated only after clicking the button: [Example code](javascript:void\(0\);)
    
        <instantiation
    	type="combo button"
    	receiver="mosWithPlaceholders.select(x|x.isPlaceholder).first"
    	name="='St'+(mos.indexOf(this)+1)+type.name"/>

Result: type="combo button" with prefetch="true". The drop-down list box is instantly filled after opening the Form-UI: [Example code](javascript:void\(0\);)
    
        <instantiation
    	type="combo button"
    	prefetch="true"
    	receiver="mosWithPlaceholders.select(x|x.isPlaceholder).first"
    	name="='St'+(mos.indexOf(this)+1)+type.name"/>

Result:
