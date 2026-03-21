---
title: "-osgi.nl"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_eclipse_args_nl.htm"
file: "admin_r_eclipse_args_nl"
category: "admin"
---

# -osgi.nl

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -osgi.nl

The following EEC argument must be transferred with the following syntax:
    
        -D<EEC-Argument>=<Wert>

Eclipse argument |  Values |  Usage  
---|---|---  
-Dosgi.nl=<Language code>_<Country code> |  de_DE  
en_US |  Optional  
**Annotation**  
Sets the user interface language of EEC, the Job Server and the Workers. Currently, German and English are supported. Is entered below -vmargs.
    
        -Dosgi.nl=<Language code>_<Country code>

Examples:
    
        -vmargs
    -Dosgi.nl=de_DE
    
        -vmargs
    -Dosgi.nl=en_US
