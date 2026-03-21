---
title: "Engineering.ImportLibrariesCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_importlibrariescommand.htm"
file: "refcommands_r_engineering_importlibrariescommand"
category: "refcommands"
---

# Engineering.ImportLibrariesCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ImportLibrariesCommand Imports the libraries into the project, which are passed by the list. Already imported libraries are ignored. Returns an error if the assigned library does not exist. The following variants are possible for using the command: Argument | Type | Description  
---|---|---  
obj | Root | Root object of the mechatronic structure or of a discipline structure  
      
        Engineering.ImportLibrariesCommand(this.mroot)

Argument | Type | Description  
---|---|---  
root | Root | Root object of the mechatronic structure or of a discipline structure  
libNames | List | Libraries to import  
      
        Engineering.ImportLibrariesCommand(this.mroot, List{Customizing_Ecad_Ui})
