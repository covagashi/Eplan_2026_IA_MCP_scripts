---
title: "Full screen mode"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_fullscreen_mode.htm"
file: "refformui_r_fullscreen_mode"
category: "refformui"
---

# Full screen mode

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Full screen mode In order to start Form-UIs in Full screen mode, the Form-UI perspective is used, where the configured user interface of the editor is displayed in full screen mode. For the Form-UI perspective, the objects and their internal form-ids, which should be displayed in full screen mode, must be fixed in the ec.ini file. The following entries in the ec.ini file are set, e.g. to open the configurator interface of the Pfuderer Golf ball machine:  
      
        -Dcom.mind8.formui.perspective.object=Pfuderer-Golfballmaschine.Mechatronik.RTS24
    -Dcom.mind8.formui.perspective.form-id=Auftragsdaten

The first argument contains the absolute name of the object; in this case the RTS24 and also the ID of the Form-UI, that is to be opened. This ID is fixed in the Form-UI for the RTS24 (<form title="Configuration: Order data" id="OrderData">). In order to start EEC with the Form-UI perspective, the following entry has to be added to the ec.ini file:
    
        -perspective
    com.mind8.mechatronic.ui.formperspective

Note It is important, that the entry is positioned prior to the vmargs (see [Runtime options](admin_r_runtime_options.htm)). [Example code](javascript:void\(0\);)
    
        -perspective
    com.mind8.mechatronic.ui.formperspective
    -product
    de.eplan.engineeringconfiguration.product
    -data
    workspace
    -clean
    -vmargs
    -Xmx512m
    -Xss1m
    -Dorg.foederal.sn.connectionURL=proxy://initial=eox:///.eox/model.eox?mode=rw
    -Dosgi.nl=de_DE
