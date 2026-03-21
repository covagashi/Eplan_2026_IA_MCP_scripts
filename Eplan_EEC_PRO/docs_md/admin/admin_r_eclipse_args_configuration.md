---
title: "-configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_eclipse_args_configuration.htm"
file: "admin_r_eclipse_args_configuration"
category: "admin"
---

# -configuration

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -configuration

Eclipse argument |  Values |  Usage  
---|---|---  
-configuration |  - |  Optional  
**Annotation**  
Specifies the path to the configuration folder where the platform configuration file ec.ini is located. By default, the configuration folder is called configuration, and is located in the execution folder of ec.exe. The explicit output of this folder is necessary if the user cannot write to the default folder in the Eclipse installation. A shared installation is one where ec.exe can be launched by different users. Typically work in an application server configuration or also in a local installation, alternating with the installation in various configurations.  
  
### Note

Typically, the option -configuration is used in combination with -data. If the configuration directory and the workspace are modified at the same time, an error message will result: Class not found. An error-free migration requires two steps:

    1. Only convert the workspace to the new directory.
    2. Then, convert the configuration.

### Note

In the case of Client-Server installations, only ini files may be in the configuration folder of the server installation. If this is not the case, EEC was launched at least once without the option configuration. In the event, EEC (due to a bug in Eclipse 3.2) will in future ignore the configuration setting stated at the start, and use the setting in the serverâs configuration folder. There, all subfolders of the configuration folder have to be deleted in this context.
