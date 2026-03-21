---
title: "-clean"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_eclipse_args_clean.htm"
file: "admin_r_eclipse_args_clean"
category: "admin"
---

# -clean

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -clean

Eclipse argument | Values | Usage  
---|---|---  
-clean | - | Optional  
**Annotation**  
During the booting of Eclipse, all plug-ins are analyzed to obtain an overview of the available plug-ins. Eclipse can cache this list in order to accelerate the boot-up time (default behavior). The parameter -clean forces an update of the cache at each boot-up. If users do not change the plug-in structure with Eclipse resources, but, for example, by copying further plug-ins directly to the plug-in folder, this change will never be recognized while the cache is enabled.
