---
title: "com.mind8.formui.perspective.object"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_formui_perspective_object.htm"
file: "admin_r_vmargs_formui_perspective_object"
category: "admin"
---

# com.mind8.formui.perspective.object

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## com.mind8.formui.perspective.object

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.formui.perspective.object=absolutePath |  Optional  
**Annotation**  
Opens the specified FormUI editor during the start and displays it. Must be used in combination with -Dcom.mind8.formui.perspective.form-id to find the project component which contains the Form-UI. absolutePath references the project component that contains the Form-UI to be displayed. Example:
    
        -Dcom.mind8.formui.perspective.object=Feeder.Mechatronic.Feeder  
  
### Note

These entries can be specified for the display of a Form-UI during the start:

-Dcom.mind8.formui.perspective.object

-Dcom.mind8.formui.perspective.form-id

-Dcom.mind8.formui.perspective.editor

If all 3 entries are available, only -Dcom.mind8.formui.perspective.editor is applied.

### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.

### Further information

     * [com.mind8.formui.perspective.editor](admin_r_vmargs_formui_perspective_editor.htm)
     * [com.mind8.formui.perspective.form-id](admin_r_vmargs_formui_perspective_formid.htm)
     * [-perspective](admin_r_eclipse_args_perspective.htm)
     * [com.mind8.mechatronic.ui.formperspective](admin_r_vmargs_mechatronic_ui_formperspective.htm)
