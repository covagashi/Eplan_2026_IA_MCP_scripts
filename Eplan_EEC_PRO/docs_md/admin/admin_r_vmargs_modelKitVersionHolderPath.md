---
title: "com.mind8.project.exchange.model.ProjectExchangeModel.modelKitVersionHolderPath"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_modelKitVersionHolderPath.htm"
file: "admin_r_vmargs_modelKitVersionHolderPath"
category: "admin"
---

# com.mind8.project.exchange.model.ProjectExchangeModel.modelKitVersionHolderPath

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## com.mind8.project.exchange.model.ProjectExchangeModel.modelKitVersionHolderPath

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.project.exchange.model.ProjectExchangeModel.modelKitVersionHolderPath=<absolutePath>.<VersionParameter> |  Optional  
**Annotation**  
Absolute name to the parameter, which contains the modular system version number. Only then is it possible to run PX updates automatically. absolutePath references the project component that contains the parameter for the model version. VersionParameter indicates the name of the parameter that stores the model version Example:
    
        -Dcom.mind8.project.exchange.model.ProjectExchangeModel.  
    modelKitVersionHolderPath=Bib.Komponenten.Basis.modellversion  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
