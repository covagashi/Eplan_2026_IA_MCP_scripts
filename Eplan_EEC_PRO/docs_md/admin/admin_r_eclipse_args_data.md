---
title: "-data"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_eclipse_args_data.htm"
file: "admin_r_eclipse_args_data"
category: "admin"
---

# -data

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -data

Eclipse argument | Values | Usage  
---|---|---  
-data | <dir> | Optional  
**Annotation**  
Specifies the path to the workspace folder. By default, the workspace folder is called workspace, and is located in the execution folder of ec.exe.  
  
### Note

Typically, the option -configuration is used in combination with -data. If the configuration directory and the workspace are modified at the same time, an error message will result: Class not found.  
An error-free migration requires two steps:

    1. Only convert the workspace to the new directory.
    2. Then, convert the configuration.
