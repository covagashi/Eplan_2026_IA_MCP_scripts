---
title: "formContentArea"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_formcontentarea.htm"
file: "refformui_r_formcontentarea"
category: "refformui"
---

# formContentArea

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  formContentArea The <formContentArea> element encloses the definition of a Form-UI which is displayed in a popup window. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
bColor | optional | 0,0,0 to 255,255,255 |  | Background color as RGB value  
id | required | any |  | Unique ID, which is referred to as reference  
img | optional | png, gif, jpg |  | assigns another image to the element  
lazy | optional | true, false | false | true = only those values are changed in the Form-UI page, which are derived directly from the EOs. Values, which are calculated by a formula, are not changed. Example: Attributes visible and enable  
false = Form-UI is rebuilt after each change, and any formulas are newly calculated  
title | required | any |  | Name of the Form-UI  
visible | optional | true, false | true | true = Form-UI is visible in the list of Form-UIs  
false = Form-UI is invisible in the list of Form-UIs  
id | required | any |  | Unique ID, which is referred to as reference  
title | required | any |  | Name of the Form-UI  
Allowed sub-elements | Quantity  
---|---  
[action](refformui_r_action.htm) | any  
[browser](refformui_r_browser.htm) | any  
[group](refformui_r_group.htm) | any  
[img](refformui_r_img.htm) | any  
[include](refformui_r_include.htm) | any  
[input](refformui_r_input.htm) | any  
[instantiation](refformui_r_instantiation.htm) | any  
[label](refformui_r_label.htm) | any  
[line](refformui_r_line.htm) | any  
[loop](refformui_r_loop.htm) | any  
[mailto](refformui_r_mailto.htm) | any  
[open](refformui_r_open.htm) | any  
[progressBar](refformui_r_progressbar.htm) | any  
[pureTable](refformui_r_puretable.htm) | any  
[switch](refformui_r_switch.htm) | any  
[table](refformui_r_table.htm) | any
