---
title: "Starting EEC with a specific Form-UI"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_start_editor.htm"
file: "refformui_r_start_editor"
category: "refformui"
---

# Starting EEC with a specific Form-UI

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Starting EEC with a specific Form-UI To start EEC showing a certain Form-UI, the initializing file of EEC has to contain an entry with the following syntax (see also [Java Virtual Machine Arguments (VMArgs)](admin_r_vmargs.htm)): -Dcom.mind8.formui.perspective.editor=absolutePath#Page:Form-UI-ID Meaning of the single items:  
     * -Dcom.mind8.formui.perspective.editor = The property that is subsequently defined.
     * absolutePath = the absolute path to the component, which contains the Form-UI.
     * #Page:Form-UI-ID = the id of the Form-UI
The following example shows an initializing file, which starts EEC with the Form-UI with the id id="start" from the demo model Documentation_UI_Configuration: [Example code](javascript:void\(0\);)
    
        -product
    de.eplan.engineeringconfiguration.product
    -data
    workspace
    --launcher.XXMaxPermSize
    128m
    -vmargs
    -Xmx512m
    -Xss1m
    -Dorg.foederal.sn.connectionURL=proxy://initial=eox:///.eox/model.eox?mode=rw
    -Dosgi.nl=de_DE
    -Dcom.mind8.formui.perspective.editor=Dokumentation_UI_Konfiguration.
    	Mechatronik.Dokumentation#Page:start
