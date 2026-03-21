---
title: "Versioning of the modular systems"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_versioning_modular_system.htm"
file: "eecbase_k_px_versioning_modular_system"
category: "eecbase"
---

# Versioning of the modular systems

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## Versioning of the modular systems

Versioning is done by introducing a string parameter that is used as a holder for the version identifier.

The value of the parameter has the following definition:
    
        [Beliebiger String] "V" + Nummer + "." + Nummer

### [Example](javascript:void\(0\);)
    
    
    Feeder3000 V 1.13

**V** , and the numbers separated by the period are relevant to the versioning; the text in front of that is optional.

The name of the version control parameter must be added to the VM arguments in the initialization file of EEC (see also [Java Virtual Machine Arguments (VMArgs)](admin_r_vmargs.htm)):
    
        com.mind8.project.exchange.model.ProjectExchangeModel.modelKitVersionHolderPath

### [Example](javascript:void\(0\);)
    
    
    -Dcom.mind8.project.exchange.model.ProjectExchangeModel.modelKitVersionHolderPath=  
    T_Mechatronik_Baukasten.Komponenten.Basis.Modellversion

The update process also uses the model name (EOX filename) beside the version number.
