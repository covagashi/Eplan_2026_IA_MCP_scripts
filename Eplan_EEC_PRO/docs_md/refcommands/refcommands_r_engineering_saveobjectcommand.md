---
title: "Engineering.SaveObjectCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_saveobjectcommand.htm"
file: "refcommands_r_engineering_saveobjectcommand"
category: "refcommands"
---

# Engineering.SaveObjectCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.SaveObjectCommand Saves all modifications in the model. Argument | Type | Description  
---|---|---  
None |  |   
Saves the object transferred as an argument. Argument | Type | Description  
---|---|---  
obj | Object | Context object, which determines what changes should be saved.  
[Example code in job definition for Job Server](javascript:void\(0\);)
    
        <action name="Engineering.SaveObjectCommand" />
    <action name="Engineering.ExportEOXCommand" arguments="=List{'C:\\MyProjects\\Feeder.eox',List{mroot.parent}}" />

[Example code in job definition for Job Server](javascript:void\(0\);)
    
        <action name="Engineering.SaveObjectCommand" arguments="=List{absRef('NewFeeder.Mechatronic.Feeder')}" />

In the Job Server context an absolute reference to the project component of the top level is specified as an object.
