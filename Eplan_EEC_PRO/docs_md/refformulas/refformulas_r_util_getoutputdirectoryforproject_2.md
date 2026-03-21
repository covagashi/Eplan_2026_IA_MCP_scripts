---
title: "getOutputDirectoryForProject(String projectName, Boolean createFolder)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_util_getoutputdirectoryforproject_2.htm"
file: "refformulas_r_util_getoutputdirectoryforproject_2"
category: "refformulas"
---

# getOutputDirectoryForProject(String projectName, Boolean createFolder)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  getOutputDirectoryForProject(String projectName, Boolean createFolder) Util methods Determines the output folder for the created files for the specified project name. If no folder exists, it can be created if required. The output folder is session-specific for the Job Server and Web EEC, meaning that it contains the session ID. getOutputDirectoryForProject(String projectName, Boolean createFolder)  
---  
Arguments | String | projectName | The name of the project whose output folder is to be determined.  
Boolean | createFolder |  true = output folder is created false = output folder is not created  
Return value | String | Absolute path of the output folder  
[Example code for a Form-UI](javascript:void\(0\);)
    
        <action type="link" name="Customizing_Engineering.OpenResourceCommand"
    arguments="List{mroot.project,
    type('Engineering.Util').getOutputDirectoryForProject(mroot.project.name + '\\ECAD\\WD_A_A.elk', true)}">
    Open project file
    </action>
