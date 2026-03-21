---
title: "de.eplan.eec.formui.renderer"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_renderer.htm"
file: "admin_r_vmargs_renderer"
category: "admin"
---

# de.eplan.eec.formui.renderer

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.formui.renderer

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.formui.renderer=<Renderer type> |  Optional  
**Annotation**  
Specifies the renderer with which Form-UIs are represented. Permitted values for the renderer type are:
     * swing: Form-UIs are rendered with SWING; no other renderer can be selected.
     * swt: Form-UIs are rendered with SWT; no other renderer can be selected.
     * all: Form-UIs are rendered either with SWING or SWT; a menu is used for the selection.
     * No value: Form-UIs are rendered with SWT by default.
Example:
    
        -Dde.eplan.eec.formui.renderer=SWING  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
