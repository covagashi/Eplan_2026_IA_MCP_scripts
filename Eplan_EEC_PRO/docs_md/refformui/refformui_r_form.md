---
title: "form"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_form.htm"
file: "refformui_r_form"
category: "refformui"
---

# form

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  form Each Form-UI element <form> is appears as a separate editor page of the instance editor. Each Form-UI needs a title and a unique ID. The title can also be determined by a formula, so that multilingual Form-UIs can be configured. The readonly attribute controls the behavior of elements that allow entries to be made in the Form-UI. Subordinate elements inherit the value of the attribute from superordinate elements (container-elements), but it can also be overwritten by them. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
bColor | optional | 0,0,0 to 255,255,255 |  | Background color as RGB value  
id | required | any |  | Unique ID, which is referred to as reference  
img | optional | png, gif, jpg |  | assigns another image to the element  
readonly | optional | true, false |  | true = Form-UI is read-only.  
false = Input fields in the Form-UI can also be written to.  
title | required | any |  | Name of the Form-UI  
visible | optional | true, false | true | true = Form-UI is visible in the list of Form-UIs  
false = Form-UI is invisible in the list of Form-UIs  
Allowed sub-elements | Quantity  
---|---  
[action](refformui_r_action.htm) | any  
[group](refformui_r_group.htm) | any  
[img](refformui_r_img.htm) | any  
[include](refformui_r_include.htm) | any  
[input](refformui_r_input.htm) | any  
[instantiation](refformui_r_instantiation.htm) | any  
[label](refformui_r_label.htm) | any  
[line](refformui_r_line.htm) | any  
[loop](refformui_r_loop.htm) | any  
[open](refformui_r_open.htm) | any  
[progressBar](refformui_r_progressbar.htm) | any  
[table](refformui_r_table.htm) | any  
[td](refformui_r_td.htm) | any  
Five empty Form-UIs are to be defined, one of which (Title B) has its own image, one (Title C) is not indicated in the list and one (Title E) is set with red background color: [Example code](javascript:void\(0\);)
    
        <uis>
    	<form title="Titel A" id="a">
    	</form>
    
    	<form title="Titel B" id = "b" img="install\icon-collection\Rumpf.png">
    	</form>
    
    	<form title="Titel C" id = "c" visible="false">
    	</form>
    
    	<form title="Titel D" id = "d" lazy="true">
    	</form>
    
    	<form title="Titel E" id = "e" bColor="255,100,100">
    	..</form>
    </uis>

Result: A Form-UI, that includes different titles for each selected language: The Form-UI includes a drop-down box to select a language. The language is determined by means of a formula and an appropriate text will be set. The language change takes effect after reloading the Form-UI. [Example code](javascript:void\(0\);)
    
        <form title="=switch $Language {
    	case 'de_DE': 'Sprachauswahl'
    	case 'en_GB': 'Language selection'
    	else: 'Language not available'}"
    	id="language">
    	
    	<input type="combo" values="=List{Pair{'Deutsch','de_DE'},
    		Pair{'English','en_GB'}}"
    		receiver="parameter('Language')"/>
    </form>

Result:
