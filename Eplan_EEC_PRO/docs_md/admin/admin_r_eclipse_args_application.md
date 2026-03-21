---
title: "-application"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_eclipse_args_application.htm"
file: "admin_r_eclipse_args_application"
category: "admin"
---

# -application

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -application

Eclipse argument | Values | Usage  
---|---|---  
-application | applicationId | Optional  
**Annotation**  
The application executed by the call of ec.exe is defined by a specific composition of plug-ins. Based on the plug-ins installed, alternative applications consisting of a different composition of plug-ins and configuration data can be launched. The default application is specified in the file config.ini in the configuration folder. It contains the entry eclipse.product=de.eplan.engineeringconfiguration.workbench A different application can be selected via the argument -application. EEC defines the following applications | applicationId | Description  
---|---  
de.eplan.engineeringconfiguration. DatabaseAdminApplication | Used for managing databases:  
Creating databases  
Importing models  
Updating models  
Deleting databases  
de.eplan.engineeringconfiguration. XMLExportApplication | Allows for the export of the model to an XML file in batch mode operation.  
  
Generally, in combination with this argument, an alternative configuration has to be provided also for ec.ini, see argument âpluginCustomization.
