---
title: "Engineering.CopyFileCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_copyfilecommand.htm"
file: "refcommands_r_engineering_copyfilecommand"
category: "refcommands"
---

# Engineering.CopyFileCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.CopyFileCommand Engineering.CopyFileCommand Copies a file or a folder to the specified target.  
    1. A file or a folder with the specified name is copied to the specified target.
Argument | Type | Description  
---|---|---  
source | String | Absolute file or folder name of the copy source.  
destination | String | Absolute file or folder name of the copy target.  
    2. A file or a folder with the specified name is copied to the specified target. If the value for the argument overwrite is true, a copy target of the same name is overwritten without any query.
Argument | Type | Description  
---|---|---  
source | String | Absolute file or folder name of the copy source.  
destination | String | Absolute file or folder name of the copy target.  
overwrite | Boolean | Option whether a target with the same name is to be overwritten.  
    3. A list of files or folders is copied to the specified target.
Argument | Type | Description  
---|---|---  
sources | List | List of file or folder names of the copy source.  
destination | String | Absolute file or folder name of the copy target.  
    4. A list of files or folders is copied to the specified target. If the value for the argument overwrite is true, a copy target of the same name is overwritten without any query.
Argument | Type | Description  
---|---|---  
sources | List | List of file or folder names of the copy source.  
destination | String | Absolute file or folder name of the copy target.  
overwrite | Boolean | Option whether a target with the same name is to be overwritten.
