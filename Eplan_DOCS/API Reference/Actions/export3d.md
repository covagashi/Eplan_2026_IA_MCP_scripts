# export3d

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/export3d.html

---

```
Action to export installation spaces into 3D formats.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 '¢ "STEP": Export to STEP format.
 '¢ "JT": Export to JT format.
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` INSTALLATIONSPACENAME
 ``` | ``` Name of a layout space to be exported.
 ``` |
| ``` INSTALLATIONSPACENAMEn
 ``` | ``` Names of a layout spaces to be exported (optional), where n is a number e.g. /INSTALLATIONSPACENAME1:BR1 /INSTALLATIONSPACENAME2:BR2 /INSTALLATIONSPACENAME:BR3 etc.
 ``` |
| ``` STRUCTURE
 ``` | ``` Structure identifier of the InstallationSpace to be exported (optional).
 ``` |
| ``` STRUCTUREn
 ``` | ``` Structure identifiers of the InstallationSpaces to be exported (optional), where n is a number e.g. /INSTALLATIONSPACENAME1:BR1 /STRUCTURE1:=EB3+ET1 /INSTALLATIONSPACENAME2:BR2 /STRUCTURE2:=EB3+ET2 etc.
 ``` |
| ``` DESTINATIONPATH
 ``` | ``` Target directory. If this directory does not exist yet, it is created.
 ``` |
| ``` EXPORTSCHEME
 ``` | ``` Export scheme (optional). If the parameter does not exist or is empty (""), the last used scheme will be applied
 ``` |
| ``` SEPARATEFILES
 ``` | ``` Determines whether separate files should be created. Only effective with TYPE parameter set to "STEP".
 ``` |
| ``` FILENAME
 ``` | ``` File name (optional). Only effective with TYPE parameter set to "JT".
 ``` |

**Remarks**

```
If no layout space parameter is specified, the entire project is exported.

```

**Example**

```
Export installation spaces BR1 and BR2 to STEP.

export3d /TYPE:STEP /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /INSTALLATIONSPACENAME1:BR1 /INSTALLATIONSPACENAME2:BR2 /DESTINATIONPATH:C:\temp\step_export

Export installation spaces BR1 and BR2 to STEP with specified structure identifiers.

export3d /TYPE:STEP /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /INSTALLATIONSPACENAME1:BR1 /STRUCTURE1:=EB3+ET1 /INSTALLATIONSPACENAME2:BR2 /STRUCTURE2:=EB3+ET2 /DESTINATIONPATH:C:\temp\step_export

```